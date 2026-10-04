---
type: project
name: "AscendOptimizer"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: unknown
maturity: research-prototype
docs: https://arxiv.org/abs/2603.23566
areas: ["agentic-kernel-optimization", "ascendc", "episodic-memory", "profiling-in-the-loop", "evolutionary-search", "host-tiling", "kernel-rewriting"]
hardware: ["ascend"]
last_verified: "2026-10"
linked_companies: []
code_availability: unconfirmed
---

# AscendOptimizer

AscendOptimizer 是面向 AscendC operator optimization 的 episodic agent research system。公开论文作者来自华东师范大学、同济大学等研究机构。

## 核心机制

Ascend 的优化对象是 host-side tiling 与 device-side kernel 的耦合系统。AscendOptimizer 因此把优化拆成两条互相迭代的路径：

- host：profiling-in-the-loop evolutionary search，探索 tiling 与 data movement；
- kernel：从优化轨迹中提炼可迁移 optimization motifs，构建 experience bank 后指导 rewriting。

这类“双工件闭环”是 Ascend Agent 与 CUDA Agent 的重要差异。

## Sources

- https://arxiv.org/abs/2603.23566

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
