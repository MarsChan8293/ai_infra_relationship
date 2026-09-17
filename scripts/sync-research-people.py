#!/usr/bin/env python3
"""Synchronize research-institution -> person reverse relationships.

Person `current_affiliations:` remains the source of truth. Values that resolve
uniquely to a `research-institution` node are mirrored into that institution's
`linked_people:` plus a generated Markdown section. Curated `people:` and all
hand-written narrative are preserved.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
AUTO_START = "<!-- BEGIN AUTO RESEARCH PEOPLE -->"
AUTO_END = "<!-- END AUTO RESEARCH PEOPLE -->"
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")

COMMON_ALIASES = {
    "微软亚洲研究院": ["Microsoft Research Asia", "MSRA"],
    "北京智源人工智能研究院": ["BAAI", "Beijing Academy of Artificial Intelligence"],
    "MADSys": ["MADSys Lab", "MADSys Group", "MADSys Lab, Tsinghua University"],
    "PACMAN": ["PACMAN Lab", "PACMAN Group", "PACMAN Lab, Tsinghua University"],
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
    return lines[1:end], "\n".join(lines[end + 1:]) + tail


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
        if not inserted and existing in {"areas", "labs", "projects", "website", "country", "city", "last_verified"}:
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


def build_index(records: list[dict]):
    institutions = [r for r in records if r["type"] == "research-institution"]
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for institution in institutions:
        ids[fold(institution["id"])] = institution
        seen = set()
        for value in aliases_for(institution):
            token = fold(value)
            if token and token not in seen:
                seen.add(token)
                aliases[token].append(institution)
    return institutions, aliases, ids


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


def display_name(person: dict) -> str:
    name, english = person["name"], person["english_name"]
    return f"{name}（{english}）" if english and fold(name) != fold(english) else name


def body_detail(person: dict, institution: dict) -> str | None:
    aliases = aliases_for(institution)
    preferred = ("当前", "工作", "研究", "经历", "简介")
    active_heading = ""
    for raw in person["body"].splitlines():
        stripped = raw.strip()
        if stripped.startswith("## "):
            active_heading = stripped[3:].strip().casefold()
            continue
        if not stripped.startswith("-") or not any(token in active_heading for token in preferred):
            continue
        folded = fold(stripped)
        if any(fold(alias) in folded for alias in aliases):
            detail = stripped.lstrip("- ").strip()
            return detail[:237].rstrip() + "..." if len(detail) > 240 else detail
    return None


def generated_section(institution: dict, people: list[dict]) -> str | None:
    if not people:
        return None
    lines = [
        AUTO_START,
        "## 关联人物（自动汇总）",
        "",
        "以下人物由其 `current_affiliations:` 反向汇总，仅表示当前公开的研究机构 affiliation，不自动推断同组、导师、直属汇报或共同项目关系。",
        "",
    ]
    for person in people:
        detail = body_detail(person, institution)
        lines.append(f"- [[{person['id']}|{display_name(person)}]]：{detail or '研究机构 affiliation；具体角色与时间以人物页公开来源为准。'}")
    lines.extend(["", AUTO_END])
    return "\n".join(lines)


def replace_auto_section(body: str, section: str | None) -> str:
    pattern = re.compile(re.escape(AUTO_START) + r".*?" + re.escape(AUTO_END), flags=re.DOTALL)
    if section is None:
        return re.sub(r"\n{3,}", "\n\n", pattern.sub("", body, count=1)).rstrip() + "\n"
    if pattern.search(body):
        updated = pattern.sub(section, body, count=1)
        return updated if updated.endswith("\n") else updated + "\n"
    return body.rstrip() + "\n\n" + section + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    institutions, aliases, ids = build_index(records)
    people = [r for r in records if r["type"] == "person"]
    reverse: dict[str, list[dict]] = defaultdict(list)

    for person in people:
        seen = set()
        for value in get_values(person["fm"], "current_affiliations"):
            institution = resolve(value, aliases, ids)
            if institution and institution["id"] not in seen:
                reverse[institution["id"]].append(person)
                seen.add(institution["id"])

    touched, associations = [], 0
    for institution in institutions:
        linked = sorted(reverse.get(institution["id"], []), key=lambda row: row["id"].casefold())
        associations += len(linked)
        updated_fm = set_block_list(institution["fm"], "linked_people", [p["id"] for p in linked])
        updated_body = replace_auto_section(institution["body"], generated_section(institution, linked))
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != institution["text"]:
            institution["path"].write_text(updated, encoding="utf-8")
            touched.append(institution["rel"])

    print(f"Research reverse sync: {len(institutions)} institutions, {associations} institution-person links, {len(touched)} files updated.")
    for rel in touched:
        print("UPDATE:", rel)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
