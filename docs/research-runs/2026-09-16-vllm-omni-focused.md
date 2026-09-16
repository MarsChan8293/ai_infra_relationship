# vLLM-Omni focused ecosystem search — 2026-09-16

## Scope

Seed: `vLLM-Omni`

This was a bounded, seed-focused heterogeneous search from current `main`. It explored four directions:

1. project governance and high-value maintainers;
2. Ascend / NPU hardware integration;
3. multimodal / diffusion RL post-training;
4. realtime omni-modal serving and academic systems links.

The goal was not to ingest the full maintainer roster or every supported model. The pass selected nodes that create durable bridges to the repository's inference-optimization graph.

## Main result

vLLM-Omni should be modeled as more than a multimodal wrapper around vLLM. Its current architecture and ecosystem form several connected AI Infra paths:

- `vLLM → vLLM-Omni → fully-disaggregated stage serving`
- `vLLM-Omni → Canlin Guo → vLLM-Ascend / MindIE-SD / Ascend NPU`
- `vLLM-Omni → Yongxiang Huang → VeRL-Omni → multimodal/diffusion RL post-training`
- `VeRL-Omni ↔ openYuanRong Team`
- `CUHK → Peiqi Yin / James Cheng → vLLM-Omni → LiveServe`
- `Huawei → Gao Han / Hongsheng Liu → vLLM-Omni governance`

## Governance findings

Official `vllm-project/vllm-omni` governance currently lists three Lead Maintainers:

- `@Gaohan123` — Gao Han
- `@hsliuustc0106` — Hongsheng Liu
- `@ywang96` — Roger Wang

The same governance document lists 17 Active Committers with subsystem ownership. This pass intentionally did **not** ingest the whole roster. It selected two committers whose responsibilities create high-value bridges:

- `@gcanlin` — Canlin Guo: hardware plugin, NPU integration, TTS; links vLLM-Omni to vLLM-Ascend / MindIE-SD.
- `@SamitHuang` — Yongxiang Huang: RL, diffusion, cache; also VeRL-Omni Lead Maintainer.

Governance explicitly states that committer status belongs to individuals, not companies. Huawei employment for Gao Han / Hongsheng Liu therefore creates person↔company and person↔project edges, **not** a Huawei ownership edge for vLLM-Omni.

## New canonical nodes

### People

- `community/vllm-project/vLLM-Omni/Gao Han`
- `community/vllm-project/vLLM-Omni/Hongsheng Liu`
- `community/vllm-project/vLLM-Omni/Canlin Guo`
- `community/vllm-project/vLLM-Omni/Yongxiang Huang`
- `university/香港中文大学/Peiqi Yin`
- `university/香港中文大学/James Cheng`

### Projects / schools

- `community/verl-project/VeRL-Omni/VeRL-Omni`
- `university/香港中文大学/LiveServe`
- `university/香港中文大学/香港中文大学`

## vLLM-Omni architecture / project evidence

The official README and 2026 paper describe vLLM-Omni as a serving system for any-to-any omni-modality models. Key system ideas include:

- stage graph abstraction for heterogeneous AR / diffusion computation;
- independent serving and batching for each stage;
- pipelined stage execution overlap;
- unified inter-stage connectors;
- dynamic per-stage resource allocation;
- broad CUDA / ROCm / XPU / NPU hardware support.

The paper reports up to 91.4% lower job completion time versus the evaluated baseline.

## Ascend / NPU path

Canlin Guo is an official vLLM-Omni Active Committer for hardware plugin / NPU integration / TTS. Public vLLM-Omni NPU roadmaps link the project to:

- `vLLM-Ascend` for the Ascend AR runtime / model runner path;
- `MindIE-SD` for Ascend-optimized diffusion operators;
- YuanRong connectors for cross-stage storage / P2P transfer.

The vLLM-Ascend contributor record also includes `@gcanlin`; this is modeled only as a contribution relationship, not a vLLM-Ascend maintainer role.

## RL / post-training path

VeRL-Omni is a dedicated RL training framework for diffusion and omni-modality models. Its README explicitly uses vLLM-Omni as a rollout backend and highlights request-level / step-wise batching, rollout routing, embed caching, asynchronous reward computation, and distributed training backends.

VeRL-Omni governance lists Yongxiang Huang (`@samithuang`) and Xibin Wu (`@wuxibin89`) as Lead Maintainers. Because Yongxiang Huang is also a vLLM-Omni Active Committer for RL / diffusion / cache, he forms a strong serving↔post-training bridge.

VeRL-Omni's project citation includes `openYuanRong Team`, so the existing openYuanRong node is linked at the **project collaboration** level. This does not imply that every member of the two projects directly collaborates with every other member.

## Realtime serving / academic path

Peiqi Yin (尹沛骐) is the first author of the vLLM-Omni paper and, as of 2026-09, a CUHK CSE PhD candidate supervised by James Cheng.

Their follow-up `LiveServe` work builds on vLLM-Omni and targets realtime omni-modal interactions. The paper introduces interaction-aware scheduling and next-use-aware KV management using playback progress, speech activity, and barge-in signals. Reported results include roughly 1.55× average improvement in P90 audio TTFP and roughly 1.15× average improvement in completed-request throughput across evaluated workloads.

No stable official public LiveServe source repository was found in this pass, so the node is conservatively marked `open_source: false`.

## Identity / affiliation resolutions

- `@Gaohan123` → Gao Han. HKUST official 2026 event material identifies him as a vLLM-Omni Maintainer at Huawei and an HKUST MSc(BDT) alumnus.
- `@hsliuustc0106` → Hongsheng Liu. GitHub profile states `Core Maintainer@vLLM-Omni, Research Scientist@Huawei`.
- `@gcanlin` → Canlin Guo. Governance establishes role; current employer was not upgraded because no equally strong public affiliation evidence was found in this pass.
- `@SamitHuang` → Yongxiang Huang. vLLM-Omni / VeRL-Omni governance establishes roles; GitHub profile supports HKUST CSE PhD graduate status. Current employer was not inferred.
- Peiqi Yin → 尹沛骐; personal site establishes CUHK PhD status and James Cheng advisor relation.

## Evidence boundaries / rejected upgrades

- Did not ingest all 17 vLLM-Omni Active Committers merely because governance lists them.
- Did not convert CODEOWNERS entries into governance roles; the project itself says CODEOWNERS is reviewer-routing metadata, not merge authority.
- Did not mark vLLM-Omni as Huawei-owned despite two verified Huawei-affiliated Lead Maintainers.
- Did not mark Canlin Guo as a vLLM-Ascend maintainer; contributor evidence is sufficient only for a contribution edge.
- Did not infer Yongxiang Huang's current employer.
- Did not mark LiveServe open source without an official repository.

## Existing nodes strengthened

- `community/vllm-project/vLLM-Omni/vLLM-Omni`
- `company/华为/华为`
- `university/香港科技大学/香港科技大学`
- `community/openEuler/openYuanRong/openYuanRong`

## Next frontier

Potential future actions from this seed, if further depth is wanted:

- Peiqi Yin → SparseServe / Progressive Sparse Attention;
- vLLM-Omni realtime full-duplex runtime and streaming speech serving;
- diffusion paged-KV / cache / offload ownership;
- VeRL-Omni rollout / agent-loop maintainers beyond the lead-maintainer bridge;
- hardware portability across ROCm / XPU / NPU without conflating hardware support with company ownership.

## Primary sources

- https://github.com/vllm-project/vllm-omni
- https://github.com/vllm-project/vllm-omni/blob/main/docs/community/governance.md
- https://github.com/vllm-project/vllm-omni/blob/main/.github/CODEOWNERS
- https://arxiv.org/abs/2602.02204
- https://github.com/verl-project/verl-omni
- https://github.com/verl-project/verl-omni/blob/main/docs/community/governance.md
- https://yinpeiqi.github.io/
- https://www.cse.cuhk.edu.hk/~jcheng/
- https://arxiv.org/abs/2606.22983
- https://seng.hkust.edu.hk/news/20260422/research-and-technology-forum-highlights-cse-departments-research-and-industry-engagement
- https://github.com/hsliuustc0106
