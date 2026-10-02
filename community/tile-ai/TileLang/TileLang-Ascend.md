---
type: project
name: TileLang-Ascend
status: active
repository: https://github.com/tile-ai/tilelang-ascend
docs: https://github.com/tile-ai/tilelang-ascend/blob/ascendc_pto/docs/TileLang-Ascend%20Programming%20Guide.md
last_verified: "2026-10"
companies: []
layer: compiler
areas: [kernel-dsl, ascend, ascend-a2, ascend-a3, ascendc, pto, npuir, gemm, attention-kernels, sparse-attention]
hardware: [ascend]
integrations: [TileLang, CANN]
linked_concepts:
  - "concept/compiler/Backend Code Generation"
  - "concept/compiler/Compiler Lowering"
  - "concept/kernel/programming/Kernel DSL"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/attention/Attention Kernel"
  - "concept/kernel/attention/Sparse Attention"
---
# TileLang-Ascend

## 项目简介
TileLang-Ascend 是 Tile-AI 面向 Huawei Ascend NPU 的专用 TileLang adapter。它延续 TileLang 的 Pythonic DSL / TVM compiler 基础设施，但把 memory hierarchy、Cube/Vector execution、同步、code generation 与 runtime 接入适配到昇腾硬件。

官方 TileLang 主 README 将其列为 Ascend A2/A3 的 ecosystem backend，而不是 TileLang 主仓 Ascend 950 backend 的同义名称。

## 两条后端技术路线
官方仓库同时维护 **Ascend C & PTO** 与 **AscendNPU IR** 两条技术路线。默认分支为 `ascendc_pto`；PTO 在 2026-01-23 成为新的 code-generation target。NPU IR 路线则通过 AscendNPU IR / MLIR 体系承担 lowering 与 compilation。

## 关键能力
截至 2026-10，官方公开能力包括 GEMM / Batch GEMM、Flash Attention / Sparse Flash Attention、dispatch & combine、Lightning Indexer / TopK Selector、`T.Pipelined`、`T.Parallel` automatic vectorization、automatic synchronization insertion、automatic buffer reuse、shared-memory put/get、PyTorch / `torch_npu` 集成与 ACLGraph 示例。

## 硬件与软件边界
- 官方明确 tested / validated devices：Ascend A2、A3。
- 环境依赖 CANN（README 当前给出至少 8.3.RC1）和 `torch_npu`（至少 2.6.0.RC1）。
- TileLang 主仓的 Ascend 950 是另一条正式 supported backend，使用 `target="ascend"`，不能把 A2/A3 结论直接外推到 950。

## DeepSeek 热路径
仓库公开 DeepSeek V4 kernels，并包含 Sparse Flash Attention、Lightning Indexer、TopK Selector、dispatch/combine 等与 DeepSeek V4 sparse-attention / MoE 热路径高度相关的实现。这是 kernel/compiler 生态关系，不等同于 DeepSeek 对该项目的治理归属。

## 图谱关系
[[community/tile-ai/TileLang/TileLang|TileLang]] · [[community/tile-ai/TileLang/TileLang-MLIR-Ascend|TileLang-MLIR-Ascend]] · [[community/Ascend/Ascend/Ascend|Ascend]] · [[community/Ascend/CANN/CANN|CANN]] · [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM-Ascend|DeepGEMM-Ascend]] · [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] · [[community/deepseek-ai/DeepSeek-Infra/DeepSelect|DeepSelect]]

## Sources
- https://github.com/tile-ai/tilelang-ascend
- https://github.com/tile-ai/tilelang-ascend/blob/ascendc_pto/README.md
- https://github.com/tile-ai/tilelang
