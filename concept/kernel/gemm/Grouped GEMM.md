---
type: concept
name: Grouped GEMM
aliases:
  - Grouped Matrix Multiplication
  - Grouped Matmul
  - 分组矩阵乘
domain: kernel
topic: gemm
parent_concepts:
  - GEMM
related_concepts:
  - Expert Parallelism
  - All-to-All
  - Kernel Fusion
projects:
  - DeepGEMM
  - FlashInfer
  - CUTLASS
last_verified: 2026-09
---

# Grouped GEMM

## 一句话定义

Grouped GEMM 把一组彼此独立、shape 可以不同的矩阵乘问题组织成一次或少量 kernel 调度完成，典型用于 MoE 中多个 expert 的小批量矩阵乘。

## 解决的问题

[[Expert Parallelism]] 下，每个 expert 实际收到的 token 数通常不同。若为每个 expert 单独 launch GEMM，会产生大量小 kernel、低 tensor-core 利用率和 launch overhead。Grouped GEMM 将多个 expert 的计算聚合，让 GPU 以更高吞吐执行。

## 核心机制

一组 GEMM 共享某些维度或数据类型，但每个 group 可以有不同的 M / offset / valid-token count。运行时通过 offsets、group descriptors 或 mask 告诉 kernel 每个子问题的边界，再由一个统一调度器把 tiles 分配给 thread blocks / SM。

MoE 推理常见两种布局：

- **Contiguous layout**：不同 expert 的 token 按 expert 连续拼接，使用 offsets 描述边界。
- **Masked layout**：为 CUDA Graph / decode 等固定 shape 场景保留最大空间，用 mask 表示每个 expert 实际有效 token 数。

## 与普通 GEMM 的区别

[[GEMM]] 描述一个矩阵乘问题；Grouped GEMM 描述多个独立 GEMM 的联合调度。它不是 batch matmul 的简单同义词，因为各 group 的有效尺寸、权重和 token 数往往不同。

## 与 MoE 通信的关系

[[All-to-All]] / DeepEP 先完成 token dispatch，Grouped GEMM 再在本地 expert 上执行计算；combine 前后还可能继续存在通信。因此 EP 性能通常由通信和 Grouped GEMM 两端共同决定。

## 项目实现

[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 提供 contiguous / masked grouped GEMM，并针对 MoE Prefill 与 Decode 分别优化；[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 提供 serving/MoE grouped GEMM 路径；[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]] 提供 Grouped GEMM kernel 与 Operator API。

## Sources

- https://github.com/deepseek-ai/DeepGEMM
- https://docs.flashinfer.ai/
- https://docs.nvidia.com/cutlass/latest/media/docs/operators/tutorials/005_grouped_gemm_contiguous_offset.html
