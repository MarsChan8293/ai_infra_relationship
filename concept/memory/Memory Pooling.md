---
type: concept
name: Memory Pooling
aliases:
  - Memory Pool
  - Disaggregated Memory Pool
  - 内存池化
domain: memory
topic: memory-pooling
related_concepts:
  - Memory Hierarchy
  - NUMA
  - CXL Memory
  - Data Movement
projects:
  - MemFabric
  - MemCache
  - YuanRong DataSystem
  - Mooncake
last_verified: 2026-09
---

# Memory Pooling

## 一句话定义

Memory Pooling 把多个设备、进程或节点上的物理内存容量组织成一个可统一分配或访问的逻辑资源池。

## 解决的问题

单个 GPU/NPU、单台服务器甚至单个 NUMA node 的内存容量都有限，但集群中常存在大量分散的 HBM/DRAM。Pool 让上层不必把数据永久绑定到某一块本地内存，而可以从更大的共享容量中动态获取空间。

## 核心机制

典型 pooling 系统需要：

1. 全局地址 / object / key 空间；
2. allocator 与 metadata service；
3. ownership / lease / consistency；
4. locality-aware placement；
5. [[Data Movement]] 或 remote access；
6. failure recovery 与容量回收。

不同实现可能提供“真正的共享地址空间”，也可能只是统一的 key/object API，不能仅凭“pool”一词假定内存一致性语义相同。

## 与 Memory Hierarchy 的区别

[[Memory Hierarchy]] 关注快慢层；Memory Pooling 关注容量如何跨设备/节点组合。一个系统可以同时是多层的、又是 pooled 的，例如 HBM + DRAM + SSD 跨多节点组成分层资源池。

## 与 CXL 的关系

[[CXL Memory]] 是实现 host-side memory expansion / pooling 的一种硬件路径；RDMA、专用 device fabric、shared-memory service 也可以实现 pooling，因此 Memory Pooling 不等于 CXL。

## 项目实现

[[community/Ascend/MemFabric/MemFabric|MemFabric]] 将多节点 DRAM/HBM 组织成统一内存池；[[community/Ascend/MemCache/MemCache|MemCache]] 在其上构建 KV pool；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 将集群 HBM/DRAM/SSD 组织成近计算 pooled cache；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Store 构建分布式 DRAM/SSD KV/data pool。

## Sources

- https://gitcode.com/Ascend/memfabric_hybrid
- https://gitcode.com/Ascend/memcache
- https://github.com/openyuanrong/datasystem
- https://github.com/kvcache-ai/Mooncake
