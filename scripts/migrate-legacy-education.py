#!/usr/bin/env python3
"""Migrate legacy person `education:` values into canonical `schools:` edges.

The repository already asserted these institutions in person frontmatter, so this
script does not research or invent education. It only normalizes known aliases,
creates missing minimal school nodes, and merges canonical school names into the
person's `schools:` field. `repair-school-links.py` then adds any missing body
wikilinks and `audit-school-links.py` validates the result.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")

CANONICAL = {
    "tsinghua university": "清华大学",
    "peking university": "北京大学",
    "pku": "北京大学",
    "zhejiang university": "浙江大学",
    "zju": "浙江大学",
    "shanghai jiao tong university": "上海交通大学",
    "sjtu": "上海交通大学",
    "fudan university": "复旦大学",
    "sun yat-sen university": "中山大学",
    "sichuan university": "四川大学",
    "wuhan university": "武汉大学",
    "beihang university": "北京航空航天大学",
    "shanghaitech university": "上海科技大学",
    "shanghaitech": "上海科技大学",
    "xi'an jiaotong-liverpool university": "西交利物浦大学",
    "xjtlu": "西交利物浦大学",
    "university of california, berkeley": "UC Berkeley",
    "berkeley": "UC Berkeley",
    "university of california, los angeles": "UCLA",
    "university of texas at austin": "University of Texas at Austin",
    "ut austin": "University of Texas at Austin",
    "university of chicago": "University of Chicago",
    "uchicago": "University of Chicago",
    "carnegie mellon university": "Carnegie Mellon University",
    "cmu": "Carnegie Mellon University",
    "northwestern polytechnical university": "西北工业大学",
    "nwpu": "西北工业大学",
    "university of electronic science and technology of china": "电子科技大学",
    "uestc": "电子科技大学",
    "huazhong university of science and technology": "华中科技大学",
    "hust": "华中科技大学",
    "xiamen university": "厦门大学",
    "xmu": "厦门大学",
}

KNOWN_COMMA_NAMES = {
    "University of California, Berkeley",
    "University of Tennessee, Knoxville",
}


def fold(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


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
    parts = [part.strip().strip("\"'") for part in parts if part.strip()]

    merged, i = [], 0
    while i < len(parts):
        if i + 1 < len(parts):
            candidate = f"{parts[i]}, {parts[i + 1]}"
            if candidate in KNOWN_COMMA_NAMES:
                merged.append(candidate)
                i += 2
                continue
        merged.append(parts[i])
        i += 1
    return merged


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


def get_block(lines: list[str], wanted: str):
    return next((block for key, block in blocks(lines) if key == wanted), None)


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block:
        return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def get_values(lines: list[str], wanted: str) -> list[str]:
    return parse_listish(get_block(lines, wanted))


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
        rows.append({
            "path": path,
            "text": text,
            "fm": fm,
            "body": body,
            "type": get_scalar(fm, "type") or "",
            "name": get_scalar(fm, "name") or path.stem,
        })
    return rows


def school_alias_index(records: list[dict]):
    by_alias: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        if record["type"] != "school":
            continue
        aliases = [record["name"], *get_values(record["fm"], "aliases")]
        for alias in aliases:
            by_alias[fold(alias)].append(record)
    return by_alias


def resolve_school(value: str, alias_index):
    candidates = alias_index.get(fold(value), [])
    if len(candidates) == 1:
        return candidates[0]
    canonical = CANONICAL.get(fold(value))
    if canonical:
        candidates = alias_index.get(fold(canonical), [])
        if len(candidates) == 1:
            return candidates[0]
    return None


def canonical_name(value: str) -> str:
    return CANONICAL.get(fold(value), value.strip())


def safe_component(value: str) -> str:
    return value.replace("/", "／").strip()


def create_school_node(root: pathlib.Path, canonical: str, original: str) -> pathlib.Path:
    component = safe_component(canonical)
    path = root / "university" / component / f"{component}.md"
    if path.exists():
        return path
    aliases = [] if fold(original) == fold(canonical) else [original]
    lines = ["---", "type: school", f"name: {json.dumps(canonical, ensure_ascii=False)}"]
    if aliases:
        lines.append("aliases:")
        lines.extend(f"  - {json.dumps(alias, ensure_ascii=False)}" for alias in aliases)
    lines.extend([
        "---",
        f"# {canonical}",
        "",
        "## 图谱说明",
        "本节点由仓库中已有的人物 `education` 元数据补齐，用于建立人物与学校的可计算关联。具体教育阶段、学位与时间以对应人物页及其公开来源为准。",
        "",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = load_records(root)
    alias_index = school_alias_index(records)
    education_values = []
    for record in records:
        if record["type"] == "person":
            education_values.extend(get_values(record["fm"], "education"))

    created = []
    for value in dict.fromkeys(v for v in education_values if v):
        if resolve_school(value, alias_index):
            continue
        canonical = canonical_name(value)
        path = create_school_node(root, canonical, value)
        created.append(path.relative_to(root).as_posix())
        records = load_records(root)
        alias_index = school_alias_index(records)

    records = load_records(root)
    alias_index = school_alias_index(records)
    touched, migrated = [], 0
    unresolved = []
    for record in records:
        if record["type"] != "person":
            continue
        education = get_values(record["fm"], "education")
        if not education:
            continue
        schools = get_values(record["fm"], "schools")
        canonical_schools = list(schools)
        for value in education:
            school = resolve_school(value, alias_index)
            if not school:
                unresolved.append((record["path"].relative_to(root).as_posix(), value))
                continue
            if school["name"] not in canonical_schools:
                canonical_schools.append(school["name"])
                migrated += 1
        updated_fm = set_block_list(record["fm"], "schools", canonical_schools)
        updated = join_frontmatter(updated_fm, record["body"])
        if updated != record["text"]:
            record["path"].write_text(updated, encoding="utf-8")
            touched.append(record["path"].relative_to(root).as_posix())

    print(
        f"Legacy education migration: {len(created)} school nodes created, "
        f"{migrated} person-school associations added, {len(touched)} person files updated, "
        f"{len(unresolved)} unresolved education values."
    )
    for rel in created:
        print("CREATE:", rel)
    for rel in touched[:80]:
        print("UPDATE:", rel)
    if len(touched) > 80:
        print(f"... plus {len(touched) - 80} more updated files")
    for rel, value in unresolved:
        print("UNRESOLVED:", rel, "->", value)
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
