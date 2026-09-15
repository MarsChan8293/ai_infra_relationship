#!/usr/bin/env python3
"""Generate a gap-aware Best-First research queue with selective DFS hints.

This script consumes the graph inventory produced by ``scripts/audit-graph.py``
and ranks person nodes for the next research pass. The goal is not to rank
people by importance. It ranks *research opportunities* by bridge value,
missing relationship dimensions, AI-infra relevance, evidence quality,
novelty, and optional distance from a seed node.

Outputs:
  generated/research-priority.json
  generated/research-queue.md

Typical usage:
  python3 scripts/audit-graph.py --root . --output generated
  python3 scripts/generate-research-queue.py --root . --generated generated
  python3 scripts/generate-research-queue.py --seed "游凯超" --limit 40
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import deque

URL_RE = re.compile(r"https?://[^\s)>\]]+", re.I)

# The groups are intentionally broad and explainable. They bias the queue toward
# inference-system talent without hard-coding particular people or companies.
RELEVANCE_GROUPS: tuple[tuple[str, tuple[str, ...], float], ...] = (
    ("serving/inference", ("inference", "serving", "推理", "在线服务"), 1.00),
    ("kv-cache", ("kv cache", "kv-cache", "kvcache", "pagedattention", "prefix cache", "lmcache"), 0.95),
    ("scheduler", ("scheduler", "scheduling", "调度", "continuous batching", "batching"), 0.85),
    ("kernel", ("kernel", "cuda", "triton", "cutlass", "算子", "内核"), 0.90),
    ("distributed", ("distributed", "parallel", "communication", "collective", "并行", "通信", "分布式"), 0.75),
    ("moe", ("moe", "mixture of experts", "expert parallel", "专家并行"), 0.75),
    ("quantization", ("quantization", "quantized", "fp8", "int8", "int4", "量化"), 0.65),
    ("disaggregation", ("disaggregation", "prefill decode", "prefill-decode", "pd separation", "解耦"), 0.85),
    ("ascend", ("ascend", "昇腾", "cann"), 1.00),
)


def as_list(value) -> list:
    if isinstance(value, list):
        return [item for item in value if item not in (None, "")]
    if value in (None, ""):
        return []
    return [value]


def first_nonempty_list(frontmatter: dict, *keys: str) -> list:
    for key in keys:
        values = as_list(frontmatter.get(key))
        if values:
            return values
    return []


def resolve_seed(seed: str, nodes: list[dict]) -> str:
    wanted = seed.strip().casefold()
    if not wanted:
        raise ValueError("empty seed")

    exact_ids = [node["id"] for node in nodes if str(node.get("id", "")).casefold() == wanted]
    if len(exact_ids) == 1:
        return exact_ids[0]

    matches = []
    for node in nodes:
        names = {
            str(node.get("name", "")).strip().casefold(),
            pathlib.PurePosixPath(str(node.get("id", ""))).name.casefold(),
        }
        fm = node.get("frontmatter") if isinstance(node.get("frontmatter"), dict) else {}
        for alias in as_list(fm.get("aliases")):
            names.add(str(alias).strip().casefold())
        if wanted in names:
            matches.append(node["id"])

    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise ValueError(f"seed not found: {seed}")
    raise ValueError(f"seed is ambiguous: {seed} -> {', '.join(matches[:8])}")


def shortest_distances(seed_id: str, neighbors: dict[str, set[str]]) -> dict[str, int]:
    distances = {seed_id: 0}
    queue = deque([seed_id])
    while queue:
        current = queue.popleft()
        for nxt in neighbors.get(current, set()):
            if nxt in distances:
                continue
            distances[nxt] = distances[current] + 1
            queue.append(nxt)
    return distances


def relevance_score(text: str) -> tuple[float, list[str]]:
    haystack = text.casefold()
    score = 0.0
    hits = []
    for label, keywords, weight in RELEVANCE_GROUPS:
        if any(keyword.casefold() in haystack for keyword in keywords):
            score += weight
            hits.append(label)
    return round(min(score, 4.0), 3), hits


def evidence_score(text: str) -> tuple[float, int]:
    urls = sorted(set(URL_RE.findall(text)))
    if not urls:
        return 0.0, 0
    score = 0.55 if len(urls) == 1 else 0.90
    trusted_markers = ("github.com/", "gitcode.com/", "gitee.com/", "arxiv.org/", "doi.org/", "docs.")
    if any(marker in url.casefold() for url in urls for marker in trusted_markers):
        score += 0.35
    if len(urls) >= 3:
        score += 0.20
    return round(min(score, 1.5), 3), len(urls)


def distance_penalty(distance: int | None, max_bfs_depth: int, seed_enabled: bool) -> float:
    if not seed_enabled:
        return 0.0
    if distance is None:
        return 4.0
    if distance <= 1:
        return 0.0
    if distance <= max_bfs_depth:
        return 0.30 * (distance - 1)
    return 0.30 * max(0, max_bfs_depth - 1) + 1.20 * (distance - max_bfs_depth)


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--seed", help="Optional person/node id, name, basename, or alias")
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--max-bfs-depth", type=int, default=2)
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    nodes_path = generated / "nodes.json"
    edges_path = generated / "edges.json"
    metrics_path = generated / "metrics.json"

    for path in (nodes_path, edges_path, metrics_path):
        if not path.exists():
            parser.error(f"missing {path}; run scripts/audit-graph.py first")

    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    edges = json.loads(edges_path.read_text(encoding="utf-8"))
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    by_id = {node["id"]: node for node in nodes}

    neighbors: dict[str, set[str]] = {node_id: set() for node_id in by_id}
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        if source in by_id and target in by_id:
            neighbors[source].add(target)
            neighbors[target].add(source)

    seed_id = None
    distances: dict[str, int] = {}
    if args.seed:
        try:
            seed_id = resolve_seed(args.seed, nodes)
        except ValueError as exc:
            parser.error(str(exc))
        distances = shortest_distances(seed_id, neighbors)

    candidates = []
    for node in nodes:
        if node.get("type") != "person":
            continue

        node_id = node["id"]
        fm = node.get("frontmatter") if isinstance(node.get("frontmatter"), dict) else {}
        path = root / str(node.get("path", ""))
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        body_len = len(text.strip())

        affiliations = first_nonempty_list(fm, "current_affiliations", "affiliations", "affiliation")
        projects = first_nonempty_list(fm, "projects")
        communities = first_nonempty_list(fm, "communities")
        relations = first_nonempty_list(fm, "relations")
        areas = first_nonempty_list(fm, "areas")
        roles = first_nonempty_list(fm, "roles")

        gaps: list[str] = []
        gap_score = 0.0
        if not affiliations:
            gaps.append("affiliation")
            gap_score += 0.90
        if not projects and not communities:
            gaps.append("projects/communities")
            gap_score += 1.10
        if not relations:
            gaps.append("relations")
            gap_score += 1.30
        if not areas:
            gaps.append("areas")
            gap_score += 0.75
        if not URL_RE.search(text):
            gaps.append("sources")
            gap_score += 1.00
        if body_len < 900:
            gaps.append("thin-page")
            gap_score += 1.00
        elif body_len < 1600:
            gaps.append("thin-page")
            gap_score += 0.50
        gap_score = round(min(gap_score, 4.5), 3)

        combined = "\n".join(
            [
                text,
                " ".join(str(item) for item in areas),
                " ".join(str(item) for item in roles),
                " ".join(str(item) for item in projects),
                " ".join(str(item) for item in communities),
            ]
        )
        relevance, relevance_hits = relevance_score(combined)
        evidence, url_count = evidence_score(text)

        adjacent = neighbors.get(node_id, set())
        neighbor_types = {str(by_id[n].get("type", "")) for n in adjacent if n in by_id}
        ecosystem_neighbors = sum(
            1 for n in adjacent if n in by_id and by_id[n].get("type") in {"project", "community", "company"}
        )
        project_neighbors = sum(
            1 for n in adjacent if n in by_id and by_id[n].get("type") in {"project", "community"}
        )
        novelty = min(3.0, 0.45 * len(neighbor_types) + 0.18 * ecosystem_neighbors)
        novelty = round(novelty, 3)

        bridge = float(metrics.get(node_id, {}).get("bridge_score", 0.0))
        distance = distances.get(node_id) if seed_id else None
        penalty = distance_penalty(distance, args.max_bfs_depth, seed_id is not None)

        score = round(
            1.60 * bridge
            + 1.80 * gap_score
            + 2.00 * relevance
            + 0.80 * evidence
            + 0.90 * novelty
            - 1.20 * penalty,
            3,
        )

        selective_dfs = (
            score >= 18.0
            and bridge >= 5.0
            and relevance >= 1.0
            and ("relations" in gaps or project_neighbors >= 2)
        )
        strategy = "selective-dfs" if selective_dfs else "best-first"

        expansion_targets = []
        label_map = {
            "affiliation": "current affiliation",
            "projects/communities": "project/community links",
            "relations": "typed person relations",
            "areas": "technical areas",
            "sources": "primary sources",
            "thin-page": "biographical/context depth",
        }
        for gap in gaps:
            label = label_map[gap]
            if label not in expansion_targets:
                expansion_targets.append(label)
        if selective_dfs and "hidden person chain" not in expansion_targets:
            expansion_targets.append("hidden person chain")

        reasons = []
        if bridge >= 5:
            reasons.append(f"bridge {bridge:.1f}")
        if gap_score >= 2:
            reasons.append(f"gap {gap_score:.1f}")
        if relevance_hits:
            reasons.append("infra: " + ", ".join(relevance_hits[:3]))
        if project_neighbors >= 2:
            reasons.append(f"multi-project {project_neighbors}")
        if seed_id and distance is not None:
            reasons.append(f"{distance}-hop from seed")
        if not reasons:
            reasons.append("underexplored node")

        candidates.append(
            {
                "id": node_id,
                "name": node.get("name") or pathlib.PurePosixPath(node_id).name,
                "score": score,
                "strategy": strategy,
                "bridge_score": round(bridge, 3),
                "gap_score": gap_score,
                "infra_relevance": relevance,
                "evidence_quality": evidence,
                "novelty": novelty,
                "distance": distance,
                "distance_penalty": round(penalty, 3),
                "gaps": gaps,
                "relevance_hits": relevance_hits,
                "url_count": url_count,
                "project_neighbors": project_neighbors,
                "ecosystem_neighbors": ecosystem_neighbors,
                "expansion_targets": expansion_targets,
                "reasons": reasons,
            }
        )

    candidates.sort(key=lambda item: (-item["score"], str(item["name"])))
    limit = max(1, args.limit)
    shown = candidates[:limit]

    payload = {
        "algorithm": "gap-aware-best-first-bfs-with-selective-dfs",
        "formula": "1.60*bridge + 1.80*gap + 2.00*infra_relevance + 0.80*evidence + 0.90*novelty - 1.20*distance_penalty",
        "seed": seed_id,
        "max_bfs_depth": args.max_bfs_depth,
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    (generated / "research-priority.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# Research Queue",
        "",
        "由 `scripts/generate-research-queue.py` 自动生成。它排序的是下一轮研究价值，不是人物重要性。",
        "",
        "算法：**Gap-aware Best-First BFS + Selective DFS**。先用局部 BFS 建立邻域，再按桥梁度、关系缺口、推理相关性、证据质量与新颖性重新排序；只有高价值桥梁人物才触发 DFS 深挖。",
        "",
        "公式：`1.60×bridge + 1.80×gap + 2.00×infra_relevance + 0.80×evidence + 0.90×novelty - 1.20×distance_penalty`。",
        "",
    ]
    if seed_id:
        lines.extend(
            [
                f"Seed: `[[{seed_id}]]`，BFS 无明显惩罚深度：{args.max_bfs_depth} hop。",
                "",
            ]
        )
    lines.extend(
        [
            "| Rank | Person | Score | Strategy | Bridge | Gap | Infra | Distance | Why / next |",
            "| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for rank, item in enumerate(shown, 1):
        distance_text = "-" if item["distance"] is None else str(item["distance"])
        next_text = "; ".join(item["reasons"])
        if item["expansion_targets"]:
            next_text += " → " + ", ".join(item["expansion_targets"][:3])
        label = escape_cell(item["name"])
        lines.append(
            f"| {rank} | [[{item['id']}|{label}]] | {item['score']:.3f} | {item['strategy']} | "
            f"{item['bridge_score']:.3f} | {item['gap_score']:.3f} | {item['infra_relevance']:.3f} | "
            f"{distance_text} | {escape_cell(next_text)} |"
        )

    lines.extend(
        [
            "",
            "## How to use",
            "",
            "- `best-first`: 优先补齐缺失关系维度，不沿单一路径无限向下钻。",
            "- `selective-dfs`: 只对高桥梁度、高推理相关、且仍存在关系缺口的人物做深挖。",
            "- 需要从某个人出发时，使用 `--seed <name-or-id>`；距离会进入评分，默认优先保留 2-hop 局部网络。",
            "",
        ]
    )
    (generated / "research-queue.md").write_text("\n".join(lines), encoding="utf-8")

    print(
        f"Research queue: {len(candidates)} person candidates, showing {len(shown)}, "
        f"selective DFS={sum(1 for item in candidates if item['strategy'] == 'selective-dfs')}."
    )
    if seed_id:
        print(f"Seed resolved to: {seed_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
