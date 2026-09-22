#!/usr/bin/env python3
"""Build the data bundle consumed by the Sigma.js graph explorer.

Markdown remains the source of truth. This script only adapts the graph audit
artifacts into a compact browser-facing payload and verifies Quartz routes when
asked. Presentation-only concepts such as layout coordinates and Louvain
communities are intentionally computed in the frontend rather than persisted in
Markdown or schemas.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from urllib.parse import quote


def load_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def list_field(frontmatter: dict, key: str) -> list:
    value = frontmatter.get(key)
    return value if isinstance(value, list) else []


def quartz_slug_segment(value: str) -> str:
    """Approximate the Quartz v5 route slug used by this repository build."""

    value = re.sub(r"\.(?=\s)", "", value.strip())
    value = value.replace(".", "-")
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def route_parts(node_id: str) -> tuple[list[str], bool]:
    if node_id == "AI Infra Relationship":
        return [], True

    parts = [quartz_slug_segment(part) for part in node_id.split("/") if part]
    if not parts:
        return [], True

    # Quartz emits Foo/Foo.md as Foo/index.html.
    if len(parts) >= 2 and parts[-1].casefold() == parts[-2].casefold():
        return parts[:-1], True
    return parts, False


def build_href(node_id: str, base_path: str, public_root: pathlib.Path | None) -> tuple[str, bool]:
    parts, is_index = route_parts(node_id)
    encoded = "/".join(quote(part, safe="-_.~") for part in parts)
    base = base_path.rstrip("/")

    if is_index:
        href = f"{base}/{encoded}/" if encoded else f"{base}/"
        target = public_root.joinpath(*parts, "index.html") if public_root else None
    else:
        href = f"{base}/{encoded}.html"
        target = public_root.joinpath(*parts[:-1], f"{parts[-1]}.html") if public_root else None

    return href, bool(target is None or target.exists())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-path", default="/ai_infra_relationship")
    parser.add_argument(
        "--public-root",
        default=None,
        help="Quartz public directory. When provided, every dynamic node href is verified against it.",
    )
    args = parser.parse_args()

    generated = pathlib.Path(args.generated)
    output = pathlib.Path(args.output)
    public_root = pathlib.Path(args.public_root).resolve() if args.public_root else None
    output.mkdir(parents=True, exist_ok=True)

    nodes = load_json(generated / "nodes.json", [])
    wiki_edges = load_json(generated / "edges.json", [])
    typed_edges = load_json(generated / "typed-edges.json", [])
    metrics = load_json(generated / "metrics.json", {})

    if not nodes:
        raise SystemExit("nodes.json is empty; run audit-graph.py first")

    node_map = {node["id"]: node for node in nodes}
    payload_nodes = []
    broken_routes = []

    for node in nodes:
        node_id = node["id"]
        frontmatter = node.get("frontmatter") or {}
        node_metrics = metrics.get(node_id) or {}
        href, route_ok = build_href(node_id, args.base_path, public_root)
        if not route_ok:
            broken_routes.append((node_id, href))

        payload_nodes.append(
            {
                "id": node_id,
                "name": node.get("name") or node_id.split("/")[-1],
                "aliases": list_field(frontmatter, "aliases"),
                "type": node.get("type") or "note",
                "category": node.get("category") or "other",
                "areas": list_field(frontmatter, "areas"),
                "communities": list_field(frontmatter, "communities"),
                "schools": list_field(frontmatter, "schools"),
                "projects": list_field(frontmatter, "projects"),
                "companies": list_field(frontmatter, "companies"),
                "currentAffiliations": list_field(frontmatter, "current_affiliations"),
                "hardware": list_field(frontmatter, "hardware"),
                "roles": list_field(frontmatter, "roles"),
                "layer": frontmatter.get("layer") if isinstance(frontmatter.get("layer"), str) else None,
                "degree": node_metrics.get("degree", 0),
                "crossCategoryDegree": node_metrics.get("cross_category_degree", 0),
                "bridgeScore": node_metrics.get("bridge_score", 0),
                "href": href,
            }
        )

    if broken_routes:
        print(f"Graph explorer route audit failed: {len(broken_routes)} node routes do not exist in Quartz public output.")
        for node_id, href in broken_routes[:80]:
            print(f"- {node_id} -> {href}")
        if len(broken_routes) > 80:
            print(f"... plus {len(broken_routes) - 80} more")
        return 1

    # Merge ordinary wikilinks and typed relations by unordered node pair. A
    # typed relation supersedes the generic `wikilink` type for the same pair.
    merged: dict[tuple[str, str], dict] = {}
    for edge in wiki_edges:
        source, target = edge.get("source"), edge.get("target")
        if source not in node_map or target not in node_map or source == target:
            continue
        key = tuple(sorted((source, target)))
        item = merged.setdefault(key, {"source": key[0], "target": key[1], "types": set(), "typed": False})
        item["types"].add("wikilink")

    for edge in typed_edges:
        source, target = edge.get("source"), edge.get("target")
        if source not in node_map or target not in node_map or source == target:
            continue
        key = tuple(sorted((source, target)))
        item = merged.setdefault(key, {"source": key[0], "target": key[1], "types": set(), "typed": False})
        item["typed"] = True
        item["types"].discard("wikilink")
        for relation_type in edge.get("relation_types") or []:
            item["types"].add(relation_type)
        if not item["types"]:
            item["types"].add("wikilink")

    payload_edges = [
        {
            "id": f"e{index}",
            "source": item["source"],
            "target": item["target"],
            "types": sorted(item["types"]),
            "typed": item["typed"],
        }
        for index, item in enumerate(merged.values())
    ]

    node_types = sorted({node["type"] for node in payload_nodes})
    relation_types = sorted({relation for edge in payload_edges for relation in edge["types"]})
    data = {
        "schemaVersion": "graph-explorer-v2",
        "basePath": args.base_path.rstrip("/"),
        "summary": {
            "nodes": len(payload_nodes),
            "edges": len(payload_edges),
            "nodeTypes": node_types,
            "relationTypes": relation_types,
        },
        "nodes": payload_nodes,
        "edges": payload_edges,
    }
    (output / "data.json").write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    print(f"Graph explorer data: {len(payload_nodes)} nodes, {len(payload_edges)} merged edges -> {output / 'data.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
