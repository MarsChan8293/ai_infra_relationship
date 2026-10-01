---
type: project
name: "K-Search"
linked_people: []
layer: optimization
status: active
repository: https://github.com/caoshiyi/K-Search
docs: https://sky.cs.berkeley.edu/project/k-search/
organization: "UC Berkeley"
areas: ["agentic-kernel-optimization", "world-model", "tree-search", "cuda", "flashinfer", "kernelbench", "evidence-driven-search"]
hardware: ["nvidia", "apple-silicon"]
last_verified: "2026-10"
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
