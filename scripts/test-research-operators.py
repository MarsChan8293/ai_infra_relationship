#!/usr/bin/env python3
"""Focused tests for the three top-level research operators."""

from __future__ import annotations

import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("plan-research-v3.py")
SPEC = importlib.util.spec_from_file_location("plan_research_v3", MODULE_PATH)
assert SPEC and SPEC.loader
PLAN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PLAN)


def action(
    *,
    action_id: str = "community/example/Project::maintainers",
    relation: str = "maintainers",
    evidence: float = 1.0,
    gap: float = 0.5,
    bucket: str = "exploration",
    distance: int | None = None,
    latest: dict | None = None,
) -> dict:
    source_id, _ = action_id.rsplit("::", 1)
    return {
        "action_id": action_id,
        "action_key": "project:maintainers:person",
        "source": {
            "id": source_id,
            "name": "Project",
            "type": "project",
            "family": "project",
        },
        "relation": relation,
        "target_families": ["person"],
        "bucket": bucket,
        "coverage": {"existing": 1, "desired": 2, "gap": gap},
        "signals": {
            "evidence_quality": evidence,
            "distance": distance,
            "bridge_score": 0.0,
        },
        "history": {"latest": latest} if latest else {},
        "eligible": True,
        "priority": 5.0,
        "reasons": [],
    }


class ResearchOperatorTests(unittest.TestCase):
    def test_operator_constants_are_minimal_complete_set(self):
        self.assertEqual(set(PLAN.RESEARCH_OPERATORS), {"expand", "discover", "verify"})

    def test_action_identity_does_not_change_when_operator_is_added(self):
        original = action()
        tagged = PLAN.tag_actions([original], seed_id="community/example/Project")[0]
        self.assertEqual(tagged["action_id"], original["action_id"])
        self.assertEqual(tagged["action_key"], original["action_key"])
        self.assertEqual(tagged["operator"], "expand")
        self.assertNotIn(tagged["operator"], tagged["action_id"])

    def test_seeded_candidate_uses_expand(self):
        candidate = action(distance=1, bucket="bridge")
        operator, trigger = PLAN.choose_operator(candidate, "community/example/Project")
        self.assertEqual(operator, "expand")
        self.assertEqual(trigger["kind"], "seed")
        self.assertEqual(trigger["distance"], 1)

    def test_weak_evidence_uses_verify(self):
        candidate = action(evidence=0.2, bucket="verification")
        operator, trigger = PLAN.choose_operator(candidate, None)
        self.assertEqual(operator, "verify")
        self.assertEqual(trigger["kind"], "weak_evidence")

    def test_global_coverage_gap_uses_discover(self):
        candidate = action(evidence=0.9, gap=0.7, bucket="exploration")
        operator, trigger = PLAN.choose_operator(candidate, None)
        self.assertEqual(operator, "discover")
        self.assertEqual(trigger["kind"], "coverage_gap")

    def test_partial_history_becomes_verify_followup_even_with_seed(self):
        candidate = action(
            latest={
                "status": "partial",
                "unresolved_dimensions": ["employer", "school"],
            }
        )
        operator, trigger = PLAN.choose_operator(candidate, "community/example/Project")
        self.assertEqual(operator, "verify")
        self.assertEqual(trigger["kind"], "history_followup")
        self.assertEqual(trigger["unresolved_dimensions"], ["employer", "school"])

    def test_verify_evidence_relation_is_always_verify(self):
        candidate = action(
            action_id="community/example/Project::verify_evidence",
            relation="verify_evidence",
            evidence=1.0,
            gap=0.0,
            bucket="exploitation",
        )
        operator, trigger = PLAN.choose_operator(candidate, "community/example/Project")
        self.assertEqual(operator, "verify")
        self.assertEqual(trigger["kind"], "weak_evidence")


if __name__ == "__main__":
    unittest.main()
