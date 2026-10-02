---
type: project
name: "CAKE"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
  - "concept/compiler/Kernel Compiler Pipeline"
layer: "agent-compiler-kernel-optimization"
status: research
docs: https://arxiv.org/abs/2608.12629
areas:
  - "agentic-kernel-optimization"
  - "compiler-agent-co-design"
  - "gpu-kernel"
  - "intermediate-representation"
  - "verification"
  - "cost-model"
  - "performance-engineering"
hardware:
  - "nvidia"
last_verified: "2026-10"
linked_companies: []
---

# CAKE

CAKE（Compiler-Agent Co-Design for Frontier Kernel Evolution）是 2026 年公开的 GPU kernel agent 研究系统。它的核心不是让 Agent 把 compiler 当成固定黑盒，而是让 **Agent 与 compiler abstraction / verifier / cost model / diagnostics 一起演化**。

## 核心机制

CAKE 让 Agent 生成 CAKE IR。该 IR 显式表达 warp role、memory movement、synchronization 与 pipeline，并由 compiler 提供：

- type / legality verification；
- localized diagnostics；
- cost modeling；
- backend lowering；
- 从重复失败中沉淀的新 verifier rule、IR primitive 和 optimization tactic。

这使 compiler 本身成为 Agent 的结构化 observation 与 action interface，而不只是“编译成功/失败”的终点。

## 与 Agentic Kernel Optimization 的关系

CAKE 是 [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]] 的代表性 compiler-agent co-design 路线：Agent 负责搜索和生成，compiler 提供可验证、硬件显式的搜索空间与反馈。

论文报告在 NVIDIA B200 上，Flash-KMeans 的最佳 CAKE IR candidate 达到 tuned FlashML baseline 的 1.144×；Agent 生成的 Kimi Delta Attention 相对官方 FlashKDA 达到 2.05× geometric-mean speedup；KNN/KMeans 在 400+ shapes 上报告 1.42×–2.12× 改进。

## 开源状态

截至 2026-10，本图谱未确认 CAKE 有独立官方开源仓库，因此记录为 **research system**，不把第三方复现或论文笔记当作 canonical implementation。

## Sources

- https://arxiv.org/abs/2608.12629

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]
- [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]]

<!-- END AUTO PROJECT CONCEPTS -->
