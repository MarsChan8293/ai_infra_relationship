---
type: concept
name: HBM
aliases:
  - High Bandwidth Memory
  - 高带宽内存
domain: memory
topic: memory-hierarchy
parent_concepts:
  - Memory Hierarchy
related_concepts:
  - Host Memory
  - Data Movement
  - KV Cache
projects:
  - MemFabric
  - MemCache
  - YuanRong DataSystem
  - Mooncake
last_verified: 2026-09
---

# HBM

## 一句话定义

HBM（High Bandwidth Memory）是紧邻 GPU/NPU 等加速器的高带宽内存，通常承载推理热路径中的模型权重、activation、KV Cache 和 kernel workspace。

## 为什么它重要

大模型推理常常不是算力不够，而是数据无法足够快地送进计算单元。Decode 阶段尤其容易受权重/KV 读取带宽限制，因此 HBM 的容量和带宽同时决定：

- 单卡能放多少权重；
- 能容纳多少 [[KV Cache]]；
- 多大 batch / 并发可以同时驻留；
- 是否需要 offload、TP/EP 或多级缓存。

## HBM 不是“普通显存”的同义词

HBM 强调的是高带宽封装/内存技术。系统层更关心它在 [[Memory Hierarchy]] 中的位置：它通常是容量最小、价格最高、最接近 accelerator compute 的快层。

## 与 Host Memory 的关系

当 HBM 不够时，系统常把冷数据下沉到 [[Host Memory]]。但 PCIe / CXL / device interconnect 带宽远低于 HBM 内部带宽，因此 offload 是否有效取决于数据复用、prefetch 和 overlap。

## 项目实现

[[community/Ascend/MemFabric/MemFabric|MemFabric]] 把多节点 HBM/DRAM 纳入统一池化/数据移动；[[community/Ascend/MemCache/MemCache|MemCache]] 将 HBM 作为 KV 快层；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 用 HBM/DRAM/SSD 构建近计算缓存；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 的 Transfer Engine / Store 支持 VRAM/DRAM 等异构内存数据路径。

## Sources

- https://gitcode.com/Ascend/memfabric_hybrid
- https://gitcode.com/Ascend/memcache
- https://github.com/openyuanrong/datasystem
- https://github.com/kvcache-ai/Mooncake
