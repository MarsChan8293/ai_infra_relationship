---
type: concept
name: Distributed Storage
aliases:
  - Distributed Storage System
  - 分布式存储
domain: storage
topic: distributed-storage
related_concepts:
  - Storage Tiering
  - Remote Object Store
  - RDMA
projects:
  - 3FS
  - Mooncake
  - YuanRong DataSystem
  - MemCache
  - LMCache
last_verified: 2026-09
---

# Distributed Storage

## 一句话定义

Distributed Storage 把数据分布在多台机器或多个存储节点上，通过复制、分片、元数据与网络数据路径提供统一的数据访问能力。

## 解决的问题

单机内存或 SSD 容量有限，也无法独立承担大规模训练、推理 checkpoint、KV Cache 和中间数据的吞吐需求。Distributed Storage 通过横向扩展容量和带宽，让数据不再绑定单个 worker。

## 核心机制

典型系统会组合：

- 数据分片 / placement。
- 元数据与 namespace。
- replication / erasure coding / durability。
- network transport 与 [[RDMA]]。
- local DRAM / SSD / NVMe tier。
- cache / prefetch / eviction。
- object、file、KV 或 stream 等上层语义。

## 与 Memory Pooling 的区别

[[Memory Pooling]] 强调把多节点内存组织成共享/统一内存资源；Distributed Storage 更强调持久化或半持久化的数据组织、命名和跨节点访问。现代 AI infra 中两者可能在同一产品里重叠。

## 项目实现

[[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] 是高性能分布式文件系统；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 用 DRAM/SSD/NIC 构建分布式 KV/data store；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 提供 Object/Stream/KV 多语义分布式缓存；[[community/Ascend/MemCache/MemCache|MemCache]] 和 [[community/LMCache/LMCache/LMCache|LMCache]] 将分布式存储机制用于 KV Cache。

## Sources

- https://github.com/deepseek-ai/3FS
- https://github.com/kvcache-ai/Mooncake
- https://github.com/openyuanrong/datasystem
- https://gitcode.com/Ascend/memcache
- https://github.com/LMCache/LMCache
