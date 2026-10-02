---
type: concept
name: Remote KV Store
aliases:
  - Remote KV Cache Store
  - Distributed KV Store
  - Remote KV Cache
  - 远程KV存储
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - KV Cache Sharing
  - KV Cache Transfer
  - Tiered KV Cache
  - Memory Pooling
projects:
  - LMCache
  - Mooncake
  - FlexKV
  - YuanRong DataSystem
  - MemCache
last_verified: 2026-09
---

# Remote KV Store

## 一句话定义

Remote KV Store 把 KV Cache 放在独立于当前 inference worker 的远端共享存储中，让多个实例按 key 查找、读取和写入已经计算好的 KV。

## 解决的问题

本地 prefix cache 只能服务一个 worker；当请求在集群间路由、worker 重启或 P/D 分离时，KV 需要跨实例继续存在。Remote KV Store 把 KV 生命周期从单个 engine 中解耦出来。

## 核心机制

远端 KV 层通常提供：

1. token/prefix/block → key 的稳定映射；
2. metadata / location lookup；
3. put/get/remove API；
4. [[KV Cache Transfer]] 数据面；
5. 多 client 的并发访问和容量管理；
6. [[KV Cache Eviction]] / TTL / lifecycle control。

底层可以是专用 distributed store，也可以是 Redis/Valkey、object/filesystem、Mooncake Store 等 backend。

## 与 KV Cache Sharing 的区别

[[KV Cache Sharing]] 是“多个实例能否复用同一份 KV”的上层能力；Remote KV Store 是实现 sharing 的一种架构。P2P sharing 不一定需要中心/远端 store。

## 与 Memory Pooling 的区别

[[Memory Pooling]] 关注物理/逻辑容量聚合；Remote KV Store 关注以 KV key/object 语义对外提供共享状态。两者可以叠加，但 API 和一致性语义不同。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 提供 distributed/L2、Valkey/Redis、S3/filesystem、Mooncake Store 等远端 backend；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Store 是分布式 KV/data store；[[community/taco-project/FlexKV/FlexKV|FlexKV]] 提供 scalable remote storage，并可把 Mooncake Store 作为 key-addressed remote cache tier；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 被 vLLM-Ascend/vLLM-Omni 用作跨节点 KV store；[[community/Ascend/MemCache/MemCache|MemCache]] 提供分布式 KV cache storage 与 MetaService。

## Sources

- https://github.com/LMCache/LMCache
- https://github.com/kvcache-ai/Mooncake
- https://github.com/taco-project/FlexKV
- https://github.com/openyuanrong/datasystem
- https://gitcode.com/Ascend/memcache
