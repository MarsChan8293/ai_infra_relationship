---
type: concept
name: RDMA
aliases:
  - Remote Direct Memory Access
  - 远程直接内存访问
domain: communication
topic: data-movement
parent_concepts:
  - Point-to-Point Transfer
related_concepts:
  - GPUDirect RDMA
projects:
  - NIXL
  - Mooncake
  - MemFabric
  - UCX
  - RCCL
  - DeepEP
last_verified: 2026-09
---

# RDMA

## 一句话定义

RDMA（Remote Direct Memory Access）允许节点通过支持 RDMA 的网络直接访问远端已注册内存，减少传统 socket 路径中的 CPU 参与和额外数据拷贝。

## 解决的问题

跨节点搬运大块 KV、权重或中间状态时，CPU copy、kernel/network stack 和内存中转会消耗额外延迟与带宽。RDMA 让 NIC 更直接地在注册内存区域之间传输数据。

## 核心机制

典型流程包括 memory registration、交换 remote key/address、提交 read/write/send 操作、NIC 执行 DMA、completion queue 通知完成。InfiniBand 和 RoCE 是常见网络承载。

## 与 GPUDirect RDMA 的区别

普通 RDMA 的目标可以是 host DRAM；[[GPUDirect RDMA]] 进一步让支持的 NIC 直接访问 GPU memory，减少 GPU↔CPU staging。

## 适用边界

RDMA 并不自动等于低延迟。性能仍受 NIC/PCIe 拓扑、NUMA、message size、多 NIC 调度、拥塞和内存注册成本影响。

## 项目实现

[[community/ai-dynamo/NIXL/NIXL|NIXL]] 可通过 UCX 等 backend 使用 RoCE/InfiniBand；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Transfer Engine 原生支持 RDMA；[[community/Ascend/MemFabric/MemFabric|MemFabric]] 覆盖 Ascend Device RoCE/相关直接数据路径；[[community/OpenUCX/UCX/UCX|UCX]] 是通用 RDMA transport abstraction；[[community/ROCm/RCCL/RCCL|RCCL]] 支持 InfiniBand/RoCE 跨节点 collective；[[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] 的跨节点 EP 路径针对 RDMA/低延迟通信优化。

## Sources

- https://github.com/ai-dynamo/nixl/blob/main/docs/doxygen/nixl_doxygen.md
- https://kvcache-ai.github.io/Mooncake/getting_started/supported-protocols.html
- https://gitcode.com/Ascend/memfabric_hybrid
- https://openucx.readthedocs.io/en/master/
- https://rocm.docs.amd.com/projects/rccl/en/latest/what-is-rccl.html
- https://github.com/deepseek-ai/DeepEP
