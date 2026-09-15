#!/usr/bin/env python3
"""Reconcile Graph Explorer hrefs against the actual Quartz public tree.

Quartz and the staged wikilink normalizer can transform punctuation in paths in
ways that are deliberately richer than build-graph-explorer.py's lightweight
slug approximation. This script treats the built `public/` tree as authority:
it matches graph node ids to real HTML output using a punctuation-insensitive
Unicode key, rewrites data.json hrefs, and fails on missing or ambiguous routes.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import unicodedata
from collections import defaultdict
from urllib.parse import quote


def loose_segment(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold().strip()
    return re.sub(r"[\W_]+", "", value, flags=re.UNICODE)


def node_keys(node_id: str) -> list[tuple[str, ...]]:
    if node_id == "AI Infra Relationship":
        return [tuple()]
    parts = [part for part in node_id.replace("\\", "/").split("/") if part]
    loose = tuple(loose_segment(part) for part in parts)
    keys = [loose]
    # Quartz commonly emits Foo/Foo.md as Foo/index.html. Compare both the
    # explicit source shape and the collapsed index shape.
    if len(loose) >= 2 and loose[-1] == loose[-2]:
        keys.append(loose[:-1])
    return keys


def route_from_html(public_root: pathlib.Path, html: pathlib.Path, base_path: str) -> tuple[tuple[str, ...], str]:
    rel = html.relative_to(public_root)
    if rel.name == "index.html":
        parts = list(rel.parent.parts)
        href_path = "/".join(quote(part, safe="-_.~") for part in parts)
        href = f"{base_path.rstrip('/')}/{href_path}/" if href_path else f"{base_path.rstrip('/')}/"
    else:
        parts = [*rel.parent.parts, rel.stem]
        href_path = "/".join(quote(part, safe="-_.~") for part in parts)
        href = f"{base_path.rstrip('/')}/{href_path}.html"
    key = tuple(loose_segment(part) for part in parts)
    return key, href


def build_route_index(public_root: pathlib.Path, base_path: str, explorer_dir: pathlib.Path) -> dict[tuple[str, ...], list[str]]:
    index: dict[tuple[str, ...], list[str]] = defaultdict(list)
    explorer_dir = explorer_dir.resolve()
    for html in sorted(public_root.rglob("*.html")):
        resolved = html.resolve()
        if resolved == explorer_dir or explorer_dir in resolved.parents:
            continue
        key, href = route_from_html(public_root, html, base_path)
        index[key].append(href)
    return index


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Graph Explorer data.json")
    parser.add_argument("--public-root", required=True, help="Built Quartz public directory")
    parser.add_argument("--base-path", default="/ai_infra_relationship")
    args = parser.parse_args()

    data_path = pathlib.Path(args.data).resolve()
    public_root = pathlib.Path(args.public_root).resolve()
    if not data_path.exists():
        raise SystemExit(f"Missing explorer data: {data_path}")
    if not public_root.exists():
        raise SystemExit(f"Missing Quartz public root: {public_root}")

    payload = json.loads(data_path.read_text(encoding="utf-8"))
    nodes = payload.get("nodes") or []
    route_index = build_route_index(public_root, args.base_path, data_path.parent)

    missing = []
    ambiguous = []
    rewritten = 0
    for node in nodes:
        node_id = str(node.get("id") or "")
        matches: list[str] = []
        for key in node_keys(node_id):
            matches.extend(route_index.get(key, []))
        matches = list(dict.fromkeys(matches))
        if not matches:
            missing.append(node_id)
            continue
        if len(matches) > 1:
            ambiguous.append((node_id, matches))
            continue
        if node.get("href") != matches[0]:
            node["href"] = matches[0]
            rewritten += 1

    if missing or ambiguous:
        print(
            f"Graph explorer route reconciliation failed: {len(missing)} missing, "
            f"{len(ambiguous)} ambiguous."
        )
        for node_id in missing[:80]:
            print("MISSING:", node_id)
        for node_id, matches in ambiguous[:40]:
            print("AMBIGUOUS:", node_id, "->", matches)
        return 1

    data_path.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(
        f"Graph explorer routes reconciled: {len(nodes)} nodes matched to Quartz output; "
        f"{rewritten} hrefs rewritten, 0 missing, 0 ambiguous."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
