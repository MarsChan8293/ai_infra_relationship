#!/usr/bin/env python3
"""Audit Concept-to-Project assertions and derived Project reverse links."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import Counter, defaultdict

PROJECT_TYPES = {"project", "community", "project-collection"}


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


def load_records(root: pathlib.Path):
    rows = []
    for dirname in ("community", "concept"):
        base = root / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm, _ = split_frontmatter(text)
            if not fm:
                continue
            rel = path.relative_to(root).as_posix()
            rows.append({
                "rel": rel,
                "id": rel[:-3],
                "fm": fm,
                "type": get_scalar(fm, "type") or "",
                "name": get_scalar(fm, "name") or path.stem,
                "layer": get_scalar(fm, "layer") or "",
                "topic": get_scalar(fm, "topic") or "",
            })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    out = root / args.generated
    out.mkdir(parents=True, exist_ok=True)

    records = load_records(root)
    projects = [r for r in records if r["type"] in PROJECT_TYPES]
    concepts = [r for r in records if r["type"] == "concept"]

    project_aliases, project_ids = build_index(projects)
    concept_by_id = {r["id"]: r for r in concepts}

    expected: dict[str, set[str]] = defaultdict(set)
    unresolved = []
    assertions = 0

    for concept in concepts:
        for value in get_values(concept["fm"], "projects"):
            target, reason, candidates = resolve(value, project_aliases, project_ids)
            if not target:
                unresolved.append({
                    "concept": concept["id"],
                    "value": value,
                    "reason": reason,
                    "candidates": candidates,
                })
                continue
            expected[target["id"]].add(concept["id"])
            assertions += 1

    mismatches = []
    for project in projects:
        actual = set(get_values(project["fm"], "linked_concepts"))
        wanted = expected.get(project["id"], set())
        if actual != wanted:
            mismatches.append({
                "project": project["id"],
                "expected": sorted(wanted),
                "actual": sorted(actual),
                "missing": sorted(wanted - actual),
                "stale": sorted(actual - wanted),
            })

    concepts_without_projects = [
        concept["id"] for concept in concepts
        if not get_values(concept["fm"], "projects")
    ]
    projects_with_concepts = [project for project in projects if expected.get(project["id"])]
    project_counts = sorted(
        (
            {
                "id": project["id"],
                "name": project["name"],
                "layer": project["layer"],
                "concepts": sorted(expected.get(project["id"], set())),
                "count": len(expected.get(project["id"], set())),
            }
            for project in projects_with_concepts
        ),
        key=lambda x: (-x["count"], x["name"].casefold()),
    )

    topic_counts = Counter((concept["topic"] or "other") for concept in concepts)
    mapped_topic_counts = Counter(
        (concept["topic"] or "other")
        for concept in concepts
        if get_values(concept["fm"], "projects")
    )

    status = "pass" if not unresolved and not mismatches else "fail"
    payload = {
        "status": status,
        "summary": {
            "concepts": len(concepts),
            "concepts_with_projects": len(concepts) - len(concepts_without_projects),
            "concepts_without_projects": len(concepts_without_projects),
            "project_like_nodes": len(projects),
            "projects_with_concepts": len(projects_with_concepts),
            "concept_project_assertions": assertions,
            "unresolved_project_refs": len(unresolved),
            "reverse_link_mismatches": len(mismatches),
        },
        "topic_counts": dict(sorted(topic_counts.items())),
        "mapped_topic_counts": dict(sorted(mapped_topic_counts.items())),
        "concepts_without_projects": concepts_without_projects,
        "projects": project_counts,
        "unresolved": unresolved,
        "mismatches": mismatches,
    }
    (out / "project-concept-coverage.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# Project ↔ Concept Coverage",
        "",
        "由 scripts/audit-project-concept-coverage.py 自动生成。Concept 节点的 projects 字段是人工事实源；Project 页的 linked_concepts 是派生反向视图。",
        "",
        f"- Status: **{status}**",
        f"- Concepts: {len(concepts)}",
        f"- Concepts with project evidence: {len(concepts) - len(concepts_without_projects)}",
        f"- Project-like nodes: {len(projects)}",
        f"- Projects linked to concepts: {len(projects_with_concepts)}",
        f"- Concept → Project assertions: {assertions}",
        f"- Unresolved project refs: {len(unresolved)}",
        f"- Reverse-link mismatches: {len(mismatches)}",
        "",
        "## Projects with the densest Concept coverage",
        "",
        "| Project | Layer | Concepts | Count |",
        "| --- | --- | --- | ---: |",
    ]
    for row in project_counts[:40]:
        concepts_text = " · ".join(
            f"[[{cid}|{concept_by_id[cid]['name']}]]"
            for cid in row["concepts"] if cid in concept_by_id
        )
        lines.append(f"| [[{row['id']}|{row['name']}]] | {row['layer']} | {concepts_text} | {row['count']} |")

    lines.extend(["", "## Concepts without project evidence", ""])
    if concepts_without_projects:
        for cid in concepts_without_projects:
            concept = concept_by_id[cid]
            lines.append(f"- [[{cid}|{concept['name']}]]")
    else:
        lines.append("- None")

    lines.extend(["", "## Mapping by topic", "", "| Topic | Concepts | With project evidence |", "| --- | ---: | ---: |"])
    for topic in sorted(topic_counts):
        lines.append(f"| {topic} | {topic_counts[topic]} | {mapped_topic_counts.get(topic, 0)} |")

    if unresolved:
        lines.extend(["", "## Unresolved project references", ""])
        for item in unresolved:
            lines.append(f"- {item['concept']} → {item['value']} ({item['reason']})")

    if mismatches:
        lines.extend(["", "## Reverse-link mismatches", ""])
        for item in mismatches:
            lines.append(f"- {item['project']} missing={item['missing']} stale={item['stale']}")

    (out / "project-concept-coverage.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(
        f"Project-concept coverage: {len(concepts)} concepts, {assertions} assertions, "
        f"{len(projects_with_concepts)} projects, {len(unresolved)} unresolved, {len(mismatches)} mismatches."
    )
    return 1 if unresolved or mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
