---
type: concept
name: SSD/NVMe Tier
aliases:
  - "SSD Tier"
  - "NVMe Tier"
  - "NVMe SSD"
  - "NVMe"
  - "NVMe Storage"
  - "SSD/NVMe Offloading"
  - "SSD卸载"
  - "NVMe固态盘"
domain: memory
topic: memory-hierarchy
parent_concepts:
  - Memory Hierarchy
related_concepts:
  - "SSD-Backed KV Cache"
  - "Storage Tiering"
  - "Tiered KV Cache"
  - "KV Cache Offloading"
  - "KV Cache Management"
  - "Direct Storage I/O"
  - "PCIe"
projects:
  - "MemCache"
  - "LMCache"
  - "Mooncake"
  - "FlexKV"
  - "YuanRong DataSystem"
  - "Tutti"
  - "PegaFlow"
  - "3FS"
  - "Edge0"
  - "Splash"
last_verified: 2026-10
---

# SSD/NVMe Tier

## 一句话定义

SSD/NVMe Tier 是把 SSD 或 NVMe 设备作为 HBM/Host Memory 之后的大容量慢层，用于保存冷 KV、模型状态或其他可恢复数据。

## 解决的问题

当 [[HBM]] 和 [[Host Memory]] 都不足以容纳长上下文、高并发 KV 或大规模模型状态时，SSD 能提供更大的单机容量，成本也远低于 accelerator memory。

## 核心机制

典型路径是：

`HBM ↔ Host Memory / pinned buffer ↔ NVMe SSD`

这里同时保留 NVMe/SSD 的设备层语义：NVMe 通常通过 PCIe 暴露高并发 block I/O，性能受 queue depth、I/O size、fragmentation、filesystem/block layer、DMA 与 multi-device striping 影响。系统层再通过 async I/O、batching，以及 [[KV Cache Management]] 中的 prefetch / eviction 隐藏慢层延迟。

## 与 Offloading / Tiering 的区别

- [[KV Cache Offloading]] 描述“把 KV 移出主加速器内存”的动作。
- [[Tiered KV Cache]] 描述整个多层 KV cache 体系。
- SSD/NVMe Tier 则是其中一个具体介质层。

## 与现有存储概念的边界

- 本页同时承担“NVMe SSD 设备/协议”与“SSD/NVMe 在 memory/storage hierarchy 中的慢层角色”，避免为同一介质维护两个高度重叠节点。
- [[concept/storage/SSD-Backed KV Cache|SSD-Backed KV Cache]] 专门描述 KV 使用 SSD 后端的缓存机制；SSD/NVMe Tier 还可以保存模型权重、checkpoint 和其他可恢复数据。
- [[concept/storage/Storage Tiering|Storage Tiering]] 描述跨层放置与迁移策略。
- [[concept/storage/Direct Storage IO|Direct Storage I/O]] 描述 accelerator ↔ storage 的低中转数据路径。

## 适用边界

SSD 带宽和延迟远低于 HBM/DRAM，因此并不是“容量越大越好”。只有冷数据、长重用距离或高重算成本的数据才适合下沉到 SSD；高频随机 miss 可能直接把 TTFT 拖垮。

## 项目实现

[[community/Ascend/MemCache/MemCache|MemCache]] 使用 HBM/DDR/SSD 多级 KV cache；[[community/LMCache/LMCache/LMCache|LMCache]] 支持 local disk/filesystem 等 backend；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Store 使用 DRAM + SSD/NVMe；[[community/taco-project/FlexKV/FlexKV|FlexKV]] 明确包含 local SSD tier；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 使用 HBM/DRAM/SSD pooled cache；[[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] 以 NVMe SSD 构建高吞吐分布式存储。

[[community/xPU-IO/Tutti/Tutti|Tutti]] 专门优化 SSD-backed KV I/O；[[community/novitalabs/pegaflow/pegaflow|PegaFlow]] 提供 host + SSD + remote RDMA 层；[[community/incoai/Splash/Splash|Splash]] 可把 KV/GDN state 下沉到 SSD。

## Sources

- https://gitcode.com/Ascend/memcache
- https://docs.lmcache.ai/
- https://github.com/kvcache-ai/Mooncake
- https://github.com/taco-project/FlexKV
- https://github.com/openyuanrong/datasystem
