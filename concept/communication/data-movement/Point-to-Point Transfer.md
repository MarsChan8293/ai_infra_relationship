---
type: concept
name: Point-to-Point Transfer
aliases:
  - P2P Transfer
  - Point-to-Point Communication
  - P2P Data Movement
  - 点到点传输
domain: communication
topic: data-movement
parent_concepts:
  - Data Movement
related_concepts:
  - RDMA
  - KV Cache Transfer
  - Collective Communication
projects:
  - NIXL
  - Mooncake
  - MemFabric
  - UCX
  - NCCL
  - RCCL
last_verified: 2026-09
---

# Point-to-Point Transfer

## 一句话定义

Point-to-Point Transfer 是一个明确源端向一个明确目标端直接发送或读取数据的通信模式。

## 解决的问题

KV handoff、权重更新、远端内存读写和 pipeline stage 之间的数据传递通常不是“所有 rank 一起做同一件事”，而是 producer 与 consumer 之间的定向数据搬运。

## 核心机制

P2P 路径通常以 send/recv 或 read/write 表达。高性能系统会进一步引入内存注册、remote descriptor、异步 completion、zero-copy、多 NIC striping 和拓扑感知。

## 与 Collective Communication 的区别

[[Collective Communication]] 要求一组 rank 共同参与，并具有 AllReduce / AllGather 等固定语义；P2P 更灵活，适合不规则或按需的数据流。很多 collective 底层最终也由一系列 P2P 传输组成，但上层语义不同。

## 与 KV Transfer 的关系

[[KV Cache Transfer]] 是 P2P transfer 的典型 serving 场景。P/D 分离时 Prefill worker 是 KV producer，Decode worker 是 consumer。

## 项目实现

[[community/ai-dynamo/NIXL/NIXL|NIXL]]、[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]、[[community/Ascend/MemFabric/MemFabric|MemFabric]] 和 [[community/OpenUCX/UCX/UCX|UCX]] 都提供通用 P2P 数据路径；[[community/NVIDIA/NCCL/NCCL|NCCL]] 与 [[community/ROCm/RCCL/RCCL|RCCL]] 也提供 GPU rank 间 send/recv。

## Sources

- https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md
- https://kvcache-ai.github.io/Mooncake/design/transfer-engine/
- https://openucx.readthedocs.io/en/master/
- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/p2p.html
- https://rocm.docs.amd.com/projects/rccl/en/latest/what-is-rccl.html
