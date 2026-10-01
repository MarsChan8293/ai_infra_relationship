---
type: project
name: "AscendOptimizer"
linked_people: []
layer: optimization
status: research
docs: https://arxiv.org/abs/2603.23566
areas: ["agentic-kernel-optimization", "ascendc", "episodic-memory", "profiling-in-the-loop", "evolutionary-search", "host-tiling", "kernel-rewriting"]
hardware: ["ascend"]
last_verified: "2026-10"
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
