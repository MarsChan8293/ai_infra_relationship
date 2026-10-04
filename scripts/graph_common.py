"""Shared, lossless YAML reading for graph exporters and validators."""
from __future__ import annotations

import re
import yaml
from functools import lru_cache


class GraphLoader(yaml.SafeLoader):
    """Keep dates as strings and reject duplicate keys instead of overwriting."""


GraphLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError("YAML mapping keys must be strings")
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


GraphLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load_yaml(text):
    return yaml.load(text, Loader=GraphLoader)


def split_frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        if text.startswith(("---\n", "---\r\n")):
            raise ValueError("Unterminated YAML frontmatter")
        return {}, text
    data = load_yaml(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a YAML mapping")
    return data, text[match.end():]


def read_frontmatter(text):
    return split_frontmatter(text)[0]


@lru_cache(maxsize=4096)
def _fields(lines):
    return load_yaml("\n".join(lines)) or {}


def field_values(lines, key):
    value = _fields(tuple(lines)).get(key)
    if value is None or value == "":
        return []
    return list(value) if isinstance(value, list) else [str(value)]


def field_scalar(lines, key):
    value = _fields(tuple(lines)).get(key)
    return str(value) if value is not None else None


def evidence_provenance(root, source_path, field):
    """Return traceable source location and source-section URLs, without inventing certainty."""
    text = (root / source_path).read_text(encoding="utf-8")
    _, body = split_frontmatter(text)
    lines = text.splitlines()
    line = next((i + 1 for i, value in enumerate(lines) if value.startswith(field + ":")), None)
    sections = []
    heading = ""
    for value in body.splitlines():
        if value.startswith("#"):
            heading = value.lstrip("#").strip()
        if re.search(r"source|来源|直接依据|参考", heading, re.I):
            sections.extend(re.findall(r"https?://[^\s)>\]]+", value))
    return {
        "source_path": source_path,
        "field": field,
        "line": line,
        "source_urls": sorted(set(sections)),
        "scope": "page-sources; individual assertion not automatically verified",
    }
