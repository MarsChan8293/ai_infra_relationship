---
type: concept
name: SSD/NVMe Tier
aliases:
  - SSD Tier
  - NVMe Tier
  - SSD/NVMe Offloading
  - SSD卸载
domain: memory
topic: memory-hierarchy
parent_concepts:
  - Memory Hierarchy
related_concepts:
  - Tiered KV Cache
  - KV Cache Offloading
  - KV Cache Prefetching
projects:
  - MemCache
  - LMCache
  - Mooncake
  - FlexKV
  - YuanRong DataSystem
last_verified: 2026-09
---

# SSD/NVMe Tier

## 一句话定义

SSD/NVMe Tier 是把 SSD 或 NVMe 设备作为 HBM/Host Memory 之后的大容量慢层，用于保存冷 KV、模型状态或其他可恢复数据。

## 解决的问题

当 [[HBM]] 和 [[Host Memory]] 都不足以容纳长上下文、高并发 KV 或大规模模型状态时，SSD 能提供更大的单机容量，成本也远低于 accelerator memory。

## 核心机制

典型路径是：

`HBM ↔ Host Memory / pinned buffer ↔ NVMe SSD`

系统需要配合 async I/O、batch read/write、[[KV Cache Prefetching]] 和 [[KV Cache Eviction]]，尽量把 SSD 的高延迟藏在计算或网络传输之后。

## 与 Offloading / Tiering 的区别

- [[KV Cache Offloading]] 描述“把 KV 移出主加速器内存”的动作。
- [[Tiered KV Cache]] 描述整个多层 KV cache 体系。
- SSD/NVMe Tier 则是其中一个具体介质层。

## 适用边界

SSD 带宽和延迟远低于 HBM/DRAM，因此并不是“容量越大越好”。只有冷数据、长重用距离或高重算成本的数据才适合下沉到 SSD；高频随机 miss 可能直接把 TTFT 拖垮。

## 项目实现

[[community/Ascend/MemCache/MemCache|MemCache]] 使用 HBM/DDR/SSD 多级 KV cache；[[community/LMCache/LMCache/LMCache|LMCache]] 支持 local disk/filesystem 等 storage backend；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Store 使用 DRAM + SSD/NVMe 构建 KV/data tiers；[[community/taco-project/FlexKV/FlexKV|FlexKV]] 明确包含 local SSD tier；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 使用 HBM/DRAM/SSD pooled cache。

## Sources

- https://gitcode.com/Ascend/memcache
- https://docs.lmcache.ai/
- https://github.com/kvcache-ai/Mooncake
- https://github.com/taco-project/FlexKV
- https://github.com/openyuanrong/datasystem
