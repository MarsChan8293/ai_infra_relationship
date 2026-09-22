# RoofLang Targeted DISCOVER — 2026-09-22

This run starts from the external project seed `https://github.com/yzygitzh/rooflang` and applies the repository evidence contract conservatively.

## Execution boundary

- Seed: RoofLang
- Mode: targeted external discovery
- New canonical nodes: 5
- Project nodes: 1
- Person nodes: 4
- Strong project-person membership edges: 4
- Direct software integrations added: 0
- Follow-up frontier candidates: SuperBench, SIGMA
- Durable planner action-history record: not added, because this seed did not originate from a checked-in planner action

## Added graph

### RoofLang

Added as an active `project` with primary layer `optimization`.

The project represents workloads and hardware as graphs, exposes semantics-preserving transformations and placement primitives, and uses roofline-based discrete-event simulation to evaluate candidate inference architectures. Its persistent optimizer-agent workflow makes it directly relevant to AI-driven LLM inference architecture search.

Hardware coverage is recorded conservatively from explicit presets / evaluation only. References to other serving systems are not converted into `integrations` without direct project-level integration evidence.

### Direct authors

Added:

- Ziyue Yang
- Yuting Jiang
- Lei Qu
- Peng Cheng

arXiv v2 explicitly maps Ziyue Yang, Yuting Jiang and Lei Qu to Shanghai Xingyunzhili Artificial Intelligence Institute, and Peng Cheng to Microsoft Research.

Repository commit evidence supports direct RoofLang code / document contribution by Ziyue Yang. The other paper authors are not promoted to maintainer roles without repository governance evidence.

## Discovery value

The author set exposes a useful longitudinal AI Infra bridge.

All four RoofLang authors also appear on **SuperBench** (USENIX ATC 2024 Best Paper), and all four appear again on **SIGMA** (2025). The resulting trajectory is:

`AI infrastructure monitoring / validation → heterogeneous training infrastructure → LLM inference architecture modeling and autonomous search`

This is stronger than a one-paper coauthor signal and makes the group a useful frontier for later EXPAND / VERIFY work.

## Deferred frontier

### SuperBench

High-value missing project node. It links the RoofLang authors to production-scale AI infrastructure reliability and Azure GPU validation.

### SIGMA

High-value missing training project / stack node. It links the same author network to early-life accelerators, distributed training reliability, stability and parallelism optimization.

These are deliberately left for a later action rather than recursively materialized in the same targeted discovery.

## Primary sources

- https://github.com/yzygitzh/rooflang
- https://yzygitzh.github.io/rooflang/
- https://arxiv.org/abs/2609.12551
- https://arxiv.org/html/2609.12551v2
- https://www.usenix.org/conference/atc24/presentation/xiong
- https://www.microsoft.com/en-us/research/publication/superbench/
- https://arxiv.org/abs/2512.13488
- https://www.microsoft.com/en-us/research/people/pengc/
