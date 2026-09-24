#!/usr/bin/env python3
"""Audit derived company/project/community -> person reverse links.

Company-person associations are the union of:
- person `current_affiliations:` that resolve to company nodes;
- person `email_affiliations:` generated from mapped public professional email domains.

The audit also verifies each person's generated `linked_companies:` canonical mirror.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
PROJECT_TYPES = {"project", "community", "project-collection"}
NON_COMPANY_AFFILIATION_TYPES = {"school", "research-institution", "model-team"}
COMPANY_START = "<!-- BEGIN AUTO COMPANY PEOPLE -->"
COMPANY_END = "<!-- END AUTO COMPANY PEOPLE -->"
PROJECT_START = "<!-- BEGIN AUTO PROJECT PEOPLE -->"
PROJECT_END = "<!-- END AUTO PROJECT PEOPLE -->"
PERSON_COMPANY_START = "<!-- BEGIN AUTO PERSON COMPANIES -->"
PERSON_COMPANY_END = "<!-- END AUTO PERSON COMPANIES -->"
COMMON_ALIASES = {
    "清华大学": ["Tsinghua University"],
    "北京大学": ["Peking University", "PKU"],
    "上海交通大学": ["Shanghai Jiao Tong University", "SJTU"],
    "浙江大学": ["Zhejiang University", "ZJU"],
    "UC Berkeley": ["University of California, Berkeley", "Berkeley"],
    "北京智源人工智能研究院": ["BAAI", "Beijing Academy of Artificial Intelligence"],
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


def load_records(root: pathlib.Path):
    rows = []
    for dirname in NODE_ROOTS:
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
                "rel": rel,
                "id": rel[:-3],
                "fm": fm,
                "body": body,
                "type": get_scalar(fm, "type") or "",
                "name": get_scalar(fm, "name") or path.stem,
            })
    return rows


def aliases_for(record: dict) -> list[str]:
    values = [record["name"], pathlib.PurePosixPath(record["id"]).name, *get_values(record["fm"], "aliases")]
    values.extend(COMMON_ALIASES.get(record["name"], []))
    return list(dict.fromkeys(v for v in values if v))


def build_index(records: list[dict], allowed_types: set[str]):
    selected = [r for r in records if r["type"] in allowed_types]
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for record in selected:
        ids[fold(record["id"])] = record
        seen = set()
        for value in aliases_for(record):
            token = fold(value)
            if token and token not in seen:
                seen.add(token)
                aliases[token].append(record)
    return selected, aliases, ids


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


def generated_block(body: str, start: str, end: str) -> str | None:
    match = re.search(re.escape(start) + r"(.*?)" + re.escape(end), body, flags=re.DOTALL)
    return match.group(1) if match else None


def audit_group(targets, expected, start, end, errors, kind):
    rows = []
    for target in targets:
        want = sorted(expected.get(target["id"], set()), key=str.casefold)
        have = sorted(get_values(target["fm"], "linked_people"), key=str.casefold)
        if want != have:
            errors.append({"kind": f"{kind}-linked-people-mismatch", "target": target["rel"], "expected": want, "actual": have})
        block = generated_block(target["body"], start, end)
        if want and block is None:
            errors.append({"kind": f"{kind}-auto-section-missing", "target": target["rel"]})
            block = ""
        if not want and block is not None:
            errors.append({"kind": f"{kind}-stale-auto-section", "target": target["rel"]})
        missing = [pid for pid in want if f"[[{pid}|" not in (block or "") and f"[[{pid}]]" not in (block or "")]
        if missing:
            errors.append({"kind": f"{kind}-auto-body-missing", "target": target["rel"], "people": missing})
        rows.append({"id": target["id"], "name": target["name"], "linked_people": len(want)})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    generated = root / args.generated
    generated.mkdir(parents=True, exist_ok=True)

    records = load_records(root)
    companies, company_aliases, company_ids = build_index(records, {"company"})
    _, noncompany_aliases, noncompany_ids = build_index(records, NON_COMPANY_AFFILIATION_TYPES)
    projects, project_aliases, project_ids = build_index(records, PROJECT_TYPES)
    people = [r for r in records if r["type"] == "person"]

    company_expected: dict[str, set[str]] = defaultdict(set)
    project_expected: dict[str, set[str]] = defaultdict(set)
    unresolved, noncompany_affiliations = [], []
    email_affiliation_links = 0
    person_link_errors = []

    for person in people:
        expected_company_ids = set()

        for value in get_values(person["fm"], "current_affiliations"):
            target = resolve(value, company_aliases, company_ids)
            if target:
                company_expected[target["id"]].add(person["id"])
                expected_company_ids.add(target["id"])
            elif resolve(value, noncompany_aliases, noncompany_ids):
                noncompany_affiliations.append({"person": person["rel"], "value": value})
            else:
                unresolved.append({"kind": "affiliation", "person": person["rel"], "value": value})

        for value in get_values(person["fm"], "email_affiliations"):
            target = resolve(value, company_aliases, company_ids)
            if target:
                company_expected[target["id"]].add(person["id"])
                expected_company_ids.add(target["id"])
                email_affiliation_links += 1
            else:
                unresolved.append({"kind": "email_affiliation", "person": person["rel"], "value": value})

        expected_links = sorted(expected_company_ids, key=str.casefold)
        actual_links = sorted(get_values(person["fm"], "linked_companies"), key=str.casefold)
        if expected_links != actual_links:
            person_link_errors.append({
                "kind": "person-linked-companies-mismatch",
                "person": person["rel"],
                "expected": expected_links,
                "actual": actual_links,
            })
        person_block = generated_block(person["body"], PERSON_COMPANY_START, PERSON_COMPANY_END)
        if expected_links and person_block is None:
            person_link_errors.append({"kind": "person-company-auto-section-missing", "person": person["rel"]})
            person_block = ""
        if not expected_links and person_block is not None:
            person_link_errors.append({"kind": "person-company-stale-auto-section", "person": person["rel"]})
        missing_company_links = [
            company_id for company_id in expected_links
            if f"[[{company_id}|" not in (person_block or "") and f"[[{company_id}]]" not in (person_block or "")
        ]
        if missing_company_links:
            person_link_errors.append({
                "kind": "person-company-auto-body-missing",
                "person": person["rel"],
                "companies": missing_company_links,
            })

        for field in ("projects", "project", "communities", "community"):
            for value in get_values(person["fm"], field):
                target = resolve(value, project_aliases, project_ids)
                if target:
                    project_expected[target["id"]].add(person["id"])
                else:
                    unresolved.append({"kind": field, "person": person["rel"], "value": value})

    errors = list(person_link_errors)
    company_rows = audit_group(companies, company_expected, COMPANY_START, COMPANY_END, errors, "company")
    project_rows = audit_group(projects, project_expected, PROJECT_START, PROJECT_END, errors, "project-community")
    company_links = sum(r["linked_people"] for r in company_rows)
    project_links = sum(r["linked_people"] for r in project_rows)

    payload = {
        "company_nodes": len(companies),
        "companies_with_linked_people": sum(1 for r in company_rows if r["linked_people"]),
        "company_person_associations": company_links,
        "email_affiliation_associations": email_affiliation_links,
        "people_with_linked_companies": sum(1 for p in people if get_values(p["fm"], "linked_companies")),
        "project_community_nodes": len(projects),
        "project_community_nodes_with_linked_people": sum(1 for r in project_rows if r["linked_people"]),
        "project_community_person_associations": project_links,
        "non_company_affiliations_recognized": noncompany_affiliations,
        "unresolved_source_values": unresolved,
        "errors": errors,
        "companies": sorted(company_rows, key=lambda r: (-r["linked_people"], str(r["name"]))),
        "projects_communities": sorted(project_rows, key=lambda r: (-r["linked_people"], str(r["name"]))),
    }
    (generated / "entity-reverse-coverage.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Company / Project → Person Reverse Coverage", "",
        "由 `scripts/audit-entity-reverse-links.py` 自动生成。公司人物边来自人物 `current_affiliations:` 与"
        " `email_affiliations:` 的并集；后者由公开职业邮箱域名规则生成，不单独代表当前任职。"
        "项目/社区反向边来自人物 `projects:` / `communities:`。", "",
        f"- Company nodes: {len(companies)}",
        f"- Companies with ≥1 linked person: {payload['companies_with_linked_people']}",
        f"- Company-person associations: {company_links}",
        f"- Email-domain-supported associations: {email_affiliation_links}",
        f"- People with generated linked_companies: {payload['people_with_linked_companies']}",
        f"- Project/community nodes: {len(projects)}",
        f"- Project/community nodes with ≥1 linked person: {payload['project_community_nodes_with_linked_people']}",
        f"- Project/community-person associations: {project_links}",
        f"- Non-company affiliations recognized and routed elsewhere: {len(noncompany_affiliations)}",
        f"- Unresolved source values (backlog, non-fatal): {len(unresolved)}",
        f"- Audit errors: {len(errors)}", "",
        "## Companies", "", "| Company | Linked people |", "| --- | ---: |",
    ]
    for row in payload["companies"]:
        if row["linked_people"]:
            lines.append(f"| [[{row['id']}\\|{row['name']}]] | {row['linked_people']} |")
    lines.extend(["", "## Projects / communities", "", "| Entity | Linked people |", "| --- | ---: |"])
    for row in payload["projects_communities"]:
        if row["linked_people"]:
            lines.append(f"| [[{row['id']}\\|{row['name']}]] | {row['linked_people']} |")
    if unresolved:
        lines.extend(["", "## Unresolved source values", "", "这些值尚未安全解析到 canonical company/project/community 节点，不自动造边。", ""])
        for item in unresolved[:80]:
            lines.append(f"- `{item['person']}` · `{item['kind']}` → `{item['value']}`")
        if len(unresolved) > 80:
            lines.append(f"- …另有 {len(unresolved) - 80} 条，详见 JSON 报告。")
    (generated / "entity-reverse-coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"Entity reverse audit: {company_links} company-person links "
        f"({email_affiliation_links} email-domain-supported), "
        f"{project_links} project/community-person links, "
        f"{len(noncompany_affiliations)} non-company affiliations recognized, "
        f"{len(unresolved)} unresolved backlog values, {len(errors)} errors."
    )
    for error in errors[:80]:
        print("ERROR:", error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
