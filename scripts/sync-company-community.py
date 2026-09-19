#!/usr/bin/env python3
"""Synchronize bidirectional company <-> community/project links.

Human-authored facts remain the source of truth on either side:
- company `projects:` / `communities:`
- project/community `companies:` / legacy singular `company:`

The union of those explicit assertions is mirrored into generated fields:
- company `linked_projects:`
- project/community `linked_companies:`

Model teams/projects are recognized as valid company `projects:` values but are
intentionally outside this community/project relation layer. No relationship is
inferred from employee participation alone. Existing prose and manual fields are
preserved; only generated fields and marked body sections are replaced.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

ROOTS = ("company", "community", "university")
ENTITY_TYPES = {"project", "community", "project-collection"}
NON_COMMUNITY_PROJECT_TYPES = {"model-team", "model-project"}
COMPANY_START = "<!-- BEGIN AUTO COMPANY COMMUNITY LINKS -->"
COMPANY_END = "<!-- END AUTO COMPANY COMMUNITY LINKS -->"
ENTITY_START = "<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->"
ENTITY_END = "<!-- END AUTO COMMUNITY COMPANY LINKS -->"


def norm(value: str) -> str:
    return value.replace("\\", "/").strip().strip("/").removesuffix(".md")


def fold(value: str) -> str:
    return re.sub(r"\s+", " ", norm(value)).casefold()


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return [], text
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return [], text
    tail = "\n" if text.endswith("\n") else ""
    return lines[1:end], "\n".join(lines[end + 1 :]) + tail


def join_frontmatter(lines: list[str], body: str) -> str:
    return "---\n" + "\n".join(lines).rstrip() + "\n---\n" + body


def key_of(line: str):
    if line.startswith((" ", "\t", "-")) or ":" not in line:
        return None
    return line.split(":", 1)[0].strip() or None


def blocks(lines: list[str]):
    result, i = [], 0
    while i < len(lines):
        key = key_of(lines[i])
        if not key:
            result.append((None, [lines[i]]))
            i += 1
            continue
        j = i + 1
        while j < len(lines) and key_of(lines[j]) is None:
            j += 1
        result.append((key, lines[i:j]))
        i = j
    return result


def parse_inline_list(body: str) -> list[str]:
    if not body.strip():
        return []
    parts, buf, quote = [], [], None
    for ch in body:
        if ch in "\"'":
            if quote == ch:
                quote = None
            elif quote is None:
                quote = ch
            buf.append(ch)
        elif ch == "," and quote is None:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf).strip())
    return [part.strip().strip("\"'") for part in parts if part.strip()]


def get_block(lines: list[str], wanted: str):
    return next((block for key, block in blocks(lines) if key == wanted), None)


def get_values(lines: list[str], wanted: str) -> list[str]:
    block = get_block(lines, wanted)
    if not block:
        return []
    value = block[0].split(":", 1)[1].strip()
    if not value:
        return [line[4:].strip().strip("\"'") for line in block[1:] if line.startswith("  - ") and line[4:].strip()]
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value[1:-1])
    return [value.strip("\"'")]


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block:
        return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def set_block_list(lines: list[str], key: str, values: list[str]) -> list[str]:
    values = list(dict.fromkeys(v for v in values if v))
    replacement = [f"{key}: []"] if not values else [f"{key}:"] + [f"  - {json.dumps(v, ensure_ascii=False)}" for v in values]
    out, replaced = [], False
    for existing, block in blocks(lines):
        if existing == key:
            if not replaced:
                out.extend(replacement)
                replaced = True
            continue
        out.extend(block)
    if not replaced:
        out.extend(replacement)
    return out


def all_markdown(root: pathlib.Path):
    for dirname in ROOTS:
        base = root / dirname
        if base.exists():
            yield from sorted(base.rglob("*.md"))


def load_records(root: pathlib.Path):
    rows = []
    for path in all_markdown(root):
        text = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if not fm:
            continue
        rel = path.relative_to(root).as_posix()
        rows.append({
            "path": path,
            "rel": rel,
            "id": rel[:-3],
            "text": text,
            "fm": fm,
            "body": body,
            "type": get_scalar(fm, "type") or "",
            "name": get_scalar(fm, "name") or get_scalar(fm, "title") or path.stem,
        })
    return rows


def aliases_for(record: dict) -> list[str]:
    values = [record["name"], pathlib.PurePosixPath(record["id"]).name, *get_values(record["fm"], "aliases")]
    return list(dict.fromkeys(v for v in values if v))


def build_index(records: list[dict], allowed_types: set[str]):
    selected = [r for r in records if r["type"] in allowed_types]
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for record in selected:
        ids[fold(record["id"])] = record
        for value in aliases_for(record):
            aliases[fold(value)].append(record)
    return selected, aliases, ids


def resolve(value: str, aliases, ids):
    value = norm(value)
    if not value:
        return None
    direct = ids.get(fold(value))
    if direct:
        return direct
    for candidate in (value, pathlib.PurePosixPath(value).name):
        unique = {r["id"]: r for r in aliases.get(fold(candidate), [])}
        if len(unique) == 1:
            return next(iter(unique.values()))
    return None


def replace_auto_section(body: str, start: str, end: str, section: str | None) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.DOTALL)
    if section is None:
        updated = pattern.sub("", body, count=1)
        return re.sub(r"\n{3,}", "\n\n", updated).rstrip() + "\n"
    if pattern.search(body):
        updated = pattern.sub(section, body, count=1)
        return updated if updated.endswith("\n") else updated + "\n"
    return body.rstrip() + "\n\n" + section + "\n"


def source_label(sources: set[str]) -> str:
    if sources == {"company", "entity"}:
        return "公司页与社区/项目页均有显式记录"
    if "entity" in sources:
        return "由社区/项目页的 `companies:` / `company:` 反向镜像"
    return "由公司页的 `projects:` / `communities:` 反向镜像"


def company_section(company: dict, targets: list[dict], pair_sources: dict, pair_relations: dict) -> str | None:
    if not targets:
        return None
    lines = [
        COMPANY_START,
        "## 社区 / 开源项目关联（自动汇总）",
        "",
        "以下关系由公司页与社区/项目页的显式元数据双向汇总。员工个人参与不会自动升级为公司官方关系。",
        "",
    ]
    for target in targets:
        key = (company["id"], target["id"])
        relation = pair_relations.get(key)
        suffix = f"；关系：`{relation}`" if relation else ""
        lines.append(f"- [[{target['id']}|{target['name']}]]：{source_label(pair_sources[key])}{suffix}。")
    lines.extend(["", COMPANY_END])
    return "\n".join(lines)


def entity_section(entity: dict, companies: list[dict], pair_sources: dict, pair_relations: dict) -> str | None:
    if not companies:
        return None
    lines = [
        ENTITY_START,
        "## 关联公司（自动汇总）",
        "",
        "以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。",
        "",
    ]
    for company in companies:
        key = (company["id"], entity["id"])
        relation = pair_relations.get(key)
        suffix = f"；关系：`{relation}`" if relation else ""
        lines.append(f"- [[{company['id']}|{company['name']}]]：{source_label(pair_sources[key])}{suffix}。")
    lines.extend(["", ENTITY_END])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    companies, company_aliases, company_ids = build_index(records, {"company"})
    entities, entity_aliases, entity_ids = build_index(records, ENTITY_TYPES)
    _, noncommunity_aliases, noncommunity_ids = build_index(records, NON_COMMUNITY_PROJECT_TYPES)

    pair_sources: dict[tuple[str, str], set[str]] = defaultdict(set)
    pair_relations: dict[tuple[str, str], str] = {}
    unresolved = []
    recognized_noncommunity = []

    for company in companies:
        for field in ("projects", "communities"):
            for value in get_values(company["fm"], field):
                target = resolve(value, entity_aliases, entity_ids)
                if not target:
                    if field == "projects" and resolve(value, noncommunity_aliases, noncommunity_ids):
                        recognized_noncommunity.append({"source": company["rel"], "value": value})
                        continue
                    unresolved.append({"kind": f"company.{field}", "source": company["rel"], "value": value})
                    continue
                pair_sources[(company["id"], target["id"])].add("company")

    for entity in entities:
        relation = get_scalar(entity["fm"], "company_relation")
        values = [*get_values(entity["fm"], "companies"), *get_values(entity["fm"], "company")]
        seen = set()
        for value in values:
            if fold(value) in seen:
                continue
            seen.add(fold(value))
            company = resolve(value, company_aliases, company_ids)
            if not company:
                unresolved.append({"kind": "entity.company", "source": entity["rel"], "value": value})
                continue
            key = (company["id"], entity["id"])
            pair_sources[key].add("entity")
            if relation:
                pair_relations[key] = relation

    company_targets: dict[str, list[dict]] = defaultdict(list)
    entity_companies: dict[str, list[dict]] = defaultdict(list)
    company_map = {r["id"]: r for r in companies}
    entity_map = {r["id"]: r for r in entities}
    for company_id, entity_id in pair_sources:
        company_targets[company_id].append(entity_map[entity_id])
        entity_companies[entity_id].append(company_map[company_id])

    touched = []
    for company in companies:
        targets = sorted(company_targets.get(company["id"], []), key=lambda r: (r["name"].casefold(), r["id"].casefold()))
        updated_fm = set_block_list(company["fm"], "linked_projects", [r["id"] for r in targets])
        updated_body = replace_auto_section(
            company["body"], COMPANY_START, COMPANY_END,
            company_section(company, targets, pair_sources, pair_relations),
        )
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != company["text"]:
            company["path"].write_text(updated, encoding="utf-8")
            touched.append(company["rel"])

    for entity in entities:
        linked = sorted(entity_companies.get(entity["id"], []), key=lambda r: (r["name"].casefold(), r["id"].casefold()))
        updated_fm = set_block_list(entity["fm"], "linked_companies", [r["id"] for r in linked])
        updated_body = replace_auto_section(
            entity["body"], ENTITY_START, ENTITY_END,
            entity_section(entity, linked, pair_sources, pair_relations),
        )
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != entity["text"]:
            entity["path"].write_text(updated, encoding="utf-8")
            touched.append(entity["rel"])

    both = sum(1 for sources in pair_sources.values() if sources == {"company", "entity"})
    company_only = sum(1 for sources in pair_sources.values() if sources == {"company"})
    entity_only = sum(1 for sources in pair_sources.values() if sources == {"entity"})
    print(
        f"Company/community sync: {len(companies)} companies, {len(entities)} project/community nodes, "
        f"{len(pair_sources)} pairs ({both} asserted on both sides, {company_only} company-only, "
        f"{entity_only} entity-only), {len(touched)} files updated, {len(unresolved)} unresolved explicit values, "
        f"{len(recognized_noncommunity)} non-community project targets recognized."
    )
    for item in unresolved[:80]:
        print(f"UNRESOLVED {item['kind']}: {item['source']} -> {item['value']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
