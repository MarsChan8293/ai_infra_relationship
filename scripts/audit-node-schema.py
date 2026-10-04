#!/usr/bin/env python3
"""Validate registered node types, required fields, field types and project enums."""
import argparse
import json
import pathlib
import re
import sys
from graph_common import load_yaml, read_frontmatter


def validate(data, schema):
    issues = []
    for field in schema.get("required", []):
        if data.get(field) in (None, "", []):
            issues.append(f"{field}: required")
    for field, spec in schema.get("fields", {}).items():
        if field not in data or data[field] is None:
            continue
        value = data[field]
        kind = spec.get("type")
        if kind == "string" and not isinstance(value, str):
            issues.append(f"{field}: expected string")
        elif kind == "array[string]" and (not isinstance(value, list) or not all(isinstance(x, str) for x in value)):
            issues.append(f"{field}: expected string list")
        if "const" in spec and value != spec["const"]:
            issues.append(f"{field}: expected {spec['const']}")
        # Lifecycle/layer/maturity vocabularies are strict; legacy person confidence
        # values remain under the existing typed-relation migration policy.
        if data.get("type") == "project" and "enum" in spec and value not in spec["enum"]:
            issues.append(f"{field}: invalid value {value!r}")
        pattern = spec.get("pattern")
        if pattern in {"YYYY-MM", "YYYY-MM or YYYY-MM-DD"}:
            regex = r"\d{4}-(0[1-9]|1[0-2])" + (r"(?:-(0[1-9]|[12]\d|3[01]))?" if "DD" in pattern else "")
            if not isinstance(value, str) or not re.fullmatch(regex, value):
                issues.append(f"{field}: invalid date {value!r}")
    if data.get("type") == "project" and data.get("code_availability") == "public":
        repository = data.get("repository")
        if not isinstance(repository, str) or not re.match(r"^https?://[^/]+/.+", repository):
            issues.append("repository: public source requires an absolute repository URL")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated", default="generated")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    generated = root / args.generated
    catalog = load_yaml((root / "schema/catalog.yaml").read_text())["node_schemas"]
    nodes = json.loads((generated / "nodes.json").read_text())
    errors = []
    for node in nodes:
        typ = node["type"]
        if typ not in catalog:
            errors.append({"source": node["path"], "detail": f"Unregistered type: {typ}"})
            continue
        data = read_frontmatter((root / node["path"]).read_text())
        if typ in {"index", "note"}:
            data = {"type": typ, "name": node["name"], **data}
        schema = load_yaml((root / catalog[typ]["file"]).read_text())
        errors.extend({"source": node["path"], "detail": issue} for issue in validate(data, schema))
    report = {"nodes": len(nodes), "errors": errors, "status": "fail" if errors else "pass"}
    (generated / "node-schema-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Node schema audit: {len(nodes)} nodes, {len(errors)} errors")
    for issue in errors[:60]:
        print(f"ERROR: {issue['source']}: {issue['detail']}")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
