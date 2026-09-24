---
type: concept
name: Attention Kernel
aliases:
  - Attention Operator Kernel
  - 注意力算子
  - Attention算子
domain: kernel
topic: attention
related_concepts:
  - FlashAttention
  - PagedAttention
  - Kernel Fusion
projects:
  - FlashInfer
  - FlashAttention
  - FlagAttention
  - vLLM
last_verified: 2026-09
---

# Attention Kernel

## 一句话定义

Attention Kernel 是把 Q/K/V 读取、score 计算、mask、softmax、value 聚合等 attention 数据流映射到 GPU/NPU 执行单元的高性能算子实现。

## 解决的问题

Attention 的数学公式很短，但实际执行会频繁访问 HBM、shared memory / SRAM，并在不同序列长度、head layout、KV cache layout 和硬件架构下呈现完全不同的性能瓶颈。高性能 serving 因此需要专门设计 attention kernel，而不是仅依赖通用算子拼接。

## 核心优化维度

- **IO / memory traffic**：减少中间矩阵写回 HBM。
- **Tiling**：把 Q/K/V 和 partial result 分块放入片上存储。
- **KV layout**：适配 contiguous、paged、MLA 等 cache layout。
- **Work partition**：在 thread block / warp / SM 之间合理切分。
- **Fusion**：把 mask、softmax、RoPE、scale 等操作尽量融入一次 kernel。
- **Prefill vs Decode**：两阶段的 query length、算术强度和 KV 访问模式不同，常需要不同 kernel。

## 主要细分

- [[FlashAttention]]：以 IO-aware tiling 避免显式 materialize 完整 attention matrix。
- [[PagedAttention]]：直接在分页/分块 KV cache 上执行 attention，重点解决 serving 中非连续 KV 布局。

两者可以同时出现：一个系统可以在 paged KV layout 上调用 FlashAttention family 或其他优化 backend。

## 项目实现

[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 提供面向 Prefill/Decode、paged KV、MLA 等多类 attention kernel；[[community/Dao-AILab/FlashAttention/FlashAttention|FlashAttention]] 是 IO-aware exact attention 的代表实现；[[community/flagos-ai/FlagAttention/FlagAttention|FlagAttention]] 专注异构 attention kernel；[[community/vllm-project/vLLM/vLLM|vLLM]] 内置并集成多种 optimized attention backend。

## Sources

- https://docs.flashinfer.ai/api/attention.html
- https://github.com/Dao-AILab/flash-attention
- https://github.com/flagos-ai/FlagAttention
- https://docs.vllm.ai/en/stable/
