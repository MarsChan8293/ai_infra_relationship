---
type: concept
name: Direct Storage I/O
aliases:
  - Direct Storage
  - GPU Direct Storage
  - GPUDirect Storage
  - GDS
  - 直接存储IO
domain: storage
topic: data-path
related_concepts:
  - NVMe SSD
  - GPUDirect RDMA
  - Point-to-Point Transfer
projects:
  - Tutti
  - NIXL
  - Mooncake
last_verified: 2026-09
---

# Direct Storage I/O

## 一句话定义

Direct Storage I/O 让 accelerator memory 与 SSD/storage backend 之间尽量绕过传统 CPU bounce buffer 和多次拷贝，缩短数据路径并降低 CPU 参与度。

## 解决的问题

传统 storage path 往往是 SSD → kernel/page cache → Host buffer → GPU，再由 CPU 负责 I/O submission 和 memcpy orchestration。对于大量 KV block，这些额外 hop 和控制开销会吞掉 NVMe 本身的并发优势。

## 核心机制

实现方式可以不同：

- GPU/accelerator direct DMA。
- GPUDirect Storage / GDS。
- GPU-side I/O submission。
- pinned host metadata + device data path。
- storage plugin / transport backend。
- async batched I/O。

因此 Direct Storage I/O 是一类数据路径设计，不等价于某个厂商 API。

## 与 GPUDirect RDMA 的区别

[[GPUDirect RDMA]] 是 GPU memory ↔ NIC/RDMA peer；Direct Storage I/O 是 accelerator memory ↔ storage device / storage service。二者都减少 CPU 中转，但终点不同。

## 项目实现

[[community/xPU-IO/Tutti/Tutti|Tutti]] 把 NVMe I/O 的关键控制和数据路径下沉到 GPU；[[community/ai-dynamo/NIXL/NIXL|NIXL]] 为 GPU/CPU/storage backend 提供统一 transfer abstraction，并支持 GPUDirect Storage 类路径；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 在 Transfer Engine / Store 中支持异构 data movement 与 storage direct path。

## Sources

- https://github.com/xPU-IO/Tutti
- https://github.com/ai-dynamo/nixl
- https://github.com/kvcache-ai/Mooncake
