---
type: project
name: Humming
linked_concepts:
  - "concept/inference/parallelism/Expert Parallelism"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/gemm/Grouped GEMM"
  - "concept/kernel/programming/JIT Kernel Compilation"
  - "concept/quantization/Weight-Only Quantization"
status: active
linked_people: []
repository: https://github.com/inclusionAI/humming
last_verified: "2026-10"
layer: kernel
areas: [gemm, quantization, moe-kernels, w4a16, w4a8, jit]
hardware: [nvidia]
integrations: [vLLM]
linked_companies: []
---
# Humming

Humming 是 inclusionAI 开源的 quantized GEMM / MoE kernel 项目，提供 INT4 weight 等低精度 GEMM 路径，并作为 vLLM 的 Humming backend 基础之一。

## 与 Chord 的关系

[[community/novitalabs/chord/chord|Chord]] 的 indexed W4A16 operator 明确基于 public Humming revision 继续开发。Chord 复用了 Humming 的 indexed routing contract 与兼容 import surface，但对 Kimi K2.x 的 H200 / Blackwell serving shape 增加了更专门的 schedule 和 kernel 优化。

因此二者不是简单“同类项目”关系，而是明确的源码演化关系：

**Humming → Chord indexed**

Chord 的 grouped SM90 路径则另有 [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 源码谱系。

## vLLM

Humming 已作为 quantized MoE/GEMM backend 与 [[community/vllm-project/vLLM/vLLM|vLLM]] 发生集成。Chord 选择兼容这一 backend interface，使其 indexed 路径能够复用既有的 vLLM integration surface。

## Sources

- https://github.com/inclusionAI/humming
- https://github.com/novitalabs/chord/blob/main/chord_kernels/operator/SOURCE.md
- https://github.com/novitalabs/chord/blob/main/docs/optimizations.md

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/parallelism/Expert Parallelism|Expert Parallelism]]
- [[concept/kernel/gemm/GEMM|GEMM]]
- [[concept/kernel/gemm/Grouped GEMM|Grouped GEMM]]
- [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]]
- [[concept/quantization/Weight-Only Quantization|Weight-Only Quantization]]

<!-- END AUTO PROJECT CONCEPTS -->
