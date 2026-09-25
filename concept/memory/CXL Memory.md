---
type: concept
name: CXL Memory
aliases:
  - Compute Express Link Memory
  - CXL Type-3 Memory
  - CXL内存
domain: memory
topic: memory-pooling
related_concepts:
  - Host Memory
  - Memory Pooling
  - Memory Hierarchy
projects:
  - LMCache
last_verified: 2026-09
---

# CXL Memory

## 一句话定义

CXL Memory 是通过 Compute Express Link 将外接/共享内存设备接入主机内存体系的路径，可用于扩展 DRAM 容量或构建更灵活的 memory pooling。

## 为什么 AI Infra 关注它

LLM serving 中，模型权重、KV Cache 和 checkpoint 都可能远大于本机 HBM。相比 SSD，CXL-attached memory 更接近 memory semantics；相比本地 DRAM，它又可以提供更大的可扩展容量。

它因此常被讨论为：

- [[Host Memory]] 扩展层；
- [[KV Cache Offloading]] 目的地；
- [[Memory Pooling]] 的硬件底座；
- CPU/GPU/NPU 与大容量共享内存之间的中间层。

## 核心边界

CXL 并不会把远端/扩展内存变成 HBM。性能仍取决于 PCIe/CXL generation、switch topology、NUMA/host placement、访问模式和 page migration。

对于 LLM，只有当计算复用收益大于 CXL access / transfer 成本时，KV/权重放入 CXL tier 才有实际价值。

## 与 RDMA 的区别

[[RDMA]] 主要提供跨网络节点的远程内存数据移动；CXL Memory 更接近 host memory fabric / expansion。两者都能扩展“本地之外的容量”，但编程与一致性语义不同。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 已把 CXL 纳入 KV cache/storage backend 与研究/工程范围，使 GPU KV 可以扩展到 host/CXL 等更大容量层。

## Sources

- https://docs.lmcache.ai/
- https://github.com/LMCache/LMCache
