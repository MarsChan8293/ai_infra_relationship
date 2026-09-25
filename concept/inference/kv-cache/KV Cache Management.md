---
type: concept
name: KV Cache Management
aliases:
  - KV管理
  - KV缓存管理
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache
related_concepts:
  - KV Cache Offloading
  - KV Cache Transfer
  - KV Cache Sharing
  - Prefix Caching
  - KV Cache Eviction
  - KV Cache Prefetching
  - Remote KV Store
projects:
  - LMCache
  - vLLM
last_verified: 2026-09
---

# KV Cache Management

## 一句话定义

KV Cache Management 是围绕 KV 的分配、寻址、复用、放置、迁移、淘汰和回收建立的一整套运行时机制。

## 解决的问题

[[KV Cache]] 并不是一块“生成后一直放着”的静态内存。在线 serving 中请求不断到达和结束，前缀可能重复，GPU KV 空间有限，多个实例还可能需要共享或转移缓存，因此需要独立的管理层控制 KV 的生命周期。

## 核心机制

管理层通常维护逻辑 token/block 与物理存储位置之间的映射，并根据容量、命中率、请求优先级和数据移动成本执行分配与回收。系统可以进一步扩展到 GPU、CPU、SSD 和远端存储，形成多层缓存。

## 细分与相邻概念

- [[KV Cache Offloading]]：解决主加速器 KV 容量不足。
- [[Tiered KV Cache]]：把多个存储层组织为统一缓存层次。
- [[KV Cache Transfer]]：负责跨位置的数据移动。
- [[KV Cache Sharing]]：让不同 serving instance 复用已经存在的 KV。
- [[Prefix Caching]]：按共享前缀命中并复用 KV。
- [[KV Cache Eviction]]：在容量压力下决定谁被删除或下沉。
- [[KV Cache Prefetching]]：在真正访问前把冷层 KV 提前拉回快层。
- [[Remote KV Store]]：把 KV 生命周期扩展到 worker 之外的共享存储。

## 代价与适用边界

更复杂的 KV 管理可以提升容量和复用率，但也会引入元数据、查找、搬运、同步与一致性成本。低并发、短上下文场景往往不需要复杂的跨层管理。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 明确定位为 LLM inference 的 KV cache management layer，提供持久化、跨引擎复用和多种存储/传输后端。[[community/vllm-project/vLLM/vLLM|vLLM]] 在 serving runtime 内管理 KV block，并提供 prefix caching、KV connector 和 offloading 能力。

## Sources

- https://docs.lmcache.ai/
- https://docs.vllm.ai/en/stable/
