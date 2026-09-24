#!/usr/bin/env python3
import argparse
import pathlib
from collections import Counter, defaultdict
from urllib.parse import quote

DOMAIN_ORDER = [
    "inference",
    "training",
    "memory",
    "communication",
    "scheduling",
    "kernel",
    "compiler",
    "quantization",
    "distributed-systems",
    "hardware",
    "data",
    "other",
]

def scalar(value):
    value = value.strip()
    if not value:
        return ""
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip("\"'") for item in value[1:-1].split(",") if item.strip()]
    if value.lower() in {"null", "none", "~"}:
        return None
    return value.strip("\"'")

def frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    data = {}
    current = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") and current:
            if not isinstance(data.get(current), list):
                if data.get(current) in ("", None):
                    data[current] = []
                else:
                    continue
            data[current].append(scalar(raw[4:]))
            continue
        if raw.startswith((" ", "-")) or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        current = key.strip()
        data[current] = scalar(value)
    return data

def values(value):
    if value in (None, ""):
        return []
    return value if isinstance(value, list) else [str(value)]

def title(value):
    return str(value or "other").replace("-", " ").title()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="generated/concept-index.md")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    concept_root = root / "concept"
    output = root / args.output

    rows = []
    if concept_root.exists():
        for path in sorted(concept_root.rglob("*.md")):
            meta = frontmatter(path.read_text(encoding="utf-8"))
            if meta.get("type") != "concept":
                continue
            rel = path.relative_to(root).with_suffix("").as_posix()
            rows.append({
                "name": str(meta.get("name") or path.stem),
                "path": rel,
                "domain": str(meta.get("domain") or "other"),
                "topic": str(meta.get("topic") or ""),
                "aliases": values(meta.get("aliases")),
                "parents": values(meta.get("parent_concepts")),
                "related": values(meta.get("related_concepts")),
                "projects": values(meta.get("projects")),
            })

    grouped = defaultdict(lambda: defaultdict(list))
    for row in rows:
        grouped[row["domain"]][row["topic"] or "other"].append(row)

    counts = Counter(row["domain"] for row in rows)
    domains = [d for d in DOMAIN_ORDER if d in grouped] + sorted(d for d in grouped if d not in DOMAIN_ORDER)

    lines = [
        "# Concept Index",
        "",
        "Automatically generated from canonical `type: concept` nodes under `concept/`.",
        "",
        f"- Concepts: {len(rows)}",
        f"- Domains: {len(grouped)}",
        "",
        "Stable portal: [[concept]] · Implementation view: [[community/Software|Software]]",
        "",
    ]

    if not rows:
        lines.extend([
            "> Ontology infrastructure is ready; no canonical concept nodes have been added yet.",
            "",
        ])

    for domain in domains:
        lines.extend([f"## {title(domain)}", "", f"{counts[domain]} concepts.", ""])
        for topic in sorted(grouped[domain]):
            if len(grouped[domain]) > 1 or topic != "other":
                lines.extend([f"### {title(topic)}", ""])
            lines.extend([
                "| Concept | Aliases | Parent | Related | Projects | Graph |",
                "| --- | --- | --- | ---: | ---: | --- |",
            ])
            for row in sorted(grouped[domain][topic], key=lambda x: x["name"].casefold()):
                aliases = ", ".join(str(x) for x in row["aliases"][:4])
                parents = ", ".join(str(x) for x in row["parents"][:3])
                focus = quote(row["name"], safe="")
                graph = f"https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus={focus}"
                lines.append(
                    f"| [[{row['path']}|{row['name']}]] | {aliases} | {parents} | "
                    f"{len(row['related'])} | {len(row['projects'])} | [focus]({graph}) |"
                )
            lines.append("")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Concept index: {len(rows)} concepts -> {output.relative_to(root)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
