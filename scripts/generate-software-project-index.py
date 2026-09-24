#!/usr/bin/env python3
import argparse
import pathlib
import sys
from collections import Counter, defaultdict
from urllib.parse import quote

ROOTS = ("company", "community", "university")
ORDER = [
    "inference-engine",
    "distributed-serving",
    "gateway",
    "kv-cache",
    "storage",
    "communication",
    "runtime",
    "kernel",
    "compiler",
    "training",
    "scheduler",
    "device-resource",
    "benchmark",
    "ecosystem",
    "optimization",
    "other",
]
TITLES = {
    "inference-engine": "Inference Engine",
    "distributed-serving": "Distributed Serving",
    "gateway": "Gateway / Routing",
    "kv-cache": "KV Cache",
    "storage": "Storage",
    "communication": "Communication / Data Movement",
    "runtime": "Runtime / Framework",
    "kernel": "Kernel / Operator",
    "compiler": "Compiler / DSL",
    "training": "Training / Post-training",
    "scheduler": "Scheduler / Orchestration",
    "device-resource": "Device / Resource",
    "benchmark": "Benchmark / Profiling",
    "ecosystem": "Ecosystem",
    "optimization": "Inference Optimization",
    "other": "Other",
}

def scalar(v):
    v = v.strip()
    if not v:
        return ""
    if v == "[]":
        return []
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
    if v.lower() in {"null", "none", "~"}:
        return None
    return v.strip("\"'")

def fm(text):
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

def vals(v):
    if v in (None, ""):
        return []
    return v if isinstance(v, list) else [str(v)]

def portal_group(layer):
    layer = str(layer or "other").strip().lower()
    if layer in ORDER:
        return layer

    # Keep fine-grained project metadata intact, but fold it into a small,
    # stable set of portal sections for navigation.
    if "compiler" in layer or layer.endswith("-dsl"):
        return "compiler"
    if "kernel" in layer or "operator-optimization" in layer:
        return "kernel"
    if "training" in layer or "post-training" in layer or layer == "rl-rollout-serving":
        return "training"
    if "kv-cache" in layer or layer in {"distributed-data-cache", "heterogeneous-memory-management"}:
        return "kv-cache"
    if (
        "communication" in layer
        or "data-movement" in layer
        or "data-transfer" in layer
        or layer == "post-training-data-plane"
    ):
        return "communication"
    if "storage" in layer:
        return "storage"
    if "scheduler" in layer or "scheduling" in layer or "load-balancing" in layer or layer == "orchestration":
        return "scheduler"
    if layer == "device-resource" or "heterogeneous-compute-platform" in layer:
        return "device-resource"
    if "benchmark" in layer or "profiling" in layer:
        return "benchmark"
    if "gateway" in layer or "routing" in layer or "api-adapter" in layer:
        return "gateway"
    if (
        "inference-engine" in layer
        or layer in {
            "genai-inference-library",
            "edge-moe-serving",
            "multimodal-serving",
            "realtime-multimodal-serving",
            "moe-inference",
            "tensor-parallel-inference",
            "multi-tenant-inference",
            "local-inference-platform",
            "research-llm-inference-engine",
            "llm-inference-engine",
        }
    ):
        return "inference-engine"
    if (
        "distributed-serving" in layer
        or "disaggregated" in layer
        or "long-context-llm-serving" in layer
        or layer in {"llm-serving", "adapter-serving"}
    ):
        return "distributed-serving"
    if (
        "runtime" in layer
        or "compute-software-stack" in layer
        or layer in {
            "heterogeneous-compute",
            "deep-learning-framework-backend",
            "inference-model-and-runtime-integration",
            "llm-serving-hardware-backend",
            "tensor-runtime",
        }
    ):
        return "runtime"
    if "optimization" in layer or "speculative-decoding" in layer or layer == "structured-generation":
        return "optimization"
    if "ecosystem" in layer:
        return "ecosystem"
    return "other"

def source_label(rel):
    parts = pathlib.PurePosixPath(rel).parts
    if len(parts) < 2:
        return parts[0] if parts else ""
    if parts[0] == "community":
        return parts[1]
    return f"{parts[0]}:{parts[1]}"

def discover_projects(root):
    projects = []
    for dirname in ROOTS:
        base = root / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            meta = fm(path.read_text(encoding="utf-8"))
            if meta.get("type") != "project":
                continue
            rel = path.relative_to(root).as_posix()
            exact_layer = str(meta.get("layer") or "other")
            projects.append(
                {
                    "name": str(meta.get("name") or path.stem),
                    "path": rel[:-3],
                    "status": str(meta.get("status") or ""),
                    "layer": exact_layer,
                    "group": portal_group(exact_layer),
                    "areas": vals(meta.get("areas")),
                    "integrations": vals(meta.get("integrations")),
                    "linked_people": vals(meta.get("linked_people")),
                    "linked_companies": vals(meta.get("linked_companies")),
                    "source": source_label(rel),
                    "root": rel.split("/", 1)[0],
                }
            )
    return projects

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="generated/software-project-index.md")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    projects = discover_projects(root)
    groups = defaultdict(list)
    for project in projects:
        groups[project["group"]].append(project)

    root_counts = Counter(p["root"] for p in projects)
    lines = [
        "# Software Project Index",
        "",
        "Automatically generated from every canonical Markdown node with `type: project` under `company/`, `community/`, and `university/`.",
        "",
        f"- Projects: {len(projects)}",
        f"- Source roots: community {root_counts.get('community', 0)} · company {root_counts.get('company', 0)} · university {root_counts.get('university', 0)}",
        "- Fine-grained `layer` metadata is preserved in the table; portal sections fold those layers into a stable navigation taxonomy.",
        "- Concepts are not included; they remain in `ai_infra_docs/software/concepts`.",
        "",
        "## Browse by technology layer",
        "",
        "| Layer | Projects |",
        "| --- | ---: |",
    ]
    for group in ORDER:
        count = len(groups.get(group, []))
        if count:
            lines.append(f"| [{TITLES[group]}](#{group}) | {count} |")
    lines.append("")

    for group in ORDER:
        rows = sorted(groups.get(group, []), key=lambda x: (x["name"].casefold(), x["path"].casefold()))
        if not rows:
            continue
        lines += [
            f"## {group}",
            "",
            f"**{TITLES[group]}** · {len(rows)} projects",
            "",
            "| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |",
            "| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |",
        ]
        for row in rows:
            areas = ", ".join(row["areas"][:5])
            focus = quote(row["name"], safe="")
            graph = f"https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus={focus}"
            lines.append(
                f"| [[{row['path']}]] | {row['layer']} | {row['status']} | {areas} | `{row['source']}` | "
                f"{len(row['integrations'])} | {len(row['linked_people'])} | "
                f"{len(row['linked_companies'])} | [Graph]({graph}) |"
            )
        lines.append("")

    other_layers = Counter(p["layer"] for p in groups.get("other", []))
    if other_layers:
        lines += [
            "## Unmapped fine-grained layers",
            "",
            "These project layers currently fold into `other`. Keeping this list visible makes taxonomy cleanup explicit rather than silently losing detail.",
            "",
        ]
        for layer, count in sorted(other_layers.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- `{layer}`: {count}")
        lines.append("")

    out = root / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"software project index: {len(projects)} canonical projects -> {out.relative_to(root)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
