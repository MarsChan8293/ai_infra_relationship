#!/usr/bin/env python3
"""Focused tests for history-aware research planning."""

from __future__ import annotations

import datetime as dt
import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("plan-research.py")
SPEC = importlib.util.spec_from_file_location("plan_research", MODULE_PATH)
assert SPEC and SPEC.loader
PLAN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PLAN)


def action(action_id: str, action_key: str, priority: float = 9.0) -> dict:
    source_id, relation = action_id.rsplit("::", 1)
    return {
        "action_id": action_id,
        "action_key": action_key,
        "source": {"id": source_id, "name": source_id, "type": "project", "family": "project"},
        "relation": relation,
        "target_families": ["person"],
        "strategies": [],
        "write_hint": "",
        "bucket": "bridge",
        "priority": priority,
        "cost": 1.0,
        "coverage": {},
        "signals": {},
        "reasons": [],
    }


class HistoryPlannerTests(unittest.TestCase):
    def test_unresolved_action_is_suppressed_during_cooldown(self):
        candidate = action("p::maintainers", "project:maintainers:person")
        history = {
            "records": [
                {
                    "run_id": "run-1",
                    "attempted_at": "2026-09-16",
                    "action_id": candidate["action_id"],
                    "action_key": candidate["action_key"],
                    "status": "unresolved",
                    "outcome": {},
                }
            ]
        }
        adjusted, summary = PLAN.apply_history([candidate], history, dt.date(2026, 9, 16))
        self.assertFalse(adjusted[0]["eligible"])
        self.assertEqual(adjusted[0]["history"]["latest"]["cooldown_until"], "2026-09-23")
        self.assertEqual(summary["suppressed_by_cooldown"], 1)

    def test_partial_action_returns_after_short_cooldown_with_followup_context(self):
        candidate = action("x::affiliation", "person:affiliation:company+school+research+team", 7.5)
        candidate["source"]["family"] = "person"
        history = {
            "records": [
                {
                    "run_id": "run-2",
                    "attempted_at": "2026-09-16",
                    "action_id": candidate["action_id"],
                    "action_key": candidate["action_key"],
                    "status": "partial",
                    "resolved_dimensions": ["identity"],
                    "unresolved_dimensions": ["employer"],
                    "outcome": {"evidence_upgraded": 1},
                }
            ]
        }
        during, _ = PLAN.apply_history([candidate], history, dt.date(2026, 9, 17))
        self.assertFalse(during[0]["eligible"])
        after, _ = PLAN.apply_history([candidate], history, dt.date(2026, 9, 18))
        self.assertTrue(after[0]["eligible"])
        self.assertGreater(after[0]["history"]["exact_status_adjustment"], 0)
        self.assertIn("partial follow-up", " ".join(after[0]["reasons"]))

    def test_history_yield_is_small_sample_shrunk(self):
        candidate = action("p::maintainers", "project:maintainers:person")
        history = {
            "records": [
                {
                    "run_id": "run-1",
                    "attempted_at": "2026-01-01",
                    "action_id": candidate["action_id"],
                    "action_key": candidate["action_key"],
                    "status": "success",
                    "outcome": {"new_nodes": 3, "new_edges": 2},
                }
            ]
        }
        adjusted, summary = PLAN.apply_history([candidate], history, dt.date(2026, 9, 16))
        change = adjusted[0]["priority"] - adjusted[0]["base_priority"]
        self.assertGreater(change, 0)
        self.assertLess(change, 0.2)
        self.assertEqual(summary["history_records"], 1)


if __name__ == "__main__":
    unittest.main()
