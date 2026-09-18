# LMSYS EXPAND — 2026-09-18

## Execution boundary
- Operator: `EXPAND`
- Seed: `LMSYS`
- Objective: expand the LMSYS seed along high-value inference-systems, governance, and talent-bridge relations without flattening the graph into a generic LLM author index.
- Evidence policy: current LMSYS website, official project/blog pages, canonical GitHub repositories, existing verified person nodes, and direct public role evidence.

## Outcome
Status: `success` with two verification follow-ups.

### Added canonical nodes
1. `community/lmsys-org/FastChat/FastChat`
2. `community/lmsys-org/S-LoRA/S-LoRA`
3. `community/lmsys-org/RouteLLM/RouteLLM`
4. `community/lmsys-org/Lookahead-Decoding/Lookahead-Decoding`
5. `company/RadixArk/Mingyi Lu`
6. `company/RadixArk/Richard Chen`

### Strengthened existing nodes
- LMSYS: official nonprofit/history, systems portfolio, current officer/advisor governance, curated high-value people.
- Ying Sheng / Lianmin Zheng / Banghua Zhu: current LMSYS officer roles.
- Ion Stoica / Joseph Gonzalez: current LMSYS advisor roles.
- Mingxing Zhang: current LMSYS advisor role, creating a direct LMSYS ↔ Tsinghua MADSys bridge.

### High-confidence graph bridges
- LMSYS → RadixArk: Ying Sheng, Banghua Zhu, Mingyi Lu, Richard Chen connect governance/community activity to SGLang / Miles production engineering.
- LMSYS → Berkeley Sky: Ion Stoica and Joseph Gonzalez are current advisors; Lianmin Zheng and Ying Sheng connect FastChat / S-LoRA / SGLang research history.
- LMSYS → Tsinghua MADSys: Mingxing Zhang is a current LMSYS advisor while already connecting Mooncake, KTransformers, Seer and DualPath in the graph.
- FastChat → SGLang: research/personnel lineage through Lianmin Zheng and the Berkeley serving network; no claim that one project directly replaced the other.
- S-LoRA → later SGLang/RadixArk network: shared authors and memory-management / serving focus, recorded as research/person-network continuity rather than project governance continuity.
- RouteLLM: adds request-level cost/quality routing as a serving-system layer.
- Lookahead Decoding: adds exact parallel/speculative decoding as a latency-optimization branch.

## Intentionally not expanded
- Chatbot Arena / LMSYS-Chat, MT-Bench, Vicuna and dataset/evaluation author fan-outs were not expanded in this pass unless they created a direct AI Infra bridge.
- Jerry Zhou, Tiancheng Xie and Benhui He are retained in the LMSYS governance prose but not all promoted to canonical person nodes in this run; identity/affiliation value is lower or needs a dedicated VERIFY before creating more nodes.
- The S-LoRA repository is archived, so it is modeled as a historically important research system, not a currently active production stack.

## Follow-up VERIFY
1. The current rendered LMSYS About page and the `lm-sys/lm-sys.github.io` main-branch `content/about.md` have different officer rosters. Re-check the source sync / governance roster in a later VERIFY cycle; current public website is used for the 2026-09 snapshot.
2. Verify stable current affiliations for remaining LMSYS officers before turning the full governance roster into canonical people nodes.

## Evidence
- https://www.lmsys.org/about/
- https://www.lmsys.org/projects/
- https://github.com/lm-sys/FastChat
- https://github.com/S-LoRA/S-LoRA
- https://github.com/lm-sys/RouteLLM
- https://github.com/hao-ai-lab/LookaheadDecoding
- https://www.lmsys.org/blog/2023-11-15-slora/
- https://www.lmsys.org/blog/2024-07-01-routellm/
- https://www.lmsys.org/blog/2023-11-21-lookahead-decoding/
- https://www.deeplearning.ai/short-courses/efficient-inference-with-sglang/
