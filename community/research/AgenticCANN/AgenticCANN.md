---
type: project
name: "AgenticCANN"
linked_people: []
layer: optimization
status: research
docs: https://arxiv.org/abs/2607.26661
areas: ["agentic-kernel-optimization", "ascendc", "knowledge-augmentation", "agentic-evolution", "operator-generation", "runtime-feedback"]
hardware: ["ascend"]
last_verified: "2026-10"
---

# AgenticCANN

AgenticCANN 是针对 Ascend C operator synthesis 的 knowledge-augmented agentic evolution framework。公开论文来自 City University of Hong Kong 与产业合作团队。

## 核心机制

系统针对 Ascend 低语料环境引入多层 domain knowledge，并根据 generation / evolution 阶段动态调整 Agent interaction mode，在候选探索与性能收敛之间切换。

它体现了 Ascend Kernel Agent 的一个关键方向：先补齐平台知识与可行性，再进行长程性能搜索。

## Sources

- https://arxiv.org/abs/2607.26661
