#!/usr/bin/env python3
"""Generate a heterogeneous ecosystem research-action queue.

This planner consumes the graph inventory produced by ``scripts/audit-graph.py``
and ranks *research actions*, not people. A research action is a typed request:

    source entity -> relation to investigate -> target entity type(s) -> source strategy

The planner is deterministic and intentionally lightweight so that a daily
ChatGPT/Codex agent can execute a bounded set of actions without inventing its
own global traversal strategy.

Primary outputs:
  generated/research-actions.json
  generated/research-queue.md

Compatibility output:
  generated/research-priority.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import pathlib
import re
import sys
from collections import Counter, deque

URL_RE = re.compile(r"https?://[^\s)>\]]+", re.I)

RELEVANCE_GROUPS: tuple[tuple[str, tuple[str, ...], float], ...] = (
    ("serving/inference", ("inference", "serving", "推理", "在线服务"), 1.00),
    ("kv-cache", ("kv cache", "kv-cache", "kvcache", "pagedattention", "prefix cache", "lmcache"), 0.95),
    ("scheduler", ("scheduler", "scheduling", "调度", "continuous batching", "batching"), 0.85),
    ("kernel", ("kernel", "cuda", "triton", "cutlass", "算子", "内核"), 0.90),
    ("distributed", ("distributed", "parallel", "communication", "collective", "并行", "通信", "分布式"), 0.75),
    ("moe", ("moe", "mixture of experts", "expert parallel", "专家并行"), 0.75),
    ("quantization", ("quantization", "quantized", "fp8", "int8", "int4", "量化"), 0.65),
    ("disaggregation", ("disaggregation", "prefill decode", "prefill-decode", "pd separation", "解耦"), 0.85),
    ("ascend", ("ascend", "昇腾", "cann", "mindie", "torch_npu"), 1.00),
)

TYPE_FAMILY = {
    "person": "person",
    "person-link": "person",
    "company": "company",
    "school": "school",
    "university": "school",
    "research-institution": "research",
    "project": "project",
    "model-project": "project",
    "project-collection": "project",
    "community": "community",
    "model-team": "team",
}

FAMILY_LABEL = {
    "person": "Person",
    "company": "Company",
    "school": "School",
    "research": "Research Institution",
    "project": "Project",
    "community": "Community",
    "team": "Team",
}

# fields are coverage hints. target_families also inspect resolved graph neighbours.
# desired_count is a saturation target for planning, not a truth/completeness claim.
ACTION_TEMPLATES: dict[str, tuple[dict, ...]] = {
    "person": (
        {"relation": "affiliation", "target_families": ("company", "school", "research", "team"), "fields": ("current_affiliations", "affiliations", "affiliation"), "desired_count": 2, "prior": 1.00, "cost": 1.0, "strategies": ("official_profile", "company_or_lab_team_page"), "write_hint": "Update affiliations/schools only with direct evidence; keep historical context in prose."},
        {"relation": "project_contribution", "target_families": ("project", "community"), "fields": ("projects", "communities"), "desired_count": 3, "prior": 1.20, "cost": 1.0, "strategies": ("github_or_gitcode_activity", "project_governance_or_release_notes"), "write_hint": "Prefer explicit project/community metadata plus evidence-backed prose."},
        {"relation": "technical_collaborator", "target_families": ("person",), "fields": ("relations",), "desired_count": 3, "prior": 0.90, "cost": 1.3, "strategies": ("github_pr_commit_review", "paper_or_technical_report"), "write_hint": "Add a typed relation only when collaboration type, context, and evidence are explicit."},
        {"relation": "academic_lineage", "target_families": ("person", "school", "research"), "fields": ("schools", "education"), "desired_count": 2, "prior": 0.75, "cost": 1.4, "strategies": ("official_academic_profile", "thesis_or_lab_page"), "write_hint": "Do not infer advisor/student from shared school; require direct evidence."},
    ),
    "company": (
        {"relation": "key_people", "target_families": ("person",), "fields": ("people", "linked_people"), "desired_count": 4, "prior": 1.00, "cost": 1.1, "strategies": ("official_team_page", "github_org_maintainers"), "write_hint": "Curate only high-value AI Infra people; linked_people remains derived."},
        {"relation": "projects", "target_families": ("project", "community", "team"), "fields": ("projects", "linked_projects", "communities"), "desired_count": 3, "prior": 1.25, "cost": 1.0, "strategies": ("github_org_repositories", "official_engineering_blog_or_docs"), "write_hint": "Require origin, governance, or core-maintainer evidence; compatibility alone is insufficient."},
        {"relation": "academic_links", "target_families": ("school", "research"), "fields": (), "desired_count": 1, "prior": 0.65, "cost": 1.5, "strategies": ("official_research_partnership_page", "paper_affiliation"), "write_hint": "Create only direct research, spinout, or institutional collaboration links."},
    ),
    "school": (
        {"relation": "labs_or_groups", "target_families": ("research", "team"), "fields": ("labs",), "desired_count": 2, "prior": 1.15, "cost": 1.1, "strategies": ("official_department_or_lab_directory",), "write_hint": "Add labs/groups only when the institutional relationship is explicit."},
        {"relation": "key_people", "target_families": ("person",), "fields": ("people", "linked_people"), "desired_count": 5, "prior": 1.20, "cost": 1.0, "strategies": ("faculty_directory", "lab_people_pages"), "write_hint": "Prioritize AI Infra faculty, students, alumni, and maintainers with verifiable relevance."},
        {"relation": "projects", "target_families": ("project", "community"), "fields": (), "desired_count": 2, "prior": 1.10, "cost": 1.2, "strategies": ("lab_github_org", "official_project_pages"), "write_hint": "Connect projects only when the school/lab relationship is directly supported."},
        {"relation": "spinouts", "target_families": ("company",), "fields": (), "desired_count": 1, "prior": 0.75, "cost": 1.6, "strategies": ("official_founder_bio", "university_news_or_tech_transfer"), "write_hint": "Require founder/alumni/lab-spinoff evidence; do not infer from geography or hiring."},
    ),
    "research": (
        {"relation": "key_people", "target_families": ("person",), "fields": ("people", "linked_people"), "desired_count": 4, "prior": 1.20, "cost": 1.0, "strategies": ("official_people_directory", "project_author_pages"), "write_hint": "Prefer researchers with concrete AI Infra projects or systems work."},
        {"relation": "projects", "target_families": ("project", "community"), "fields": ("projects", "communities"), "desired_count": 3, "prior": 1.25, "cost": 1.0, "strategies": ("official_project_pages", "github_org_repositories"), "write_hint": "Connect only projects with direct institutional authorship or governance evidence."},
        {"relation": "parent_or_partner_org", "target_families": ("school", "company", "research"), "fields": ("affiliations", "parent"), "desired_count": 1, "prior": 0.70, "cost": 1.3, "strategies": ("official_about_page", "institutional_partnership_page"), "write_hint": "Distinguish parent institution from collaboration or sponsorship."},
    ),
    "project": (
        {"relation": "maintainers", "target_families": ("person",), "fields": ("people", "linked_people"), "desired_count": 4, "prior": 1.35, "cost": 0.9, "strategies": ("governance_maintainers_codeowners", "github_or_gitcode_contributors"), "write_hint": "Prefer governance, CODEOWNERS, MAINTAINERS, release credits, or sustained contribution evidence."},
        {"relation": "originating_org", "target_families": ("company", "school", "research", "community", "team"), "fields": ("companies", "linked_companies", "company"), "desired_count": 1, "prior": 1.10, "cost": 1.0, "strategies": ("official_repository_org", "project_docs_or_announcement"), "write_hint": "Distinguish origin/core governance from downstream usage, integration, or sponsorship."},
        {"relation": "related_projects", "target_families": ("project", "community"), "fields": ("integrations", "related_projects"), "desired_count": 3, "prior": 0.95, "cost": 1.2, "strategies": ("official_docs_integrations", "repository_dependencies_or_design_docs"), "write_hint": "Record the concrete technical relationship; compatibility alone is not a people relation."},
    ),
    "community": (
        {"relation": "core_people", "target_families": ("person",), "fields": ("people", "linked_people"), "desired_count": 4, "prior": 1.20, "cost": 1.0, "strategies": ("governance_or_maintainers", "github_or_gitcode_activity"), "write_hint": "Prefer organizers/maintainers with direct public evidence."},
        {"relation": "projects", "target_families": ("project",), "fields": ("projects",), "desired_count": 3, "prior": 1.20, "cost": 1.0, "strategies": ("community_docs", "official_repository_namespace"), "write_hint": "Add concrete projects that belong to or are governed by the community."},
        {"relation": "member_orgs", "target_families": ("company", "school", "research"), "fields": ("companies", "linked_companies"), "desired_count": 3, "prior": 0.90, "cost": 1.3, "strategies": ("governance_membership_page", "official_announcements"), "write_hint": "Require governance, founding, or core-maintainer evidence; sponsorship alone is insufficient."},
    ),
    "team": (
        {"relation": "key_people", "target_families": ("person",), "fields": ("people", "linked_people"), "desired_count": 4, "prior": 1.20, "cost": 1.0, "strategies": ("official_team_or_author_page", "github_activity"), "write_hint": "Prefer people with direct technical responsibility or authorship."},
        {"relation": "parent_org", "target_families": ("company", "school", "research"), "fields": ("company", "companies", "affiliations"), "desired_count": 1, "prior": 0.90, "cost": 0.8, "strategies": ("official_team_page", "parent_org_docs"), "write_hint": "Attach to the canonical parent organization rather than creating duplicate company entities."},
        {"relation": "projects", "target_families": ("project", "community"), "fields": ("projects", "communities"), "desired_count": 3, "prior": 1.10, "cost": 1.0, "strategies": ("official_project_page", "github_org_repositories"), "write_hint": "Connect projects with direct team authorship or governance evidence."},
    ),
}

FRONTIER_PRIOR = {"person": 0.75, "company": 1.00, "school": 1.00, "research": 1.05, "project": 1.15, "community": 1.10, "team": 1.00}


def as_list(value) -> list:
    if isinstance(value, list):
        return [item for item in value if item not in (None, "")]
    if value in (None, ""):
        return []
    return [value]


def type_family(raw_type: object) -> str | None:
    return TYPE_FAMILY.get(str(raw_type or "").strip())


def resolve_seed(seed: str, nodes: list[dict]) -> str:
    wanted = seed.strip().casefold()
    if not wanted:
        raise ValueError("empty seed")
    exact_ids = [node["id"] for node in nodes if str(node.get("id", "")).casefold() == wanted]
    if len(exact_ids) == 1:
        return exact_ids[0]
    matches = []
    for node in nodes:
        names = {str(node.get("name", "")).strip().casefold(), pathlib.PurePosixPath(str(node.get("id", ""))).name.casefold()}
        fm = node.get("frontmatter") if isinstance(node.get("frontmatter"), dict) else {}
        names.update(str(alias).strip().casefold() for alias in as_list(fm.get("aliases")))
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


def project_freshness_age_months(value: object) -> int | None:
    match = re.fullmatch(r"(\d{4})-(\d{2})", str(value or "").strip())
    if not match:
        return None
    year, month = int(match.group(1)), int(match.group(2))
    if not 1 <= month <= 12:
        return None
    today = dt.date.today()
    return max(0, (today.year - year) * 12 + today.month - month)


def evidence_score(text: str) -> tuple[float, int]:
    urls = sorted(set(URL_RE.findall(text)))
    if not urls:
        return 0.0, 0
    score = 0.45 if len(urls) == 1 else 0.75
    primary_markers = ("github.com/", "gitcode.com/", "gitee.com/", "arxiv.org/", "doi.org/", ".edu/", ".edu.cn/", "docs.")
    if any(marker in url.casefold() for url in urls for marker in primary_markers):
        score += 0.35
    if len(urls) >= 3:
        score += 0.20
    return round(min(score, 1.30), 3), len(urls)


def field_count(frontmatter: dict, fields: tuple[str, ...]) -> int:
    refs: set[str] = set()
    for field in fields:
        for item in as_list(frontmatter.get(field)):
            text = str(item).strip().casefold()
            if text:
                refs.add(text)
    return len(refs)


def neighbor_family_count(node_id: str, target_families: tuple[str, ...], neighbors: dict[str, set[str]], by_id: dict[str, dict]) -> int:
    return sum(1 for neighbor_id in neighbors.get(node_id, set()) if neighbor_id in by_id and type_family(by_id[neighbor_id].get("type")) in target_families)


def existing_coverage(node: dict, template: dict, neighbors: dict[str, set[str]], by_id: dict[str, dict]) -> int:
    fm = node.get("frontmatter") if isinstance(node.get("frontmatter"), dict) else {}
    explicit = field_count(fm, tuple(template.get("fields", ())))
    graph_count = neighbor_family_count(node["id"], tuple(template.get("target_families", ())), neighbors, by_id)
    return max(explicit, graph_count)


def soft_distance_penalty(distance: int | None, seed_enabled: bool, max_bfs_depth: int) -> float:
    if not seed_enabled:
        return 0.0
    if distance is None:
        return 1.20
    if distance <= max_bfs_depth:
        return 0.0
    return min(1.20, 0.16 * (distance - max_bfs_depth))


def action_bucket(evidence: float, degree: int, novelty: float, bridge_component: float) -> str:
    if evidence < 0.45:
        return "verification"
    if degree <= 3 and novelty >= 0.60:
        return "exploration"
    if bridge_component >= 0.75 and novelty >= 0.35:
        return "bridge"
    return "exploitation"


def build_actions(root: pathlib.Path, nodes: list[dict], edges: list[dict], metrics: dict, seed_id: str | None, max_bfs_depth: int) -> list[dict]:
    by_id = {node["id"]: node for node in nodes}
    neighbors: dict[str, set[str]] = {node_id: set() for node_id in by_id}
    for edge in edges:
        source, target = edge.get("source"), edge.get("target")
        if source in by_id and target in by_id:
            neighbors[source].add(target)
            neighbors[target].add(source)
    distances = shortest_distances(seed_id, neighbors) if seed_id else {}
    actions: list[dict] = []

    for node in nodes:
        family = type_family(node.get("type"))
        if family not in ACTION_TEMPLATES:
            continue
        node_id = node["id"]
        path = root / str(node.get("path", ""))
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        relevance, relevance_hits = relevance_score(text)
        evidence, url_count = evidence_score(text)
        metric = metrics.get(node_id, {})
        degree = int(metric.get("degree", len(neighbors.get(node_id, set()))))
        bridge_raw = float(metric.get("bridge_score", 0.0))
        bridge_component = min(1.50, bridge_raw / 8.0)
        distance = distances.get(node_id) if seed_id else None
        distance_penalty = soft_distance_penalty(distance, seed_id is not None, max_bfs_depth)
        neighbor_families = {type_family(by_id[n].get("type")) for n in neighbors.get(node_id, set()) if n in by_id and type_family(by_id[n].get("type"))}

        for template in ACTION_TEMPLATES[family]:
            desired = max(1, int(template["desired_count"]))
            existing = existing_coverage(node, template, neighbors, by_id)
            gap = max(0.0, 1.0 - min(existing, desired) / desired)
            if gap <= 0.0:
                continue
            targets = tuple(template["target_families"])
            unseen_targets = sum(1 for target in targets if target not in neighbor_families)
            novelty = unseen_targets / max(1, len(targets))
            frontier = FRONTIER_PRIOR.get(family, 0.8) / math.sqrt(max(1.0, degree + 1.0))
            uncertainty = min(1.0, 0.55 * gap + 0.45 * max(0.0, 1.0 - evidence / 1.30))
            redundancy = 0.20 * math.log1p(existing) + 0.08 * math.log1p(max(0, degree))
            prior, cost = float(template["prior"]), max(0.5, float(template["cost"]))
            gain_proxy = 2.30 * gap + 1.35 * min(1.50, relevance / 2.0) + 1.15 * novelty + 0.90 * bridge_component + 0.80 * frontier + 0.65 * uncertainty + 0.35 * evidence + 0.80 * prior
            priority = round(gain_proxy / cost - redundancy - distance_penalty, 3)
            bucket = action_bucket(evidence, degree, novelty, bridge_component)
            action_key = f"{family}:{template['relation']}:{'+'.join(targets)}"
            reasons = [f"coverage {existing}/{desired}", f"source type {FAMILY_LABEL.get(family, family)}"]
            if relevance_hits:
                reasons.append("infra: " + ", ".join(relevance_hits[:3]))
            if novelty >= 0.60:
                reasons.append("opens underrepresented target types")
            if bridge_raw >= 6.0:
                reasons.append(f"bridge {bridge_raw:.1f}")
            if url_count == 0:
                reasons.append("missing source URLs")
            if seed_id and distance is not None:
                reasons.append(f"{distance}-hop from seed")
            actions.append({
                "action_id": f"{node_id}::{template['relation']}",
                "action_key": action_key,
                "source": {"id": node_id, "name": node.get("name") or pathlib.PurePosixPath(node_id).name, "type": node.get("type"), "family": family},
                "relation": template["relation"],
                "target_families": list(targets),
                "strategies": list(template["strategies"]),
                "write_hint": template["write_hint"],
                "bucket": bucket,
                "priority": priority,
                "cost": cost,
                "coverage": {"existing": existing, "desired": desired, "gap": round(gap, 3)},
                "signals": {"infra_relevance": relevance, "evidence_quality": evidence, "url_count": url_count, "bridge_score": round(bridge_raw, 3), "novelty": round(novelty, 3), "frontier_potential": round(frontier, 3), "uncertainty": round(uncertainty, 3), "redundancy_penalty": round(redundancy, 3), "distance": distance, "distance_penalty": round(distance_penalty, 3)},
                "reasons": reasons,
            })

        # Verification is a first-class action so weak evidence does not silently accumulate.
        desired_urls = 2
        if url_count < desired_urls:
            gap = 1.0 - url_count / desired_urls
            cost = 0.8
            redundancy = 0.05 * math.log1p(max(0, degree))
            gain_proxy = 2.00 * gap + 0.80 * min(1.50, relevance / 2.0) + 0.65 * bridge_component + 0.50 * FRONTIER_PRIOR.get(family, 0.8)
            priority = round(gain_proxy / cost - redundancy - distance_penalty, 3)
            actions.append({
                "action_id": f"{node_id}::verify_evidence",
                "action_key": f"{family}:verify_evidence:none",
                "source": {"id": node_id, "name": node.get("name") or pathlib.PurePosixPath(node_id).name, "type": node.get("type"), "family": family},
                "relation": "verify_evidence",
                "target_families": [],
                "strategies": ["official_primary_sources", "repository_or_paper_sources"],
                "write_hint": "Strengthen or reject important claims; do not create a new relation without direct evidence.",
                "bucket": "verification",
                "priority": priority,
                "cost": cost,
                "coverage": {"existing": url_count, "desired": desired_urls, "gap": round(gap, 3)},
                "signals": {"infra_relevance": relevance, "evidence_quality": evidence, "url_count": url_count, "bridge_score": round(bridge_raw, 3), "novelty": 0.0, "frontier_potential": round(FRONTIER_PRIOR.get(family, 0.8), 3), "uncertainty": round(gap, 3), "redundancy_penalty": round(redundancy, 3), "distance": distance, "distance_penalty": round(distance_penalty, 3)},
                "reasons": [f"source coverage {url_count}/{desired_urls}", "evidence quality below target"],
            })

        if family == "project":
            fm = node.get("frontmatter") if isinstance(node.get("frontmatter"), dict) else {}
            freshness_age = project_freshness_age_months(fm.get("last_verified"))
            if freshness_age is None or freshness_age >= 3:
                freshness_gap = 1.0 if freshness_age is None else min(1.0, freshness_age / 12.0)
                cost = 0.9
                redundancy = 0.05 * math.log1p(max(0, degree))
                gain_proxy = 1.70 * freshness_gap + 0.65 * min(1.50, relevance / 2.0) + 0.35 * bridge_component
                priority = round(gain_proxy / cost - redundancy - distance_penalty, 3)
                reasons = [
                    "missing last_verified" if freshness_age is None else f"last_verified age {freshness_age} months",
                    f"status={fm.get('status') or 'unknown'}",
                ]
                integrations = as_list(fm.get("integrations"))
                if integrations:
                    reasons.append(f"{len(integrations)} integrations to re-check")
                actions.append({
                    "action_id": f"{node_id}::verify_project_freshness",
                    "action_key": "project:verify_project_freshness:none",
                    "source": {"id": node_id, "name": node.get("name") or pathlib.PurePosixPath(node_id).name, "type": node.get("type"), "family": family},
                    "relation": "verify_project_freshness",
                    "target_families": [],
                    "strategies": ["official_repository_releases", "official_docs", "integration_docs"],
                    "write_hint": "Re-check project status, canonical repository/docs, integrations, governance drift, and refresh last_verified only with current evidence.",
                    "bucket": "verification",
                    "priority": priority,
                    "cost": cost,
                    "coverage": {"existing": 0 if freshness_age is None else max(0, 3 - freshness_age), "desired": 3, "gap": round(freshness_gap, 3)},
                    "signals": {"infra_relevance": relevance, "evidence_quality": evidence, "url_count": url_count, "bridge_score": round(bridge_raw, 3), "novelty": 0.0, "frontier_potential": round(FRONTIER_PRIOR.get(family, 0.8), 3), "uncertainty": round(freshness_gap, 3), "redundancy_penalty": round(redundancy, 3), "distance": distance, "distance_penalty": round(distance_penalty, 3), "freshness_age_months": freshness_age},
                    "reasons": reasons,
                })

    actions.sort(key=lambda item: (-float(item["priority"]), str(item["source"]["name"]), str(item["relation"])))
    return actions


def portfolio_select(actions: list[dict], budget: int, max_actions_per_source: int) -> list[dict]:
    if budget <= 0:
        return []
    family_cap = max(1, math.ceil(budget * 0.40))
    selected: list[dict] = []
    selected_ids: set[str] = set()
    source_counts: Counter[str] = Counter()
    family_counts: Counter[str] = Counter()
    for relaxed in (False, True):
        for action in actions:
            if len(selected) >= budget:
                break
            action_id, source_id, family = action["action_id"], action["source"]["id"], action["source"]["family"]
            if action_id in selected_ids or source_counts[source_id] >= max_actions_per_source:
                continue
            if not relaxed and family_counts[family] >= family_cap:
                continue
            selected.append(action)
            selected_ids.add(action_id)
            source_counts[source_id] += 1
            family_counts[family] += 1
        if len(selected) >= budget:
            break
    return selected


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_markdown(path: pathlib.Path, selected: list[dict], actions: list[dict], seed_id: str | None, budget: int) -> None:
    lines = [
        "# Ecosystem Research Action Queue", "",
        "由 `scripts/generate-research-queue.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。", "",
        "算法：**Typed Action Planner + heterogeneous portfolio selection**。每个动作由 `source entity × relation × target type × source strategy` 构成；优先级综合关系覆盖缺口、AI Infra 相关性、桥梁价值、目标类型新颖性、证据质量、frontier potential、uncertainty、research cost、redundancy/hub penalty 与可选 seed 距离。", "",
        f"- Daily budget: {budget}", f"- Seed: `{seed_id}`" if seed_id else "- Seed: none (global ecosystem mode)", f"- Candidate actions: {len(actions)}", f"- Selected actions: {len(selected)}", "",
        "## Selected actions", "", "| Rank | Source | Type | Research action | Target | Bucket | Priority | Why |", "| ---: | --- | --- | --- | --- | --- | ---: | --- |",
    ]
    for rank, action in enumerate(selected, 1):
        source = action["source"]
        target = ", ".join(action["target_families"]) or "evidence"
        why = "；".join(action["reasons"][:3])
        lines.append(f"| {rank} | [[{source['id']}\\|{escape_cell(source['name'])}]] | {escape_cell(source['family'])} | {escape_cell(action['relation'])} | {escape_cell(target)} | {escape_cell(action['bucket'])} | {float(action['priority']):.3f} | {escape_cell(why)} |")
    lines.extend([
        "", "## Agent execution contract", "", "对每个 selected action：", "",
        "1. 优先查官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文或机构一手资料。",
        "2. 只新增可核验节点/边；兼容、点赞、关注、同校或同公司本身不得自动升级为人物直接关系。",
        "3. 新发现但超出本 action 的线索不要无限递归，留给下一轮 planner。",
        "4. 修改 Markdown 后重新运行 graph audit、typed relation audit 和 schema generation。",
        "5. 记录 rejected/unresolved 线索，避免后续 agent 反复消费同一弱证据。", "",
        "## Next frontier", "", "| Rank | Source | Type | Action | Priority |", "| ---: | --- | --- | --- | ---: |",
    ])
    selected_ids = {item["action_id"] for item in selected}
    frontier = [item for item in actions if item["action_id"] not in selected_ids][:30]
    for rank, action in enumerate(frontier, 1):
        source = action["source"]
        lines.append(f"| {rank} | [[{source['id']}\\|{escape_cell(source['name'])}]] | {escape_cell(source['family'])} | {escape_cell(action['relation'])} | {float(action['priority']):.3f} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--seed", help="Optional node id, name, basename, or alias; any supported entity type is allowed")
    parser.add_argument("--budget", type=int, default=10, help="Number of actions selected for one agent run")
    parser.add_argument("--limit", type=int, default=60, help="Number of ranked candidates exposed in compatibility output")
    parser.add_argument("--max-actions-per-source", type=int, default=1)
    parser.add_argument("--max-bfs-depth", type=int, default=2, help="Soft seed-distance radius; not a traversal cutoff")
    parser.add_argument("--dfs-budget", type=int, default=0, help="Deprecated compatibility flag. DFS is replaced by typed research actions.")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    generated.mkdir(parents=True, exist_ok=True)
    nodes_path, edges_path, metrics_path = generated / "nodes.json", generated / "edges.json", generated / "metrics.json"
    for path in (nodes_path, edges_path, metrics_path):
        if not path.exists():
            parser.error(f"missing {path}; run scripts/audit-graph.py first")
    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    edges = json.loads(edges_path.read_text(encoding="utf-8"))
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))

    seed_id = None
    if args.seed:
        try:
            seed_id = resolve_seed(args.seed, nodes)
        except ValueError as exc:
            parser.error(str(exc))

    actions = build_actions(root, nodes, edges, metrics, seed_id, max(0, args.max_bfs_depth))
    budget = max(1, args.budget)
    selected = portfolio_select(actions, budget, max(1, args.max_actions_per_source))
    family_counts = Counter(action["source"]["family"] for action in selected)
    bucket_counts = Counter(action["bucket"] for action in selected)
    payload = {
        "algorithm": "heterogeneous-active-ecosystem-search-v1",
        "ranking_unit": "research-action",
        "seed": seed_id,
        "budget": budget,
        "candidate_count": len(actions),
        "selected_count": len(selected),
        "selected_family_counts": dict(sorted(family_counts.items())),
        "selected_bucket_counts": dict(sorted(bucket_counts.items())),
        "scoring_note": "Heuristic expected-gain proxy: typed coverage gap + AI Infra relevance + target novelty + bridge/frontier potential + uncertainty + evidence, normalized by action cost and penalized for redundancy/hub bias and soft seed distance.",
        "selected_actions": selected,
        "candidates": actions,
    }
    (generated / "research-actions.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    legacy_limit = max(1, args.limit)
    compatibility = {"algorithm": payload["algorithm"], "ranking_unit": payload["ranking_unit"], "deprecated_filename": True, "replacement": "generated/research-actions.json", "seed": seed_id, "budget": budget, "candidate_count": len(actions), "selected_actions": selected, "candidates": actions[:legacy_limit]}
    (generated / "research-priority.json").write_text(json.dumps(compatibility, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(generated / "research-queue.md", selected, actions, seed_id, budget)

    print(f"Research planner: {len(actions)} candidate actions, {len(selected)} selected across {len(family_counts)} entity families.")
    if args.dfs_budget:
        print("WARN: --dfs-budget is deprecated and ignored; typed actions replace selective DFS.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
