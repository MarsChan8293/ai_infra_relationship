---
type: concept
name: Sequence Parallelism
aliases:
  - SP
  - Sequence Parallel
  - 序列并行
domain: inference
topic: parallelism
parent_concepts:
  - Parallelism
related_concepts:
  - Tensor Parallelism
  - Context Parallelism
last_verified: 2026-09
---

# Sequence Parallelism

## 一句话定义

经典 Sequence Parallelism（SP）是在已有 Tensor Parallelism 基础上，把原本在 TP ranks 上复制的部分 activation 沿 sequence 维进一步切分，以减少 activation memory 和重复计算。

## 解决的问题

Tensor Parallelism 虽然切了大矩阵权重，但 LayerNorm、Dropout 等某些算子的 activation 仍可能在各 TP rank 上复制。SP 通过 sequence 维 sharding 降低这部分内存。

## 核心机制

在经典 Megatron-style SP 中，sequence dimension 主要用于分片 LayerNorm / Dropout 一类 activation，并与 TP 的 ReduceScatter / AllGather 配合。它并不意味着整个 attention context、KV state 和全部层 activation 都按 sequence 维完全分布。

## 与 Context Parallelism 的区别

[[Context Parallelism]] 是更完整的长上下文并行：输入及更广泛的网络 activation / attention context 沿 sequence 维跨 rank 分片，并需要专门的 attention communication。SP 则是 TP 周边的局部 activation sharding。

因此不能把所有“沿 sequence 维切分”的方案都统一写成 SP。

## 代价与适用边界

SP 通常依赖 TP 通信布局，主要价值是降低 activation memory。对于推理中超长 context 的 attention/KV 分片问题，[[Context Parallelism]] 更直接。

## Sources

- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
- https://docs.nvidia.com/megatron-core/developer-guide/latest/api-guide/context_parallel.html
