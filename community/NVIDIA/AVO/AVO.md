---
type: project
name: "AVO"
linked_people: []
layer: optimization
status: research
docs: https://arxiv.org/abs/2603.24517
areas: ["agentic-kernel-optimization", "evolutionary-search", "agentic-variation-operators", "attention", "cuda", "ptx", "execution-feedback"]
hardware: ["nvidia"]
companies: ["NVIDIA"]
last_verified: "2026-10"
---

# AVO

AVO（Agentic Variation Operators）把传统 evolutionary search 中固定的 mutation / crossover 替换为自主 coding agent。Agent 可以读取 lineage、domain knowledge 和 execution feedback，自主提出、修复、批评并验证 kernel edit。

公开论文在 NVIDIA Blackwell B200 attention kernel 上评估该机制。这里把 AVO 记录为 research system，不把论文作者网络自动等价为某一组织的单独所有权。

## Sources

- https://arxiv.org/abs/2603.24517
