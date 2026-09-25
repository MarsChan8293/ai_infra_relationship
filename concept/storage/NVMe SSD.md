---
type: concept
name: NVMe SSD
aliases:
  - NVMe
  - NVMe Storage
  - SSD
  - NVMe固态盘
domain: storage
topic: storage-media
related_concepts:
  - Storage Tiering
  - SSD-Backed KV Cache
  - Direct Storage I/O
  - PCIe
projects:
  - Tutti
  - 3FS
  - MemCache
  - Mooncake
  - YuanRong DataSystem
last_verified: 2026-09
---

# NVMe SSD

## 一句话定义

NVMe SSD 是通过 PCIe/NVMe 协议提供高并发、低延迟块存储的固态介质，在 AI Infra 中常作为 DRAM 之后的大容量低成本 tier。

## 为什么对 LLM 推理重要

相比 DRAM，NVMe 延迟高得多，但容量和成本优势明显。对于长上下文 KV、checkpoint、模型权重 staging 和冷数据，它可以把“容量不足”问题转化为“如何隐藏 I/O 延迟”的系统问题。

## 核心性能因素

- queue depth / parallel I/O。
- sequential vs fragmented I/O。
- PCIe bandwidth。
- filesystem / block layer overhead。
- pinned memory / DMA。
- multi-device striping。
- prefetch 与 overlap。

## 与普通 SSD 使用的区别

LLM serving 的 KV block 往往小而碎，若 CPU 负责大量细粒度 I/O submission，软件开销可能先于 SSD 带宽成为瓶颈。因此 [[Direct Storage I/O]] 与 GPU-centric storage 会变得重要。

## 项目实现

[[community/xPU-IO/Tutti/Tutti|Tutti]] 直接面向 NVMe SSD-backed KV Cache；[[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] 使用 NVMe SSD 构建高吞吐分布式文件系统；[[community/Ascend/MemCache/MemCache|MemCache]]、[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 和 [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 都把 SSD 作为多级存储的一层。

## Sources

- https://github.com/xPU-IO/Tutti
- https://github.com/deepseek-ai/3FS
- https://gitcode.com/Ascend/memcache
- https://github.com/kvcache-ai/Mooncake
- https://github.com/openyuanrong/datasystem
