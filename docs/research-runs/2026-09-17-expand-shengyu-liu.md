# EXPAND Research Run — Shengyu Liu — 2026-09-17

This run executes a seed-driven EXPAND pass from `community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu`.

## Seed

- Person: 刘胜与 / Shengyu Liu / `@interestingLSY`
- Current public affiliation: DeepSeek-AI, since 2025-04
- Focus: MLSys, LLM serving, GPU kernels, MLA, sparse attention, TopK

## Expansion result

Eight high-value frontier nodes were selected instead of recursively adding every coauthor.

### New projects

1. `DeepSelect` — DeepSeek Sparse Attention / sampler TopK kernels; 2026-09 author and current commit evidence directly links Shengyu Liu.
2. `DistServe` — OSDI 2024 prefill/decode disaggregated serving.
3. `LoongServe` — SOSP 2024 elastic sequence parallelism for long-context serving.
4. `SwiftLLM` — Shengyu Liu's compact research inference engine with Triton/PagedAttention data plane.

### New people

1. `Xin Jin` — verified PKU advisor and long-term LLM systems coauthor.
2. `Yinmin Zhong` — long-term PKU systems collaborator; both public homepages show DeepSeek employment from 2025-04, supporting a time-bounded coworker edge.
3. `Bingyang Wu` — long-term PKU serving collaborator across LoongServe / FastServe / RLHFuse.
4. `Yi Qian` (`@skip2004`) — DeepSelect author and direct implementation/documentation collaborator; current employer intentionally not inferred.

## Important current evidence

- 2026-09-10 FlashMLA commit by Shengyu Liu adds DeepSeek V4.1 attention kernels: SM100 sparse prefill/decode, V4.1 FP8/FP4 KV-cache paths, and fused norm + RoPE + attention operators.
- 2026-09-14 Shengyu Liu fixes FlashMLA CUDA 13.0 compilation using `shengyuliu@deepseek.com`.
- DeepSelect v1.0.0 was released in 2026-09 and credits Yi Qian, Shengyu Liu, and Yichen Li. Commit history maps Shengyu Liu to `@interestingLSY` and Yi Qian to `@skip2004`.
- Shengyu Liu's current homepage explicitly states DeepSeek-AI employment from 2025-04 and PKU research under Xin Jin.

## Evidence boundaries

- DeepSeek repository authorship alone is not treated as employment evidence. Yi Qian therefore remains a project-credit identity without `current_affiliations`.
- Yichen Li is retained as a DeepSelect author in prose but not created as a canonical person node because current evidence is insufficient for stable identity resolution.
- Technical adjacency is not promoted to direct collaboration. Later Bingyang Wu MoE work is described as adjacent to DeepSeek kernel work, not as a new pairwise collaboration after their verified shared papers.

## Primary sources

- https://interestinglsy.github.io/
- https://github.com/deepseek-ai/FlashMLA/commit/07a1089857b63e74e3133630c02b083b75e8d4b2
- https://github.com/deepseek-ai/FlashMLA/commit/063a9f05aaf86d25c3da213a6e79cd5c879f99fe
- https://github.com/deepseek-ai/DeepSelect
- https://github.com/deepseek-ai/DeepSelect/commit/671e260b3ae8c5b12352dec063569b54d34e12b1
- https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin
- https://arxiv.org/abs/2404.09526
- https://xinjin.github.io/
- https://www.yinminzhong.com/
- https://bingyangwu.github.io/
- https://github.com/interestingLSY/swiftLLM
