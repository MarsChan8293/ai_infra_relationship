#!/usr/bin/env python3
"""Append or replace one durable research-action outcome record."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

VALID_STATUS = ("success", "partial", "unresolved", "rejected")


def load_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def find_action(generated: pathlib.Path, action_id: str) -> dict | None:
    path = generated / "research-actions.json"
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    for section in ("selected_actions", "candidates"):
        for action in payload.get(section, []) or []:
            if str(action.get("action_id")) == action_id:
                return action
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action_id", help="Stable action id: <node-id>::<relation>")
    parser.add_argument("--status", choices=VALID_STATUS, required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--history", default="research/action-history.json")
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--attempted-at", default=dt.date.today().isoformat())
    parser.add_argument("--action-key", help="Optional override; otherwise resolved from generated/research-actions.json")
    parser.add_argument("--source-name")
    parser.add_argument("--note", default="")
    parser.add_argument("--resolved", action="append", default=[], help="Resolved dimension; may be repeated")
    parser.add_argument("--unresolved", action="append", default=[], help="Unresolved dimension; may be repeated")
    parser.add_argument("--new-nodes", type=int, default=0)
    parser.add_argument("--new-edges", type=int, default=0)
    parser.add_argument("--evidence-upgraded", type=int, default=0)
    parser.add_argument("--verified-claims", type=int, default=0)
    parser.add_argument("--rejected-claims", type=int, default=0)
    parser.add_argument("--reward", type=float)
    parser.add_argument("--retry-after-days", type=int)
    parser.add_argument("--replace", action="store_true", help="Replace an existing record with same run_id + action_id")
    args = parser.parse_args()

    try:
        dt.date.fromisoformat(args.attempted_at)
    except ValueError:
        parser.error("--attempted-at must be YYYY-MM-DD")

    root = pathlib.Path(args.root).resolve()
    history_path = (root / args.history).resolve()
    generated = (root / args.generated).resolve()
    action = find_action(generated, args.action_id)

    action_key = args.action_key or (str(action.get("action_key")) if action else "")
    if not action_key:
        parser.error("--action-key is required when action_id is not present in generated/research-actions.json")

    source = action.get("source", {}) if action else {}
    source_name = args.source_name or source.get("name")

    record = {
        "run_id": args.run_id,
        "attempted_at": args.attempted_at,
        "action_id": args.action_id,
        "action_key": action_key,
        "status": args.status,
        "source_name": source_name,
        "resolved_dimensions": list(args.resolved),
        "unresolved_dimensions": list(args.unresolved),
        "outcome": {
            "new_nodes": max(0, args.new_nodes),
            "new_edges": max(0, args.new_edges),
            "evidence_upgraded": max(0, args.evidence_upgraded),
            "verified_claims": max(0, args.verified_claims),
            "rejected_claims": max(0, args.rejected_claims),
        },
        "note": args.note,
    }
    if args.reward is not None:
        record["reward"] = args.reward
    if args.retry_after_days is not None:
        record["retry_after_days"] = max(0, args.retry_after_days)

    payload = load_json(
        history_path,
        {"schema": "ai-infra-relationship/research-action-history-v1", "records": []},
    )
    if not isinstance(payload, dict) or not isinstance(payload.get("records"), list):
        parser.error(f"invalid history file: {history_path}")

    records = payload["records"]
    duplicate_indexes = [
        i
        for i, item in enumerate(records)
        if item.get("run_id") == args.run_id and item.get("action_id") == args.action_id
    ]
    if duplicate_indexes and not args.replace:
        parser.error("record already exists for this run_id + action_id; pass --replace to update it")
    if duplicate_indexes:
        records[duplicate_indexes[-1]] = record
    else:
        records.append(record)

    history_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Recorded {args.status}: {args.action_id} -> {history_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
