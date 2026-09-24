---
type: concept
name: Context Parallelism
aliases:
  - CP
  - Context Parallel
  - 上下文并行
domain: inference
topic: parallelism
parent_concepts:
  - Parallelism
related_concepts:
  - Sequence Parallelism
  - Tensor Parallelism
  - P-D Disaggregation
projects:
  - vLLM
last_verified: 2026-09
---

# Context Parallelism

## 一句话定义

Context Parallelism（CP）沿 sequence / context 维把长上下文的输入、activation、attention 或 KV 相关工作跨多个 rank 分片，让单个请求的 context 不再完全落在一个设备上。

## 解决的问题

超长上下文会同时放大 attention 计算和 KV/activation 内存。即使模型权重已经通过 [[Tensor Parallelism]] 切分，单请求 context 仍可能成为容量或带宽瓶颈。

## 核心机制

不同系统的 CP 实现并不完全相同。共同点是把 sequence/context token 分给多个 rank，并通过 P2P、AllGather、All-to-All 或 ring-style attention communication 交换计算 attention 所需的信息。

vLLM 当前进一步区分：

- Prefill Context Parallel（PCP）：主要服务长 prompt prefill。
- Decode Context Parallel（DCP）：把 decode 阶段的 context/KV 工作跨 ranks 分片。

## 与 Sequence Parallelism 的区别

[[Sequence Parallelism]] 的经典定义主要切 LayerNorm/Dropout 等 TP 周边 activation；CP 则覆盖更完整的 context/attention 计算和状态，因此更直接面向长序列扩展。

## 代价与适用边界

CP 能降低单 rank 的 context 内存压力，但 attention 需要跨 rank 获取足够信息，因此通信模式和互联带宽非常关键。短上下文下，额外通信可能得不偿失。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 当前 ParallelConfig 暴露 `prefill_context_parallel_size` 与 `decode_context_parallel_size`，并有独立 Context Parallel Deployment 文档。

## Sources

- https://docs.vllm.ai/en/latest/serving/context_parallel_deployment/
- https://docs.vllm.ai/en/latest/api/vllm/config/parallel/
- https://docs.nvidia.com/megatron-core/developer-guide/latest/api-guide/context_parallel.html
