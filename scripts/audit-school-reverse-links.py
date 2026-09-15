#!/usr/bin/env python3
"""Audit exhaustive school -> person reverse links generated from person `schools:`."""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import re
from collections import defaultdict

AUTO_START = "<!-- BEGIN AUTO SCHOOL PEOPLE -->"
AUTO_END = "<!-- END AUTO SCHOOL PEOPLE -->"


def load_sync_module(root: pathlib.Path):
    path = root / "scripts" / "sync-school-people.py"
    spec = importlib.util.spec_from_file_location("school_people_sync", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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

    sync = load_sync_module(root)
    records = sync.load_records(root)
    schools, aliases, ids = sync.build_school_index(records)
    people = [record for record in records if record["type"] == "person"]

    expected: dict[str, set[str]] = defaultdict(set)
    errors = []
    for person in people:
        for value in sync.get_values(person["fm"], "schools"):
            school = sync.resolve_school(value, aliases, ids)
            if not school:
                errors.append({"kind": "reverse-source-unresolved-school", "person": person["rel"], "school": value})
                continue
            expected[school["id"]].add(person["id"])

    rows = []
    for school in schools:
        want = sorted(expected.get(school["id"], set()), key=str.casefold)
        have = sorted(sync.get_values(school["fm"], "linked_people"), key=str.casefold)
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

        missing_body = [
            person_id
            for person_id in want
            if f"[[{person_id}|" not in block and f"[[{person_id}]]" not in block
        ]
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
    sorted_rows = sorted(rows, key=lambda row: (-row["linked_people"], str(row["school"])))
    payload = {
        "school_nodes": len(schools),
        "schools_with_linked_people": schools_with_people,
        "reverse_person_school_associations": associations,
        "errors": errors,
        "rows": sorted_rows,
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
    for row in sorted_rows:
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
