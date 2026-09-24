---
type: concept
name: AllGather
aliases:
  - All-Gather
  - 全收集
domain: communication
topic: collective-communication
parent_concepts:
  - Collective Communication
related_concepts:
  - ReduceScatter
  - Tensor Parallelism
  - Sequence Parallelism
projects:
  - NCCL
  - RCCL
  - FlagCX
  - VCCL
last_verified: 2026-09
---

# AllGather

## 一句话定义

AllGather 把每个 rank 持有的数据分片收集起来，并让所有 rank 都得到按 rank 顺序拼接后的完整结果。

## 解决的问题

模型并行会让 tensor、sequence 或参数只存在于局部 rank。后续算子若需要完整 tensor，就必须把这些分片重新收集到每个参与 rank。

## 核心机制

假设 N 个 rank 分别持有 `x_0 ... x_(N-1)`，AllGather 后每个 rank 都得到：

`[x_0, x_1, ..., x_(N-1)]`

它只做收集和拼接，不执行 reduction。

## 与相邻 collective 的区别

- [[AllReduce]]：聚合后所有 rank 得到同一个 reduction 结果。
- [[ReduceScatter]]：聚合后每个 rank 只保留不同分片。
- [[All-to-All]]：每个 rank 为每个目标 rank 准备不同数据，通信模式更接近全互换。

## 并行关系

[[Tensor Parallelism]] 和 [[Sequence Parallelism]] 中经常需要在局部分片与完整 activation 之间切换，因此 AllGather 与 ReduceScatter 常成对出现。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]]、[[community/ROCm/RCCL/RCCL|RCCL]]、[[community/flagos-ai/FlagCX/FlagCX|FlagCX]]、[[community/sii-research/VCCL/VCCL|VCCL]] 均覆盖 AllGather 类 collective。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
- https://rocm.docs.amd.com/projects/rccl/en/latest/api-reference/api-library.html
- https://github.com/flagos-ai/FlagCX
- https://vccl-doc.readthedocs.io/en/latest/
