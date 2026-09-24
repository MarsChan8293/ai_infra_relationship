---
type: concept
name: GPUDirect RDMA
aliases:
  - GDR
  - GPU Direct RDMA
  - GPUDirect Remote Direct Memory Access
domain: communication
topic: data-movement
parent_concepts:
  - RDMA
related_concepts:
  - Data Movement
projects:
  - NIXL
  - Mooncake
last_verified: 2026-09
---

# GPUDirect RDMA

## 一句话定义

GPUDirect RDMA 是 NVIDIA 的 device-direct RDMA 路径，使支持的 NIC 可以直接读写 GPU memory，绕过常规 host staging copy。

## 解决的问题

普通跨机 GPU 数据流常见路径是 GPU → CPU DRAM → NIC → 网络 → CPU DRAM → GPU。对 KV、权重和 hidden states 这类大对象，中间 host copy 会增加 PCIe 流量、CPU 开销和延迟。

## 核心机制

GPU memory 被注册为可供 RDMA NIC 访问的 memory region，NIC DMA engine 直接在本地/远端 GPU memory 与网络之间传输。系统仍需处理 memory registration、拓扑、peer-memory 能力和 completion。

## 与通用 RDMA 的区别

[[RDMA]] 是更广的远程内存访问机制；GPUDirect RDMA 专指 NVIDIA GPU memory 直接参与 RDMA 的能力。AMD、Ascend 等平台有各自 device-direct 通路，不应统一冒充为 GPUDirect。

## 项目实现

[[community/ai-dynamo/NIXL/NIXL|NIXL]] 的 backend/transport 能覆盖 GPUDirect RDMA 等 GPU-direct 路径；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 文档明确支持 (GPUDirect) RDMA，在 DRAM/VRAM 之间进行 zero-copy transfer。

## Sources

- https://github.com/ai-dynamo/nixl/blob/main/docs/doxygen/nixl_doxygen.md
- https://kvcache-ai.github.io/Mooncake/design/architecture.html
- https://kvcache-ai.github.io/Mooncake/design/transfer-engine/
