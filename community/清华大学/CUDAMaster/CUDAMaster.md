---
type: project
name: "CUDAMaster"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: unknown
maturity: research-prototype
docs: https://hanyx2021.github.io/MSKernelBenchDemo/
organization: "清华大学"
areas: ["agentic-kernel-optimization", "multi-agent", "cuda", "hardware-aware", "profiling", "toolchain-generation", "mskernelbench"]
hardware: ["nvidia"]
last_verified: "2026-10"
linked_companies: []
code_availability: unconfirmed
---

# CUDAMaster

CUDAMaster 是清华大学研究团队公开的 multi-agent、hardware-aware CUDA kernel optimization 系统，并与 MSKernelBench 一起用于多场景 kernel 优化评估。

## 核心机制

系统利用 profiling 信息进行硬件感知优化，并自动构建完整 compilation / execution toolchain。研究范围覆盖常见 LLM kernel，也覆盖 sparse matrix 与 scientific computing 等场景。

当前公开证据以论文与 demo 为主，因此本节点按 research project 记录，不把它描述成完整开源仓库。

## Sources

- https://arxiv.org/abs/2603.07169
- https://hanyx2021.github.io/MSKernelBenchDemo/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
