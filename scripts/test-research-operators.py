#!/usr/bin/env python3
"""Focused tests for the three top-level research operators."""

from __future__ import annotations

import importlib.util
import pathlib
import unittest

GEN_PATH = pathlib.Path(__file__).with_name("generate-research-queue.py")
SPEC = importlib.util.spec_from_file_location("generate_research_queue", GEN_PATH)
assert SPEC and SPEC.loader
GEN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GEN)


class ResearchOperatorTests(unittest.TestCase):
    def test_action_identity_does_not_include_operator(self):
        source_id = "community/example/Project"
        relation = "maintainers"
        action_id = f"{source_id}::{relation}"
        self.assertEqual(action_id, "community/example/Project::maintainers")
        self.assertNotIn("expand", action_id)
        self.assertNotIn("discover", action_id)
        self.assertNotIn("verify", action_id)

    def test_operator_constants_are_minimal_complete_set(self):
        self.assertEqual(set(GEN.RESEARCH_OPERATORS), {"expand", "discover", "verify"})

    def test_choose_operator_prefers_expand_for_seeded_candidate(self):
        operator, trigger = GEN.choose_operator(
            seed_enabled=True,
            distance=1,
            bucket="bridge",
            evidence=1.0,
            coverage_gap=0.5,
        )
        self.assertEqual(operator, "expand")
        self.assertEqual(trigger["kind"], "seed")
        self.assertEqual(trigger["distance"], 1)

    def test_choose_operator_uses_verify_for_weak_evidence(self):
        operator, trigger = GEN.choose_operator(
            seed_enabled=False,
            distance=None,
            bucket="verification",
            evidence=0.2,
            coverage_gap=0.3,
        )
        self.assertEqual(operator, "verify")
        self.assertEqual(trigger["kind"], "weak_evidence")

    def test_choose_operator_defaults_to_discover_for_global_gap(self):
        operator, trigger = GEN.choose_operator(
            seed_enabled=False,
            distance=None,
            bucket="exploration",
            evidence=0.9,
            coverage_gap=0.7,
        )
        self.assertEqual(operator, "discover")
        self.assertEqual(trigger["kind"], "coverage_gap")


if __name__ == "__main__":
    unittest.main()
