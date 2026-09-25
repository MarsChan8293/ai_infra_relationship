---
type: concept
name: Storage Tiering
aliases:
  - Tiered Storage
  - Multi-tier Storage
  - 分层存储
domain: storage
topic: storage-tiering
related_concepts:
  - Memory Hierarchy
  - Tiered KV Cache
  - KV Cache Offloading
  - NVMe SSD
projects:
  - LMCache
  - MemCache
  - Mooncake
  - YuanRong DataSystem
  - Tutti
last_verified: 2026-09
---

# Storage Tiering

## 一句话定义

Storage Tiering 把同一类数据按热度、成本和访问延迟分布到 HBM、Host DRAM、SSD/NVMe、远端存储等不同层级，并在层级之间动态迁移。

## 解决的问题

最快介质通常最贵、容量最小。长上下文 serving、KV Cache 和训练数据都无法只依赖 HBM，因此系统需要让热点数据靠近计算、冷数据下沉到更便宜的大容量介质。

## 核心机制

- hot/cold classification。
- promotion / demotion。
- async prefetch。
- eviction / writeback。
- admission control。
- bandwidth-aware placement。

它关注“数据放在哪一层以及何时迁移”，而不是单纯描述硬件层次本身。

## 与 Memory Hierarchy 的区别

[[Memory Hierarchy]] 是系统结构；Storage Tiering 是在层次结构上执行的数据放置和迁移策略。[[Tiered KV Cache]] 则是这种机制在 KV Cache 上的专门化。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 把 KV 扩展到 GPU、CPU 与 L2 storage；[[community/Ascend/MemCache/MemCache|MemCache]] 组织 HBM/DDR/SSD 多级缓存池；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 使用 CPU DRAM、SSD 与网络资源构建分层 KV store；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 组织 HBM/DRAM/SSD heterogeneous cache；[[community/xPU-IO/Tutti/Tutti|Tutti]] 专注 SSD-backed KV tier。

## Sources

- https://docs.lmcache.ai/
- https://gitcode.com/Ascend/memcache
- https://github.com/kvcache-ai/Mooncake
- https://github.com/openyuanrong/datasystem
- https://github.com/xPU-IO/Tutti
