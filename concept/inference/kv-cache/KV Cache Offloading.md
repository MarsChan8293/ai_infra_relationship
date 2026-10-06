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
  - "Tiered KV Cache"
  - "KV Cache Transfer"
  - "SSD/NVMe Tier"
  - "Remote KV Store"
  - "KV Cache Management"
projects:
  - "LMCache"
  - "vLLM"
  - "SGLang"
  - "Mooncake"
  - "MemCache"
  - "FlexKV"
  - "Tutti"
  - "PegaFlow"
  - "Splash"
  - "vLLM-Ascend"
last_verified: 2026-10
---

# KV Cache Offloading

## 一句话定义

KV Cache Offloading 是把暂时不需要驻留在 GPU/NPU 主 KV 空间中的缓存迁移到 CPU RAM、SSD 或远端存储，并在再次使用时加载回来。

## 解决的问题

长上下文和高并发会让 [[KV Cache]] 很快吃满昂贵的加速器内存。Offloading 用容量更大、成本更低但更慢的存储层换取更大的有效 KV 容量。

## 核心机制

运行时在主 KV 层和 secondary storage 之间执行 store/load。真正的系统瓶颈不是“能不能放下”，而是命中预测、搬运带宽、异步流水、pinned memory、淘汰策略和恢复 KV 的等待时间能否把慢层延迟隐藏起来。

## 细分与相邻概念

- CPU KV Offloading：GPU/NPU ↔ Host DRAM。
- SSD / Local Disk Offloading：Host staging ↔ 本地 SSD/NVMe。
- Remote KV Offloading：通过网络访问 [[Remote KV Store]]。
- [[Tiered KV Cache]]：当多个 offload 目的地长期协同时形成分层缓存体系。
- [[KV Cache Transfer]]：offload 的数据面动作之一，但 transfer 也用于 P/D、P2P 等非 offload 场景。
- [[KV Cache Management]]：负责 eviction、prefetch、admission 与 lifecycle policy；这些动作不再单独拆成顶层 concept。

## 代价与适用边界

Offloading 增加可用容量，但慢层延迟可能直接进入 TTFT 或调度等待。只有当复用节省的计算/容量收益大于数据搬运成本时才值得使用。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 支持 CPU、本地磁盘和远端 backend；[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 KV offloading / connector / tiering；[[community/sgl-project/SGLang/SGLang|SGLang]] 的 HiCache 把 KV 扩展到 CPU 与外部存储层。

[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]、[[community/Ascend/MemCache/MemCache|MemCache]]、[[community/taco-project/FlexKV/FlexKV|FlexKV]] 和 [[community/novitalabs/pegaflow/pegaflow|PegaFlow]] 都提供多层或外部 KV 存储路径；[[community/xPU-IO/Tutti/Tutti|Tutti]] 专注 GPU-centric SSD-backed KV；[[community/incoai/Splash/Splash|Splash]] 可把 KV/GDN state 下沉到 SSD；[[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] 通过 KV Pool / external storage backend 接入 Ascend 场景。

## Sources

- https://docs.lmcache.ai/getting_started/quickstart/offload_kv_cache.html
- https://docs.lmcache.ai/
- https://docs.vllm.ai/en/latest/features/kv_offloading_usage/
