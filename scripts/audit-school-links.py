#!/usr/bin/env python3
"""Validate and report person -> school coverage.

Absence of a school is not an error: thin contributor nodes may not expose an
education history. Errors are reserved for declared `schools:` values that do
not resolve to canonical school nodes or lack a corresponding Markdown link.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

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


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return [], text
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return [], text
    return lines[1:end], "\n".join(lines[end + 1:])


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


def unique_lookup(index: dict[str, list[dict]], value: str):
    candidates = index.get(fold(value), [])
    return candidates[0] if len(candidates) == 1 else None


def resolve_school(value: str, alias_map, id_map):
    value = norm(value)
    direct = id_map.get(fold(value))
    if direct:
        return direct
    return unique_lookup(alias_map, pathlib.PurePosixPath(value).name) or unique_lookup(alias_map, value)


def body_has_school_link(body: str, school: dict, alias_map, id_map) -> bool:
    for match in WIKILINK_RE.finditer(body):
        resolved = resolve_school(link_target(match.group(1)), alias_map, id_map)
        if resolved and resolved["id"] == school["id"]:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    generated.mkdir(parents=True, exist_ok=True)

    records = load_records(root)
    schools, alias_map, id_map = build_school_index(records)
    people = [record for record in records if record["type"] == "person"]
    metrics_path = generated / "metrics.json"
    metrics = json.loads(metrics_path.read_text(encoding="utf-8")) if metrics_path.exists() else {}

    errors = []
    rows = []
    school_counts = Counter()
    for person in people:
        declared = get_values(person["fm"], "schools")
        resolved = []
        seen = set()
        for value in declared:
            school = resolve_school(value, alias_map, id_map)
            if not school:
                errors.append({
                    "kind": "person-school-unresolved",
                    "source": person["rel"],
                    "school": value,
                })
                continue
            if school["id"] in seen:
                errors.append({
                    "kind": "person-school-duplicate",
                    "source": person["rel"],
                    "school": school["name"],
                })
                continue
            seen.add(school["id"])
            resolved.append(school)
            if not body_has_school_link(person["body"], school, alias_map, id_map):
                errors.append({
                    "kind": "person-school-missing-wikilink",
                    "source": person["rel"],
                    "school": school["name"],
                })

        for school in resolved:
            school_counts[school["name"]] += 1

        metric = metrics.get(person["id"], {})
        rows.append({
            "id": person["id"],
            "name": person["name"],
            "schools": [school["name"] for school in resolved],
            "school_count": len(resolved),
            "bridge_score": metric.get("bridge_score", 0),
            "degree": metric.get("degree", 0),
        })

    with_school = sum(1 for row in rows if row["school_count"] > 0)
    without_school = len(rows) - with_school
    total_associations = sum(row["school_count"] for row in rows)
    coverage = round(with_school / len(rows), 4) if rows else 0.0

    unknown = [row for row in rows if row["school_count"] == 0]
    unknown.sort(key=lambda row: (-row["bridge_score"], -row["degree"], str(row["name"])))
    rows.sort(key=lambda row: str(row["id"]).casefold())

    payload = {
        "person_nodes": len(rows),
        "people_with_school": with_school,
        "people_without_school": without_school,
        "person_school_coverage": coverage,
        "person_school_associations": total_associations,
        "school_nodes": len(schools),
        "errors": errors,
        "school_counts": dict(sorted(school_counts.items(), key=lambda item: (-item[1], item[0]))),
        "rows": rows,
    }
    (generated / "school-coverage.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# School Link Coverage",
        "",
        "由 `scripts/audit-school-links.py` 自动生成。`schools:` 只表示可核验的教育、任职或访问研究关联，"
        "不自动推断导师、同学或同门关系。",
        "",
        f"- Person nodes: {len(rows)}",
        f"- People with ≥1 school: {with_school}",
        f"- People without known school: {without_school}",
        f"- Coverage: {coverage:.1%}",
        f"- Person-school associations: {total_associations}",
        f"- School nodes: {len(schools)}",
        f"- Audit errors: {len(errors)}",
        "",
        "## Top schools by linked people",
        "",
        "| School | People |",
        "| --- | ---: |",
    ]
    for school, count in school_counts.most_common(30):
        safe_school = school.replace("|", "\\|")
        lines.append(f"| {safe_school} | {count} |")
    lines.extend([
        "",
        "## High-value people still missing a verified school association",
        "",
        "| Rank | Person | Bridge score | Degree |",
        "| ---: | --- | ---: | ---: |",
    ])
    for rank, row in enumerate(unknown[:50], 1):
        label = str(row["name"]).replace("|", "\\|")
        lines.append(
            f"| {rank} | [[{row['id']}\\|{label}]] | {row['bridge_score']} | {row['degree']} |"
        )
    (generated / "school-coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"School-link audit: {len(rows)} people, {with_school} with school links "
        f"({coverage:.1%}), {total_associations} associations, {len(errors)} errors."
    )
    for issue in errors[:80]:
        print("ERROR:", issue)
    if len(errors) > 80:
        print(f"... plus {len(errors) - 80} more errors; see {generated / 'school-coverage.json'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
