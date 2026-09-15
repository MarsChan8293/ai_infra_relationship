#!/usr/bin/env python3
"""Reconcile Graph Explorer hrefs against the actual Quartz public tree.

Most explorer hrefs are already correct. Quartz may additionally emit
case-normalized aliases, and the staged wikilink normalizer may change a small
number of punctuation-heavy Markdown basenames. This script therefore keeps an
existing href whenever it really exists in `public/`, and only resolves nodes
whose original href is missing. Missing routes are matched with a Unicode,
punctuation-insensitive key; case-only aliases are treated as equivalent.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from urllib.parse import quote, unquote, urlsplit


def loose_segment(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold().strip()
    return re.sub(r"[\W_]+", "", value, flags=re.UNICODE)


def node_keys(node_id: str) -> list[tuple[str, ...]]:
    if node_id == "AI Infra Relationship":
        return [tuple()]
    parts = [part for part in node_id.replace("\\", "/").split("/") if part]
    loose = tuple(loose_segment(part) for part in parts)
    keys = [loose]
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
    return tuple(loose_segment(part) for part in parts), href


def build_route_index(
    public_root: pathlib.Path,
    base_path: str,
    explorer_dir: pathlib.Path,
) -> tuple[dict[tuple[str, ...], list[str]], set[str]]:
    index: dict[tuple[str, ...], list[str]] = defaultdict(list)
    all_hrefs: set[str] = set()
    explorer_dir = explorer_dir.resolve()
    for html in sorted(public_root.rglob("*.html")):
        resolved = html.resolve()
        if resolved == explorer_dir or explorer_dir in resolved.parents:
            continue
        key, href = route_from_html(public_root, html, base_path)
        index[key].append(href)
        all_hrefs.add(href)
    return index, all_hrefs


def route_parts_from_href(href: str, base_path: str) -> list[str]:
    path = unquote(urlsplit(href).path)
    base = "/" + base_path.strip("/")
    if path == base:
        return []
    if path.startswith(base + "/"):
        path = path[len(base) + 1 :]
    path = path.strip("/")
    if path.endswith(".html"):
        path = path[:-5]
    return [part for part in path.split("/") if part]


def case_similarity(node_id: str, href: str, base_path: str) -> float:
    source = "/".join(part.replace(" ", "-") for part in node_id.split("/") if part)
    target = "/".join(route_parts_from_href(href, base_path))
    return SequenceMatcher(None, source, target).ratio()


def choose_missing_route(node_id: str, matches: list[str], base_path: str) -> tuple[str | None, list[str]]:
    """Choose among true route candidates while preserving real ambiguity.

    Quartz often emits both original-case and lowercase aliases. Those differ
    only by case and are one semantic route, so collapse each casefold group.
    If punctuation normalization changed a repeated Foo/Foo.md basename, prefer
    the explicit leaf route; otherwise prefer Quartz's ordinary index route.
    """

    unique_matches = list(dict.fromkeys(matches))
    groups: dict[str, list[str]] = defaultdict(list)
    for href in unique_matches:
        groups[href.casefold()].append(href)

    representatives = [
        max(group, key=lambda href: case_similarity(node_id, href, base_path))
        for group in groups.values()
    ]
    if len(representatives) == 1:
        return representatives[0], representatives

    source_parts = [part for part in node_id.replace("\\", "/").split("/") if part]
    desired_depth = len(source_parts)
    if len(source_parts) >= 2 and loose_segment(source_parts[-1]) == loose_segment(source_parts[-2]):
        staged_leaf = re.sub(r"\.(?=\s)", "", source_parts[-1])
        desired_depth = len(source_parts) if staged_leaf != source_parts[-1] else len(source_parts) - 1

    depth_matches = [
        href
        for href in representatives
        if len(route_parts_from_href(href, base_path)) == desired_depth
    ]
    if len(depth_matches) == 1:
        return depth_matches[0], representatives
    if depth_matches:
        representatives = depth_matches

    ranked = sorted(
        ((case_similarity(node_id, href, base_path), href) for href in representatives),
        reverse=True,
    )
    if len(ranked) == 1 or (ranked[0][0] - ranked[1][0]) > 0.01:
        return ranked[0][1], representatives
    return None, representatives


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
    route_index, all_hrefs = build_route_index(public_root, args.base_path, data_path.parent)

    missing = []
    ambiguous = []
    rewritten = 0
    already_valid = 0
    for node in nodes:
        node_id = str(node.get("id") or "")
        current_href = str(node.get("href") or "")

        # Preserve the explorer's deterministic route whenever Quartz actually
        # emitted it. This avoids treating lowercase compatibility aliases as
        # ambiguity for the hundreds of ordinary routes that are already right.
        if current_href in all_hrefs:
            already_valid += 1
            continue

        matches: list[str] = []
        for key in node_keys(node_id):
            matches.extend(route_index.get(key, []))
        if not matches:
            missing.append(node_id)
            continue

        chosen, semantic_matches = choose_missing_route(node_id, matches, args.base_path)
        if not chosen:
            ambiguous.append((node_id, semantic_matches))
            continue
        node["href"] = chosen
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
        f"Graph explorer routes reconciled: {len(nodes)} nodes; {already_valid} existing hrefs kept, "
        f"{rewritten} hrefs rewritten, 0 missing, 0 ambiguous."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
