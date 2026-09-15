#!/usr/bin/env python3
"""Audit exhaustive school -> person reverse links generated from person `schools:`."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
AUTO_START = "<!-- BEGIN AUTO SCHOOL PEOPLE -->"
AUTO_END = "<!-- END AUTO SCHOOL PEOPLE -->"


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
    return lines[1:end], "\n".join(lines[end + 1 :])


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
        return [
            line[4:].strip().strip("\"'")
            for line in block[1:]
            if line.startswith("  - ") and line[4:].strip()
        ]
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value[1:-1])
    return [value.strip("\"'")]


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block:
        return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


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
                "fm": fm,
                "body": body,
                "type": get_scalar(fm, "type") or "",
                "name": get_scalar(fm, "name") or path.stem,
            }
        )
    return rows


def school_index(records: list[dict]):
    schools = [r for r in records if r["type"] == "school"]
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for school in schools:
        ids[fold(school["id"])] = school
        for value in [school["name"], pathlib.PurePosixPath(school["id"]).name, *get_values(school["fm"], "aliases")]:
            if value:
                aliases[fold(value)].append(school)
    return schools, aliases, ids


def resolve_school(value: str, aliases, ids):
    value = norm(value)
    direct = ids.get(fold(value))
    if direct:
        return direct
    for candidate in (value, pathlib.PurePosixPath(value).name):
        hits = aliases.get(fold(candidate), [])
        if len(hits) == 1:
            return hits[0]
    return None


def generated_block(body: str) -> str | None:
    match = re.search(re.escape(AUTO_START) + r"(.*?)" + re.escape(AUTO_END), body, flags=re.DOTALL)
    return match.group(1) if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    generated = root / args.generated
    generated.mkdir(parents=True, exist_ok=True)

    records = load_records(root)
    schools, aliases, ids = school_index(records)
    people = [r for r in records if r["type"] == "person"]
    expected: dict[str, set[str]] = defaultdict(set)
    errors = []

    for person in people:
        for value in get_values(person["fm"], "schools"):
            school = resolve_school(value, aliases, ids)
            if not school:
                errors.append({"kind": "reverse-source-unresolved-school", "person": person["rel"], "school": value})
                continue
            expected[school["id"]].add(person["id"])

    rows = []
    for school in schools:
        want = sorted(expected.get(school["id"], set()), key=str.casefold)
        have = sorted(get_values(school["fm"], "linked_people"), key=str.casefold)
        block = generated_block(school["body"])
        missing_frontmatter = sorted(set(want) - set(have))
        extra_frontmatter = sorted(set(have) - set(want))
        if missing_frontmatter:
            errors.append({"kind": "school-linked-people-missing", "school": school["rel"], "people": missing_frontmatter})
        if extra_frontmatter:
            errors.append({"kind": "school-linked-people-extra", "school": school["rel"], "people": extra_frontmatter})
        if block is None:
            errors.append({"kind": "school-auto-people-section-missing", "school": school["rel"]})
            block = ""
        missing_body = [person_id for person_id in want if f"[[{person_id}|" not in block and f"[[{person_id}]]" not in block]
        if missing_body:
            errors.append({"kind": "school-auto-people-body-missing", "school": school["rel"], "people": missing_body})
        rows.append({
            "school": school["name"],
            "id": school["id"],
            "linked_people": len(want),
            "frontmatter_people": len(have),
            "body_people": len(want) - len(missing_body),
        })

    associations = sum(row["linked_people"] for row in rows)
    schools_with_people = sum(1 for row in rows if row["linked_people"])
    payload = {
        "school_nodes": len(schools),
        "schools_with_linked_people": schools_with_people,
        "reverse_person_school_associations": associations,
        "errors": errors,
        "rows": sorted(rows, key=lambda row: (-row["linked_people"], str(row["school"]))),
    }
    (generated / "school-reverse-coverage.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# School → Person Reverse Coverage",
        "",
        "由 `scripts/audit-school-reverse-links.py` 自动生成。反向关系以人物页 `schools:` 为唯一事实源。",
        "",
        f"- School nodes: {len(schools)}",
        f"- Schools with ≥1 linked person: {schools_with_people}",
        f"- Reverse person-school associations: {associations}",
        f"- Audit errors: {len(errors)}",
        "",
        "| School | Linked people |",
        "| --- | ---: |",
    ]
    for row in payload["rows"]:
        lines.append(f"| [[{row['id']}|{row['school']}]] | {row['linked_people']} |")
    (generated / "school-reverse-coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"School reverse audit: {len(schools)} schools, {associations} associations, "
        f"{schools_with_people} schools with people, {len(errors)} errors."
    )
    for error in errors[:80]:
        print("ERROR:", error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
