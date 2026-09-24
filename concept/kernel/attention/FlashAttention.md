---
type: concept
name: FlashAttention
aliases:
  - Flash Attention
  - IO-Aware Attention
domain: kernel
topic: attention
parent_concepts:
  - Attention Kernel
related_concepts:
  - Kernel Fusion
projects:
  - FlashAttention
  - FlashInfer
  - vLLM
last_verified: 2026-09
---

# FlashAttention

## 一句话定义

FlashAttention 是一种 IO-aware exact attention 算法与 kernel 设计，通过 tile 化和在线 softmax 在片上存储中完成 attention block，避免把完整 N×N attention matrix 写回 HBM。

## 解决的问题

标准 attention 若按 GEMM → softmax → GEMM 的方式分成多个 kernel，会生成巨大的中间 score matrix，并在 HBM 与片上存储之间反复搬运。长序列时，内存 IO 往往比纯算术更昂贵。

## 核心机制

FlashAttention 将 Q/K/V 分块加载到 SRAM/shared memory，按 block 计算局部 score，并维护在线 softmax 所需的 running max / normalization state。每个 block 的结果直接累积到输出，不 materialize 完整 attention matrix。

因此它的核心不是“近似 attention”，而是重新安排 exact attention 的计算顺序和 IO。

## 与 PagedAttention 的区别

[[PagedAttention]] 关注 KV cache 的物理分页与非连续寻址；FlashAttention 关注 attention 数学计算的 IO-aware tiling。Paged KV cache 可以由支持该 layout 的 FlashAttention/FlashInfer 等 backend 消费，两者不是替代关系。

## 代价与适用边界

kernel 性能取决于 head dimension、sequence length、causal/mask、GPU generation 和 tile 配置。Prefill 与 Decode 的 shape 差异很大，因此同一套 FlashAttention kernel 并不总是所有 serving 场景的最优实现。

## 项目实现

[[community/Dao-AILab/FlashAttention/FlashAttention|FlashAttention]] 是官方算法实现；[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 的 attention backend 可调用/适配 FA2/FA3 等路径；[[community/vllm-project/vLLM/vLLM|vLLM]] 当前支持 FlashAttention 等 optimized attention kernels。

## Sources

- https://github.com/Dao-AILab/flash-attention
- https://docs.flashinfer.ai/api/attention.html
- https://docs.vllm.ai/en/stable/
