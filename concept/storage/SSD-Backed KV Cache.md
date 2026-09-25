---
type: concept
name: SSD-Backed KV Cache
aliases:
  - SSD KV Cache
  - NVMe KV Cache
  - SSD-backed KV
  - SSD后端KV缓存
domain: storage
topic: kv-cache-storage
related_concepts:
  - KV Cache Offloading
  - Tiered KV Cache
  - NVMe SSD
  - Direct Storage I/O
projects:
  - Tutti
  - MemCache
  - Mooncake
last_verified: 2026-09
---

# SSD-Backed KV Cache

## 一句话定义

SSD-Backed KV Cache 把一部分 KV Cache 放在 SSD/NVMe 上，在需要时预取回 Host 或 accelerator memory，以大幅扩展可缓存的 token 容量。

## 解决的问题

当上下文长度和并发增加时，KV Cache 会快速吃满 HBM 与 Host DRAM。SSD 容量大、成本低，但延迟高，因此系统必须通过异步 I/O、prefetch、batching 和 locality 管理把 SSD 延迟隐藏在计算后面。

## 核心机制

- KV block / object 持久化到 NVMe。
- 异步 prefetch 到 DRAM/HBM。
- hot/cold eviction。
- request-level / prefix-level locality。
- multi-SSD striping。
- layerwise I/O 与 compute overlap。

## 与 KV Cache Offloading 的关系

[[KV Cache Offloading]] 是更广的上位机制，可以 offload 到 CPU、SSD、远端节点或其他 tier。SSD-Backed KV Cache 专门关注 NVMe/SSD 这一层及其 I/O 特性。

## 项目实现

[[community/xPU-IO/Tutti/Tutti|Tutti]] 专门研究 GPU-centric SSD-backed KV Cache；[[community/Ascend/MemCache/MemCache|MemCache]] 支持 DRAM↔SSD 冷热 KV 迁移；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 的分布式 KV store 使用 CPU DRAM、SSD 与 NIC 资源扩展缓存容量。

## Sources

- https://github.com/xPU-IO/Tutti
- https://gitcode.com/Ascend/memcache
- https://www.usenix.org/conference/fast25/presentation/qin
