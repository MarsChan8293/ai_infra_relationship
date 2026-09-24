---
type: concept
name: Collective Communication
aliases:
  - Collective Operations
  - Communication Collectives
  - 集合通信
domain: communication
topic: collective-communication
related_concepts:
  - AllReduce
  - AllGather
  - ReduceScatter
  - All-to-All
  - Point-to-Point Transfer
projects:
  - NCCL
  - RCCL
  - FlagCX
  - VCCL
  - DeepEP
last_verified: 2026-09
---

# Collective Communication

## 一句话定义

Collective Communication 是一组 rank 按预定义语义共同参与的数据交换操作，例如 AllReduce、AllGather、ReduceScatter 和 All-to-All。

## 解决的问题

Tensor/Data/Expert Parallel 等并行方式会把模型状态或计算切到多个 device。每轮执行后，rank 之间需要同步、聚合或重分布数据，如果每个框架都手写 P2P 通信，性能和正确性都很难维护。

## 核心机制

collective library 接收 rank group、buffer 和 operation，依据 NVLink/xGMI/PCIe/IB/RoCE 等拓扑选择 ring、tree、hierarchical 或专用算法，并尽量让通信与计算重叠。

## 核心子概念

- [[AllReduce]]：所有 rank 得到相同 reduction 结果。
- [[AllGather]]：所有 rank 收集所有 rank 的分片。
- [[ReduceScatter]]：先 reduce，再把结果分片给不同 rank。
- [[All-to-All]]：每个 rank 向每个其他 rank 发送不同分片，MoE EP 中尤其关键。

## 与 P2P 的区别

[[Point-to-Point Transfer]] 只定义一对 source/destination；collective 具有 group-level 语义，所有参与 rank 的调用必须相互匹配。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]]、[[community/ROCm/RCCL/RCCL|RCCL]]、[[community/flagos-ai/FlagCX/FlagCX|FlagCX]]、[[community/sii-research/VCCL/VCCL|VCCL]] 是通用或异构 collective communication library；[[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] 则针对 MoE Expert Parallel 的 All-to-All / dispatch / combine 做专门优化。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
- https://rocm.docs.amd.com/projects/rccl/en/latest/what-is-rccl.html
- https://github.com/flagos-ai/FlagCX
- https://vccl-doc.readthedocs.io/en/latest/
- https://github.com/deepseek-ai/DeepEP
