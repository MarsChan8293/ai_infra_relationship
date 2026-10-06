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
  - "KV Cache Offloading"
  - "KV Cache Transfer"
  - "KV Cache Management"
  - "Remote KV Store"
  - "SSD/NVMe Tier"
projects:
  - "LMCache"
  - "Mooncake"
  - "vLLM"
  - "SGLang"
  - "MemCache"
  - "FlexKV"
  - "PegaFlow"
  - "Tutti"
  - "YuanRong DataSystem"
  - "Splash"
  - "vLLM-Ascend"
last_verified: 2026-10
---

# Tiered KV Cache

## 一句话定义

Tiered KV Cache 把 GPU/NPU HBM、CPU DRAM、SSD/NVMe 和远端 KV store 等不同性能/容量介质组织成一个分层缓存体系。

## 解决的问题

单一存储层很难同时满足“低延迟、高带宽、大容量、低成本”。分层设计让最热 KV 靠近计算设备，较冷 KV 下沉到更大但更慢的层。

## 核心机制

每个 tier 具有不同的容量、带宽和访问延迟。运行时根据命中、热度、容量压力和数据移动成本决定 KV 的放置、晋升、下沉与淘汰。CPU 层经常既是缓存，也承担 GPU 与磁盘/远端 backend 之间的 staging buffer。

## 细分与相邻概念

- [[KV Cache Offloading]] 描述从主加速器层移出的动作；Tiering 描述多个层长期协同后的整体结构。
- [[KV Cache Transfer]] 是层与层之间的数据面。
- [[KV Cache Sharing]] 可以建立在共享的远端 tier 之上，但两者不是同义词。
- [[concept/memory/SSD-NVMe Tier|SSD/NVMe Tier]] 是具体慢层介质；[[Remote KV Store]] 提供跨 worker 的共享存储语义。
- eviction、prefetch、promotion、demotion 等冷热策略统一归入 [[KV Cache Management]]。

## 代价与适用边界

层次越多，容量越大，但元数据、miss handling、数据搬运和一致性也越复杂。真正的性能取决于 workload 的重用距离和各层带宽，而不是 tier 数量本身。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]]、[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]、[[community/Ascend/MemCache/MemCache|MemCache]]、[[community/taco-project/FlexKV/FlexKV|FlexKV]] 与 [[community/novitalabs/pegaflow/pegaflow|PegaFlow]] 都把 KV 扩展到至少两级以上的本地或远端层。

[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 tiering/offloading 配置；[[community/sgl-project/SGLang/SGLang|SGLang]] HiCache 提供本地 + 外部层；[[community/xPU-IO/Tutti/Tutti|Tutti]] 强化 SSD tier；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 组织 HBM/DRAM/SSD pooled cache；[[community/incoai/Splash/Splash|Splash]] 提供 SSD 下沉；[[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] 可通过 KV Pool backend 使用外部层。

## Sources

- https://docs.lmcache.ai/kv_cache/cpu_ram.html
- https://kvcache-ai.github.io/Mooncake/
- https://docs.vllm.ai/en/latest/features/kv_offloading_usage/
