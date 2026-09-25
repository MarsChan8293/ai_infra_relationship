---
type: concept
name: Host Memory
aliases:
  - CPU Memory
  - System Memory
  - Host DRAM
  - 主机内存
domain: memory
topic: memory-hierarchy
parent_concepts:
  - Memory Hierarchy
related_concepts:
  - HBM
  - NUMA
  - KV Cache Offloading
projects:
  - LMCache
  - MemCache
  - Mooncake
  - FlexKV
  - KTransformers
  - MemFabric
last_verified: 2026-09
---

# Host Memory

## 一句话定义

Host Memory 是 CPU 侧 DRAM / system memory，在 AI inference 中常作为 HBM 之外的大容量中间层，用于权重、KV Cache、staging buffer 和异构计算。

## 解决的问题

HBM 容量昂贵且有限，而服务器 DRAM 通常容量大得多。把不需要立刻访问的数据放到 Host Memory，可以扩大单机有效模型/KV 容量，并减少对 SSD/remote storage 的依赖。

## 常见用途

- [[KV Cache Offloading]]：GPU/NPU KV ↔ host DRAM。
- 模型权重 offload：只把当前需要的 layer/expert 搬入 accelerator。
- pinned buffer / staging：网络、SSD 与 GPU/NPU 之间的数据中转。
- CPU-GPU hybrid inference：CPU 直接执行部分算子或 experts。

## NUMA 影响

多路 CPU 服务器的 host DRAM 具有 [[NUMA]] 拓扑。对某张 GPU/NIC 来说，“本地 CPU memory”和“远端 socket memory”延迟/带宽不同，因此 pinned memory placement、worker affinity 和 NIC/GPU topology 会直接影响 offload 性能。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 把 CPU RAM 作为 KV cache tier；[[community/Ascend/MemCache/MemCache|MemCache]] 使用 DDR 作为 HBM 与 SSD 之间的 KV 层；[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 使用 host DRAM 参与 Store/Transfer；[[community/taco-project/FlexKV/FlexKV|FlexKV]] 使用 CPU memory 作为多级 KV cache；[[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] 直接利用大容量 CPU memory 运行超大 MoE；[[community/Ascend/MemFabric/MemFabric|MemFabric]] 将 DRAM/HBM 统一纳入数据面。

## Sources

- https://docs.lmcache.ai/kv_cache/cpu_ram.html
- https://gitcode.com/Ascend/memcache
- https://github.com/kvcache-ai/Mooncake
- https://github.com/taco-project/FlexKV
- https://github.com/kvcache-ai/ktransformers
- https://gitcode.com/Ascend/memfabric_hybrid
