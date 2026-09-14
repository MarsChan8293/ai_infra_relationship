#!/usr/bin/env python3
"""Repository-wide Markdown quality migration.

Idempotent migration: Markdown remains the source of truth. The script
normalizes legacy frontmatter, adds source URLs to thin contributor pages,
resolves known red links by creating canonical nodes, and converts explicit
human-written `## 人物关系` bullets into conservative typed relations.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")

PROJECT_SOURCE_BY_PREFIX = {
    "community/ModelTC/LightLLM/": "https://github.com/ModelTC/lightllm",
    "community/NVIDIA/TensorRT-LLM/": "https://github.com/NVIDIA/TensorRT-LLM",
    "community/ai-dynamo/Dynamo/": "https://github.com/ai-dynamo/dynamo",
    "community/ai-dynamo/NIXL/": "https://github.com/ai-dynamo/nixl",
    "community/deepseek-ai/DeepSeek-Infra/": "https://github.com/deepseek-ai",
    "community/flashinfer-ai/FlashInfer/": "https://github.com/flashinfer-ai/flashinfer",
    "community/kvcache-ai/KTransformers/": "https://github.com/kvcache-ai/ktransformers",
    "community/llm-d/llm-d/": "https://github.com/llm-d/llm-d",
    "community/triton-inference-server/Triton-Inference-Server/": "https://github.com/triton-inference-server/server",
    "community/vllm-project/AIBrix/": "https://github.com/vllm-project/aibrix",
}

AREA_BY_COMMUNITY = {
    "vLLM": "llm-inference", "SGLang": "llm-inference", "Ray": "distributed-systems",
    "Mooncake": "kv-cache", "LMCache": "kv-cache", "KTransformers": "heterogeneous-inference",
    "FlashInfer": "attention-kernels", "DeepGEMM": "gpu-kernels", "FlashMLA": "attention-kernels",
    "DeepSeek-Infra": "llm-inference", "TensorRT-LLM": "llm-inference",
    "llm-d": "distributed-inference", "AIBrix": "distributed-inference",
    "Dynamo": "distributed-inference", "NIXL": "data-transfer",
}

UNWRAP_TARGETS = {
    "人物名", "实体名", "A", "B", "人物",
    "Two Sigma", "Russell Bryant", "Apple AIML",
}

SCHOOL_NODES = {
    "西交利物浦大学": ("Xi'an Jiaotong-Liverpool University", "https://www.xjtlu.edu.cn/"),
    "Cornell Tech": ("Cornell Tech", "https://tech.cornell.edu/"),
    "Columbia University": ("Columbia University", "https://www.columbia.edu/"),
    "复旦大学": ("Fudan University", "https://www.fudan.edu.cn/"),
    "北京航空航天大学": ("Beihang University", "https://www.buaa.edu.cn/"),
    "中山大学": ("Sun Yat-sen University", "https://www.sysu.edu.cn/"),
    "四川大学": ("Sichuan University", "https://www.scu.edu.cn/"),
    "上海科技大学": ("ShanghaiTech University", "https://www.shanghaitech.edu.cn/"),
    "University of Toronto": ("University of Toronto", "https://www.utoronto.ca/"),
    "University of Tennessee, Knoxville": ("University of Tennessee, Knoxville", "https://www.utk.edu/"),
    "University of Warwick": ("University of Warwick", "https://warwick.ac.uk/"),
    "Harvard University": ("Harvard University", "https://www.harvard.edu/"),
    "University of Texas at Austin": ("University of Texas at Austin", "https://www.utexas.edu/"),
    "武汉大学": ("Wuhan University", "https://www.whu.edu.cn/"),
    "Cornell University": ("Cornell University", "https://www.cornell.edu/"),
    "Princeton University": ("Princeton University", "https://www.princeton.edu/"),
    "UCLA": ("University of California, Los Angeles", "https://www.ucla.edu/"),
}

PROJECT_NODES = {
    "Ray": ("community/ray-project/Ray/Ray.md", "Ray", "https://github.com/ray-project/ray",
            "Ray 是面向 AI 与 Python 工作负载的分布式计算框架，Ray Serve 等组件被广泛用于模型服务与 AI Infra。", "ray-project"),
    "EnvPool": ("community/sail-sg/EnvPool/EnvPool.md", "EnvPool", "https://github.com/sail-sg/envpool",
                "EnvPool 是高性能并行强化学习环境执行引擎，以 C++ 批处理与线程池降低 environment simulation 开销。", "sail-sg"),
    "TileScale": ("community/tile-ai/TileScale/TileScale.md", "TileScale", "https://github.com/tile-ai/tilescale",
                  "TileScale 是 TileLang 的分布式扩展，把 tile-level 编程模型扩展到多 GPU、多节点与分布式加速器架构。", "tile-ai"),
}

RESEARCH_NODES = {
    "Oak Ridge National Laboratory": ("Oak Ridge National Laboratory", "https://www.ornl.gov/"),
}


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return [], text
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return [], text
    return lines[1:end], "\n".join(lines[end + 1:]) + ("\n" if text.endswith("\n") else "")


def join_frontmatter(lines: list[str], body: str) -> str:
    return "---\n" + "\n".join(lines).rstrip() + "\n---\n" + body


def key_of(line: str):
    if line.startswith((" ", "\t", "-")) or ":" not in line:
        return None
    return line.split(":", 1)[0].strip() or None


def blocks(lines: list[str]):
    result, i = [], 0
    while i < len(lines):
        key = key_of(lines[i])
        if not key:
            result.append((None, [lines[i]])); i += 1; continue
        j = i + 1
        while j < len(lines) and key_of(lines[j]) is None:
            j += 1
        result.append((key, lines[i:j])); i = j
    return result


def parse_listish(block: list[str]) -> list[str]:
    if not block:
        return []
    value = block[0].split(":", 1)[1].strip()
    if not value:
        return [line[4:].strip().strip("\"'") for line in block[1:] if line.startswith("  - ") and line[4:].strip()]
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        if not body:
            return []
        parts, buf, quote = [], [], None
        for ch in body:
            if ch in "\"'":
                if quote == ch: quote = None
                elif quote is None: quote = ch
                buf.append(ch)
            elif ch == "," and quote is None:
                parts.append("".join(buf).strip()); buf = []
            else:
                buf.append(ch)
        parts.append("".join(buf).strip())
        return [p.strip().strip("\"'") for p in parts if p.strip()]
    return [value.strip("\"'")]


def get_block(lines: list[str], wanted: str):
    return next((block for key, block in blocks(lines) if key == wanted), None)


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block: return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def get_values(lines: list[str], wanted: str) -> list[str]:
    block = get_block(lines, wanted)
    return parse_listish(block) if block else []


def set_key(lines: list[str], key: str, value_line: str, remove_keys=()):
    remove = set(remove_keys) | {key}
    out, inserted = [], False
    for existing, block in blocks(lines):
        if existing in remove:
            if not inserted:
                out.append(f"{key}: {value_line}"); inserted = True
            continue
        out.extend(block)
    if not inserted:
        rel_index = next((i for i, line in enumerate(out) if key_of(line) == "relations"), None)
        if rel_index is None: out.append(f"{key}: {value_line}")
        else: out.insert(rel_index, f"{key}: {value_line}")
    return out


def json_array(values: list[str]) -> str:
    return json.dumps(values, ensure_ascii=False, separators=(",", ":"))


def normalize_frontmatter(lines: list[str]):
    node_type = get_scalar(lines, "type") or ""
    if node_type == "person":
        keys = ["current_affiliations", "affiliations", "affiliation", "companies", "company"]
        merged, seen = [], set()
        for key in keys:
            for value in get_values(lines, key):
                if value and value not in seen:
                    seen.add(value); merged.append(value)
        if merged:
            lines = set_key(lines, "current_affiliations", json_array(merged), remove_keys=keys)
    elif node_type == "project":
        keys = ["companies", "company"]
        merged, seen = [], set()
        for key in keys:
            for value in get_values(lines, key):
                if value and value not in seen:
                    seen.add(value); merged.append(value)
        if merged or any(get_block(lines, k) for k in keys):
            lines = set_key(lines, "companies", json_array(merged), remove_keys=keys)
    return lines


def ensure_source(text: str, rel: str):
    if URL_RE.search(text):
        return text
    url = next((u for prefix, u in PROJECT_SOURCE_BY_PREFIX.items() if rel.startswith(prefix)), None)
    if not url:
        return text
    line = f"- Project source / contributor context: {url}"
    if re.search(r"(?m)^## Sources\s*$", text):
        return re.sub(r"(?m)^(## Sources\s*)$", r"\1\n" + line, text, count=1)
    return text.rstrip() + "\n\n## Sources\n" + line + "\n"


def derive_areas(lines: list[str]) -> list[str]:
    areas = get_values(lines, "areas")
    if areas: return areas
    result = []
    for community in get_values(lines, "communities"):
        area = AREA_BY_COMMUNITY.get(community)
        if area and area not in result: result.append(area)
    return result or ["ai-infrastructure"]


def relation_types(text: str) -> list[str]:
    lowered, types = text.casefold(), []
    def add(value):
        if value not in types: types.append(value)
    if any(x in text for x in ("共同创业", "联合创始")) or "cofound" in lowered: add("cofounder")
    if any(x in text for x in ("论文合著", "共同署名", "共同作者", "论文作者", "论文/系统合作", "论文合作")) or "paper coauthor" in lowered: add("paper-coauthor")
    if any(x in text for x in ("开源协作", "开源项目协作", "社区协作", "共同维护", "维护网络", "开源项目合作")): add("open-source-collaboration")
    neg_coworker = any(x in text for x in ("不是同事", "非同事", "分属", "跨公司"))
    if not neg_coworker and ("同事" in text or "同公司" in text or "公司技术/创业协作" in text): add("coworker")
    if any(x in text for x in ("技术协作", "技术合作", "系统合作", "工程协作")): add("technical-collaboration")
    if any(x in text for x in ("研究合作", "学术合作", "合作网络", "博士后合作", "长期合作", "研究网络")): add("research-collaboration")
    if any(x in text for x in ("导师", "指导", "师生")): add("mentor-network")
    if any(x in text for x in ("人才迁移", "职业连接", "职业轨迹", "career")): add("career-connection")
    if any(x in text for x in ("同门", "同实验室", "实验室同学")): add("same-lab")
    return types


def load_person_index(nodes_path: pathlib.Path):
    if not nodes_path.exists(): return {}, defaultdict(list), defaultdict(list)
    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    by_id, by_base, by_name = {}, defaultdict(list), defaultdict(list)
    for node in nodes:
        if node.get("type") != "person": continue
        node_id = str(node["id"]); by_id[node_id.casefold()] = node
        by_base[pathlib.PurePosixPath(node_id).name.casefold()].append(node)
        name = str(node.get("name") or "").strip().casefold()
        if name: by_name[name].append(node)
    return by_id, by_base, by_name


def resolve_person(target: str, by_id, by_base, by_name):
    target = target.strip().replace("\\", "/").removesuffix(".md").strip("/")
    node = by_id.get(target.casefold())
    if node: return node
    candidates = by_base.get(pathlib.PurePosixPath(target).name.casefold(), [])
    if len(candidates) == 1: return candidates[0]
    candidates = by_name.get(target.casefold(), [])
    return candidates[0] if len(candidates) == 1 else None


def existing_relation_targets(lines: list[str]):
    result = set(); block = get_block(lines, "relations")
    if not block: return result
    for raw in block[1:]:
        if not raw.startswith("  - "): continue
        value = raw[4:].strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'": value = value[1:-1]
        try: obj = json.loads(value)
        except Exception: continue
        target = obj.get("target")
        if isinstance(target, str): result.add(pathlib.PurePosixPath(target.replace("\\", "/")).name.casefold())
    return result


def add_relation_items(lines: list[str], relations: list[dict]):
    if not relations: return lines
    encoded = []
    for relation in relations:
        js = json.dumps(relation, ensure_ascii=False, separators=(",", ":"))
        encoded.append("  - '" + js.replace("'", "''") + "'")
    out, found = [], False
    for key, block in blocks(lines):
        if key == "relations":
            found = True; out.extend(block); out.extend(encoded)
        else: out.extend(block)
    if not found:
        out.append("relations:"); out.extend(encoded)
    return out


def infer_relations(rel: str, lines: list[str], body: str, by_id, by_base, by_name):
    if get_scalar(lines, "type") != "person" or not get_values(lines, "current_affiliations"):
        return lines, 0
    match = re.search(r"(?ms)^## 人物关系\s*\n(.*?)(?=^## |\Z)", body)
    if not match: return lines, 0
    urls = []
    for url in URL_RE.findall(body):
        url = url.rstrip(".,;，。；")
        if url not in urls: urls.append(url)
    if not urls: return lines, 0
    existing, source_id, new_relations = existing_relation_targets(lines), rel[:-3], []
    for bullet in match.group(1).splitlines():
        if not bullet.lstrip().startswith("- "): continue
        types = relation_types(bullet)
        if not types: continue
        for wikilink in WIKILINK_RE.findall(bullet):
            target_raw = wikilink.split("|", 1)[0].split("#", 1)[0].strip()
            target_node = resolve_person(target_raw, by_id, by_base, by_name)
            if not target_node or target_node.get("id") == source_id: continue
            base = pathlib.PurePosixPath(str(target_node["id"])).name.casefold()
            if base in existing: continue
            strong = {"cofounder", "coworker", "paper-coauthor", "open-source-collaboration"}
            new_relations.append({
                "target": target_node["id"], "type": types,
                "confidence": "high" if strong.intersection(types) else "medium",
                "evidence": urls[:3],
            })
            existing.add(base)
    if not new_relations: return lines, 0
    if not get_values(lines, "areas"): lines = set_key(lines, "areas", json_array(derive_areas(lines)))
    if not get_scalar(lines, "last_verified"): lines = set_key(lines, "last_verified", '"2026-09"')
    return add_relation_items(lines, new_relations), len(new_relations)


def create_canonical_nodes(root: pathlib.Path):
    created = []
    for target, (english, url) in SCHOOL_NODES.items():
        path = root / "university" / target / f"{target}.md"
        if path.exists(): continue
        path.parent.mkdir(parents=True, exist_ok=True)
        aliases = [english] if english != target else []
        alias_line = f"aliases: {json_array(aliases)}\n" if aliases else ""
        path.write_text(
            "---\ntype: school\n" + f"name: {target}\n" + alias_line + "last_verified: \"2026-09\"\n---\n"
            + f"# {target}\n\n{target} 是图谱中的高校节点，用于连接 AI Infra 人物的教育、访问研究与学术合作经历。"
              "本页只记录与人才图谱相关的公开连接，不推断未公开的师生或同事关系。\n\n"
            + "## Sources\n" + f"- {url}\n", encoding="utf-8")
        created.append(path.relative_to(root).as_posix())
    for _, (path_str, name, repo, desc, org) in PROJECT_NODES.items():
        path = root / path_str
        if path.exists(): continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\ntype: project\n" + f"name: {name}\nrepository: {repo}\nopen_source: true\nareas: [ai-infrastructure]\nlast_verified: \"2026-09\"\n---\n"
            + f"# {name}\n\n## 项目简介\n{desc}\n\n## GitHub\n{repo}\n\n## 主要维护者 / 组织\n- {org}\n\n"
              "## 生态关系\n该节点用于承接仓库中已有的人才与项目关系；具体人物边仍以人物页的公开证据为准。\n",
            encoding="utf-8")
        created.append(path.relative_to(root).as_posix())
    for target, (name, url) in RESEARCH_NODES.items():
        path = root / "university" / target / f"{target}.md"
        if path.exists(): continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\ntype: research-institution\n" + f"name: {name}\nlast_verified: \"2026-09\"\n---\n"
            + f"# {name}\n\n{name} 是图谱中的研究机构节点，用于连接 HPC、AI systems 与推理基础设施相关人才经历。\n\n"
              "## Sources\n" + f"- {url}\n", encoding="utf-8")
        created.append(path.relative_to(root).as_posix())
    return created


def repair_unwanted_wikilinks(text: str):
    for target in UNWRAP_TARGETS:
        text = text.replace(f"[[{target}]]", target)
    return text


def repair_uc_berkeley_alias(root: pathlib.Path):
    path = root / "university" / "UC Berkeley" / "UC Berkeley.md"
    if not path.exists(): return False
    text = path.read_text(encoding="utf-8")
    old, new = "aliases: [University of California, Berkeley]", 'aliases: ["University of California, Berkeley"]'
    if old not in text: return False
    path.write_text(text.replace(old, new), encoding="utf-8"); return True


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--root", default="."); parser.add_argument("--generated", default="generated")
    args = parser.parse_args(); root = pathlib.Path(args.root).resolve()
    by_id, by_base, by_name = load_person_index(root / args.generated / "nodes.json")
    created, touched, relation_count = create_canonical_nodes(root), [], 0
    paths = [root / "AI Infra Relationship.md"] if (root / "AI Infra Relationship.md").exists() else []
    for dirname in NODE_ROOTS:
        base = root / dirname
        if base.exists(): paths.extend(sorted(base.rglob("*.md")))
    for path in paths:
        rel = path.relative_to(root).as_posix(); original = path.read_text(encoding="utf-8")
        text = repair_unwanted_wikilinks(original); fm_lines, body = split_frontmatter(text)
        if fm_lines:
            fm_lines = normalize_frontmatter(fm_lines)
            text = ensure_source(join_frontmatter(fm_lines, body), rel)
            fm_lines, body = split_frontmatter(text)
            fm_lines, added = infer_relations(rel, fm_lines, body, by_id, by_base, by_name); relation_count += added
            text = join_frontmatter(fm_lines, body)
        if text != original:
            path.write_text(text, encoding="utf-8"); touched.append(rel)
    if repair_uc_berkeley_alias(root) and "university/UC Berkeley/UC Berkeley.md" not in touched:
        touched.append("university/UC Berkeley/UC Berkeley.md")
    print(f"Markdown repair: {len(touched)} files updated, {len(created)} canonical nodes created, {relation_count} typed relations added.")
    for path in created: print("CREATE:", path)
    for path in touched[:80]: print("UPDATE:", path)
    if len(touched) > 80: print(f"... plus {len(touched) - 80} more updated files")


if __name__ == "__main__":
    main()
