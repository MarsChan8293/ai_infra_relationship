#!/usr/bin/env python3
"""Backfill explicit person -> school associations without inventing education.

Markdown remains the source of truth. The migration only uses evidence already
present in the repository: school-page backlinks, a person's own education /
career sections, current academic affiliations, or a canonical person page
stored below a school directory. It never infers advisor/classmate relations.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
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
OWN_SECTION_HINTS = (
    "教育", "education", "academic", "学习", "工作经历", "career",
    "research experience", "经历", "履历",
)
SKIP_SECTION_HINTS = ("人物关系", "relationship", "sources", "参考", "项目关系")


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


def parse_listish(block: list[str]) -> list[str]:
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
        body = value[1:-1].strip()
        if not body:
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
    return [value.strip("\"'")]


def get_block(lines: list[str], wanted: str):
    return next((block for key, block in blocks(lines) if key == wanted), None)


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block:
        return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def get_values(lines: list[str], wanted: str) -> list[str]:
    block = get_block(lines, wanted)
    return parse_listish(block) if block else []


def set_block_list(lines: list[str], key: str, values: list[str]) -> list[str]:
    values = list(dict.fromkeys(value for value in values if value))
    replacement = [f"{key}:"] + [f"  - {json.dumps(value, ensure_ascii=False)}" for value in values]
    out, inserted = [], False
    for existing, block in blocks(lines):
        if existing == key:
            if not inserted:
                out.extend(replacement)
                inserted = True
            continue
        if not inserted and existing in {"communities", "projects", "areas", "roles", "relations"}:
            out.extend(replacement)
            inserted = True
        out.extend(block)
    if not inserted:
        out.extend(replacement)
    return out


def norm(value: str) -> str:
    return value.replace("\\", "/").strip().strip("/").removesuffix(".md")


def fold(value: str) -> str:
    return re.sub(r"\s+", " ", norm(value)).casefold()


def link_target(inner: str) -> str:
    return norm(inner.split("|", 1)[0].split("#", 1)[0].strip())


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
        })
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


def build_person_index(records: list[dict]):
    people = [record for record in records if record["type"] == "person"]
    aliases: dict[str, list[dict]] = defaultdict(list)
    by_id = {}
    for person in people:
        by_id[fold(person["id"])] = person
        candidates = [
            person["name"],
            pathlib.PurePosixPath(person["id"]).name,
            get_scalar(person["fm"], "english_name"),
            *get_values(person["fm"], "aliases"),
        ]
        for candidate in candidates:
            if candidate:
                aliases[fold(candidate)].append(person)
    return people, aliases, by_id


def unique_lookup(index: dict[str, list[dict]], value: str):
    candidates = index.get(fold(value), [])
    return candidates[0] if len(candidates) == 1 else None


def resolve_school(value: str, alias_map, id_map):
    value = norm(value)
    direct = id_map.get(fold(value))
    if direct:
        return direct
    base = pathlib.PurePosixPath(value).name
    return unique_lookup(alias_map, base) or unique_lookup(alias_map, value)


def resolve_person(value: str, alias_map, id_map):
    value = norm(value)
    direct = id_map.get(fold(value))
    if direct:
        return direct
    base = pathlib.PurePosixPath(value).name
    return unique_lookup(alias_map, base) or unique_lookup(alias_map, value)


def has_ascii(value: str) -> bool:
    return any(ord(ch) < 128 and ch.isalpha() for ch in value)


def contains_alias(text: str, alias: str) -> bool:
    if not alias:
        return False
    if not has_ascii(alias):
        return alias in text
    if len(alias) < 4 and alias.upper() not in {"PKU", "ZJU", "SJTU", "CMU"}:
        return False
    return re.search(r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])", text, re.I) is not None


def own_context(body: str) -> str:
    """Return intro + education/career sections, excluding relationship/source sections."""
    lines = body.splitlines()
    kept = []
    current = "intro"
    include = True
    for line in lines:
        if line.startswith("## "):
            current = line[3:].strip()
            lowered = current.casefold()
            include = (
                any(h.casefold() in lowered for h in OWN_SECTION_HINTS)
                and not any(h.casefold() in lowered for h in SKIP_SECTION_HINTS)
            )
            continue
        if line.startswith("# "):
            continue
        if current == "intro" or include:
            kept.append(line)
    return "\n".join(kept)


def infer_person_schools(person: dict, schools, school_alias_map, school_id_map, reverse: dict[str, set[str]]):
    found: dict[str, str] = {}

    def add(school: dict | None, reason: str):
        if school:
            found.setdefault(school["id"], reason)

    for value in get_values(person["fm"], "schools"):
        add(resolve_school(value, school_alias_map, school_id_map), "existing-structured")

    parts = pathlib.PurePosixPath(person["id"]).parts
    if len(parts) >= 3 and parts[0] == "university":
        add(unique_lookup(school_alias_map, parts[1]), "school-directory")

    for value in get_values(person["fm"], "current_affiliations"):
        add(resolve_school(value, school_alias_map, school_id_map), "current-affiliation")

    for school_id in reverse.get(person["id"], set()):
        add(school_id_map.get(fold(school_id)), "school-backlink")

    context = own_context(person["body"])
    for school in schools:
        if school["id"] in found:
            continue
        for alias in school_aliases(school):
            if contains_alias(context, alias):
                add(school, "person-education-or-career-text")
                break

    return found


def build_reverse_school_links(schools, person_alias_map, person_id_map):
    reverse: dict[str, set[str]] = defaultdict(set)
    for school in schools:
        for match in WIKILINK_RE.finditer(school["body"]):
            person = resolve_person(link_target(match.group(1)), person_alias_map, person_id_map)
            if person:
                reverse[person["id"]].add(school["id"])
    return reverse


def body_has_school_link(body: str, school: dict, school_alias_map, school_id_map) -> bool:
    for match in WIKILINK_RE.finditer(body):
        resolved = resolve_school(link_target(match.group(1)), school_alias_map, school_id_map)
        if resolved and resolved["id"] == school["id"]:
            return True
    return False


def add_school_section(body: str, missing: list[dict]) -> str:
    if not missing:
        return body
    bullets = [
        f"- [[{school['id']}|{school['name']}]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。"
        for school in missing
    ]
    lines = body.rstrip().splitlines()

    for i, line in enumerate(lines):
        if line.strip() == "## 学校关联":
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            insertion = ([] if j == i + 1 or (j > i + 1 and lines[j - 1] == "") else [""]) + bullets
            lines[j:j] = insertion
            return "\n".join(lines).rstrip() + "\n"

    source_index = next((i for i, line in enumerate(lines) if line.strip() == "## Sources"), len(lines))
    section = ["", "## 学校关联", *bullets, ""]
    lines[source_index:source_index] = section
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    schools, school_alias_map, school_id_map = build_school_index(records)
    people, person_alias_map, person_id_map = build_person_index(records)
    reverse = build_reverse_school_links(schools, person_alias_map, person_id_map)
    school_by_id = {school["id"]: school for school in schools}

    touched = []
    association_count = 0
    linked_count = 0
    for person in people:
        associations = infer_person_schools(person, schools, school_alias_map, school_id_map, reverse)
        if not associations:
            continue

        canonical_schools = [school_by_id[school_id]["name"] for school_id in sorted(associations)]
        fm = set_block_list(person["fm"], "schools", canonical_schools)
        missing_links = [
            school_by_id[school_id]
            for school_id in sorted(associations)
            if not body_has_school_link(person["body"], school_by_id[school_id], school_alias_map, school_id_map)
        ]
        body = add_school_section(person["body"], missing_links)
        updated = join_frontmatter(fm, body)

        association_count += len(associations)
        linked_count += len(missing_links)
        if updated != person["text"]:
            person["path"].write_text(updated, encoding="utf-8")
            touched.append(person["rel"])

    print(
        f"School-link repair: {len(people)} people scanned, "
        f"{association_count} structured person-school associations, "
        f"{linked_count} body links added, {len(touched)} files updated."
    )
    for rel in touched[:80]:
        print("UPDATE:", rel)
    if len(touched) > 80:
        print(f"... plus {len(touched) - 80} more updated files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
