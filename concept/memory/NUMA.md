---
type: concept
name: NUMA
aliases:
  - Non-Uniform Memory Access
  - 非一致内存访问
domain: memory
topic: memory-topology
related_concepts:
  - Host Memory
  - Memory Pooling
  - Data Movement
projects:
  - KTransformers
  - MemCache
last_verified: 2026-09
---

# NUMA

## 一句话定义

NUMA（Non-Uniform Memory Access）表示多路 CPU 系统中，不同 CPU socket / NUMA node 访问不同内存区域的延迟和带宽并不相同。

## 为什么 AI inference 会受影响

GPU/NPU、NIC 和 CPU socket 都挂在具体 PCIe / interconnect 拓扑上。若 GPU 要访问远端 NUMA node 的 host memory，数据可能跨 socket interconnect，导致额外延迟和带宽损失。

因此以下路径都需要 NUMA-aware placement：

- pinned host memory；
- GPU ↔ CPU offload；
- NIC/RDMA buffer；
- CPU-GPU hybrid inference；
- 多 socket 上的 CPU expert / embedding / sampling worker。

## 核心机制

操作系统把 CPU core 和 DRAM 划分为 NUMA nodes。应用可以通过 CPU affinity、memory binding、first-touch policy 或 NUMA API 控制线程与内存放置。

理想情况是让：

`GPU/NPU ↔ NIC ↔ CPU core ↔ Host Memory`

尽量位于相近 topology domain，减少跨 socket hop。

## 与 Memory Pooling 的关系

[[Memory Pooling]] 试图把多个物理内存资源抽象成统一容量；NUMA 则提醒我们“逻辑统一”不代表“访问代价相同”。pooling 层如果忽略 locality，很容易把容量收益换成带宽/延迟损失。

## 项目实现

[[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] 明确面向多 NUMA CPU + GPU 的异构 MoE inference；[[community/Ascend/MemCache/MemCache|MemCache]] 工程中包含 NUMA scan / host-memory locality 路径，用于多级 KV 与数据搬运。

## Sources

- https://github.com/kvcache-ai/ktransformers
- https://gitcode.com/Ascend/memcache
