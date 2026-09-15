#!/usr/bin/env python3
"""Make explicit company <-> community/project assertions symmetric.

This is a conservative canonicalization pass. It never invents a relationship:
if either side already explicitly asserts a company/project-community pair, the
same pair is written to the counterpart explicit field.

- company `projects:` / `communities:` -> entity `companies:`
- entity `companies:` / `company:` -> company `projects:`

Model-team/model-project values are valid company `projects:` entries but are
outside the open-source community relation layer and are left untouched.
"""
from __future__ import annotations

import argparse
import importlib.util
import pathlib

MODULE_PATH = pathlib.Path(__file__).with_name("sync-company-community.py")
spec = importlib.util.spec_from_file_location("sync_company_community", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load {MODULE_PATH}")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    records = sync.load_records(root)
    companies, company_aliases, company_ids = sync.build_index(records, {"company"})
    entities, entity_aliases, entity_ids = sync.build_index(records, sync.ENTITY_TYPES)
    _, noncommunity_aliases, noncommunity_ids = sync.build_index(records, sync.NON_COMMUNITY_PROJECT_TYPES)

    company_map = {r["id"]: r for r in companies}
    entity_map = {r["id"]: r for r in entities}
    pairs: set[tuple[str, str]] = set()
    unresolved = []
    recognized_noncommunity = []

    for company in companies:
        for field in ("projects", "communities"):
            for value in sync.get_values(company["fm"], field):
                entity = sync.resolve(value, entity_aliases, entity_ids)
                if entity:
                    pairs.add((company["id"], entity["id"]))
                    continue
                if field == "projects" and sync.resolve(value, noncommunity_aliases, noncommunity_ids):
                    recognized_noncommunity.append((company["id"], value))
                    continue
                unresolved.append((f"company.{field}", company["rel"], value))

    for entity in entities:
        values = [*sync.get_values(entity["fm"], "companies"), *sync.get_values(entity["fm"], "company")]
        seen = set()
        for value in values:
            token = sync.fold(value)
            if token in seen:
                continue
            seen.add(token)
            company = sync.resolve(value, company_aliases, company_ids)
            if company:
                pairs.add((company["id"], entity["id"]))
            else:
                unresolved.append(("entity.company", entity["rel"], value))

    company_additions: dict[str, list[str]] = {r["id"]: [] for r in companies}
    entity_additions: dict[str, list[str]] = {r["id"]: [] for r in entities}
    for company_id, entity_id in pairs:
        company = company_map[company_id]
        entity = entity_map[entity_id]
        company_explicit = []
        for field in ("projects", "communities"):
            company_explicit.extend(sync.get_values(company["fm"], field))
        company_has = any(
            (resolved := sync.resolve(value, entity_aliases, entity_ids)) and resolved["id"] == entity_id
            for value in company_explicit
        )
        entity_explicit = [*sync.get_values(entity["fm"], "companies"), *sync.get_values(entity["fm"], "company")]
        entity_has = any(
            (resolved := sync.resolve(value, company_aliases, company_ids)) and resolved["id"] == company_id
            for value in entity_explicit
        )
        if not company_has:
            company_additions[company_id].append(entity["name"])
        if not entity_has:
            entity_additions[entity_id].append(company["name"])

    touched = []
    additions = 0
    for company in companies:
        add = sorted(set(company_additions[company["id"]]), key=str.casefold)
        if not add:
            continue
        values = sync.get_values(company["fm"], "projects")
        updated_fm = sync.set_block_list(company["fm"], "projects", [*values, *add])
        updated = sync.join_frontmatter(updated_fm, company["body"])
        company["path"].write_text(updated, encoding="utf-8")
        touched.append(company["rel"])
        additions += len(add)

    for entity in entities:
        add = sorted(set(entity_additions[entity["id"]]), key=str.casefold)
        if not add:
            continue
        values = sync.get_values(entity["fm"], "companies")
        if not values:
            legacy = sync.get_values(entity["fm"], "company")
            values = legacy
        updated_fm = sync.set_block_list(entity["fm"], "companies", [*values, *add])
        updated = sync.join_frontmatter(updated_fm, entity["body"])
        entity["path"].write_text(updated, encoding="utf-8")
        touched.append(entity["rel"])
        additions += len(add)

    print(
        f"Explicit company/community symmetry: {len(pairs)} pairs, {additions} counterpart assertions added, "
        f"{len(touched)} files updated, {len(recognized_noncommunity)} non-community project targets recognized, "
        f"{len(unresolved)} unresolved explicit values."
    )
    for kind, source, value in unresolved[:80]:
        print(f"UNRESOLVED {kind}: {source} -> {value}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
