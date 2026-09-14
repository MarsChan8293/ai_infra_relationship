#!/usr/bin/env python3
import html.parser
import pathlib
import posixpath
import sys
from urllib.parse import unquote, urlparse

public_root = pathlib.Path(sys.argv[1]).resolve()
base_path = (sys.argv[2] if len(sys.argv) > 2 else "").strip()
if base_path and not base_path.startswith("/"):
    base_path = "/" + base_path
base_path = base_path.rstrip("/")

if not public_root.exists():
    print(f"Public directory does not exist: {public_root}", file=sys.stderr)
    sys.exit(2)

SITE_HOSTS = {"marschan8293.github.io"}


class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.hrefs.append(value)
                break


def normalize_local_path(source_rel, href):
    href = href.strip()
    if not href or href.startswith("#") or href.startswith("//"):
        return None

    parsed = urlparse(href)
    if parsed.scheme:
        if parsed.scheme not in {"http", "https"} or parsed.netloc.lower() not in SITE_HOSTS:
            return None
        raw_path = parsed.path
    else:
        raw_path = parsed.path

    if not raw_path:
        return None

    raw_path = unquote(raw_path)
    if base_path and raw_path == base_path:
        raw_path = "/"
    elif base_path and raw_path.startswith(base_path + "/"):
        raw_path = raw_path[len(base_path):]

    if raw_path.startswith("/"):
        local = posixpath.normpath(raw_path.lstrip("/"))
    else:
        source_dir = posixpath.dirname(source_rel)
        local = posixpath.normpath(posixpath.join(source_dir, raw_path))

    while local.startswith("../"):
        local = local[3:]
    if local in {"", "."}:
        return "index"
    return local.rstrip("/")


def target_exists(local):
    candidates = [public_root / local]
    path_obj = pathlib.PurePosixPath(local)
    if path_obj.suffix == "":
        candidates.extend([
            public_root / f"{local}.html",
            public_root / local / "index.html",
        ])
    elif path_obj.suffix.lower() in {".htm", ".html"}:
        candidates.append(public_root / local.removesuffix(path_obj.suffix) / "index.html")
    return any(candidate.exists() for candidate in candidates)


html_files = sorted(public_root.rglob("*.html"))
broken = []
checked = 0

for html_file in html_files:
    source_rel = html_file.relative_to(public_root).as_posix()
    parser = LinkParser()
    try:
        parser.feed(html_file.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))

    for href in parser.hrefs:
        local = normalize_local_path(source_rel, href)
        if local is None:
            continue
        checked += 1
        if not target_exists(local):
            broken.append((source_rel, href, local))

print(f"Internal link audit: {len(html_files)} HTML files, {checked} local links checked, {len(broken)} broken links.")
if broken:
    for source, href, local in broken[:300]:
        print(f"BROKEN: {source} -> {href} (resolved: {local})")
    if len(broken) > 300:
        print(f"... plus {len(broken) - 300} more broken links")
    sys.exit(1)
