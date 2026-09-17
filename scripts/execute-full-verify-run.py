#!/usr/bin/env python3
from __future__ import annotations

import collections
import concurrent.futures
import json
import pathlib
import re
import subprocess
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
RUN_ID = "verify-full-2026-09-18"
AS_OF = "2026-09-18"


def run(cmd):
    subprocess.run(cmd, cwd=ROOT, check=True)


def frontmatter_bounds(lines):
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing frontmatter")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    raise ValueError("unterminated frontmatter")


def add_list_item(path, key, value):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    _, end = frontmatter_bounds(lines)
    idx = next((i for i in range(1, end) if lines[i].startswith(key + ":")), None)
    if idx is None:
        insert = next((i + 1 for i in range(1, end) if lines[i].startswith("name:")), 2)
        lines[insert:insert] = [f"{key}:", f'  - "{value}"']
    else:
        line = lines[idx]
        if "[" in line and "]" in line:
            raw = line.split(":", 1)[1].strip()
            vals = []
            if raw not in ("[]", ""):
                vals = [x.strip().strip("\"'") for x in raw.strip("[]").split(",") if x.strip()]
            if value not in vals:
                vals.append(value)
            lines[idx:idx+1] = [f"{key}:"] + [f'  - "{v}"' for v in vals]
        else:
            j = idx + 1
            vals = []
            while j < end and (lines[j].startswith("  - ") or not lines[j].strip()):
                if lines[j].startswith("  - "):
                    vals.append(lines[j].split("-", 1)[1].strip().strip("\"'"))
                j += 1
            if value not in vals:
                lines.insert(j, f'  - "{value}"')
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_section(path, heading, body):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if heading in text:
        return
    p.write_text(text.rstrip() + "\n\n" + heading + "\n" + body.strip() + "\n", encoding="utf-8")


def create_lab(spec):
    p = ROOT / spec["file"]
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        areas = ", ".join(spec["areas"])
        sources = "\n".join(f"- {u}" for u in spec["sources"])
        body = (
            "---\n"
            "type: research-institution\n"
            f'name: "{spec["lab"]}"\n'
            f'organization: "{spec["school"]}"\n'
            f"areas: [{areas}]\n"
            f'website: {spec["website"]}\n'
            f'country: "{spec["country"]}"\n'
            f'city: "{spec["city"]}"\n'
            'last_verified: "2026-09"\n'
            "---\n"
            f'# {spec["lab"]}\n\n{spec["summary"]}\n\n## Sources\n{sources}\n'
        )
        p.write_text(body, encoding="utf-8")
    add_list_item(spec["school_path"], "labs", spec["lab"])


LABS = [
    dict(school_path="university/北京邮电大学/北京邮电大学.md", school="北京邮电大学",
         lab="网络与交换技术全国重点实验室", file="university/北京邮电大学/网络与交换技术全国重点实验室.md",
         website="https://sklnst.bupt.edu.cn/", country="China", city="Beijing",
         areas=["networking","distributed-systems","cloud-systems","ai-infrastructure"],
         summary="北京邮电大学网络与交换技术全国重点实验室。官方页面展示网络、云与系统研究，并持续出现系统论文与大模型相关研究活动。",
         sources=["https://sklnst.bupt.edu.cn/","https://ai.bupt.edu.cn/info/1078/3919.htm"]),
    dict(school_path="university/电子科技大学/电子科技大学.md", school="电子科技大学",
         lab="Intelligent Computing Systems Laboratory", file="university/电子科技大学/Intelligent Computing Systems Laboratory.md",
         website="https://www.nise.ac.cn/", country="China", city="Chengdu",
         areas=["intelligent-computing","edge-cloud","systems","machine-learning"],
         summary="电子科技大学计算机学院 Intelligent Computing Systems Laboratory，研究覆盖智能计算、边云协同、系统软件与机器学习。",
         sources=["https://www.nise.ac.cn/"]),
    dict(school_path="university/西北工业大学/西北工业大学.md", school="西北工业大学",
         lab="边云智能创新实验室", file="university/西北工业大学/边云智能创新实验室.md",
         website="https://soai.nwpu.edu.cn/info/1039/4694.htm", country="China", city="Xi’an",
         areas=["edge-cloud","large-language-models","multi-agent-systems","ai-systems"],
         summary="西北工业大学人工智能学院边云智能创新实验室。学校官方团队介绍明确列出 AI 大模型、多智能体协同与边云智能等方向。",
         sources=["https://soai.nwpu.edu.cn/info/1039/4694.htm"]),
    dict(school_path="university/南京大学/南京大学.md", school="南京大学",
         lab="大模型研究协同创新中心", file="university/南京大学/大模型研究协同创新中心.md",
         website="https://cs.nju.edu.cn/lm/en/index.html", country="China", city="Nanjing",
         areas=["large-language-models","llm-systems","distributed-training","inference-optimization"],
         summary="南京大学计算机学院大模型研究协同创新中心。官方页面覆盖可扩展大模型系统架构、高性能机器学习平台、训练/推理性能与云端大模型系统优化。",
         sources=["https://cs.nju.edu.cn/lm/en/index.html","https://cs.nju.edu.cn/lm/en/research/index.html"]),
    dict(school_path="university/Stony Brook University/Stony Brook University.md", school="Stony Brook University",
         lab="AI Innovation Institute", file="university/Stony Brook University/AI Innovation Institute.md",
         website="https://ai.stonybrook.edu/", country="USA", city="Stony Brook, NY",
         areas=["ai-systems","machine-learning","gpu-computing","large-language-models"],
         summary="Stony Brook University AI Innovation Institute。官方研究页将 AI Systems and Machine Learning 列为研究方向，并运营面向大规模机器学习研究的 GPU 计算设施。",
         sources=["https://ai.stonybrook.edu/research","https://ai.stonybrook.edu/resources/computingresources"]),
    dict(school_path="university/Massachusetts Institute of Technology/Massachusetts Institute of Technology.md", school="Massachusetts Institute of Technology",
         lab="HAN Lab", file="university/Massachusetts Institute of Technology/HAN Lab.md",
         website="https://hanlab.mit.edu/", country="USA", city="Cambridge, MA",
         areas=["efficient-ai","llm-serving","gpu-systems","quantization","sparse-attention"],
         summary="MIT HAN Lab 聚焦 efficient generative AI 与 algorithm-system co-design；公开项目覆盖 QServe、LServe、OmniServe、KV-cache 与稀疏 attention 等高效推理方向。",
         sources=["https://hanlab.mit.edu/","https://github.com/mit-han-lab/omniserve"]),
    dict(school_path="university/Seoul National University/Seoul National University.md", school="Seoul National University",
         lab="Machine Learning Systems Lab", file="university/Seoul National University/Machine Learning Systems Lab.md",
         website="https://mlsys.snu.ac.kr/", country="South Korea", city="Seoul",
         areas=["machine-learning-systems","llm-training","llm-inference","quantization"],
         summary="Seoul National University Machine Learning Systems Lab。实验室主页明确将大规模 ML systems、LLM training/inference optimization、quantization 列为核心主题。",
         sources=["https://mlsys.snu.ac.kr/"]),
    dict(school_path="university/UC Davis/UC Davis.md", school="UC Davis",
         lab="GATE Lab", file="university/UC Davis/GATE Lab.md",
         website="https://www.ece.ucdavis.edu/~avesta/", country="USA", city="Davis, CA",
         areas=["hardware-for-ml","ml-systems","inference-efficiency","hw-sw-codesign"],
         summary="UC Davis GATE Lab（Green, Accelerated, and Trustworthy Engineering），研究覆盖 ML systems、硬件加速、HW/SW co-design 与高效 inference。",
         sources=["https://www.ece.ucdavis.edu/~avesta/","https://ece.ucdavis.edu/directory/avesta-sasan"]),
    dict(school_path="university/University of British Columbia/University of British Columbia.md", school="University of British Columbia",
         lab="Systems and Architectures (STAR) Lab", file="university/University of British Columbia/Systems and Architectures STAR Lab.md",
         website="https://prashantnair.bitbucket.io/", country="Canada", city="Vancouver",
         areas=["computer-architecture","memory-systems","ml-systems","llm-inference"],
         summary="UBC Systems and Architectures (STAR) Lab，由 Prashant Nair 领导，研究计算机体系结构、内存系统与 AI/ML systems；相关工作包括 Keyformer 等 LLM inference/KV-cache 优化。",
         sources=["https://prashantnair.bitbucket.io/","https://people.ece.ubc.ca/adnan/"]),
    dict(school_path="university/Georgia Institute of Technology/Georgia Institute of Technology.md", school="Georgia Institute of Technology",
         lab="Systems for Artificial Intelligence Lab", file="university/Georgia Institute of Technology/Systems for Artificial Intelligence Lab.md",
         website="https://faculty.cc.gatech.edu/~atumanov/", country="USA", city="Atlanta, GA",
         areas=["ai-systems","distributed-systems","llm-inference","resource-management"],
         summary="Georgia Tech Systems for Artificial Intelligence Lab (SAIL)，由 Alexey Tumanov 领导，研究 distributed systems support for ML 与 large foundation model inference/reasoning systems。",
         sources=["https://faculty.cc.gatech.edu/~atumanov/"]),
    dict(school_path="university/University of Washington/University of Washington.md", school="University of Washington",
         lab="SyFI Lab", file="university/University of Washington/SyFI Lab.md",
         website="https://syfi.cs.washington.edu/", country="USA", city="Seattle, WA",
         areas=["ai-infrastructure","llm-serving","distributed-training","gpu-systems"],
         summary="University of Washington SyFI Lab（Systems for Future Intelligence），专注面向未来 AI 的高效、灵活、可靠基础设施；公开项目覆盖 LLM serving、distributed training、FlashInfer-Bench 等。",
         sources=["https://syfi.cs.washington.edu/","https://syfi.cs.washington.edu/publications/"]),
]


SEMANTIC = {
"company/xAI/xAI::projects":("unresolved",[],["xai_led_inference_project"],"No xAI-led/open inference-infrastructure project was established; downstream engine use is not project ownership."),
"university/清华大学/Weimin Zheng::project_contribution":("success",["Mooncake paper contribution"],[],"Mooncake authorship and MADSys publication records directly verify the contribution."),
"community/vllm-project/vLLM-Ascend/weijinqian0::affiliation":("partial",["Huawei organizational association via public corporate email","vLLM-Ascend maintainer identity"],["current_employment_status"],"Public Huawei email and current vLLM-Ascend identity are verified; current Huawei employment is not promoted without an employer-side source."),
"company/Fireworks AI/Fireworks AI::key_people":("partial",["Lin Qiao: CEO/co-founder"],["additional_key_people_canonicalization"],"Fireworks official site verifies Lin Qiao as CEO; one canonical key-person node was added."),
"university/北京邮电大学/北京邮电大学::labs_or_groups":("partial",["网络与交换技术全国重点实验室"],["second_high_value_ai_infra_group"],"Verified official national key lab; one canonical research-institution node added."),
"company/道客/道客::projects":("success",["HAMi contributor/company ecosystem relation"],[],"DaoCloud documentation and CNCF material support a direct HAMi contributor/deployment relationship without implying sole ownership."),
"university/上海交通大学/上海交通大学::labs_or_groups":("partial",["IPADS"],["NNE_Lab_canonicalization"],"IPADS is canonical and strongly verified; NNE-Lab remains insufficiently stable for a separate canonical node."),
"university/电子科技大学/电子科技大学::labs_or_groups":("partial",["Intelligent Computing Systems Laboratory"],["second_high_value_ai_infra_group"],"Official UESTC laboratory page verified; one canonical node added."),
"university/西北工业大学/西北工业大学::labs_or_groups":("partial",["边云智能创新实验室"],["second_high_value_ai_infra_group"],"Official NWPU AI-school team page verifies the lab and large-model/edge-cloud research."),
"company/商汤科技/商汤科技::projects":("partial",["LightLLM employee-contributor network"],["company_governance_or_ownership"],"SenseTime-affiliated LightLLM contributors establish a company/project talent edge; this does not establish project ownership."),
"university/南京大学/南京大学::labs_or_groups":("partial",["大模型研究协同创新中心"],["second_high_value_ai_infra_group"],"Official NJU center pages verify large-model systems, training/inference performance and cloud LLM system groups."),
"university/Stony Brook University/Stony Brook University::labs_or_groups":("partial",["AI Innovation Institute"],["second_high_value_ai_infra_group"],"Official institute pages verify AI Systems and Machine Learning plus dedicated GPU research infrastructure."),
"university/Binghamton University/Binghamton University::labs_or_groups":("unresolved",[],["ai_infra_specific_lab"],"No stable AI-infra/LLM-systems group suitable for canonicalization was verified."),
"university/Case Western Reserve University/Case Western Reserve University::labs_or_groups":("partial",["reSAID Lab candidate"],["ai_infra_fit","canonicalization"],"A current CWRU LLM/AI-software lab was identified, but its focus is responsible AI software rather than inference infrastructure."),
"university/Franklin W. Olin College of Engineering/Franklin W. Olin College of Engineering::labs_or_groups":("unresolved",[],["ai_infra_specific_lab"],"No stable AI-infra/LLM-systems research group was identified; institutional AI activity alone is insufficient."),
"university/Lobachevsky State University of Nizhny Novgorod/Lobachevsky State University of Nizhny Novgorod::labs_or_groups":("unresolved",[],["ai_infra_specific_lab"],"No sufficiently stable public AI-infra/LLM-systems lab identity was verified."),
"university/Massachusetts Institute of Technology/Massachusetts Institute of Technology::labs_or_groups":("partial",["HAN Lab"],["second_high_value_ai_infra_group"],"MIT HAN Lab is directly verified and strongly aligned with efficient LLM inference, serving, quantization and sparse attention."),
"university/Nanyang Technological University/Nanyang Technological University::labs_or_groups":("partial",["GLINT Lab candidate","Network Systems Lab candidate"],["ai_infra_fit","canonicalization"],"Relevant NTU LLM/network groups were identified, but direct serving-infrastructure fit is not strong enough for canonicalization."),
"university/Seoul National University/Seoul National University::labs_or_groups":("partial",["Machine Learning Systems Lab"],["second_high_value_ai_infra_group"],"SNU MLSys Lab explicitly lists LLM training/inference optimization and large-scale ML systems."),
"university/Technion - Israel Institute of Technology/Technion - Israel Institute of Technology::labs_or_groups":("unresolved",[],["ai_infra_specific_lab"],"Efficient LLM systems work was found, but no stable current lab/group identity was verified for canonicalization."),
"university/UC Davis/UC Davis::labs_or_groups":("partial",["GATE Lab"],["second_high_value_ai_infra_group"],"UC Davis GATE Lab is verified with hardware/ML systems, HW/SW co-design and inference-efficiency work."),
"university/University of British Columbia/University of British Columbia::labs_or_groups":("partial",["Systems and Architectures (STAR) Lab"],["second_high_value_ai_infra_group"],"UBC STAR Lab is verified; members work on memory systems, ML systems and KV-cache/generative-inference optimization."),
"university/华中科技大学/华中科技大学::labs_or_groups":("partial",["智能信息与大数据实验室 candidate"],["ai_infra_fit","canonicalization"],"A HUST lab with LLM/KV-cache work was identified, but evidence is stronger for algorithms/survey work than a dedicated infra group."),
"university/江南大学/江南大学::labs_or_groups":("unresolved",[],["research_group_not_teaching_lab"],"An AI practice/innovation teaching laboratory was found, but it is not a research group suitable for this graph."),
"university/Georgia Institute of Technology/Georgia Institute of Technology::labs_or_groups":("partial",["Systems for Artificial Intelligence Lab"],["second_high_value_ai_infra_group"],"Georgia Tech SAIL is verified and explicitly studies distributed support for ML and large-foundation-model inference."),
"university/University of Washington/University of Washington::labs_or_groups":("partial",["SyFI Lab"],["second_high_value_ai_infra_group"],"UW SyFI is verified and directly focuses on AI infrastructure, LLM serving, training and system reliability."),
"university/厦门大学/厦门大学::labs_or_groups":("partial",["谷雨大模型实验室 candidate","空间感知与计算实验室 candidate"],["ai_infra_fit","canonicalization"],"XMU groups with LLM/agent work were found, but direct AI-inference-infrastructure fit remains too weak for canonicalization."),
"company/RadixArk/RadixArk::projects":("success",["SGLang","Miles"],[],"RadixArk publicly identifies SGLang and Miles as its two open-source foundations."),
"company/趋境科技/Weiyu Xie::project_contribution":("success",["KTransformers maintainer","KTransformers SOSP author"],[],"KTransformers project and MADSys sources directly verify Weiyu Xie's maintainer and paper contribution."),
"university/清华大学/Yongwei Wu::project_contribution":("success",["Mooncake","KTransformers"],[],"MADSys publication records directly verify Yongwei Wu on Mooncake and KTransformers."),
"company/Meta/Meta::projects":("success",["vLLM contributor network"],[],"Multiple current Meta-affiliated vLLM contributors support the company/project contributor-network edge; this is not project ownership."),
"company/HPE/HPE::projects":("partial",["NIXL employee-contributor network"],["company_governance_or_ownership"],"HPE-affiliated Ryan Hankins contributes NIXL/libfabric/CXI work; the edge is contributor-network evidence, not HPE ownership."),
}


def apply_graph_updates():
    for spec in LABS:
        create_lab(spec)

    fp = ROOT / "company/Fireworks AI/Lin Qiao.md"
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text('''---
type: person
name: Lin Qiao
current_affiliations: ["Fireworks AI"]
roles: [CEO, Co-founder]
linked_companies:
  - "company/Fireworks AI/Fireworks AI"
areas: [ai-inference, model-serving, ai-infrastructure]
confidence: verified
last_verified: "2026-09"
---
# Lin Qiao

Fireworks AI CEO and co-founder. Fireworks' official site identifies Lin Qiao as CEO; the company's investor profile lists her among the founding team.

## Sources
- https://fireworks.ai/
- https://www.indexventures.com/companies/fireworks-ai/
''', encoding="utf-8")
    add_list_item("company/Fireworks AI/Fireworks AI.md", "linked_people", "company/Fireworks AI/Lin Qiao")
    append_section("company/Fireworks AI/Fireworks AI.md", "## Sources", "- https://fireworks.ai/\n- https://www.indexventures.com/companies/fireworks-ai/")

    add_list_item("company/商汤科技/商汤科技.md", "projects", "LightLLM")
    add_list_item("company/商汤科技/商汤科技.md", "linked_projects", "community/ModelTC/LightLLM/LightLLM")
    append_section("company/商汤科技/商汤科技.md", "## VERIFY note — LightLLM", "The LightLLM edge records a verified overlap between current SenseTime-affiliated contributor nodes and the LightLLM project. It does **not** assert that SenseTime owns or governs LightLLM.\n\n### Sources\n- https://github.com/ModelTC/LightLLM")

    add_list_item("company/HPE/HPE.md", "projects", "NIXL")
    add_list_item("company/HPE/HPE.md", "linked_projects", "community/ai-dynamo/NIXL/NIXL")
    append_section("company/HPE/HPE.md", "## VERIFY note — NIXL", "The NIXL edge records HPE-affiliated contributor Ryan Hankins' work on libfabric/CXI integration. It is a contributor-network edge, not an HPE ownership claim.\n\n### Sources\n- https://github.com/ai-dynamo/nixl")

    append_section("company/道客/道客.md", "## Sources", "- https://docs.daocloud.io/community/hami/\n- https://www.cncf.io/blog/2026/07/15/hami-becomes-a-cncf-incubating-project/")
    append_section("company/RadixArk/RadixArk.md", "## Sources", "- https://www.radixark.com/blog/radixark-launches-100m-seed\n- https://github.com/radixark/miles\n- https://github.com/sgl-project/sglang")


def probe_urls(selected):
    rx = re.compile(r'https?://[^\s<>()\]"\'\]]+')
    action_urls = {}
    all_urls = []
    for a in selected:
        if a["relation"] != "verify_evidence":
            continue
        p = ROOT / (a["source"]["id"] + ".md")
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        urls = []
        for u in rx.findall(text):
            u = u.rstrip(".,;:!?`})]")
            if u not in urls:
                urls.append(u)
        urls = urls[:6]
        action_urls[a["action_id"]] = urls
        all_urls.extend(urls)

    def probe(url):
        req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 full-verify/1.0","Range":"bytes=0-512"})
        try:
            with urllib.request.urlopen(req, timeout=8) as r:
                return url, True, int(getattr(r, "status", 200) or 200)
        except urllib.error.HTTPError as e:
            return url, e.code in (401,403,405,429), int(e.code)
        except Exception:
            return url, False, 0

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as ex:
        for u, ok, code in ex.map(probe, list(dict.fromkeys(all_urls))):
            results[u] = (ok, code)
    return action_urls, results


def record_history(selected):
    action_urls, probe_results = probe_urls(selected)
    hp = ROOT / "research/action-history.json"
    hist = json.loads(hp.read_text(encoding="utf-8"))
    records = hist["records"]
    records[:] = [r for r in records if r.get("run_id") != RUN_ID]
    counts = collections.Counter()

    created_action_ids = {
        "company/Fireworks AI/Fireworks AI::key_people",
        "university/北京邮电大学/北京邮电大学::labs_or_groups",
        "university/电子科技大学/电子科技大学::labs_or_groups",
        "university/西北工业大学/西北工业大学::labs_or_groups",
        "university/南京大学/南京大学::labs_or_groups",
        "university/Stony Brook University/Stony Brook University::labs_or_groups",
        "university/Massachusetts Institute of Technology/Massachusetts Institute of Technology::labs_or_groups",
        "university/Seoul National University/Seoul National University::labs_or_groups",
        "university/UC Davis/UC Davis::labs_or_groups",
        "university/University of British Columbia/University of British Columbia::labs_or_groups",
        "university/Georgia Institute of Technology/Georgia Institute of Technology::labs_or_groups",
        "university/University of Washington/University of Washington::labs_or_groups",
    }

    for a in selected:
        aid = a["action_id"]
        if a["relation"] == "verify_evidence":
            urls = action_urls.get(aid, [])
            reachable = sum(1 for u in urls if probe_results.get(u, (False,0))[0])
            if not urls:
                status, resolved, unresolved = "unresolved", [], ["source_url","semantic_claim_match"]
                note = "No source URL is present on the node; no semantic verification was possible."
            elif reachable == 0:
                status, resolved, unresolved = "unresolved", [], ["source_liveness","semantic_claim_match"]
                note = "Existing sampled source URLs could not be confirmed reachable; semantic claims remain unverified."
            else:
                status, resolved, unresolved = "partial", ["source_liveness"], ["semantic_claim_match"]
                note = f"{reachable}/{len(urls)} sampled source URLs were reachable or access-controlled. This resolves source availability only, not semantic claim fidelity."
            outcome = {"new_nodes":0,"new_edges":0,"evidence_upgraded":1 if reachable else 0,"verified_claims":0,"rejected_claims":0}
        else:
            if aid not in SEMANTIC:
                raise RuntimeError(f"missing semantic outcome for {aid}")
            status, resolved, unresolved, note = SEMANTIC[aid]
            new_nodes = 1 if aid in created_action_ids else 0
            new_edges = 1 if new_nodes or aid in {"company/商汤科技/商汤科技::projects","company/HPE/HPE::projects"} else 0
            outcome = {"new_nodes":new_nodes,"new_edges":new_edges,"evidence_upgraded":1 if resolved else 0,"verified_claims":len(resolved),"rejected_claims":0}
        counts[status] += 1
        rec = {
            "run_id":RUN_ID, "attempted_at":AS_OF, "action_id":aid, "action_key":a["action_key"],
            "operator":"verify", "status":status, "source_name":a["source"]["name"],
            "resolved_dimensions":resolved, "unresolved_dimensions":unresolved, "outcome":outcome, "note":note
        }
        if status == "unresolved":
            rec["retry_after_days"] = 7
        elif status == "partial":
            rec["retry_after_days"] = 2
        records.append(rec)
    hp.write_text(json.dumps(hist, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return counts


def write_runlog(selected, counts):
    p = ROOT / "docs/research-runs/2026-09-18-verify-full.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    ev_count = sum(1 for a in selected if a["relation"] == "verify_evidence")
    lines = [
        "# Full VERIFY Research Run — 2026-09-18","",
        "This run executes the VERIFY operator against the full currently eligible portfolio rather than the mixed daily budget.","",
        f"- Baseline VERIFY actions: **{len(selected)}**",
        f"- Evidence-only actions: **{ev_count}**",
        f"- Relationship/semantic actions: **{len(SEMANTIC)}**",
        f'- Durable outcomes: success={counts["success"]}, partial={counts["partial"]}, unresolved={counts["unresolved"]}, rejected={counts["rejected"]}',"",
        "## Evidence-only policy","",
        "For `verify_evidence` actions, this run checked source availability across the full set. Reachability is deliberately recorded as `partial`, not `success`, because a live URL does not by itself prove that every semantic claim on the node is correct. Nodes with no URLs or no reachable sampled source are recorded `unresolved`.","",
        "## Semantic outcomes","",
        "| Action | Status | Resolved | Unresolved |",
        "|---|---|---|---|",
    ]
    for aid, (status, resolved, unresolved, note) in SEMANTIC.items():
        lines.append(f'| `{aid}` | {status} | {"; ".join(resolved) or "—"} | {"; ".join(unresolved) or "—"} |')
    lines += ["","## Evidence boundary","",
              "- Adoption/compatibility is not project ownership.",
              "- Employee participation in an open-source project is recorded as a contributor-network edge unless company governance is directly documented.",
              "- Corporate email proves an organizational association, not necessarily current employment.",
              "- A university-wide AI initiative or teaching lab is not automatically canonicalized as an AI-infrastructure research group.",
              "- Unresolved dimensions remain visible for future VERIFY passes.",""]
    p.write_text("\n".join(lines), encoding="utf-8")


def main():
    run(["python3","scripts/plan-research-v3.py","--operator","verify","--budget","2000","--limit","2000","--as-of",AS_OF])
    payload = json.loads((ROOT/"generated/research-actions.json").read_text(encoding="utf-8"))
    selected = payload["selected_actions"]
    if len(selected) != 177:
        raise RuntimeError(f"expected 177 baseline VERIFY actions, got {len(selected)}")
    if sum(1 for a in selected if a["relation"] != "verify_evidence") != 32:
        raise RuntimeError("semantic VERIFY action count drifted")
    apply_graph_updates()
    counts = record_history(selected)
    write_runlog(selected, counts)
    print("full VERIFY outcomes", dict(counts))


if __name__ == "__main__":
    main()
