---
type: project
name: TileLang-MLIR-Ascend
linked_concepts:
  - "concept/kernel/attention/Attention Kernel"
  - "concept/compiler/Backend Code Generation"
  - "concept/compiler/Compiler Lowering"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/programming/Kernel DSL"
status: active
linked_people: []
repository: https://github.com/tile-ai/tilelang-mlir-ascend
docs: https://github.com/tile-ai/tilelang-mlir-ascend
last_verified: "2026-10"
companies: []
layer: compiler
areas: [kernel-dsl, mlir, ascendnpu-ir, ascend, ascend-a2, ascend-a3, gemm, attention-kernels, deepseek-v4]
hardware: [ascend]
integrations: [TileLang, CANN]
linked_companies: []
---
# TileLang-MLIR-Ascend

## 项目简介
TileLang-MLIR-Ascend 是 Tile-AI 的 **MLIR-based TileLang Ascend Adapter**。它把 TileLang DSL 通过 AscendNPU IR / MLIR 路线 lowering 到 Ascend NPU 执行栈，目标是在保留 TileLang 开发体验的同时提供面向昇腾的高性能 code generation。

## 技术路线
核心链路为 `TileLang DSL → MLIR / AscendNPU IR → Ascend codegen/runtime → Ascend NPU`。官方说明已经从早期 string-based compilation 迁移到 MLIR API，并支持与开源 AscendNPU-IR 一体化编译；运行环境依赖 Ascend Toolkit / CANN 与 `torch_npu`。

## 已公开算子与性能证据
官方 README 的 developer-mode 示例覆盖 GEMM / Batch GEMM、vector operators、DeepSeek V4 mHC、Flash Attention，以及 AscendNPU IR vector-add / GEMM quick start。README 中与手写 AscendC 的性能对照属于特定 shape / toolkit / device 条件下的实现成熟度证据，不泛化成所有 workload 的统一结论。

## 硬件边界
官方说明已在 Huawei Ascend A2/A3 上测试验证。TileLang 主仓 2026-09-30 新增的 Ascend 950 backend 是另一条内置 supported backend；两者共享 TileLang 语义与生态，但硬件目标、编译实现和发布节奏不同。

## DeepSeek V4 关系
仓库公开 DeepSeek V4 mHC 等示例，因此在图谱中连接到 DeepSeek V4 kernel/compiler 热路径；但该项目属于 Tile-AI 的 Ascend adapter 项目，不因示例内容而归属 DeepSeek。

## 图谱关系
[[community/tile-ai/TileLang/TileLang|TileLang]] · [[community/tile-ai/TileLang/TileLang-Ascend|TileLang-Ascend]] · [[community/Ascend/Ascend/Ascend|Ascend]] · [[community/Ascend/CANN/CANN|CANN]] · [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM-Ascend|DeepGEMM-Ascend]]

## Sources
- https://github.com/tile-ai/tilelang-mlir-ascend
- https://github.com/tile-ai/tilelang-mlir-ascend/blob/main/README.md
- https://github.com/tile-ai/tilelang

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/attention/Attention Kernel|Attention Kernel]]
- [[concept/compiler/Backend Code Generation|Backend Code Generation]]
- [[concept/compiler/Compiler Lowering|Compiler Lowering]]
- [[concept/kernel/gemm/GEMM|GEMM]]
- [[concept/kernel/programming/Kernel DSL|Kernel DSL]]

<!-- END AUTO PROJECT CONCEPTS -->
