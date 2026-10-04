---
type: project
name: "K-Search"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/caoshiyi/K-Search
docs: https://sky.cs.berkeley.edu/project/k-search/
organization: "UC Berkeley"
areas: ["agentic-kernel-optimization", "world-model", "tree-search", "cuda", "flashinfer", "kernelbench", "evidence-driven-search"]
hardware: ["nvidia", "apple-silicon"]
last_verified: "2026-10"
linked_companies: []
code_availability: public
---

# K-Search

K-Search 是 UC Berkeley Sky Computing Lab 公开的自动化高性能 GPU kernel generation 系统，由 Shiyi Cao、Ziming Mao、Joseph E. Gonzalez、Ion Stoica 等研究者开发。

## 核心机制

它维护一个 **co-evolving intrinsic world model**：不是只保留当前最好代码，而是维护关于 bottleneck、设计替代、优化策略和实验结果的结构化搜索树。

这种把“性能世界模型”与“具体 kernel 候选”分离的设计，使优化策略可以跨越暂时失败或暂时变慢的中间实现。

## Sources

- https://sky.cs.berkeley.edu/project/k-search/
- https://github.com/caoshiyi/K-Search
- https://arxiv.org/abs/2602.19128

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
