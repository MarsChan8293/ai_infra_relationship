---
type: concept
name: KV Cache Offloading
aliases:
  - KV Offloading
  - KV Cache 卸载
  - KV缓存卸载
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - Tiered KV Cache
  - KV Cache Transfer
projects:
  - LMCache
  - vLLM
last_verified: 2026-09
---

# KV Cache Offloading

## 一句话定义

KV Cache Offloading 是把暂时不需要驻留在 GPU/NPU 主 KV 空间中的缓存迁移到 CPU RAM、SSD 或远端存储，并在再次使用时加载回来。

## 解决的问题

长上下文和高并发会让 [[KV Cache]] 很快吃满昂贵的加速器内存。Offloading 用容量更大、成本更低但更慢的存储层换取更大的有效 KV 容量。

## 核心机制

运行时在主 KV 层和 secondary storage 之间执行 store/load。真正的系统瓶颈不是“能不能放下”，而是命中预测、搬运带宽、异步流水、pinned memory、淘汰策略和恢复 KV 的等待时间能否把慢层延迟隐藏起来。

## 细分与相邻概念

- CPU KV Offloading：GPU/NPU ↔ host RAM。
- SSD / Local Disk Offloading：host staging ↔ 本地 SSD/NVMe。
- Remote KV Offloading：通过网络访问远端 KV store。
- [[Tiered KV Cache]]：当多个 offload 目的地按层次共同工作时形成 tiered cache。
- [[KV Cache Transfer]]：offload 的数据面动作之一，但 transfer 也用于 P/D、P2P 等不属于 offload 的场景。

## 代价与适用边界

Offloading 增加可用容量，但慢层延迟可能直接进入 TTFT 或调度等待。只有当复用节省的计算/容量收益大于数据搬运成本时才值得使用。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 支持 CPU RAM、本地磁盘以及多种远端 backend。当前 [[community/vllm-project/vLLM/vLLM|vLLM]] 也提供 KV Offloading connector 与 tiering 配置。

## Sources

- https://docs.lmcache.ai/getting_started/quickstart/offload_kv_cache.html
- https://docs.lmcache.ai/
- https://docs.vllm.ai/en/latest/features/kv_offloading_usage/
