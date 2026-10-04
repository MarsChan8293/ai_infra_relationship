---
type: project
name: VeriTile
linked_people: []
linked_concepts:
  - "concept/kernel/programming/Kernel DSL"
  - "concept/kernel/verification/Kernel Formal Verification"
layer: compiler
status: active
repository: https://github.com/Lizn-zn/VeriTile
docs: https://lizn-zn.github.io/VeriTile/
areas:
  - "formal-verification"
  - "triton-style-dsl"
  - "kernel-correctness"
  - "kernel-refinement"
  - "lean4"
  - "proof-carrying-kernels"
last_verified: "2026-10"
linked_companies: []
code_availability: public
---
# VeriTile
## 项目定位

VeriTile 是用 Lean 4 对 Triton-style kernel 建模并做 correctness / refinement proof 的框架。它把 kernel 语言以 typed DSL 嵌入 Lean，并提供从数学规格到 kernel、以及 kernel-to-kernel refinement 的 theorem surface。

## 证明对象

- 单个 kernel 是否满足数学 output specification；
- 两个 kernel 是否在声明的 scratch region 之外产生等价 writes；
- 带抽象 rounding model 的 narrow-float 行为；
- memory view / launch composition 等可机器检查的语义条件。

因此它同时属于 [[concept/kernel/programming/Kernel DSL|Kernel DSL]] 和新建的 [[concept/kernel/verification/Kernel Formal Verification|Kernel Formal Verification]]。

## 与 Agentic Kernel Engineering 的关系

仓库提供 LLM proof wrapper 与 comparator gate，可以把“Agent 生成/修改 kernel”之后的 correctness 检查从纯测试提升到 theorem-backed validation。它与 [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]] 是互补关系，但 VeriTile 自身不是性能 optimizer。

## 明确边界

官方文档明确把 IEEE-754 精确语义、PTX/TMA、完整 concurrency 等 compute-to-algorithm gap 留给外部检查。形式化证明覆盖范围必须与真实 GPU 行为边界一起记录，不能把 Lean theorem 等价为“所有硬件执行细节已证明”。

## Sources

- https://github.com/Lizn-zn/VeriTile
- https://lizn-zn.github.io/VeriTile/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/programming/Kernel DSL|Kernel DSL]]
- [[concept/kernel/verification/Kernel Formal Verification|Kernel Formal Verification]]

<!-- END AUTO PROJECT CONCEPTS -->
