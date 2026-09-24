#!/usr/bin/env python3
"""Audit research-institution -> person reverse relationships."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
AUTO_START = "<!-- BEGIN AUTO RESEARCH PEOPLE -->"
AUTO_END = "<!-- END AUTO RESEARCH PEOPLE -->"
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
            result.append((None, [lines[i]])); i += 1; continue
        j = i + 1
        while j < len(lines) and key_of(lines[j]) is None:
            j += 1
        result.append((key, lines[i:j])); i = j
    return result


def parse_inline_list(body: str) -> list[str]:
    if not body.strip(): return []
    parts, buf, quote = [], [], None
    for ch in body:
        if ch in "\"'":
            if quote == ch: quote = None
            elif quote is None: quote = ch
            buf.append(ch)
        elif ch == "," and quote is None:
            parts.append("".join(buf).strip()); buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf).strip())
    return [p.strip().strip("\"'") for p in parts if p.strip()]


def get_block(lines: list[str], wanted: str):
    return next((block for key, block in blocks(lines) if key == wanted), None)


def get_values(lines: list[str], wanted: str) -> list[str]:
    block = get_block(lines, wanted)
    if not block: return []
    value = block[0].split(":", 1)[1].strip()
    if not value:
        return [line[4:].strip().strip("\"'") for line in block[1:] if line.startswith("  - ") and line[4:].strip()]
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value[1:-1])
    return [value.strip("\"'")]


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block: return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def load_records(root: pathlib.Path):
    rows = []
    for dirname in NODE_ROOTS:
        base = root / dirname
        if not base.exists(): continue
        for path in sorted(base.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm, body = split_frontmatter(text)
            if not fm: continue
            rel = path.relative_to(root).as_posix()
            rows.append({"rel": rel, "id": rel[:-3], "fm": fm, "body": body, "type": get_scalar(fm, "type") or "", "name": get_scalar(fm, "name") or path.stem})
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
                seen.add(token); aliases[token].append(institution)
    return institutions, aliases, ids


def resolve(value: str, aliases, ids):
    value = norm(value)
    direct = ids.get(fold(value))
    if direct: return direct
    for candidate in (value, pathlib.PurePosixPath(value).name):
        unique = {r["id"]: r for r in aliases.get(fold(candidate), [])}
        if len(unique) == 1: return next(iter(unique.values()))
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
    institutions, aliases, ids = build_index(records)
    people = [r for r in records if r["type"] == "person"]
    expected: dict[str, set[str]] = defaultdict(set)
    for person in people:
        for value in get_values(person["fm"], "current_affiliations"):
            institution = resolve(value, aliases, ids)
            if institution:
                expected[institution["id"]].add(person["id"])

    errors, rows = [], []
    for institution in institutions:
        want = sorted(expected.get(institution["id"], set()), key=str.casefold)
        have = sorted(get_values(institution["fm"], "linked_people"), key=str.casefold)
        if want != have:
            errors.append({"kind": "research-linked-people-mismatch", "institution": institution["rel"], "expected": want, "actual": have})
        block = generated_block(institution["body"])
        if want and block is None:
            errors.append({"kind": "research-auto-section-missing", "institution": institution["rel"]}); block = ""
        if not want and block is not None:
            errors.append({"kind": "research-stale-auto-section", "institution": institution["rel"]})
        missing = [pid for pid in want if f"[[{pid}|" not in (block or "") and f"[[{pid}]]" not in (block or "")]
        if missing:
            errors.append({"kind": "research-auto-body-missing", "institution": institution["rel"], "people": missing})
        rows.append({"id": institution["id"], "name": institution["name"], "linked_people": len(want)})

    associations = sum(r["linked_people"] for r in rows)
    with_people = sum(1 for r in rows if r["linked_people"])
    payload = {"research_institution_nodes": len(institutions), "institutions_with_linked_people": with_people, "research_person_associations": associations, "errors": errors, "rows": sorted(rows, key=lambda r: (-r["linked_people"], str(r["name"])))}
    (generated / "research-reverse-coverage.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = ["# Research Institution → Person Reverse Coverage", "", "由 `scripts/audit-research-links.py` 自动生成。反向边来自人物 `current_affiliations:`。", "", f"- Research institution nodes: {len(institutions)}", f"- Institutions with ≥1 linked person: {with_people}", f"- Research-person associations: {associations}", f"- Audit errors: {len(errors)}", "", "| Research institution | Linked people |", "| --- | ---: |"]
    for row in payload["rows"]:
        lines.append(f"| [[{row['id']}\\|{row['name']}]] | {row['linked_people']} |")
    (generated / "research-reverse-coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Research reverse audit: {len(institutions)} institutions, {associations} research-person links, {with_people} institutions with people, {len(errors)} errors.")
    for error in errors[:80]: print("ERROR:", error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
