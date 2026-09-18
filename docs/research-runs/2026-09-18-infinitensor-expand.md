# EXPAND: InfiniTensor ecosystem — 2026-09-18

## Seed
https://github.com/InfiniTensor

User-facing seed page:
https://marschan8293.github.io/ai_infra_relationship/community/infinitensor/

## Scope
从单一 InfiniTensor inference-engine 节点扩展为 2026 九源异构 AI Infra 软件栈，优先覆盖 runtime / operators / communication / inference / training / DSL-kernel 主线。

## Added project nodes
- InfiniCore
- InfiniOps
- InfiniRT
- InfiniCCL
- InfiniLM
- InfiniTrain
- NineToothed
- ntops

## Added person nodes
- zhangyue207
- baominghelly
- qinyiqun
- wooway777
- GordonYang1

## Enriched existing people
- 王豪杰 / whjthu → InfiniTensor + NineToothed + InfiniLM
- 黄嘉成 / voltjia → NineToothed + InfiniCore + InfiniOps + InfiniRT + InfiniCCL + InfiniLM
- 潘泽众 / PanZezhong1725 → InfiniCore + InfiniLM

## Key graph structure
`启元实验室 → InfiniCore → InfiniRT / InfiniOps / InfiniCCL → InfiniLM / InfiniTrain`

`清华 HPC / PACMAN → PET / EinNet → InfiniTensor`

`启元实验室 → NineToothed ↔ TileLang → DeepSeek TileKernels`

`InfiniOps → Ascend attention / KV-cache kernels`

## Evidence boundaries
- High GitHub activity and many merged PRs prove direct engineering contribution, not formal maintainer authority.
- Handle-only nodes are retained as handles when real-name disambiguation is not stable.
- Shared organization or adjacent backend integration does not imply employment, co-worker, or project governance relations.
- The original InfiniTensor repository remains active and is modeled as original/legacy inference engine plus research lineage, not as the entire organization.

## Primary sources
- https://github.com/InfiniTensor/InfiniTensor
- https://github.com/InfiniTensor/InfiniCore
- https://github.com/InfiniTensor/InfiniOps
- https://github.com/InfiniTensor/InfiniRT
- https://github.com/InfiniTensor/InfiniCCL
- https://github.com/InfiniTensor/InfiniLM
- https://github.com/InfiniTensor/InfiniTrain
- https://github.com/InfiniTensor/ninetoothed
- https://github.com/InfiniTensor/ntops
