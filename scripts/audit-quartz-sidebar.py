#!/usr/bin/env python3
"""Regression gate: Quartz folder/tag pages must retain Graph and Backlinks.

Folder notes (for example Mooncake/Mooncake.md) use the `folder` layout rather
than `content`. Quartz v5's default `positions.right: []` suppresses the
whole right sidebar on folder and tag pages. Check the actual HTML, not just
the generated YAML, so a future Quartz update cannot silently reintroduce it.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys


CLASS_ATTRIBUTE = re.compile(r"""\bclass\s*=\s*(["'])(.*?)\1""", re.IGNORECASE | re.DOTALL)
REFRESH_REDIRECT = re.compile(r"""<meta\b[^>]*http-equiv\s*=\s*["']?refresh\b""", re.IGNORECASE)


def has_component(html: str, name: str) -> bool:
    return any(name in value.split() for _, value in CLASS_ATTRIBUTE.findall(html))


def is_redirect(html: str) -> bool:
    return bool(REFRESH_REDIRECT.search(html))


def verify(public: pathlib.Path) -> tuple[int, list[str]]:
    failures: list[str] = []
    checked = 0
    sections = ("community", "company", "concept", "university")

    for section in sections:
        folder = public / section
        if not folder.is_dir():
            failures.append(f"Missing deployed content section: {section}")
            continue
        tested = 0
        for path in sorted(folder.rglob("index.html")):
            html = path.read_text(encoding="utf-8")
            if is_redirect(html):
                continue
            tested += 1
            checked += 1
            if not has_component(html, "graph"):
                failures.append(f"Folder page missing Graph: {path.relative_to(public)}")
        if tested == 0:
            failures.append(f"No rendered folder index pages found in {section}")

    tag_folder = public / "tags"
    if tag_folder.is_dir():
        for path in sorted(tag_folder.rglob("*.html")):
            html = path.read_text(encoding="utf-8")
            if is_redirect(html):
                continue
            checked += 1
            if not has_component(html, "graph"):
                failures.append(f"Tag page missing Graph: {path.relative_to(public)}")

    # The original regression: Mooncake's URL is a folder landing page, and
    # TENT references Mooncake explicitly. The Graph should be present and the
    # Backlinks component should not be absent due to folder layout rules.
    candidates = [
        path for path in (public / "community").rglob("index.html")
        if tuple(part.casefold() for part in path.relative_to(public).parts)
        == ("community", "kvcache-ai", "mooncake", "index.html")
    ] if (public / "community").exists() else []
    pages = [
        (path, path.read_text(encoding="utf-8"))
        for path in candidates
    ]
    pages = [(path, html) for path, html in pages if not is_redirect(html)]
    if not pages:
        failures.append("Mooncake folder landing page is missing or is only a redirect")
    else:
        for path, html in pages:
            if not has_component(html, "graph"):
                failures.append(f"Mooncake missing Graph: {path.relative_to(public)}")
            if not has_component(html, "backlinks"):
                failures.append(f"Mooncake missing Backlinks: {path.relative_to(public)}")

    return checked, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public", type=pathlib.Path, required=True)
    args = parser.parse_args()
    if not args.public.is_dir():
        parser.error(f"Quartz public directory does not exist: {args.public}")

    checked, failures = verify(args.public)
    print(f"Quartz sidebar audit: {checked} folder/tag pages checked; {len(failures)} failures.")
    for failure in failures[:100]:
        print("FAIL:", failure, file=sys.stderr)
    if len(failures) > 100:
        print(f"... plus {len(failures) - 100} further failures", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
