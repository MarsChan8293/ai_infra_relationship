---
type: project
name: "Astra"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: unknown
maturity: research-prototype
repository: https://github.com/Anjiang-Wei/Astra
organization: "Stanford University"
areas: ["agentic-kernel-optimization", "multi-agent", "cuda", "sglang", "profiling", "planning", "serving-kernel"]
hardware: ["nvidia"]
last_verified: "2026-10"
linked_companies: []
code_availability: public
---

# Astra

Astra 是面向已有 CUDA kernel 的多 Agent 性能优化系统。与从 PyTorch specification 重新生成 kernel 的路线不同，Astra 直接从 SGLang 中已有 CUDA 实现出发，让专门化 Agent 通过 generation、testing、profiling 和 planning 迭代优化。

## 图谱价值

它特别贴近 inference-engine-native kernel optimization：优化对象不是随机 microbenchmark，而是 LLM serving 框架中的真实 kernel。

公开论文作者网络连接 Stanford、上海交通大学与南京大学；本节点仅记录公开项目和论文事实，不把所有作者自动视为仓库 maintainer。

## Sources

- https://github.com/Anjiang-Wei/Astra
- https://arxiv.org/abs/2509.07506

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
