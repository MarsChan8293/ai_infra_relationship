#!/usr/bin/env python3
"""Conservative Markdown normalization without prose-to-typed-edge inference.

This wrapper intentionally reuses the safe normalization helpers from
`repair-markdown-quality.py` while skipping `infer_relations()`. Human prose is
not sufficient evidence to create a strong typed relationship automatically.
Relationship candidates should be researched and written explicitly instead.
"""
from __future__ import annotations

import argparse
import importlib.util
import pathlib

NODE_ROOTS = ("company", "community", "university")


def load_legacy_module(root: pathlib.Path):
    path = root / "scripts" / "repair-markdown-quality.py"
    spec = importlib.util.spec_from_file_location("repair_markdown_quality_legacy", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    legacy = load_legacy_module(root)

    created = legacy.create_canonical_nodes(root)
    touched: list[str] = []
    paths = [root / "AI Infra Relationship.md"] if (root / "AI Infra Relationship.md").exists() else []
    for dirname in NODE_ROOTS:
        base = root / dirname
        if base.exists():
            paths.extend(sorted(base.rglob("*.md")))

    for path in paths:
        rel = path.relative_to(root).as_posix()
        original = path.read_text(encoding="utf-8")
        text = legacy.repair_unwanted_wikilinks(original)
        fm_lines, body = legacy.split_frontmatter(text)
        if fm_lines:
            fm_lines = legacy.normalize_frontmatter(fm_lines)
            text = legacy.ensure_source(legacy.join_frontmatter(fm_lines, body), rel)
        if text != original:
            path.write_text(text, encoding="utf-8")
            touched.append(rel)

    if legacy.repair_uc_berkeley_alias(root) and "university/UC Berkeley/UC Berkeley.md" not in touched:
        touched.append("university/UC Berkeley/UC Berkeley.md")

    print(
        f"Safe Markdown repair: {len(touched)} files updated, "
        f"{len(created)} canonical nodes created, 0 typed relations inferred from prose."
    )
    for path in created:
        print("CREATE:", path)
    for path in touched[:80]:
        print("UPDATE:", path)
    if len(touched) > 80:
        print(f"... plus {len(touched) - 80} more updated files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
