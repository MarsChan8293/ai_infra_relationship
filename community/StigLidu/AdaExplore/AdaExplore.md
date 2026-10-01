---
type: project
name: "AdaExplore"
linked_people: []
layer: optimization
status: research
repository: https://github.com/StigLidu/AdaExplore
areas: ["agentic-kernel-optimization", "failure-memory", "tree-search", "triton", "self-improvement", "execution-feedback"]
hardware: ["nvidia"]
last_verified: "2026-10"
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
