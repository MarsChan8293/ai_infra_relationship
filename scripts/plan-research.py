#!/usr/bin/env python3
"""Generate a history-aware heterogeneous research-action queue.

This is the canonical daily planner entrypoint. It first runs the deterministic
candidate generator (generate-research-queue.py), then applies durable action
history to:

- suppress exact retries during status-specific cooldown windows;
- preserve partial outcomes and surface unresolved dimensions;
- apply a deliberately small empirical yield adjustment by action_key;
- re-run bounded heterogeneous portfolio selection over eligible actions.

Durable history lives outside generated/ so graph regeneration never erases it.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import pathlib
import subprocess
import sys
from collections import Counter, defaultdict

STATUS_COOLDOWN_DAYS = {
    "success": 1,
    "partial": 2,
    "unresolved": 7,
    "rejected": 30,
}

STATUS_VALUE = {
    "success": 1.0,
    "partial": 0.35,
    "unresolved": -0.50,
    "rejected": -1.0,
}

EXACT_STATUS_ADJUSTMENT = {
    "success": 0.0,
    "partial": 0.15,
    "unresolved": -0.25,
    "rejected": -0.60,
}


def parse_date(value: object) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def load_history(path: pathlib.Path) -> dict:
    if not path.exists():
        return {"schema": "ai-infra-relationship/research-action-history-v1", "records": []}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"history root must be an object: {path}")
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError(f"history.records must be an array: {path}")
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"history.records[{index}] must be an object")
        status = str(record.get("status", ""))
        if status not in STATUS_COOLDOWN_DAYS:
            raise ValueError(f"unsupported history status {status!r} at record {index}")
        if not record.get("action_id"):
            raise ValueError(f"missing action_id at history record {index}")
        if not record.get("action_key"):
            raise ValueError(f"missing action_key at history record {index}")
        if parse_date(record.get("attempted_at")) is None:
            raise ValueError(f"invalid attempted_at at history record {index}")
    return payload


def status_cooldown_days(record: dict) -> int:
    override = record.get("retry_after_days")
    if override is not None:
        try:
            return max(0, int(override))
        except (TypeError, ValueError):
            pass
    return STATUS_COOLDOWN_DAYS[str(record["status"])]


def outcome_reward(record: dict) -> float:
    explicit = record.get("reward")
    if explicit is not None:
        try:
            return float(explicit)
        except (TypeError, ValueError):
            pass

    outcome = record.get("outcome")
    if not isinstance(outcome, dict):
        outcome = {}

    def num(key: str) -> float:
        try:
            return float(outcome.get(key, 0) or 0)
        except (TypeError, ValueError):
            return 0.0

    return (
        2.0 * num("new_nodes")
        + 1.0 * num("new_edges")
        + 0.50 * num("evidence_upgraded")
        + 0.75 * num("verified_claims")
        + 0.50 * len(record.get("resolved_dimensions") or [])
        - 0.25 * num("rejected_claims")
    )


def build_history_indexes(records: list[dict]) -> tuple[dict[str, list[dict]], dict[str, dict]]:
    exact: dict[str, list[dict]] = defaultdict(list)
    key_stats_raw: dict[str, dict] = defaultdict(
        lambda: {
            "attempts": 0,
            "statuses": Counter(),
            "status_value_sum": 0.0,
            "reward_sum": 0.0,
        }
    )

    for record in records:
        action_id = str(record["action_id"])
        action_key = str(record["action_key"])
        exact[action_id].append(record)

        stats = key_stats_raw[action_key]
        stats["attempts"] += 1
        status = str(record["status"])
        stats["statuses"][status] += 1
        stats["status_value_sum"] += STATUS_VALUE[status]
        stats["reward_sum"] += outcome_reward(record)

    for entries in exact.values():
        entries.sort(key=lambda item: (str(item.get("attempted_at", "")), str(item.get("run_id", ""))))

    key_stats: dict[str, dict] = {}
    for key, raw in key_stats_raw.items():
        attempts = int(raw["attempts"])
        mean_status = raw["status_value_sum"] / max(1, attempts)
        mean_reward = raw["reward_sum"] / max(1, attempts)
        reward_signal = math.tanh(mean_reward / 4.0)
        combined_yield = 0.75 * mean_status + 0.25 * reward_signal
        confidence = min(1.0, attempts / 6.0)
        yield_adjustment = max(-0.35, min(0.35, 0.35 * combined_yield * confidence))
        key_stats[key] = {
            "attempts": attempts,
            "statuses": dict(sorted(raw["statuses"].items())),
            "mean_status_value": round(mean_status, 3),
            "mean_reward": round(mean_reward, 3),
            "reward_signal": round(reward_signal, 3),
            "yield_adjustment": round(yield_adjustment, 3),
        }
    return dict(exact), key_stats


def apply_history(actions: list[dict], history: dict, as_of: dt.date) -> tuple[list[dict], dict]:
    records = history.get("records", [])
    exact, key_stats = build_history_indexes(records)

    suppressed = 0
    partial_followups = 0
    status_counts: Counter[str] = Counter()

    adjusted: list[dict] = []
    for original in actions:
        action = dict(original)
        action["signals"] = dict(original.get("signals") or {})
        action["reasons"] = list(original.get("reasons") or [])

        action_id = str(action.get("action_id", ""))
        action_key = str(action.get("action_key", ""))
        base_priority = float(action.get("priority", 0.0))
        class_stats = key_stats.get(
            action_key,
            {
                "attempts": 0,
                "statuses": {},
                "mean_status_value": 0.0,
                "mean_reward": 0.0,
                "reward_signal": 0.0,
                "yield_adjustment": 0.0,
            },
        )
        key_adjustment = float(class_stats.get("yield_adjustment", 0.0))
        exact_entries = exact.get(action_id, [])
        latest = exact_entries[-1] if exact_entries else None

        eligible = True
        cooldown_until: dt.date | None = None
        exact_adjustment = 0.0
        history_reason = None
        latest_summary = None

        if latest:
            status = str(latest["status"])
            status_counts[status] += 1
            attempted_at = parse_date(latest.get("attempted_at"))
            cooldown_days = status_cooldown_days(latest)
            if attempted_at is not None:
                cooldown_until = attempted_at + dt.timedelta(days=cooldown_days)
                if as_of < cooldown_until:
                    eligible = False
                    suppressed += 1

            exact_adjustment = EXACT_STATUS_ADJUSTMENT[status]
            resolved = list(latest.get("resolved_dimensions") or [])
            unresolved = list(latest.get("unresolved_dimensions") or [])
            latest_summary = {
                "run_id": latest.get("run_id"),
                "attempted_at": latest.get("attempted_at"),
                "status": status,
                "note": latest.get("note"),
                "resolved_dimensions": resolved,
                "unresolved_dimensions": unresolved,
                "cooldown_days": cooldown_days,
                "cooldown_until": cooldown_until.isoformat() if cooldown_until else None,
            }

            if status == "partial":
                partial_followups += 1
                if unresolved:
                    history_reason = "partial follow-up: unresolved " + ", ".join(str(x) for x in unresolved[:3])
                else:
                    history_reason = "partial outcome retained for follow-up"
            elif status == "unresolved":
                history_reason = "prior unresolved action"
            elif status == "rejected":
                history_reason = "prior rejected claim/search direction"
            elif status == "success":
                history_reason = "recent successful action"

            if not eligible:
                remaining = max(0, (cooldown_until - as_of).days) if cooldown_until else 0
                history_reason = f"cooldown active ({status}, {remaining}d remaining)"

        adjusted_priority = round(base_priority + key_adjustment + (exact_adjustment if eligible else 0.0), 3)
        action["base_priority"] = round(base_priority, 3)
        action["priority"] = adjusted_priority
        action["eligible"] = eligible
        action["history"] = {
            "exact_attempts": len(exact_entries),
            "latest": latest_summary,
            "action_key_stats": class_stats,
            "key_yield_adjustment": round(key_adjustment, 3),
            "exact_status_adjustment": round(exact_adjustment if eligible else 0.0, 3),
        }
        action["signals"]["history_yield_adjustment"] = round(key_adjustment, 3)
        action["signals"]["history_status_adjustment"] = round(exact_adjustment if eligible else 0.0, 3)
        action["signals"]["history_eligible"] = eligible
        if cooldown_until:
            action["signals"]["cooldown_until"] = cooldown_until.isoformat()
        if history_reason:
            action["reasons"].append(history_reason)
        adjusted.append(action)

    adjusted.sort(
        key=lambda item: (
            not bool(item.get("eligible", True)),
            -float(item.get("priority", 0.0)),
            str(item.get("source", {}).get("name", "")),
            str(item.get("relation", "")),
        )
    )

    summary = {
        "as_of": as_of.isoformat(),
        "history_records": len(records),
        "suppressed_by_cooldown": suppressed,
        "partial_followup_candidates": partial_followups,
        "latest_status_counts_in_current_candidates": dict(sorted(status_counts.items())),
        "action_key_stats": dict(sorted(key_stats.items())),
    }
    return adjusted, summary


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
            if not action.get("eligible", True):
                continue
            action_id = str(action["action_id"])
            source_id = str(action["source"]["id"])
            family = str(action["source"]["family"])
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


def write_markdown(path: pathlib.Path, payload: dict, history_summary: dict) -> None:
    selected = payload["selected_actions"]
    actions = payload["candidates"]
    budget = int(payload["budget"])
    seed_id = payload.get("seed")
    eligible = [item for item in actions if item.get("eligible", True)]
    suppressed = [item for item in actions if not item.get("eligible", True)]

    lines = [
        "# Ecosystem Research Action Queue",
        "",
        "由 `scripts/plan-research.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。",
        "",
        "算法：**Typed Action Planner + Action History + Cooldown + Heterogeneous Portfolio Selection**。基础 expected-gain 分数来自图谱缺口；历史只做轻量 yield 修正，并用 cooldown 阻止同一弱证据 action 在短期内反复占用预算。",
        "",
        f"- Daily budget: {budget}",
        f"- Seed: `{seed_id}`" if seed_id else "- Seed: none (global ecosystem mode)",
        f"- Candidate actions: {len(actions)}",
        f"- Eligible actions: {len(eligible)}",
        f"- Cooldown-suppressed: {len(suppressed)}",
        f"- History records: {history_summary.get('history_records', 0)}",
        f"- Selected actions: {len(selected)}",
        "",
        "## Selected actions",
        "",
        "| Rank | Source | Type | Research action | Target | Bucket | Priority | History | Why |",
        "| ---: | --- | --- | --- | --- | --- | ---: | --- | --- |",
    ]

    for rank, action in enumerate(selected, 1):
        source = action["source"]
        target = ", ".join(action.get("target_families") or []) or "evidence"
        latest = (action.get("history") or {}).get("latest") or {}
        history_label = latest.get("status") or "new"
        why = "；".join((action.get("reasons") or [])[:4])
        lines.append(
            f"| {rank} | [[{source['id']}|{escape_cell(source['name'])}]] | "
            f"{escape_cell(source['family'])} | {escape_cell(action['relation'])} | "
            f"{escape_cell(target)} | {escape_cell(action['bucket'])} | "
            f"{float(action['priority']):.3f} | {escape_cell(history_label)} | {escape_cell(why)} |"
        )

    lines.extend(
        [
            "",
            "## Agent execution contract",
            "",
            "对每个 selected action：",
            "",
            "1. 优先查官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文或机构一手资料。",
            "2. 只新增可核验节点/边；兼容、点赞、关注、同校或同公司本身不得自动升级为人物直接关系。",
            "3. 新发现但超出本 action 的线索不要无限递归，留给下一轮 planner。",
            "4. 执行后用 `scripts/record-research-action.py` 写入 success / partial / unresolved / rejected outcome。",
            "5. partial 必须记录 resolved_dimensions 与 unresolved_dimensions，不能被压扁成 success/failure。",
            "6. 修改 Markdown 后重新运行 graph audit、typed relation audit 和 schema generation。",
            "",
            "## Next eligible frontier",
            "",
            "| Rank | Source | Type | Action | Priority |",
            "| ---: | --- | --- | --- | ---: |",
        ]
    )

    selected_ids = {item["action_id"] for item in selected}
    frontier = [item for item in eligible if item["action_id"] not in selected_ids][:30]
    for rank, action in enumerate(frontier, 1):
        source = action["source"]
        lines.append(
            f"| {rank} | [[{source['id']}|{escape_cell(source['name'])}]] | "
            f"{escape_cell(source['family'])} | {escape_cell(action['relation'])} | "
            f"{float(action['priority']):.3f} |"
        )

    lines.extend(
        [
            "",
            "## Cooldown / history-suppressed",
            "",
            "| Source | Action | Latest outcome | Eligible after | Base |",
            "| --- | --- | --- | --- | ---: |",
        ]
    )
    for action in suppressed[:30]:
        source = action["source"]
        latest = (action.get("history") or {}).get("latest") or {}
        lines.append(
            f"| [[{source['id']}|{escape_cell(source['name'])}]] | "
            f"{escape_cell(action['relation'])} | {escape_cell(latest.get('status', 'unknown'))} | "
            f"{escape_cell(latest.get('cooldown_until', ''))} | {float(action.get('base_priority', 0.0)):.3f} |"
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_base_generator(args: argparse.Namespace, root: pathlib.Path) -> None:
    script = root / "scripts" / "generate-research-queue.py"
    command = [
        sys.executable,
        str(script),
        "--root",
        str(root),
        "--generated",
        args.generated,
        "--budget",
        str(args.budget),
        "--limit",
        str(args.limit),
        "--max-actions-per-source",
        str(args.max_actions_per_source),
        "--max-bfs-depth",
        str(args.max_bfs_depth),
    ]
    if args.seed:
        command.extend(["--seed", args.seed])
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--history", default="research/action-history.json")
    parser.add_argument("--seed")
    parser.add_argument("--budget", type=int, default=10)
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--max-actions-per-source", type=int, default=1)
    parser.add_argument("--max-bfs-depth", type=int, default=2)
    parser.add_argument("--as-of", help="ISO date used for cooldown evaluation; defaults to today")
    parser.add_argument("--ignore-history", action="store_true")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    generated = (root / args.generated).resolve()
    history_path = (root / args.history).resolve()

    run_base_generator(args, root)

    base_path = generated / "research-actions.json"
    payload = json.loads(base_path.read_text(encoding="utf-8"))
    actions = list(payload.get("candidates") or [])
    history = {"schema": "ai-infra-relationship/research-action-history-v1", "records": []}
    if not args.ignore_history:
        history = load_history(history_path)

    as_of = parse_date(args.as_of) if args.as_of else dt.date.today()
    if as_of is None:
        parser.error("--as-of must be YYYY-MM-DD")

    adjusted, history_summary = apply_history(actions, history, as_of)
    budget = max(1, int(args.budget))
    selected = portfolio_select(adjusted, budget, max(1, int(args.max_actions_per_source)))
    family_counts = Counter(item["source"]["family"] for item in selected)
    bucket_counts = Counter(item["bucket"] for item in selected)

    payload.update(
        {
            "algorithm": "heterogeneous-active-ecosystem-search-v2-history-aware",
            "planner_entrypoint": "scripts/plan-research.py",
            "history_path": str(pathlib.PurePosixPath(args.history)),
            "history_as_of": as_of.isoformat(),
            "history_summary": history_summary,
            "candidate_count": len(adjusted),
            "eligible_count": sum(1 for item in adjusted if item.get("eligible", True)),
            "suppressed_count": sum(1 for item in adjusted if not item.get("eligible", True)),
            "selected_count": len(selected),
            "selected_family_counts": dict(sorted(family_counts.items())),
            "selected_bucket_counts": dict(sorted(bucket_counts.items())),
            "scoring_note": (
                "Base expected-gain proxy plus small-sample-shrunk action_key history yield; "
                "exact recent success/partial/unresolved/rejected actions are temporarily suppressed "
                "by status-specific cooldowns. Partial outcomes retain resolved/unresolved dimensions."
            ),
            "selected_actions": selected,
            "candidates": adjusted,
        }
    )
    base_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    compatibility_path = generated / "research-priority.json"
    compatibility = json.loads(compatibility_path.read_text(encoding="utf-8"))
    compatibility.update(
        {
            "algorithm": payload["algorithm"],
            "planner_entrypoint": payload["planner_entrypoint"],
            "history_path": payload["history_path"],
            "history_as_of": payload["history_as_of"],
            "history_summary": history_summary,
            "candidate_count": len(adjusted),
            "eligible_count": payload["eligible_count"],
            "suppressed_count": payload["suppressed_count"],
            "selected_actions": selected,
            "candidates": adjusted[: max(1, int(args.limit))],
        }
    )
    compatibility_path.write_text(json.dumps(compatibility, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (generated / "research-history-summary.json").write_text(
        json.dumps(history_summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(generated / "research-queue.md", payload, history_summary)

    print(
        "History-aware planner: "
        f"{len(adjusted)} candidates, {payload['eligible_count']} eligible, "
        f"{payload['suppressed_count']} cooldown-suppressed, {len(selected)} selected."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
