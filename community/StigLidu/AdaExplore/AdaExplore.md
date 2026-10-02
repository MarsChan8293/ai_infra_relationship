---
type: project
name: "AdaExplore"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: research
repository: https://github.com/StigLidu/AdaExplore
areas: ["agentic-kernel-optimization", "failure-memory", "tree-search", "triton", "self-improvement", "execution-feedback"]
hardware: ["nvidia"]
last_verified: "2026-10"
linked_companies: []
---

# AdaExplore

AdaExplore 是面向性能 kernel generation 的 LLM Agent 框架，公开代码与论文重点研究两类机制：**failure-driven adaptation** 与 **diversity-preserving search**。

## 核心机制

- Adapt：从编译 / runtime failures 中提炼跨任务 validity rules，构建可复用 skill memory。
- Explore：将候选组织成树，在局部 refinement 与结构性 regeneration 之间切换，避免单链搜索过早陷入局部最优。

该项目适合作为 Agentic Kernel Optimization 中 **Failure Memory + Search Tree** 的参考。

## Sources

- https://github.com/StigLidu/AdaExplore
- https://arxiv.org/abs/2604.16625

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
