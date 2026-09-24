---
type: concept
name: KV Cache Sharing
aliases:
  - KV Sharing
  - Shared KV Cache
  - KV缓存共享
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - KV Cache Transfer
  - Prefix Caching
projects:
  - LMCache
  - Mooncake
last_verified: 2026-09
---

# KV Cache Sharing

## 一句话定义

KV Cache Sharing 让多个 serving instance 或 worker 发现并复用其他实例已经计算好的 KV，而不是每个实例都重新执行同一段 prefill。

## 解决的问题

负载均衡会把具有相同上下文的请求送往不同 worker，单实例 [[Prefix Caching]] 因此可能失效。共享 KV 把复用范围从“一个 engine 的本地缓存”扩大到多个实例甚至整个集群。

## 核心机制

系统需要解决两个问题：先发现“谁拥有我要的 KV”，再通过 [[KV Cache Transfer]] 或共享 KV store 把数据交给消费者。实现可以是 P2P，也可以通过中心化/分布式存储池。

## 与相邻概念的区别

Prefix Caching 描述“相同前缀如何命中”；KV Sharing 描述“这个命中能否跨实例成立”。二者经常组合，但一个本地 prefix cache 并不自动构成分布式 sharing。

## 代价与适用边界

跨实例共享可以减少重复 prefill，但会增加 lookup、网络传输和缓存目录维护开销。若共享前缀很短或网络很慢，重新计算可能更划算。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 提供 P2P KV Cache Sharing，也支持通过共享 backend 跨实例复用。[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 的 Mooncake Store 提供分布式 KV cache pooling，可作为跨 serving instance 的共享缓存层。

## Sources

- https://docs.lmcache.ai/kv_cache/p2p_sharing.html
- https://docs.lmcache.ai/distributed_kv_cache.html
- https://kvcache-ai.github.io/Mooncake/getting_started/quick-start.html
