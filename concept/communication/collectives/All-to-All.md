---
type: concept
name: All-to-All
aliases:
  - AllToAll
  - All-to-All Communication
  - 全互换通信
domain: communication
topic: collective-communication
parent_concepts:
  - Collective Communication
related_concepts:
  - Expert Parallelism
  - Point-to-Point Transfer
projects:
  - NCCL
  - RCCL
  - DeepEP
last_verified: 2026-09
---

# All-to-All

## 一句话定义

All-to-All 让每个 rank 都向每个其他 rank 发送一个目标专属的数据分片，并同时接收来自所有其他 rank 的分片。

## 解决的问题

MoE [[Expert Parallelism]] 中，token 根据 router 结果会被分配到不同 GPU 上的 expert。一个 rank 上的 token 可能要发往多个远端 rank，同时又要接收其他 rank 路由过来的 token，因此形成典型的 All-to-All 数据重分布。

## 核心机制

若有 N 个 rank，每个 rank 的 send buffer 通常被切成 N 段，第 j 段发送给 rank j；接收端则从所有源 rank 接收对应分片。与 AllGather 不同，每个目标 rank 得到的数据集合可以不同。

## MoE Dispatch / Combine

MoE 通常包含两个相反方向的数据流：

1. **Dispatch**：根据 expert routing 把 token 发送到 expert 所在 rank。
2. **Combine**：expert 计算结束后把输出送回 token 原始位置，并按权重合并。

[[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] 把这两条路径作为高吞吐/低延迟 All-to-All kernel 的核心对象，并支持通信与计算重叠。

## 性能边界

All-to-All 容易产生复杂的 many-to-many 流量，对跨节点 NIC 带宽、拥塞控制、拓扑和负载不均非常敏感。MoE expert imbalance 还会让通信量进一步偏斜。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]] 与 [[community/ROCm/RCCL/RCCL|RCCL]] 提供标准 All-to-All collective；[[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] 针对 MoE dispatch/combine 提供专用高性能 All-to-All 实现。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
- https://rocm.docs.amd.com/projects/rccl/en/latest/api-reference/api-library.html
- https://github.com/deepseek-ai/DeepEP
