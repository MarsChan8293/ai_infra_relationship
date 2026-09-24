---
type: concept
name: ReduceScatter
aliases:
  - Reduce-Scatter
  - 归约分散
domain: communication
topic: collective-communication
parent_concepts:
  - Collective Communication
related_concepts:
  - AllReduce
  - AllGather
  - Sequence Parallelism
projects:
  - NCCL
  - RCCL
  - VCCL
last_verified: 2026-09
---

# ReduceScatter

## 一句话定义

ReduceScatter 先跨 rank 对输入执行 reduction，再把 reduction 结果切成不同分片分发给各 rank。

## 解决的问题

如果后续计算只需要结果的一部分，就没有必要像 [[AllReduce]] 那样让所有 rank 都保留完整聚合结果。ReduceScatter 可以降低每个 rank 的输出体积，并与后续分片计算自然衔接。

## 核心机制

可以把它理解成：

1. 所有 rank 对对应位置做 reduce。
2. 完整 reduction 结果按 rank 切分。
3. rank i 只得到第 i 个分片。

[[ReduceScatter]] + [[AllGather]] 在语义上可以组成 AllReduce。

## 并行关系

在 [[Sequence Parallelism]]、FSDP/ZeRO 类训练以及一些 Tensor Parallel execution 中，ReduceScatter 常用于把聚合结果直接留在分片形态，避免每个 rank 保存完整 tensor。

## 与 All-to-All 的区别

ReduceScatter 的目标分片来自一个全局 reduction 结果；[[All-to-All]] 不做 reduction，每个源 rank 可以给不同目标发送不同数据块。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]]、[[community/ROCm/RCCL/RCCL|RCCL]] 和 [[community/sii-research/VCCL/VCCL|VCCL]] 明确提供 ReduceScatter。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
- https://rocm.docs.amd.com/projects/rccl/en/latest/what-is-rccl.html
- https://vccl-doc.readthedocs.io/en/latest/
