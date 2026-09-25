---
type: concept
name: Memory Hierarchy
aliases:
  - Hierarchical Memory
  - Multi-tier Memory
  - 分层内存
  - 内存层次
domain: memory
topic: memory-hierarchy
related_concepts:
  - HBM
  - Host Memory
  - Memory Pooling
  - Tiered KV Cache
projects:
  - MemCache
  - LMCache
  - Mooncake
  - FlexKV
  - YuanRong DataSystem
  - MemFabric
last_verified: 2026-09
---

# Memory Hierarchy

## 一句话定义

Memory Hierarchy 是把容量、带宽、延迟和成本不同的存储层组织成层次，让最热的数据尽量靠近计算单元，较冷数据下沉到更大但更慢的层。

## 为什么 AI Infra 特别依赖它

LLM 推理同时处理模型权重、[[KV Cache]]、activation、通信 buffer 和临时 workspace。单靠 GPU/NPU HBM 往往无法同时容纳所有状态，因此系统会组合：

- accelerator HBM / VRAM；
- [[Host Memory]] / DDR；
- CXL 扩展内存；
- SSD / NVMe；
- 远端 DRAM / distributed store。

不同数据对象的访问局部性不同，因此“放哪里”本身就是性能设计的一部分。

## 核心机制

分层系统通常包含：

1. **placement**：决定数据初始放在哪一层；
2. **promotion / demotion**：热点上移、冷数据下沉；
3. **prefetch**：在真正访问前提前搬入快层；
4. **eviction**：快层容量不足时淘汰；
5. **data movement**：通过 PCIe、RDMA、NVLink、HCCS 等链路搬运。

因此 Memory Hierarchy 与 [[Data Movement]]、[[KV Cache Offloading]]、[[Tiered KV Cache]] 强相关。

## 与 Tiered KV Cache 的区别

Memory Hierarchy 是通用系统概念；[[Tiered KV Cache]] 只描述 KV Cache 在 GPU/CPU/SSD/remote storage 等层上的具体缓存体系。

## 项目实现

[[community/Ascend/MemCache/MemCache|MemCache]] 组织 HBM/DDR/SSD 多级 KV pool；[[community/LMCache/LMCache/LMCache|LMCache]] 覆盖 GPU/CPU/disk/remote KV tiers；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 使用 DRAM/SSD/VRAM 构建数据与 KV 层次；[[community/taco-project/FlexKV/FlexKV|FlexKV]] 覆盖 CPU memory、local SSD 和 remote storage；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 将 HBM/DRAM/SSD 组织成 pooled cache；[[community/Ascend/MemFabric/MemFabric|MemFabric]] 为多层内存提供统一数据面。

## Sources

- https://gitcode.com/Ascend/memcache
- https://docs.lmcache.ai/
- https://github.com/kvcache-ai/Mooncake
- https://github.com/taco-project/FlexKV
- https://github.com/openyuanrong/datasystem
- https://gitcode.com/Ascend/memfabric_hybrid
