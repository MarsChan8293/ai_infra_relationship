---
type: concept
name: Data Movement
aliases:
  - Inference Data Movement
  - Distributed Data Movement
  - 数据搬运
  - 数据移动
domain: communication
topic: data-movement
related_concepts:
  - Point-to-Point Transfer
  - Collective Communication
  - KV Cache Transfer
projects:
  - NIXL
  - Mooncake
  - MemFabric
last_verified: 2026-09
---

# Data Movement

## 一句话定义

Data Movement 是在 GPU/NPU、CPU、远端内存、SSD 和网络节点之间搬运模型运行状态的数据平面能力。

## 解决的问题

分布式推理不只是在多卡上“做计算”。KV cache、模型权重、hidden states、checkpoint、MoE token 和训练/推理中间状态都可能跨设备、跨节点或跨存储层移动。很多系统的实际瓶颈因此从 FLOPs 转向带宽、拓扑和 copy path。

## 核心机制

数据移动层通常负责：

1. 注册本地和远端内存/存储区域。
2. 选择可用 transport，例如 memcpy、NVLink、TCP、RDMA、NVMe-oF。
3. 提交异步 read/write 或 transfer request。
4. 管理 completion、重试、分片、多 NIC 和拓扑选择。
5. 尽量减少 CPU staging 与额外 copy。

## 两类主要路径

- [[Point-to-Point Transfer]]：明确的 producer → consumer 搬运，例如 KV、权重和 hidden states。
- [[Collective Communication]]：一组 rank 共同参与的同步/重分布，例如 AllReduce、AllGather、All-to-All。

[[KV Cache Transfer]] 是 Data Movement 在 LLM serving 中最重要的具体应用之一。

## 项目实现

[[community/ai-dynamo/NIXL/NIXL|NIXL]] 为 GPU、CPU、storage 与多种 transport 提供统一传输抽象；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Transfer Engine 提供跨 DRAM/VRAM/NVMe 的 zero-copy 数据传输；[[community/Ascend/MemFabric/MemFabric|MemFabric]] 为 Ascend 构建异构内存池和跨机直接数据访问底座。

## Sources

- https://github.com/ai-dynamo/nixl/blob/main/docs/BackendGuide.md
- https://kvcache-ai.github.io/Mooncake/design/transfer-engine/
- https://gitcode.com/Ascend/memfabric_hybrid
