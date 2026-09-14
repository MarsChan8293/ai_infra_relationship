#!/usr/bin/env python3
"""Semantic audit + graph export for the AI Infra Relationship Markdown graph.

The repository intentionally contains legacy frontmatter and a small number of
research leads/red links. v1 therefore treats only structural ambiguity and
broken canonical references as hard errors. Migration issues are warnings.

Outputs:
  generated/audit.json
  generated/nodes.json
  generated/edges.json
  generated/graph.json
  generated/metrics.json
  generated/research-queue.md
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import re
import sys
from collections import Counter, defaultdict, deque

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
REPO_RE = re.compile(r"https?://(?:www\.)?(?:github\.com|gitcode\.com)/[^\s)>\]]+", re.I)

NODE_ROOTS = ("company", "community", "university")
INDEX_BASENAMES = {"company", "community", "university"}


def norm(value: str) -> str:
    return value.replace("\\", "/").strip().strip("/").removesuffix(".md")


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
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none", "~"}:
        return None
    return value.strip("\"'")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, text

    data: dict[str, object] = {}
    current_key: str | None = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") and current_key:
            items = data.setdefault(current_key, [])
            if isinstance(items, list):
                items.append(parse_scalar(raw[4:]))
            continue
        if raw.startswith("-") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        if not key:
            continue
        data[key] = parse_scalar(value)
        current_key = key
    body = "\n".join(lines[end + 1 :])
    return data, body


def category_for(rel: str) -> str:
    first = rel.split("/", 1)[0]
    return first if first in NODE_ROOTS else "root"


def infer_type(rel: str, fm: dict) -> str:
    explicit = fm.get("type")
    if isinstance(explicit, str) and explicit:
        return explicit
    stem = pathlib.PurePosixPath(rel).stem
    if stem in INDEX_BASENAMES or rel == "AI Infra Relationship.md":
        return "index"
    if category_for(rel) == "university" and pathlib.PurePosixPath(rel).parent.name == stem:
        return "university"
    if category_for(rel) == "company" and pathlib.PurePosixPath(rel).parent.name == stem:
        return "company"
    return "note"


def link_target(inner: str) -> str:
    target = inner.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    return norm(target)


def resolve(target: str, source: dict, by_rel: dict, by_base: dict):
    if not target:
        return None, "same-page", []
    target = norm(target)
    exact = by_rel.get(target.lower(), [])
    if len(exact) == 1:
        return exact[0], "exact", []
    if len(exact) > 1:
        return None, "ambiguous", [r["path"] for r in exact]

    source_dir = str(pathlib.PurePosixPath(source["rel_no_ext"]).parent)
    relative = norm(str(pathlib.PurePosixPath(source_dir) / target))
    candidates = by_rel.get(relative.lower(), [])
    if len(candidates) == 1:
        return candidates[0], "relative", []

    base = pathlib.PurePosixPath(target).name.lower()
    candidates = by_base.get(base, [])
    if len(candidates) == 1:
        return candidates[0], "unique-basename", []
    if len(candidates) > 1:
        same_dir = [r for r in candidates if str(pathlib.PurePosixPath(r["rel_no_ext"]).parent) == source_dir]
        if len(same_dir) == 1:
            return same_dir[0], "same-directory", []
        return None, "ambiguous", [r["path"] for r in candidates]
    return None, "missing", []


def short_issue(issue: dict) -> str:
    suffix = f" -> {issue['target']}" if issue.get("target") else ""
    return f"{issue['kind']}: {issue['source']}{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="generated")
    parser.add_argument("--fail-on-missing", action="store_true", help="Treat unresolved wikilinks as hard errors")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    out = (root / args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)

    paths: list[pathlib.Path] = []
    root_index = root / "AI Infra Relationship.md"
    if root_index.exists():
        paths.append(root_index)
    for dirname in NODE_ROOTS:
        base = root / dirname
        if base.exists():
            paths.extend(sorted(base.rglob("*.md")))

    records: list[dict] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        rel = path.relative_to(root).as_posix()
        rel_no_ext = rel[:-3] if rel.lower().endswith(".md") else rel
        records.append(
            {
                "id": rel_no_ext,
                "path": rel,
                "rel_no_ext": rel_no_ext,
                "basename": pathlib.PurePosixPath(rel_no_ext).name,
                "category": category_for(rel),
                "type": infer_type(rel, fm),
                "name": fm.get("name") or pathlib.PurePosixPath(rel_no_ext).name,
                "frontmatter": fm,
                "body": body,
                "text": text,
            }
        )

    by_rel: dict[str, list[dict]] = defaultdict(list)
    by_base: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_rel[record["rel_no_ext"].lower()].append(record)
        by_base[record["basename"].lower()].append(record)

    errors: list[dict] = []
    warnings: list[dict] = []
    edges_set: set[tuple[str, str]] = set()
    unresolved_counter = Counter()

    for record in records:
        fm = record["frontmatter"]
        source = record["path"]

        # Legacy-schema migration warnings. These are deliberately non-fatal in v1.
        if record["type"] == "project" and "company" in fm:
            warnings.append({"kind": "legacy-project-company-field", "source": source, "detail": "prefer companies"})
        if "affiliation" in fm:
            warnings.append({"kind": "legacy-affiliation-field", "source": source, "detail": "prefer affiliations/current_affiliations"})
        if record["type"] == "person" and not fm.get("name"):
            warnings.append({"kind": "person-missing-name", "source": source})
        if record["type"] == "project" and not REPO_RE.search(record["text"]):
            warnings.append({"kind": "project-missing-official-repo", "source": source})
        if record["type"] == "person" and not URL_RE.search(record["text"]):
            warnings.append({"kind": "person-missing-source-url", "source": source})

        if record["type"] == "person-link":
            canonical = fm.get("canonical")
            if not isinstance(canonical, str) or not canonical.strip():
                errors.append({"kind": "person-link-missing-canonical", "source": source})
            else:
                target, reason, candidates = resolve(canonical, record, by_rel, by_base)
                if target is None:
                    errors.append(
                        {
                            "kind": "person-link-broken-canonical",
                            "source": source,
                            "target": canonical,
                            "reason": reason,
                            "candidates": candidates,
                        }
                    )
                elif target["type"] != "person":
                    errors.append(
                        {
                            "kind": "person-link-canonical-not-person",
                            "source": source,
                            "target": target["path"],
                            "target_type": target["type"],
                        }
                    )

        for match in WIKILINK_RE.finditer(record["text"]):
            target_raw = link_target(match.group(1))
            if not target_raw:
                continue
            target, reason, candidates = resolve(target_raw, record, by_rel, by_base)
            if target is not None:
                if target["id"] != record["id"]:
                    edges_set.add((record["id"], target["id"]))
                continue
            unresolved_counter[reason] += 1
            issue = {
                "kind": f"wikilink-{reason}",
                "source": source,
                "target": target_raw,
                "candidates": candidates,
            }
            if reason == "ambiguous" or args.fail_on_missing:
                errors.append(issue)
            else:
                warnings.append(issue)

    # Duplicate canonical person names are suspicious but can be legitimate namesakes.
    person_names: dict[str, list[str]] = defaultdict(list)
    for record in records:
        if record["type"] != "person":
            continue
        name = str(record["frontmatter"].get("name") or record["name"]).strip().casefold()
        if name:
            person_names[name].append(record["path"])
    for name, files in person_names.items():
        if len(files) > 1:
            warnings.append({"kind": "duplicate-person-name", "source": files[0], "detail": files})

    # Undirected neighborhood metrics over resolved Markdown links.
    neighbors: dict[str, set[str]] = defaultdict(set)
    for source, target in edges_set:
        neighbors[source].add(target)
        neighbors[target].add(source)

    by_id = {record["id"]: record for record in records}
    metrics: dict[str, dict] = {}
    for record in records:
        node_id = record["id"]
        adjacent = neighbors.get(node_id, set())
        categories = {by_id[n]["category"] for n in adjacent if n in by_id}
        cross_category = sum(1 for n in adjacent if n in by_id and by_id[n]["category"] != record["category"])
        degree = len(adjacent)
        bridge_score = round(math.log2(degree + 1) + 1.5 * len(categories) + 0.35 * cross_category, 3)
        metrics[node_id] = {
            "degree": degree,
            "cross_category_degree": cross_category,
            "neighbor_categories": sorted(categories),
            "bridge_score": bridge_score,
        }
        if record["type"] in {"person", "person-link", "project", "company", "university"} and degree == 0:
            warnings.append({"kind": "orphan-node", "source": record["path"]})

    # Connected components help spot accidental islands without requiring networkx.
    components: list[list[str]] = []
    seen: set[str] = set()
    for node_id in by_id:
        if node_id in seen:
            continue
        component = []
        queue = deque([node_id])
        seen.add(node_id)
        while queue:
            current = queue.popleft()
            component.append(current)
            for nxt in neighbors.get(current, set()):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        components.append(sorted(component))
    components.sort(key=len, reverse=True)

    nodes_export = []
    for record in records:
        nodes_export.append(
            {
                "id": record["id"],
                "path": record["path"],
                "name": record["name"],
                "type": record["type"],
                "category": record["category"],
                "frontmatter": record["frontmatter"],
            }
        )
    edges_export = [
        {"source": source, "target": target, "kind": "wikilink"}
        for source, target in sorted(edges_set)
    ]

    # Research queue: favor inference-relevant people with bridge value, while
    # nudging thin/under-sourced nodes upward for verification work.
    candidates = []
    for record in records:
        if record["type"] != "person":
            continue
        fm = record["frontmatter"]
        m = metrics[record["id"]]
        body_len = len(record["body"].strip())
        thin_bonus = 2.0 if body_len < 900 else (1.0 if body_len < 1600 else 0.0)
        source_bonus = 1.2 if not URL_RE.search(record["text"]) else 0.0
        areas = fm.get("areas") if isinstance(fm.get("areas"), list) else []
        relevance = 1.0 if areas else 0.0
        score = round(m["bridge_score"] + thin_bonus + source_bonus + relevance, 3)
        candidates.append((score, record, m, thin_bonus, source_bonus))
    candidates.sort(key=lambda item: (-item[0], str(item[1]["name"])))

    queue_lines = [
        "# Research Queue",
        "",
        "由 `scripts/audit-graph.py` 自动生成。它不是事实排名，而是下一轮人工核验 / BFS 的优先级提示。",
        "",
        "评分偏好：跨目录桥梁度、已有连接密度、薄节点、缺少来源链接，以及已有 `areas` 技术标签。",
        "",
        "| Rank | Person | Score | Degree | Cross-category | Why inspect |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for rank, (score, record, m, thin_bonus, source_bonus) in enumerate(candidates[:40], 1):
        reasons = []
        if m["cross_category_degree"]:
            reasons.append(f"跨类别边 {m['cross_category_degree']}")
        if thin_bonus:
            reasons.append("页面偏薄")
        if source_bonus:
            reasons.append("缺来源 URL")
        if not reasons:
            reasons.append("高连接度")
        label = str(record["name"]).replace("|", "\\|")
        queue_lines.append(
            f"| {rank} | [[{record['id']}|{label}]] | {score:.3f} | {m['degree']} | {m['cross_category_degree']} | {'；'.join(reasons)} |"
        )
    queue_lines.extend(
        [
            "",
            "## Audit snapshot",
            "",
            f"- Markdown nodes: {len(records)}",
            f"- Resolved graph edges: {len(edges_export)}",
            f"- Connected components: {len(components)}",
            f"- Hard errors: {len(errors)}",
            f"- Warnings: {len(warnings)}",
            f"- Missing wikilinks: {unresolved_counter.get('missing', 0)}",
            f"- Ambiguous wikilinks: {unresolved_counter.get('ambiguous', 0)}",
        ]
    )

    audit = {
        "markdown_nodes": len(records),
        "resolved_edges": len(edges_export),
        "components": [len(c) for c in components],
        "unresolved": dict(unresolved_counter),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
    }

    (out / "nodes.json").write_text(json.dumps(nodes_export, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "edges.json").write_text(json.dumps(edges_export, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "graph.json").write_text(
        json.dumps({"nodes": nodes_export, "edges": edges_export, "metrics": metrics}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (out / "research-queue.md").write_text("\n".join(queue_lines) + "\n", encoding="utf-8")

    print(
        f"Graph audit: {len(records)} Markdown nodes, {len(edges_export)} resolved edges, "
        f"{len(errors)} errors, {len(warnings)} warnings, {len(components)} components."
    )
    for issue in errors[:80]:
        print("ERROR:", short_issue(issue))
    if len(errors) > 80:
        print(f"... plus {len(errors) - 80} more errors; see {out / 'audit.json'}")
    for issue in warnings[:30]:
        print("WARN:", short_issue(issue))
    if len(warnings) > 30:
        print(f"... plus {len(warnings) - 30} more warnings; see {out / 'audit.json'}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
