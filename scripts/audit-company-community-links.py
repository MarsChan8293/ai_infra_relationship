#!/usr/bin/env python3
"""Audit bidirectional company <-> community/project links and write coverage reports."""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
from collections import defaultdict

MODULE_PATH = pathlib.Path(__file__).with_name("sync-company-community.py")
spec = importlib.util.spec_from_file_location("sync_company_community", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load {MODULE_PATH}")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def wikilink(record: dict) -> str:
    return f"[[{record['id']}|{record['name']}]]"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    generated.mkdir(parents=True, exist_ok=True)

    records = sync.load_records(root)
    companies, company_aliases, company_ids = sync.build_index(records, {"company"})
    entities, entity_aliases, entity_ids = sync.build_index(records, sync.ENTITY_TYPES)
    company_map = {r["id"]: r for r in companies}
    entity_map = {r["id"]: r for r in entities}

    pair_sources: dict[tuple[str, str], set[str]] = defaultdict(set)
    pair_relations: dict[tuple[str, str], str] = {}
    unresolved = []

    for company in companies:
        for field in ("projects", "communities"):
            for value in sync.get_values(company["fm"], field):
                target = sync.resolve(value, entity_aliases, entity_ids)
                if not target:
                    unresolved.append({"kind": f"company.{field}", "source": company["rel"], "value": value})
                    continue
                pair_sources[(company["id"], target["id"])].add("company")

    for entity in entities:
        relation = sync.get_scalar(entity["fm"], "company_relation")
        values = [*sync.get_values(entity["fm"], "companies"), *sync.get_values(entity["fm"], "company")]
        seen = set()
        for value in values:
            token = sync.fold(value)
            if token in seen:
                continue
            seen.add(token)
            company = sync.resolve(value, company_aliases, company_ids)
            if not company:
                unresolved.append({"kind": "entity.company", "source": entity["rel"], "value": value})
                continue
            key = (company["id"], entity["id"])
            pair_sources[key].add("entity")
            if relation:
                pair_relations[key] = relation

    expected_company: dict[str, set[str]] = defaultdict(set)
    expected_entity: dict[str, set[str]] = defaultdict(set)
    for company_id, entity_id in pair_sources:
        expected_company[company_id].add(entity_id)
        expected_entity[entity_id].add(company_id)

    errors = []
    for company in companies:
        actual = set(sync.get_values(company["fm"], "linked_projects"))
        expected = expected_company.get(company["id"], set())
        if actual != expected:
            errors.append({
                "kind": "company-linked-projects-mismatch",
                "node": company["id"],
                "missing": sorted(expected - actual),
                "stale": sorted(actual - expected),
            })

    for entity in entities:
        actual = set(sync.get_values(entity["fm"], "linked_companies"))
        expected = expected_entity.get(entity["id"], set())
        if actual != expected:
            errors.append({
                "kind": "entity-linked-companies-mismatch",
                "node": entity["id"],
                "missing": sorted(expected - actual),
                "stale": sorted(actual - expected),
            })

    both = sum(1 for sources in pair_sources.values() if sources == {"company", "entity"})
    company_only = sum(1 for sources in pair_sources.values() if sources == {"company"})
    entity_only = sum(1 for sources in pair_sources.values() if sources == {"entity"})
    companies_with_links = len({company_id for company_id, _ in pair_sources})
    entities_with_links = len({entity_id for _, entity_id in pair_sources})

    rows = []
    for (company_id, entity_id), sources in sorted(
        pair_sources.items(),
        key=lambda item: (company_map[item[0][0]]["name"].casefold(), entity_map[item[0][1]]["name"].casefold()),
    ):
        company, entity = company_map[company_id], entity_map[entity_id]
        rows.append({
            "company_id": company_id,
            "company_name": company["name"],
            "entity_id": entity_id,
            "entity_name": entity["name"],
            "entity_type": entity["type"],
            "relation": pair_relations.get((company_id, entity_id)),
            "sources": sorted(sources),
        })

    report = {
        "format": "ai-infra-relationship/company-community-coverage-v1",
        "company_nodes": len(companies),
        "companies_with_links": companies_with_links,
        "project_community_nodes": len(entities),
        "project_community_nodes_with_links": entities_with_links,
        "association_pairs": len(pair_sources),
        "asserted_on_both_sides": both,
        "company_side_only": company_only,
        "entity_side_only": entity_only,
        "unresolved_source_values": unresolved,
        "audit_errors": errors,
        "pairs": rows,
    }
    (generated / "company-community-coverage.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "# Company ↔ Community / Project Coverage",
        "",
        "由 `scripts/audit-company-community-links.py` 自动生成。人工事实来自公司 `projects:` / `communities:` 与社区/项目 `companies:` / `company:`；派生镜像分别写入 `linked_projects:` 与 `linked_companies:`。员工个人参与不会自动升级为公司级关系。",
        "",
        f"- Company nodes: {len(companies)}",
        f"- Companies with ≥1 linked project/community: {companies_with_links}",
        f"- Project/community nodes: {len(entities)}",
        f"- Project/community nodes with ≥1 linked company: {entities_with_links}",
        f"- Bidirectional association pairs: {len(pair_sources)}",
        f"- Explicitly asserted on both sides: {both}",
        f"- Company-side only explicit assertions: {company_only}",
        f"- Entity-side only explicit assertions: {entity_only}",
        f"- Unresolved explicit source values: {len(unresolved)}",
        f"- Audit errors: {len(errors)}",
        "",
        "| Company | Community / project | Type | Relation | Explicit source |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        company = company_map[row["company_id"]]
        entity = entity_map[row["entity_id"]]
        source = "both" if row["sources"] == ["company", "entity"] else row["sources"][0]
        md.append(
            f"| {wikilink(company)} | {wikilink(entity)} | {row['entity_type']} | "
            f"{row['relation'] or ''} | {source} |"
        )
    if unresolved:
        md.extend(["", "## Unresolved explicit values", ""])
        for item in unresolved:
            md.append(f"- `{item['kind']}` {item['source']} → `{item['value']}`")
    if errors:
        md.extend(["", "## Audit errors", ""])
        for item in errors:
            md.append(f"- `{item['kind']}` {item['node']}: missing={item['missing']}, stale={item['stale']}")
    (generated / "company-community-coverage.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(
        f"Company/community audit: {len(pair_sources)} pairs, {both} both-side assertions, "
        f"{company_only} company-only, {entity_only} entity-only, {len(unresolved)} unresolved, {len(errors)} errors."
    )
    for item in unresolved[:80]:
        print(f"UNRESOLVED {item['kind']}: {item['source']} -> {item['value']}")
    for item in errors[:80]:
        print(f"ERROR {item['kind']}: {item['node']} missing={item['missing']} stale={item['stale']}")
    return 1 if unresolved or errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
