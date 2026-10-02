---
type: concept
name: KV Cache Eviction
aliases:
  - KV Eviction
  - Cache Eviction
  - KV缓存淘汰
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - Tiered KV Cache
  - KV Cache Offloading
  - KV Cache Prefetching
  - Remote KV Store
projects:
  - LMCache
  - MemCache
last_verified: 2026-09
---

# KV Cache Eviction

## 一句话定义

KV Cache Eviction 是在缓存容量不足或数据价值降低时，选择哪些 KV block / key 被删除、下沉或失效的策略。

## 解决的问题

[[KV Cache]] 容量是有限的，而在线请求会不断产生新的 KV。若没有 eviction，cache 最终必然耗尽；若淘汰错误，又会让高价值 prefix 被迫重新 Prefill。

## 核心机制

Eviction 通常依据一种或多种信号：

- LRU / recency；
- LFU / reuse frequency；
- prefix 长度和重算 FLOPs；
- 请求优先级 / tenant；
- storage tier pressure；
- TTL / lease；
- 预测的未来复用概率。

对多级系统而言，“evict”不一定代表真正删除，也可能只是从 HBM 下沉到 DRAM/SSD，形成 demotion。

## 与 Offloading 的区别

[[KV Cache Offloading]] 强调数据被移动到较慢层；Eviction 强调“谁应该让出当前 cache capacity”。一个被 eviction 的 entry 可以被删除，也可以被 offload。

## 与 Prefetch 的关系

[[KV Cache Prefetching]] 是反方向操作：在预期将被使用前把冷层 KV 拉回快层。Eviction 与 Prefetch 共同决定 tiered cache 的冷热循环。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 2026 架构中已有 distributed eviction、cache controller 和 L1/L2 storage lifecycle；[[community/Ascend/MemCache/MemCache|MemCache]] 直接实现 key eviction，并与 DRAM↔SSD prefetch/冷热迁移结合。

## Sources

- https://github.com/LMCache/LMCache
- https://gitcode.com/Ascend/memcache
