#!/usr/bin/env python3
"""Synchronize reverse school -> person relationships into school Markdown.

Person Markdown remains the source of truth. This script reads each person's
`schools:` field, resolves canonical school nodes, then writes:

1. `linked_people:` in school frontmatter as the exhaustive derived reverse set.
2. A generated `关联人物（自动汇总）` section in each school Markdown page.

Existing hand-written school narrative and curated `people:` fields are kept.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
AUTO_START = "<!-- BEGIN AUTO SCHOOL PEOPLE -->"
AUTO_END = "<!-- END AUTO SCHOOL PEOPLE -->"
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")

COMMON_ALIASES = {
    "清华大学": ["Tsinghua University"],
    "北京大学": ["Peking University", "PKU"],
    "浙江大学": ["Zhejiang University", "ZJU"],
    "上海交通大学": ["Shanghai Jiao Tong University", "SJTU"],
    "复旦大学": ["Fudan University"],
    "中山大学": ["Sun Yat-sen University"],
    "四川大学": ["Sichuan University"],
    "武汉大学": ["Wuhan University"],
    "北京航空航天大学": ["Beihang University"],
    "上海科技大学": ["ShanghaiTech University", "ShanghaiTech"],
    "西交利物浦大学": ["Xi'an Jiaotong-Liverpool University", "XJTLU"],
    "UC Berkeley": ["University of California, Berkeley", "Berkeley"],
    "Carnegie Mellon University": ["CMU"],
    "University of Chicago": ["UChicago"],
    "UCLA": ["University of California, Los Angeles"],
    "University of Texas at Austin": ["UT Austin"],
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


def parse_listish(block: list[str] | None) -> list[str]:
    if not block:
        return []
    value = block[0].split(":", 1)[1].strip()
    if not value:
        return [
            line[4:].strip().strip("\"'")
            for line in block[1:]
            if line.startswith("  - ") and line[4:].strip()
        ]
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value[1:-1])
    return [value.strip("\"'")]


def get_values(lines: list[str], wanted: str) -> list[str]:
    return parse_listish(get_block(lines, wanted))


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block:
        return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def set_block_list(lines: list[str], key: str, values: list[str]) -> list[str]:
    values = list(dict.fromkeys(value for value in values if value))
    replacement = [f"{key}:"] + [f"  - {json.dumps(value, ensure_ascii=False)}" for value in values]
    out, inserted = [], False
    preferred_after = {"aliases", "labs", "people"}
    for existing, block in blocks(lines):
        out.extend(block)
        if existing == key:
            out = out[: -len(block)]
            if not inserted:
                out.extend(replacement)
                inserted = True
            continue
        if not inserted and existing in preferred_after:
            continue
    if not inserted:
        # Place reverse references near other relationship-oriented fields.
        rebuilt = []
        placed = False
        for existing, block in blocks(out):
            if not placed and existing in {"areas", "country", "city", "website", "last_verified"}:
                rebuilt.extend(replacement)
                placed = True
            rebuilt.extend(block)
        if not placed:
            rebuilt.extend(replacement)
        out = rebuilt
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
        rows.append(
            {
                "path": path,
                "rel": rel,
                "id": rel[:-3],
                "text": text,
                "fm": fm,
                "body": body,
                "type": get_scalar(fm, "type") or "",
                "name": get_scalar(fm, "name") or path.stem,
                "english_name": get_scalar(fm, "english_name") or "",
            }
        )
    return rows


def school_aliases(record: dict) -> list[str]:
    values = [record["name"], pathlib.PurePosixPath(record["id"]).name]
    values.extend(get_values(record["fm"], "aliases"))
    values.extend(COMMON_ALIASES.get(record["name"], []))
    return list(dict.fromkeys(value for value in values if value))


def build_school_index(records: list[dict]):
    schools = [record for record in records if record["type"] == "school"]
    alias_map: dict[str, list[dict]] = defaultdict(list)
    id_map = {}
    for school in schools:
        id_map[fold(school["id"])] = school
        for alias in school_aliases(school):
            alias_map[fold(alias)].append(school)
    return schools, alias_map, id_map


def unique_lookup(index: dict[str, list[dict]], value: str):
    candidates = index.get(fold(value), [])
    return candidates[0] if len(candidates) == 1 else None


def resolve_school(value: str, alias_map, id_map):
    value = norm(value)
    direct = id_map.get(fold(value))
    if direct:
        return direct
    return unique_lookup(alias_map, pathlib.PurePosixPath(value).name) or unique_lookup(alias_map, value)


def education_school_ids(person: dict, alias_map, id_map) -> set[str]:
    result = set()
    for value in get_values(person["fm"], "education"):
        school = resolve_school(value, alias_map, id_map)
        if school:
            result.add(school["id"])
    return result


def link_target(inner: str) -> str:
    return norm(inner.split("|", 1)[0].split("#", 1)[0].strip())


def body_detail(person: dict, school: dict, alias_map, id_map) -> str | None:
    """Return a concise existing education/academic bullet when safely available."""
    active_heading = ""
    for raw in person["body"].splitlines():
        stripped = raw.strip()
        if stripped.startswith("## "):
            active_heading = stripped[3:].strip().casefold()
            continue
        if not stripped.startswith("-"):
            continue
        if not any(token in active_heading for token in ("教育", "education", "学术", "经历")):
            continue
        matched = False
        for match in WIKILINK_RE.finditer(stripped):
            resolved = resolve_school(link_target(match.group(1)), alias_map, id_map)
            if resolved and resolved["id"] == school["id"]:
                matched = True
                break
        if not matched:
            folded_line = fold(stripped)
            matched = any(fold(alias) in folded_line for alias in school_aliases(school))
        if matched:
            detail = stripped.lstrip("- ").strip()
            if len(detail) > 220:
                detail = detail[:217].rstrip() + "..."
            return detail
    return None


def display_name(person: dict) -> str:
    name = person["name"]
    english = person["english_name"]
    if english and fold(name) != fold(english):
        return f"{name}（{english}）"
    return name


def generated_section(school: dict, people: list[dict], alias_map, id_map) -> str:
    lines = [AUTO_START, "## 关联人物（自动汇总）", ""]
    if not people:
        lines.append("当前尚无人物节点通过 `schools:` 明确关联到本校。")
    else:
        lines.append(
            "以下关系由人物页 `schools:` 反向汇总。它只表示已公开核验的教育、访问、任职或研究关联，"
            "不会因为同校自动推断同学、导师或合作关系。"
        )
        lines.append("")
        for person in people:
            detail = body_detail(person, school, alias_map, id_map)
            edu_ids = education_school_ids(person, alias_map, id_map)
            if detail:
                description = detail
            elif school["id"] in edu_ids:
                description = "教育关联；人物页 `education` 已明确记录该校。"
            else:
                description = "学术关联；具体属于访问、任职或研究等哪一类，以人物页公开来源为准。"
            lines.append(f"- [[{person['id']}|{display_name(person)}]]：{description}")
    lines.extend(["", AUTO_END])
    return "\n".join(lines)


def replace_auto_section(body: str, section: str) -> str:
    pattern = re.compile(
        re.escape(AUTO_START) + r".*?" + re.escape(AUTO_END),
        flags=re.DOTALL,
    )
    if pattern.search(body):
        updated = pattern.sub(section, body, count=1)
        return updated if updated.endswith("\n") else updated + "\n"
    base = body.rstrip()
    return base + "\n\n" + section + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    schools, alias_map, id_map = build_school_index(records)
    people = [record for record in records if record["type"] == "person"]

    reverse: dict[str, list[dict]] = defaultdict(list)
    unresolved = []
    for person in people:
        seen = set()
        for value in get_values(person["fm"], "schools"):
            school = resolve_school(value, alias_map, id_map)
            if not school:
                unresolved.append((person["rel"], value))
                continue
            if school["id"] in seen:
                continue
            seen.add(school["id"])
            reverse[school["id"]].append(person)

    touched = []
    associations = 0
    for school in schools:
        linked = sorted(reverse.get(school["id"], []), key=lambda row: row["id"].casefold())
        associations += len(linked)
        linked_ids = [person["id"] for person in linked]
        updated_fm = set_block_list(school["fm"], "linked_people", linked_ids)
        section = generated_section(school, linked, alias_map, id_map)
        updated_body = replace_auto_section(school["body"], section)
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != school["text"]:
            school["path"].write_text(updated, encoding="utf-8")
            touched.append(school["rel"])

    print(
        f"School reverse sync: {len(schools)} school pages, {associations} reverse associations, "
        f"{len(touched)} files updated, {len(unresolved)} unresolved person-school values."
    )
    for rel in touched[:100]:
        print("UPDATE:", rel)
    if len(touched) > 100:
        print(f"... plus {len(touched) - 100} more updated files")
    for rel, value in unresolved:
        print("UNRESOLVED:", rel, "->", value)
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
