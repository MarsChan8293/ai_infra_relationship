---
type: concept
name: GEMM
aliases:
  - General Matrix Multiplication
  - Matrix Multiplication Kernel
  - 通用矩阵乘
domain: kernel
topic: gemm
related_concepts:
  - Grouped GEMM
  - Kernel Fusion
  - Kernel DSL
projects:
  - DeepGEMM
  - FlashInfer
  - TileLang
  - Triton
last_verified: 2026-09
---

# GEMM

## 一句话定义

GEMM（General Matrix Multiplication）是形如 C = A×B + C 的通用矩阵乘核心原语，是 Transformer 中 Linear、QKV projection、MLP 和 expert FFN 的主要计算热点。

## 解决的问题

大模型的大部分 dense FLOPs 最终落在矩阵乘。理论 FLOPs 相同并不代表实际速度相同，性能取决于 tensor core tile、数据类型、layout、memory hierarchy、pipeline、epilogue 和具体 M/N/K shape。

## 核心机制

高性能 GEMM 通常把矩阵切成 CTA/warp/tensor-core tiles，并在 global memory → shared memory → register / tensor core 之间建立 software pipeline。现代 kernel 还会融合 quantization scale、bias、activation 或其他 epilogue，减少额外 memory traffic。

## 推理场景的特殊性

- Prefill 常出现较大的 M，接近传统高吞吐 GEMM。
- Decode 的 M 往往很小，更容易被 launch / memory / shape inefficiency 限制。
- MoE 中多个 expert 产生许多不同 M 的小 GEMM，进一步引出 [[Grouped GEMM]]。

## 项目实现

[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 专注 FP8/FP4/BF16 GEMM 与 MoE kernel；[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 提供多精度 GEMM 与 grouped GEMM；[[community/tile-ai/TileLang/TileLang|TileLang]] 和 [[community/triton-lang/Triton/Triton|Triton]] 都提供编写/生成高性能 GEMM kernel 的 DSL/编译能力。

## Sources

- https://github.com/deepseek-ai/DeepGEMM
- https://docs.flashinfer.ai/
- https://tilelang.com/
- https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html
