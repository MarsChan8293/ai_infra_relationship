---
type: concept
name: AllReduce
aliases:
  - All-Reduce
  - 全归约
domain: communication
topic: collective-communication
parent_concepts:
  - Collective Communication
related_concepts:
  - ReduceScatter
  - Data Parallelism
  - Tensor Parallelism
projects:
  - NCCL
  - RCCL
  - FlagCX
  - VCCL
last_verified: 2026-09
---

# AllReduce

## 一句话定义

AllReduce 把所有 rank 的输入按 sum/max/min 等操作做 reduction，并把相同的最终结果返回给每一个 rank。

## 解决的问题

多个 device 各自计算局部结果后，经常需要让所有参与者得到一致的聚合结果。最典型场景是 Data Parallel 梯度同步，也常出现在 Tensor Parallel 的部分算子输出同步中。

## 核心机制

逻辑语义可以理解为 Reduce + Broadcast，但高性能库通常不会真的分两步执行，而是使用 ring、tree、hierarchical、NVLink/NVSwitch 等拓扑优化算法。

对于 sum AllReduce：

`out = x_0 + x_1 + ... + x_(N-1)`

每个 rank 最终都得到同一个 `out`。

## 与 ReduceScatter 的关系

[[ReduceScatter]] 只把 reduction 后的不同分片留在不同 rank；随后再做 [[AllGather]]，在语义上可以组成 AllReduce。现代分布式框架常利用这种拆分减少峰值内存或实现更细粒度通信。

## 并行关系

- [[Data Parallelism]]：梯度同步的经典通信原语。
- [[Tensor Parallelism]]：某些 row-parallel / partial result 路径需要跨 rank reduction。
- 与 MoE [[Expert Parallelism]] 更典型的 [[All-to-All]] 不同，AllReduce 不负责 token 重分布。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]]、[[community/ROCm/RCCL/RCCL|RCCL]]、[[community/flagos-ai/FlagCX/FlagCX|FlagCX]]、[[community/sii-research/VCCL/VCCL|VCCL]] 都提供 AllReduce 或兼容的 collective abstraction。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
- https://rocm.docs.amd.com/projects/rccl/en/latest/what-is-rccl.html
- https://github.com/flagos-ai/FlagCX
- https://vccl-doc.readthedocs.io/en/latest/
