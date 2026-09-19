#!/usr/bin/env python3
"""Research Operator Planner v3.

This is the user-facing orchestration layer for the three top-level research
operators:

    EXPAND   seed-driven heterogeneous local expansion
    DISCOVER global coverage-gap/frontier/bridge discovery
    VERIFY   evidence strengthening, contradiction checks, history follow-up

It intentionally preserves action_id/action_key produced by the existing
history-aware planner. Operator is trigger semantics, never action identity.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import pathlib
import subprocess
import sys
from collections import Counter

RESEARCH_OPERATORS = ("expand", "discover", "verify")
VERIFY_HISTORY_STATUSES = {"partial", "unresolved", "rejected"}


def load_plan_module(script_dir: pathlib.Path):
    path = script_dir / "plan-research.py"
    spec = importlib.util.spec_from_file_location("plan_research_v2", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def choose_operator(action: dict, seed_id: str | None) -> tuple[str, dict]:
    """Assign exactly one operator without changing durable action identity."""
    relation = str(action.get("relation", ""))
    signals = action.get("signals") if isinstance(action.get("signals"), dict) else {}
    coverage = action.get("coverage") if isinstance(action.get("coverage"), dict) else {}
    history = action.get("history") if isinstance(action.get("history"), dict) else {}
    latest = history.get("latest") if isinstance(history.get("latest"), dict) else {}

    distance = signals.get("distance")
    evidence = float(signals.get("evidence_quality", 0.0) or 0.0)
    gap = float(coverage.get("gap", 0.0) or 0.0)
    bucket = str(action.get("bucket", ""))

    if relation in {"verify_evidence", "verify_project_freshness"}:
        return "verify", {
            "kind": "weak_evidence",
            "detail": "evidence/freshness verification action",
        }

    latest_status = str(latest.get("status", ""))
    unresolved = list(latest.get("unresolved_dimensions") or [])
    if latest_status in VERIFY_HISTORY_STATUSES:
        trigger = {
            "kind": "history_followup",
            "detail": f"prior {latest_status} action",
        }
        if unresolved:
            trigger["unresolved_dimensions"] = unresolved
        return "verify", trigger

    if seed_id:
        trigger = {
            "kind": "seed",
            "seed": seed_id,
        }
        if distance is not None:
            trigger["distance"] = int(distance)
        return "expand", trigger

    if bucket == "verification" or evidence < 0.45:
        return "verify", {
            "kind": "weak_evidence",
            "detail": f"evidence_quality={evidence:.3f}",
        }

    if bucket == "bridge":
        return "discover", {
            "kind": "bridge",
            "detail": f"bridge_score={float(signals.get('bridge_score', 0.0) or 0.0):.3f}",
        }

    if gap > 0:
        return "discover", {
            "kind": "coverage_gap",
            "detail": f"coverage_gap={gap:.3f}",
        }

    return "discover", {
        "kind": "frontier",
        "detail": "global graph frontier",
    }


def tag_actions(actions: list[dict], seed_id: str | None) -> list[dict]:
    tagged: list[dict] = []
    for original in actions:
        action = dict(original)
        operator, trigger = choose_operator(action, seed_id)
        action["operator"] = operator
        action["trigger"] = trigger
        tagged.append(action)
    return tagged


def resolve_requested_operators(raw: list[str], seed_id: str | None, parser: argparse.ArgumentParser) -> tuple[str, ...]:
    requested = tuple(dict.fromkeys(raw))
    if not requested:
        return ("expand", "verify") if seed_id else ("discover", "verify")
    if "expand" in requested and not seed_id:
        parser.error("--operator expand requires --seed")
    return requested


def operator_portfolio_select(
    actions: list[dict],
    budget: int,
    max_actions_per_source: int,
    active_operators: tuple[str, ...],
) -> list[dict]:
    """Select a heterogeneous portfolio with soft family and operator caps."""
    if budget <= 0:
        return []

    family_cap = max(1, math.ceil(budget * 0.40))
    operator_cap = max(1, math.ceil(budget * 0.60)) if len(active_operators) > 1 else budget

    selected: list[dict] = []
    selected_ids: set[str] = set()
    source_counts: Counter[str] = Counter()
    family_counts: Counter[str] = Counter()
    operator_counts: Counter[str] = Counter()

    # Pass 1 keeps family/operator diversity. Pass 2 relaxes operator cap.
    # Pass 3 relaxes both caps so a small candidate pool can still fill budget.
    for relax_operator, relax_family in ((False, False), (True, False), (True, True)):
        for action in actions:
            if len(selected) >= budget:
                break
            if not action.get("eligible", True):
                continue

            action_id = str(action.get("action_id", ""))
            source = action.get("source") if isinstance(action.get("source"), dict) else {}
            source_id = str(source.get("id", ""))
            family = str(source.get("family", ""))
            operator = str(action.get("operator", ""))

            if operator not in active_operators:
                continue
            if action_id in selected_ids:
                continue
            if source_counts[source_id] >= max_actions_per_source:
                continue
            if not relax_family and family_counts[family] >= family_cap:
                continue
            if not relax_operator and operator_counts[operator] >= operator_cap:
                continue

            selected.append(action)
            selected_ids.add(action_id)
            source_counts[source_id] += 1
            family_counts[family] += 1
            operator_counts[operator] += 1

        if len(selected) >= budget:
            break

    return selected


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_markdown(path: pathlib.Path, payload: dict, history_summary: dict) -> None:
    selected = payload["selected_actions"]
    actions = payload["candidates"]
    operators = payload["operators"]
    seed_id = payload.get("seed")

    lines = [
        "# Research Operator Queue",
        "",
        "由 `scripts/plan-research-v3.py` 自动生成。仓库只保留三个一级研究方法："
        "`EXPAND`、`DISCOVER`、`VERIFY`。Operator 解释为什么查；relation 解释查什么；strategy 解释去哪查。",
        "",
        f"- Operators: {', '.join(op.upper() for op in operators)}",
        f"- Seed: `{seed_id}`" if seed_id else "- Seed: none (global mode)",
        f"- Candidate actions: {len(actions)}",
        f"- Selected actions: {len(selected)}",
        f"- History records: {history_summary.get('history_records', 0)}",
        "",
        "## Selected portfolio",
        "",
        "| Rank | Operator | Trigger | Source | Type | Relation | Target | Bucket | Priority | History | Why |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |",
    ]

    for rank, action in enumerate(selected, 1):
        source = action["source"]
        target = ", ".join(action.get("target_families") or []) or "evidence"
        trigger = action.get("trigger") or {}
        latest = (action.get("history") or {}).get("latest") or {}
        history_label = latest.get("status") or "new"
        why = "；".join((action.get("reasons") or [])[:4])
        lines.append(
            f"| {rank} | {escape_cell(str(action['operator']).upper())} | "
            f"{escape_cell(trigger.get('kind', ''))} | "
            f"[[{source['id']}|{escape_cell(source['name'])}]] | "
            f"{escape_cell(source['family'])} | {escape_cell(action['relation'])} | "
            f"{escape_cell(target)} | {escape_cell(action['bucket'])} | "
            f"{float(action['priority']):.3f} | {escape_cell(history_label)} | {escape_cell(why)} |"
        )

    for operator in RESEARCH_OPERATORS:
        subset = [action for action in selected if action.get("operator") == operator]
        if not subset:
            continue
        lines.extend(["", f"## {operator.upper()}", ""])
        if operator == "expand":
            lines.append("Seed-driven heterogeneous expansion. Distance is a soft signal, not a hard BFS cutoff.")
        elif operator == "discover":
            lines.append("Global graph completion driven by coverage gaps, novelty, frontier and bridge value.")
        else:
            lines.append("Evidence strengthening, contradiction checking and durable-history follow-up.")

    lines.extend(
        [
            "",
            "## Agent execution contract",
            "",
            "1. 优先官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文与机构一手资料。",
            "2. Operator 只授权调查，不授权无证据创建节点或边。",
            "3. contributor 不自动等于 maintainer；同校不自动等于同学；兼容不自动等于人物直接合作。",
            "4. 新发现但超出当前 action 的线索留给下一轮 planner，不无限递归。",
            "5. 执行后用 `scripts/record-research-action.py` 记录 success / partial / unresolved / rejected。",
            "6. `action_id` / `action_key` 永远不包含 operator，同一 objective 跨 operator 共享 cooldown/history。",
            "",
            "完整说明：`docs/research-action-planner.md`；快速使用：`docs/research-operators.md`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan research with EXPAND / DISCOVER / VERIFY.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--history", default="research/action-history.json")
    parser.add_argument("--seed", help="Optional seed entity id/name/basename/alias.")
    parser.add_argument(
        "--operator",
        action="append",
        choices=RESEARCH_OPERATORS,
        default=[],
        help="Research operator; repeat to mix modes. Defaults to DISCOVER+VERIFY, or EXPAND+VERIFY with --seed.",
    )
    parser.add_argument("--budget", type=int, default=10)
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--max-actions-per-source", type=int, default=1)
    parser.add_argument("--max-bfs-depth", type=int, default=2, help="Soft seed-distance radius.")
    parser.add_argument("--as-of", help="History/cooldown date override YYYY-MM-DD.")
    parser.add_argument("--ignore-history", action="store_true")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    script_dir = pathlib.Path(__file__).resolve().parent
    base = script_dir / "plan-research.py"

    command = [
        sys.executable,
        str(base),
        "--root",
        str(root),
        "--generated",
        args.generated,
        "--history",
        args.history,
        "--budget",
        str(max(1, args.budget)),
        "--limit",
        str(max(1, args.limit)),
        "--max-actions-per-source",
        str(max(1, args.max_actions_per_source)),
        "--max-bfs-depth",
        str(max(0, args.max_bfs_depth)),
    ]
    if args.seed:
        command.extend(["--seed", args.seed])
    if args.as_of:
        command.extend(["--as-of", args.as_of])
    if args.ignore_history:
        command.append("--ignore-history")

    subprocess.run(command, cwd=root, check=True)

    actions_path = generated / "research-actions.json"
    payload = json.loads(actions_path.read_text(encoding="utf-8"))
    seed_id = payload.get("seed")
    operators = resolve_requested_operators(args.operator, seed_id, parser)

    tagged = tag_actions(list(payload.get("candidates") or []), seed_id)
    filtered = [action for action in tagged if action.get("operator") in operators]
    selected = operator_portfolio_select(
        filtered,
        max(1, args.budget),
        max(1, args.max_actions_per_source),
        operators,
    )

    payload["algorithm"] = "research-operator-planner-v3"
    payload["operator_model"] = "EXPAND/DISCOVER/VERIFY"
    payload["operators"] = list(operators)
    payload["candidate_count"] = len(filtered)
    payload["selected_count"] = len(selected)
    payload["selected_operator_counts"] = dict(
        sorted(Counter(str(action["operator"]) for action in selected).items())
    )
    payload["selected_family_counts"] = dict(
        sorted(Counter(str(action["source"]["family"]) for action in selected).items())
    )
    payload["selected_bucket_counts"] = dict(
        sorted(Counter(str(action["bucket"]) for action in selected).items())
    )
    payload["selected_actions"] = selected
    payload["candidates"] = filtered
    payload["scoring_note"] = (
        "Three research operators share stable action identity. EXPAND uses explicit seed context; "
        "DISCOVER uses global graph gaps/frontiers/bridges; VERIFY handles weak evidence and history follow-up. "
        "Existing graph priority, cooldown and empirical-yield adjustments are preserved."
    )
    actions_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    legacy_limit = max(1, args.limit)
    compatibility = {
        "algorithm": payload["algorithm"],
        "ranking_unit": "research-action",
        "deprecated_filename": True,
        "replacement": "generated/research-actions.json",
        "seed": seed_id,
        "operators": list(operators),
        "budget": max(1, args.budget),
        "candidate_count": len(filtered),
        "selected_actions": selected,
        "candidates": filtered[:legacy_limit],
    }
    (generated / "research-priority.json").write_text(
        json.dumps(compatibility, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    history_summary_path = generated / "research-history-summary.json"
    history_summary = (
        json.loads(history_summary_path.read_text(encoding="utf-8"))
        if history_summary_path.exists()
        else {}
    )
    write_markdown(generated / "research-queue.md", payload, history_summary)

    counts = Counter(str(action["operator"]) for action in selected)
    summary = ", ".join(f"{key.upper()}={value}" for key, value in sorted(counts.items())) or "none"
    print(
        f"Research Operator Planner v3: {len(filtered)} candidates, "
        f"{len(selected)} selected ({summary})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
