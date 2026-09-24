---
type: concept
name: Tiered KV Cache
aliases:
  - Hierarchical KV Cache
  - Multi-tier KV Cache
  - 分层KV缓存
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - KV Cache Offloading
  - KV Cache Transfer
projects:
  - LMCache
  - Mooncake
  - vLLM
last_verified: 2026-09
---

# Tiered KV Cache

## 一句话定义

Tiered KV Cache 把 GPU/NPU HBM、CPU DRAM、SSD/NVMe 和远端 KV store 等不同性能/容量介质组织成一个分层缓存体系。

## 解决的问题

单一存储层很难同时满足“低延迟、高带宽、大容量、低成本”。分层设计让最热 KV 靠近计算设备，较冷 KV 下沉到更大但更慢的层。

## 核心机制

每个 tier 具有不同的容量、带宽和访问延迟。运行时根据命中、热度、容量压力和数据移动成本决定 KV 的放置、晋升、下沉与淘汰。CPU 层经常既是缓存，也承担 GPU 与磁盘/远端 backend 之间的 staging buffer。

## 细分与相邻概念

- [[KV Cache Offloading]] 描述“从主层移出去”的动作。
- Tiering 描述多个层长期协同后的整体缓存结构。
- [[KV Cache Transfer]] 是层与层之间的数据面。
- [[KV Cache Sharing]] 可以建立在共享的远端 tier 之上，但两者不是同义词。

## 代价与适用边界

层次越多，容量越大，但元数据、miss handling、数据搬运和一致性也越复杂。真正的性能取决于 workload 的重用距离和各层带宽，而不是 tier 数量本身。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 文档把 CPU RAM 作为可缓存热数据的层，并可结合 disk/remote backend。[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 的 Mooncake Store 提供 DRAM 与 SSD/NVMe 多层 KV cache。[[community/vllm-project/vLLM/vLLM|vLLM]] 的 KV Offloading 支持 `TieringOffloadingSpec` 和 secondary tiers。

## Sources

- https://docs.lmcache.ai/kv_cache/cpu_ram.html
- https://kvcache-ai.github.io/Mooncake/
- https://docs.vllm.ai/en/latest/features/kv_offloading_usage/
