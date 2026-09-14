#!/usr/bin/env python3
"""Validate and export typed relationship edges embedded in person frontmatter.

Migration encoding:

relations:
  - '{"target":"community/.../Person","type":["paper-coauthor"],"confidence":"high","evidence":["https://..."]}'

Each list item is a JSON object encoded as a YAML string. This keeps relations
machine-readable while remaining compatible with the repository's legacy
frontmatter parser. A later schema migration can switch these items to native
YAML objects without changing the relation model.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

NODE_ROOTS = ("company", "community", "university")
DATE_RE = re.compile(r"^\d{4}(?:-(?:0[1-9]|1[0-2]))?$")
URL_RE = re.compile(r"^https?://", re.I)
DEFAULT_TYPES = {
    "advisor",
    "student",
    "coworker",
    "cofounder",
    "same-lab",
    "open-source-collaboration",
    "community-maintainer",
    "paper-coauthor",
    "research-collaboration",
    "technical-collaboration",
    "career-connection",
    "project-integration",
    "mentor-network",
}
VALID_CONFIDENCE = {"high", "medium", "low"}


def norm(value: str) -> str:
    value = value.strip().strip("\"'").replace("\\", "/")
    if value.lower().endswith(".md"):
        value = value[:-3]
    return value.strip("/")


def parse_scalar(raw: str):
    value = raw.strip()
    if not value:
        return ""
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        if not body:
            return []
        return [item.strip().strip("\"'") for item in body.split(",") if item.strip()]
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none", "~"}:
        return None
    return value


def frontmatter_lines(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return []
    return lines[1:end]


def parse_frontmatter(text: str) -> dict:
    data: dict[str, object] = {}
    current_key: str | None = None
    for raw in frontmatter_lines(text):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") and current_key:
            items = data.setdefault(current_key, [])
            if isinstance(items, list):
                items.append(parse_scalar(raw[4:]))
            continue
        if raw.startswith(" ") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        if not key:
            continue
        data[key] = [] if key == "relations" and not value.strip() else parse_scalar(value)
        current_key = key
    return data


def load_allowed_types(schema_path: pathlib.Path) -> set[str]:
    if not schema_path.exists():
        return set(DEFAULT_TYPES)
    types: set[str] = set()
    in_types = False
    for raw in schema_path.read_text(encoding="utf-8").splitlines():
        if raw.strip() == "types:":
            in_types = True
            continue
        if in_types:
            if raw.startswith("  - "):
                types.add(raw[4:].strip())
                continue
            if raw and not raw.startswith(" "):
                break
    return types or set(DEFAULT_TYPES)


def resolve_target(target: str, by_id: dict[str, dict], by_base: dict[str, list[dict]], by_name: dict[str, list[dict]]):
    target = norm(target)
    exact = by_id.get(target.casefold())
    if exact:
        return exact, "exact", []

    base = pathlib.PurePosixPath(target).name.casefold()
    candidates = by_base.get(base, [])
    if len(candidates) == 1:
        return candidates[0], "unique-basename", []
    if len(candidates) > 1:
        return None, "ambiguous", [item["id"] for item in candidates]

    candidates = by_name.get(target.casefold(), [])
    if len(candidates) == 1:
        return candidates[0], "unique-name", []
    if len(candidates) > 1:
        return None, "ambiguous", [item["id"] for item in candidates]
    return None, "missing", []


def relation_json(item, source: str, index: int, errors: list[dict]):
    if isinstance(item, dict):
        return item
    if not isinstance(item, str):
        errors.append({"kind": "relation-invalid-item", "source": source, "index": index})
        return None
    try:
        parsed = json.loads(item)
    except json.JSONDecodeError as exc:
        errors.append({
            "kind": "relation-invalid-json",
            "source": source,
            "index": index,
            "detail": str(exc),
        })
        return None
    if not isinstance(parsed, dict):
        errors.append({"kind": "relation-json-not-object", "source": source, "index": index})
        return None
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    generated.mkdir(parents=True, exist_ok=True)

    nodes_path = generated / "nodes.json"
    metrics_path = generated / "metrics.json"
    links_path = generated / "edges.json"
    if not nodes_path.exists():
        print(f"Missing {nodes_path}; run audit-graph.py first.", file=sys.stderr)
        return 2

    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    metrics = json.loads(metrics_path.read_text(encoding="utf-8")) if metrics_path.exists() else {}
    wikilink_edges = json.loads(links_path.read_text(encoding="utf-8")) if links_path.exists() else []

    by_id = {norm(node["id"]).casefold(): node for node in nodes}
    by_base: dict[str, list[dict]] = defaultdict(list)
    by_name: dict[str, list[dict]] = defaultdict(list)
    for node in nodes:
        by_base[pathlib.PurePosixPath(norm(node["id"])).name.casefold()].append(node)
        name = str(node.get("name") or "").strip().casefold()
        if name:
            by_name[name].append(node)

    allowed_types = load_allowed_types(root / "schema" / "relation.yaml")
    errors: list[dict] = []
    warnings: list[dict] = []
    typed_edges: list[dict] = []
    relation_sources: set[str] = set()
    pair_seen: set[tuple[str, str, tuple[str, ...]]] = set()

    for dirname in NODE_ROOTS:
        base = root / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            raw_relations = fm.get("relations")
            if not raw_relations:
                continue
            rel_source = path.relative_to(root).as_posix()
            source_id = rel_source[:-3]
            source_node = by_id.get(source_id.casefold())
            if not source_node:
                errors.append({"kind": "relation-source-not-in-graph", "source": rel_source})
                continue
            if not isinstance(raw_relations, list):
                errors.append({"kind": "relations-not-list", "source": rel_source})
                continue

            relation_sources.add(source_id)
            if source_node.get("type") == "person":
                if not fm.get("current_affiliations"):
                    warnings.append({"kind": "typed-person-missing-current-affiliations", "source": rel_source})
                if not fm.get("areas"):
                    warnings.append({"kind": "typed-person-missing-areas", "source": rel_source})
                if not fm.get("last_verified"):
                    warnings.append({"kind": "typed-person-missing-last-verified", "source": rel_source})

            last_verified = fm.get("last_verified")
            if isinstance(last_verified, str) and last_verified and not re.fullmatch(r"\d{4}-(?:0[1-9]|1[0-2])", last_verified):
                errors.append({"kind": "invalid-last-verified", "source": rel_source, "value": last_verified})

            for index, item in enumerate(raw_relations, 1):
                relation = relation_json(item, rel_source, index, errors)
                if not relation:
                    continue

                target_raw = relation.get("target")
                if not isinstance(target_raw, str) or not target_raw.strip():
                    errors.append({"kind": "relation-missing-target", "source": rel_source, "index": index})
                    continue
                target_node, reason, candidates = resolve_target(target_raw, by_id, by_base, by_name)
                if target_node is None:
                    errors.append({
                        "kind": "relation-target-unresolved",
                        "source": rel_source,
                        "index": index,
                        "target": target_raw,
                        "reason": reason,
                        "candidates": candidates,
                    })
                    continue
                if target_node["id"] == source_id:
                    errors.append({"kind": "relation-self-edge", "source": rel_source, "index": index})
                    continue

                types = relation.get("type")
                if isinstance(types, str):
                    types = [types]
                if not isinstance(types, list) or not types or not all(isinstance(value, str) and value for value in types):
                    errors.append({"kind": "relation-invalid-type", "source": rel_source, "index": index})
                    continue
                invalid_types = sorted({value for value in types if value not in allowed_types})
                if invalid_types:
                    errors.append({
                        "kind": "relation-unknown-type",
                        "source": rel_source,
                        "index": index,
                        "types": invalid_types,
                    })
                    continue

                confidence = relation.get("confidence")
                if confidence not in VALID_CONFIDENCE:
                    errors.append({
                        "kind": "relation-invalid-confidence",
                        "source": rel_source,
                        "index": index,
                        "value": confidence,
                    })
                    continue

                for field in ("start", "end"):
                    value = relation.get(field)
                    if value in {None, ""}:
                        continue
                    value = str(value)
                    if not DATE_RE.fullmatch(value):
                        errors.append({
                            "kind": "relation-invalid-date",
                            "source": rel_source,
                            "index": index,
                            "field": field,
                            "value": value,
                        })

                evidence = relation.get("evidence") or []
                if isinstance(evidence, str):
                    evidence = [evidence]
                if not isinstance(evidence, list):
                    errors.append({"kind": "relation-invalid-evidence", "source": rel_source, "index": index})
                    evidence = []
                invalid_urls = [url for url in evidence if not isinstance(url, str) or not URL_RE.match(url)]
                if invalid_urls:
                    errors.append({
                        "kind": "relation-invalid-evidence-url",
                        "source": rel_source,
                        "index": index,
                        "values": invalid_urls,
                    })
                if not evidence:
                    warnings.append({"kind": "relation-missing-evidence", "source": rel_source, "index": index})

                key = (source_id, target_node["id"], tuple(sorted(types)))
                if key in pair_seen:
                    warnings.append({
                        "kind": "relation-duplicate-edge",
                        "source": rel_source,
                        "index": index,
                        "target": target_node["id"],
                        "types": sorted(types),
                    })
                pair_seen.add(key)

                typed_edges.append({
                    "source": source_id,
                    "target": target_node["id"],
                    "kind": "typed-relation",
                    "relation_types": types,
                    "project": relation.get("project"),
                    "company": relation.get("company"),
                    "start": relation.get("start"),
                    "end": relation.get("end"),
                    "confidence": confidence,
                    "evidence": evidence,
                })

    person_ids = {node["id"] for node in nodes if node.get("type") == "person"}
    linked_person_neighbors: dict[str, set[str]] = defaultdict(set)
    for edge in wikilink_edges:
        source = edge.get("source")
        target = edge.get("target")
        if source in person_ids and target in person_ids and source != target:
            linked_person_neighbors[source].add(target)
    typed_person_neighbors: dict[str, set[str]] = defaultdict(set)
    for edge in typed_edges:
        if edge["source"] in person_ids and edge["target"] in person_ids:
            typed_person_neighbors[edge["source"]].add(edge["target"])

    coverage_rows = []
    for node in nodes:
        node_id = node["id"]
        if node.get("type") != "person":
            continue
        link_count = len(linked_person_neighbors.get(node_id, set()))
        typed_count = len(typed_person_neighbors.get(node_id, set()))
        coverage = round(typed_count / link_count, 3) if link_count else (1.0 if typed_count else 0.0)
        metric = metrics.get(node_id, {})
        coverage_rows.append({
            "id": node_id,
            "name": node.get("name"),
            "degree": metric.get("degree", 0),
            "bridge_score": metric.get("bridge_score", 0),
            "person_links": link_count,
            "typed_person_relations": typed_count,
            "typed_person_link_coverage": coverage,
        })

    type_counts = Counter()
    for edge in typed_edges:
        type_counts.update(edge["relation_types"])

    coverage_rows.sort(key=lambda row: (-row["bridge_score"], -row["degree"], str(row["name"])))
    migration_queue = [row for row in coverage_rows if row["person_links"] > 0 and row["typed_person_relations"] == 0]

    audit = {
        "typed_edges": len(typed_edges),
        "relation_sources": len(relation_sources),
        "errors": errors,
        "warnings": warnings,
        "relation_type_counts": dict(sorted(type_counts.items())),
    }
    coverage = {
        "person_nodes": len(person_ids),
        "person_nodes_with_typed_relations": sum(1 for row in coverage_rows if row["typed_person_relations"] > 0),
        "typed_edges": len(typed_edges),
        "relation_sources": len(relation_sources),
        "rows": coverage_rows,
    }

    (generated / "typed-edges.json").write_text(json.dumps(typed_edges, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (generated / "typed-relations-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (generated / "relation-coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Typed Relation Coverage",
        "",
        "由 `scripts/audit-typed-relations.py` 自动生成。`typed_person_link_coverage` 只表示人物页中已解析的人物 wikilink 有多少被结构化关系覆盖，不代表事实完整度。",
        "",
        f"- Typed relation edges: {len(typed_edges)}",
        f"- Person nodes with typed relations: {coverage['person_nodes_with_typed_relations']} / {len(person_ids)}",
        f"- Hard errors: {len(errors)}",
        f"- Warnings: {len(warnings)}",
        "",
        "## Relation types",
        "",
    ]
    if type_counts:
        for relation_type, count in type_counts.most_common():
            lines.append(f"- `{relation_type}`: {count}")
    else:
        lines.append("- 暂无结构化关系。")

    lines.extend([
        "",
        "## Next migration candidates",
        "",
        "优先展示 bridge score 高、已有 person-to-person wikilink、但尚未建立 typed relations 的人物。",
        "",
        "| Rank | Person | Bridge | Degree | Person links | Typed relations |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ])
    for rank, row in enumerate(migration_queue[:40], 1):
        label = str(row["name"]).replace("|", "\\|")
        lines.append(
            f"| {rank} | [[{row['id']}|{label}]] | {row['bridge_score']:.3f} | {row['degree']} | {row['person_links']} | {row['typed_person_relations']} |"
        )

    lines.extend([
        "",
        "## Structured bridge nodes",
        "",
        "| Person | Bridge | Person links | Typed | Coverage |",
        "| --- | ---: | ---: | ---: | ---: |",
    ])
    for row in [r for r in coverage_rows if r["typed_person_relations"] > 0][:30]:
        label = str(row["name"]).replace("|", "\\|")
        lines.append(
            f"| [[{row['id']}|{label}]] | {row['bridge_score']:.3f} | {row['person_links']} | {row['typed_person_relations']} | {row['typed_person_link_coverage']:.1%} |"
        )

    (generated / "typed-relation-coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"Typed relation audit: {len(typed_edges)} edges from {len(relation_sources)} sources; "
        f"{len(errors)} errors, {len(warnings)} warnings."
    )
    for issue in errors[:80]:
        print("ERROR:", json.dumps(issue, ensure_ascii=False))
    for issue in warnings[:40]:
        print("WARN:", json.dumps(issue, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
