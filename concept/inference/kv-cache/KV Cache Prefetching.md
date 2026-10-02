---
type: concept
name: KV Cache Prefetching
aliases:
  - KV Prefetch
  - Cache Prefetching
  - KV缓存预取
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - KV Cache Eviction
  - KV Cache Offloading
  - SSD/NVMe Tier
  - Remote KV Store
projects:
  - LMCache
  - MemCache
  - FlexKV
last_verified: 2026-09
---

# KV Cache Prefetching

## 一句话定义

KV Cache Prefetching 在请求真正需要某段 KV 之前，提前把它从 CPU、SSD 或 remote store 搬到更靠近计算的层，以隐藏 miss latency。

## 解决的问题

当 KV 被 [[KV Cache Offloading]] 到慢层后，命中并不等于“免费”。如果等 attention 真正需要它时才开始读取 SSD/remote store，I/O 延迟会直接进入 TTFT 或 decode stall。

## 核心机制

Prefetch 需要同时回答两个问题：

1. **prefetch what**：哪些 prefix/block 很可能马上被请求；
2. **prefetch when**：多早开始搬运，才能和排队、Prefill 或其他计算重叠。

系统可以利用 request queue、prefix lookup、历史复用、scheduler hint 或显式应用 hint 触发异步 transfer。

## 与普通 Cache Hit 的区别

cache hit 只说明数据存在；prefetch 关注数据是否已经在“正确时间出现在正确层”。一个 remote hit 如果没有提前搬运，仍可能产生很长的等待。

## 与 Eviction 的关系

[[KV Cache Eviction]] 把低价值数据从快层移走；Prefetch 把即将使用的数据拉回。二者共同影响 tiered cache 的命中率、数据移动量和 tail latency。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 的 CacheBlend / sparse prefetch 与多层 storage 路径包含显式预取机制；[[community/Ascend/MemCache/MemCache|MemCache]] 已实现 DRAM↔SSD key prefetch/eviction；[[community/taco-project/FlexKV/FlexKV|FlexKV]] 通过异步 transfer / prefetch 降低远端或 SSD KV 恢复开销。

## Sources

- https://github.com/LMCache/LMCache
- https://gitcode.com/Ascend/memcache
- https://github.com/taco-project/FlexKV
