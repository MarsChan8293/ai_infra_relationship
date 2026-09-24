#!/usr/bin/env python3
"""Synchronize Concept -> Project assertions into derived Project reverse links.

Human-authored source of truth:
- concept pages: `projects:`

Derived Project views:
- `linked_concepts:` frontmatter
- marked "关联概念（自动汇总）" Markdown section

The script never infers Concept relationships from Project `areas` or prose keywords.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

PROJECT_TYPES = {"project", "community", "project-collection"}
CONCEPT_START = "<!-- BEGIN AUTO PROJECT CONCEPTS -->"
CONCEPT_END = "<!-- END AUTO PROJECT CONCEPTS -->"


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
    insertion_before = {
        "areas", "hardware", "integrations", "companies", "company_relation",
        "layer", "status", "repository", "docs", "last_verified",
    }
    for existing, block in blocks(lines):
        if existing == key:
            if not inserted:
                out.extend(replacement)
                inserted = True
            continue
        if not inserted and existing in insertion_before:
            out.extend(replacement)
            inserted = True
        out.extend(block)
    if not inserted:
        out.extend(replacement)
    return out


def aliases_for(record: dict) -> list[str]:
    return list(dict.fromkeys([
        record["name"],
        pathlib.PurePosixPath(record["id"]).name,
        *get_values(record["fm"], "aliases"),
    ]))


def build_index(records: list[dict]):
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for record in records:
        ids[fold(record["id"])] = record
        seen = set()
        for value in aliases_for(record):
            token = fold(value)
            if token and token not in seen:
                aliases[token].append(record)
                seen.add(token)
    return aliases, ids


def resolve(value: str, aliases, ids):
    value = norm(value)
    direct = ids.get(fold(value))
    if direct:
        return direct, "id", []
    for candidate in (value, pathlib.PurePosixPath(value).name):
        unique = {r["id"]: r for r in aliases.get(fold(candidate), [])}
        if len(unique) == 1:
            return next(iter(unique.values())), "alias", []
        if len(unique) > 1:
            return None, "ambiguous", sorted(unique)
    return None, "missing", []


def replace_auto_section(body: str, section: str | None) -> str:
    pattern = re.compile(re.escape(CONCEPT_START) + r".*?" + re.escape(CONCEPT_END), flags=re.DOTALL)
    if section is None:
        updated = pattern.sub("", body, count=1)
        return re.sub(r"\n{3,}", "\n\n", updated).rstrip() + "\n"
    if pattern.search(body):
        updated = pattern.sub(section, body, count=1)
        return updated if updated.endswith("\n") else updated + "\n"
    return body.rstrip() + "\n\n" + section + "\n"


def project_section(concepts: list[dict]) -> str | None:
    if not concepts:
        return None
    lines = [
        CONCEPT_START,
        "## 关联概念（自动汇总）",
        "",
        "以下概念由 canonical Concept 节点的 `projects:` 反向汇总。"
        "它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；"
        "本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。",
        "",
    ]
    for concept in sorted(concepts, key=lambda r: r["name"].casefold()):
        lines.append(f"- [[{concept['id']}|{concept['name']}]]")
    lines.extend(["", CONCEPT_END])
    return "\n".join(lines)


def load_records(root: pathlib.Path):
    rows = []
    for dirname in ("community", "concept"):
        base = root / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
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
            })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    projects = [r for r in records if r["type"] in PROJECT_TYPES]
    concepts = [r for r in records if r["type"] == "concept"]
    project_aliases, project_ids = build_index(projects)

    reverse: dict[str, list[dict]] = defaultdict(list)
    errors = []
    links = 0

    for concept in concepts:
        seen = set()
        for value in get_values(concept["fm"], "projects"):
            target, reason, candidates = resolve(value, project_aliases, project_ids)
            if not target:
                errors.append({
                    "concept": concept["rel"],
                    "value": value,
                    "reason": reason,
                    "candidates": candidates,
                })
                continue
            if target["id"] in seen:
                continue
            seen.add(target["id"])
            reverse[target["id"]].append(concept)
            links += 1

    if errors:
        print(f"Project-concept sync aborted: {len(errors)} unresolved/ambiguous project references.")
        for item in errors[:80]:
            extra = f" candidates={item['candidates']}" if item["candidates"] else ""
            print(f"- {item['concept']}: {item['value']} ({item['reason']}){extra}")
        return 1

    touched = []
    for project in projects:
        concept_rows = reverse.get(project["id"], [])
        linked_ids = [row["id"] for row in sorted(concept_rows, key=lambda r: r["name"].casefold())]
        new_fm = set_block_list(project["fm"], "linked_concepts", linked_ids)
        new_body = replace_auto_section(project["body"], project_section(concept_rows))
        updated = join_frontmatter(new_fm, new_body)
        if updated != project["text"]:
            project["path"].write_text(updated, encoding="utf-8")
            touched.append(project["rel"])

    print(
        f"Project-concept sync: {len(concepts)} concepts, {len(projects)} project-like nodes, "
        f"{links} assertions, {len(reverse)} projects linked, {len(touched)} files updated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
