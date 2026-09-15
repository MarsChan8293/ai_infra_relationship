#!/usr/bin/env python3
"""Synchronize company/project/community -> person reverse relationships.

Person Markdown remains the source of truth:
- `current_affiliations:` -> company `linked_people:` when the affiliation resolves to a company.
- school/research/model-team affiliations are valid but handled by their own entity layers.
- `projects:` / `project:` / `communities:` / `community:` -> project/community `linked_people:`.

Existing hand-written narrative and curated `people:` fields are preserved. Only
explicitly marked generated sections are replaced.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
PROJECT_TYPES = {"project", "community", "infra-project", "project-collection"}
NON_COMPANY_AFFILIATION_TYPES = {"school", "research-institution", "model-team"}
COMPANY_START = "<!-- BEGIN AUTO COMPANY PEOPLE -->"
COMPANY_END = "<!-- END AUTO COMPANY PEOPLE -->"
PROJECT_START = "<!-- BEGIN AUTO PROJECT PEOPLE -->"
PROJECT_END = "<!-- END AUTO PROJECT PEOPLE -->"
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")

COMMON_ALIASES = {
    "清华大学": ["Tsinghua University"],
    "北京大学": ["Peking University", "PKU"],
    "上海交通大学": ["Shanghai Jiao Tong University", "SJTU"],
    "浙江大学": ["Zhejiang University", "ZJU"],
    "UC Berkeley": ["University of California, Berkeley", "Berkeley"],
    "北京智源人工智能研究院": ["BAAI", "Beijing Academy of Artificial Intelligence"],
}


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
    out, inserted = [], False
    for existing, block in blocks(lines):
        if existing == key:
            if not inserted:
                out.extend(replacement)
                inserted = True
            continue
        if not inserted and existing in {"areas", "projects", "companies", "company_relation", "category", "layer", "open_source", "repository", "governance", "last_verified"}:
            out.extend(replacement)
            inserted = True
        out.extend(block)
    if not inserted:
        out.extend(replacement)
    return out


def all_markdown(root: pathlib.Path):
    for dirname in NODE_ROOTS:
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
            "name": get_scalar(fm, "name") or path.stem,
            "english_name": get_scalar(fm, "english_name") or "",
        })
    return rows


def aliases_for(record: dict) -> list[str]:
    values = [record["name"], pathlib.PurePosixPath(record["id"]).name, *get_values(record["fm"], "aliases")]
    values.extend(COMMON_ALIASES.get(record["name"], []))
    return list(dict.fromkeys(v for v in values if v))


def build_index(records: list[dict], allowed_types: set[str]):
    selected = [r for r in records if r["type"] in allowed_types]
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for record in selected:
        ids[fold(record["id"])] = record
        seen = set()
        for value in aliases_for(record):
            token = fold(value)
            if token and token not in seen:
                seen.add(token)
                aliases[token].append(record)
    return selected, aliases, ids


def resolve(value: str, aliases, ids):
    value = norm(value)
    direct = ids.get(fold(value))
    if direct:
        return direct
    for candidate in (value, pathlib.PurePosixPath(value).name):
        unique = {r["id"]: r for r in aliases.get(fold(candidate), [])}
        if len(unique) == 1:
            return next(iter(unique.values()))
    return None


def link_target(inner: str) -> str:
    return norm(inner.split("|", 1)[0].split("#", 1)[0].strip())


def display_name(person: dict) -> str:
    name, english = person["name"], person["english_name"]
    return f"{name}（{english}）" if english and fold(name) != fold(english) else name


def body_detail(person: dict, target: dict, aliases, ids, preferred_tokens: tuple[str, ...], strict_preferred: bool = False) -> str | None:
    active_heading, fallback = "", None
    for raw in person["body"].splitlines():
        stripped = raw.strip()
        if stripped.startswith("## "):
            active_heading = stripped[3:].strip().casefold()
            continue
        if not stripped.startswith("-"):
            continue
        matched = False
        for match in WIKILINK_RE.finditer(stripped):
            resolved = resolve(link_target(match.group(1)), aliases, ids)
            if resolved and resolved["id"] == target["id"]:
                matched = True
                break
        if not matched:
            folded = fold(stripped)
            matched = any(fold(alias) in folded for alias in aliases_for(target))
        if not matched:
            continue
        detail = stripped.lstrip("- ").strip()
        if len(detail) > 240:
            detail = detail[:237].rstrip() + "..."
        if any(token in active_heading for token in preferred_tokens):
            return detail
        if not strict_preferred:
            fallback = fallback or detail
    return fallback


def replace_auto_section(body: str, start: str, end: str, section: str | None) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.DOTALL)
    if section is None:
        updated = pattern.sub("", body, count=1)
        return re.sub(r"\n{3,}", "\n\n", updated).rstrip() + "\n"
    if pattern.search(body):
        updated = pattern.sub(section, body, count=1)
        return updated if updated.endswith("\n") else updated + "\n"
    return body.rstrip() + "\n\n" + section + "\n"


def company_section(company: dict, people: list[dict], aliases, ids) -> str | None:
    if not people:
        return None
    lines = [COMPANY_START, "## 当前关联人物（自动汇总）", "", "以下人物由其 `current_affiliations:` 反向汇总，仅表示当前公开 affiliation，不自动推断直属汇报、团队归属或历史任职关系。", ""]
    for person in people:
        detail = body_detail(person, company, aliases, ids, ("当前", "工作", "经历", "简介"), strict_preferred=True)
        lines.append(f"- [[{person['id']}|{display_name(person)}]]：{detail or '当前 affiliation；具体职位与时间以人物页公开来源为准。'}")
    lines.extend(["", COMPANY_END])
    return "\n".join(lines)


def project_section(target: dict, people: list[dict], source_fields: dict[str, set[str]], aliases, ids) -> str | None:
    if not people:
        return None
    lines = [PROJECT_START, "## 关联人物（自动汇总）", "", "以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。", ""]
    for person in people:
        detail = body_detail(person, target, aliases, ids, ("项目", "社区", "贡献", "当前", "核心", "技术"))
        fields = source_fields.get(person["id"], set())
        if detail:
            description = detail
        elif "projects" in fields or "project" in fields:
            description = "项目关联；人物页已明确记录该项目。"
        else:
            description = "社区贡献关联；人物页已明确记录该社区。"
        lines.append(f"- [[{person['id']}|{display_name(person)}]]：{description}")
    lines.extend(["", PROJECT_END])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    companies, company_aliases, company_ids = build_index(records, {"company"})
    noncompanies, noncompany_aliases, noncompany_ids = build_index(records, NON_COMPANY_AFFILIATION_TYPES)
    project_nodes, project_aliases, project_ids = build_index(records, PROJECT_TYPES)
    people = [r for r in records if r["type"] == "person"]

    company_reverse: dict[str, list[dict]] = defaultdict(list)
    project_reverse: dict[str, list[dict]] = defaultdict(list)
    project_sources: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    unresolved = []

    for person in people:
        seen_companies = set()
        for value in get_values(person["fm"], "current_affiliations"):
            target = resolve(value, company_aliases, company_ids)
            if not target:
                # Schools, research institutions and model teams are legitimate current
                # affiliations but do not belong in the company reverse set.
                if resolve(value, noncompany_aliases, noncompany_ids):
                    continue
                unresolved.append({"kind": "affiliation", "person": person["rel"], "value": value})
                continue
            if target["id"] not in seen_companies:
                company_reverse[target["id"]].append(person)
                seen_companies.add(target["id"])

        seen_projects = set()
        for field in ("projects", "project", "communities", "community"):
            for value in get_values(person["fm"], field):
                target = resolve(value, project_aliases, project_ids)
                if not target:
                    unresolved.append({"kind": field, "person": person["rel"], "value": value})
                    continue
                project_sources[target["id"]][person["id"]].add(field)
                if target["id"] not in seen_projects:
                    project_reverse[target["id"]].append(person)
                    seen_projects.add(target["id"])

    touched, company_associations, project_associations = [], 0, 0
    for company in companies:
        linked = sorted(company_reverse.get(company["id"], []), key=lambda r: r["id"].casefold())
        company_associations += len(linked)
        updated_fm = set_block_list(company["fm"], "linked_people", [p["id"] for p in linked])
        updated_body = replace_auto_section(company["body"], COMPANY_START, COMPANY_END, company_section(company, linked, company_aliases, company_ids))
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != company["text"]:
            company["path"].write_text(updated, encoding="utf-8")
            touched.append(company["rel"])

    for target in project_nodes:
        linked = sorted(project_reverse.get(target["id"], []), key=lambda r: r["id"].casefold())
        project_associations += len(linked)
        updated_fm = set_block_list(target["fm"], "linked_people", [p["id"] for p in linked])
        updated_body = replace_auto_section(target["body"], PROJECT_START, PROJECT_END, project_section(target, linked, project_sources.get(target["id"], {}), project_aliases, project_ids))
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != target["text"]:
            target["path"].write_text(updated, encoding="utf-8")
            touched.append(target["rel"])

    print(f"Entity reverse sync: {len(companies)} companies / {company_associations} current-affiliation links; {len(project_nodes)} project-community nodes / {project_associations} contribution links; {len(touched)} files updated; {len(unresolved)} unresolved source values; {len(noncompanies)} non-company affiliation targets recognized.")
    for rel in touched[:120]:
        print("UPDATE:", rel)
    if len(touched) > 120:
        print(f"... plus {len(touched) - 120} more updated files")
    for item in unresolved[:120]:
        print("UNRESOLVED:", item)
    if len(unresolved) > 120:
        print(f"... plus {len(unresolved) - 120} more unresolved values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
