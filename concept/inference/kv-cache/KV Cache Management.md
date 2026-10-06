---
type: concept
name: KV Cache Management
aliases:
  - KV管理
  - KV缓存管理
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache
related_concepts:
  - "KV Cache Offloading"
  - "KV Cache Transfer"
  - "KV Cache Sharing"
  - "Prefix Caching"
  - "Tiered KV Cache"
  - "Remote KV Store"
projects:
  - "LMCache"
  - "vLLM"
  - "SGLang"
  - "Mooncake"
  - "MemCache"
  - "FlexKV"
  - "PegaFlow"
  - "vLLM-Ascend"
  - "AgentInfer"
  - "ModelSphere"
  - "vllm-rlt"
last_verified: 2026-10
---

# KV Cache Management

## 一句话定义

KV Cache Management 是围绕 KV 的分配、寻址、复用、放置、迁移、淘汰和回收建立的一整套运行时机制。

## 解决的问题

[[KV Cache]] 并不是一块“生成后一直放着”的静态内存。在线 serving 中请求不断到达和结束，前缀可能重复，GPU KV 空间有限，多个实例还可能需要共享或转移缓存，因此需要独立的管理层控制 KV 的生命周期。

## 核心机制

管理层通常维护逻辑 token/block 与物理存储位置之间的映射，并覆盖完整生命周期：

1. allocation / admission：决定 KV 如何分配与是否进入缓存；
2. reuse / lookup：根据 prefix、block 或 request identity 查找可复用状态；
3. eviction / demotion：容量受压时删除或下沉低价值 KV；
4. prefetch / promotion：在真正访问前把慢层 KV 拉回快层；
5. placement / tiering：在 HBM、Host DRAM、SSD 与远端层之间放置数据；
6. transfer / consistency：跨设备、worker 或存储层移动 KV，并维护可解释的 metadata。

这样把 eviction 与 prefetch 视为 KV 生命周期管理的策略动作，而不是独立的顶层 ontology 节点。

## 细分与相邻概念

- [[KV Cache Offloading]]：把 KV 从主加速器层移到更便宜的层。
- [[Tiered KV Cache]]：把多个存储层组织成统一缓存层次。
- [[KV Cache Transfer]]：负责跨设备、worker 与存储层的数据移动。
- [[KV Cache Sharing]]：让不同 serving instance 复用已经存在的 KV。
- [[Prefix Caching]]：按共享前缀命中并复用 KV。
- [[Remote KV Store]]：把 KV 生命周期扩展到 worker 之外的共享存储。
- eviction / prefetch：作为本页 lifecycle policy 的组成部分，不再单独建 concept。

## 代价与适用边界

更复杂的 KV 管理可以提升容量和复用率，但也会引入元数据、查找、搬运、同步与一致性成本。低并发、短上下文场景往往不需要复杂的跨层管理。

## 项目实现

[[community/LMCache/LMCache/LMCache|LMCache]] 明确定位为 KV cache management layer；[[community/vllm-project/vLLM/vLLM|vLLM]] 在 serving runtime 内管理 KV block、prefix cache、connector 与 offloading；[[community/sgl-project/SGLang/SGLang|SGLang]] 通过 RadixAttention / HiCache 管理本地与外部 KV。

[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]、[[community/Ascend/MemCache/MemCache|MemCache]]、[[community/taco-project/FlexKV/FlexKV|FlexKV]] 与 [[community/novitalabs/pegaflow/pegaflow|PegaFlow]] 分别提供分布式、多级或独立生命周期的 KV 管理能力；[[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] 通过 KV Pool / AscendStore backend 暴露异构 KV 管理路径。[[community/modelsphere/ModelSphere/ModelSphere|ModelSphere]]、[[community/ThinkFlowLab/vllm-rlt/vllm-rlt|vllm-rlt]] 与 [[community/openJiuwen-ai/AgentInfer/AgentInfer|AgentInfer]] 则把 KV 管理进一步接到平台调度、recurrent model 或 agent inference 场景。

## Sources

- https://docs.lmcache.ai/
- https://docs.vllm.ai/en/stable/
