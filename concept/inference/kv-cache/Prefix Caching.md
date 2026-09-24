---
type: concept
name: Prefix Caching
aliases:
  - Automatic Prefix Caching
  - APC
  - Prefix KV Caching
  - 前缀缓存
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - KV Cache Sharing
  - Continuous Batching
projects:
  - vLLM
  - SGLang
last_verified: 2026-09
---

# Prefix Caching

## 一句话定义

Prefix Caching 缓存已经处理过的共享 prompt 前缀对应的 KV，使后续具有相同前缀的请求跳过这部分 prefill 计算。

## 解决的问题

系统提示词、长文档、多轮对话历史和 agent context 往往会在多个请求中重复出现。若每次都重新 prefill，GPU 会重复做已经完成过的 attention 计算。

## 核心机制

运行时把 token prefix 与对应 [[KV Cache]] block 建立可查找的映射。新请求到达时先寻找最长可复用前缀，只为 miss 的后续 token 计算新 KV。缓存通常还需要哈希、引用计数或淘汰策略来管理生命周期。

## 与相邻概念的区别

- Prefix Caching 依赖“token 前缀相同”这一复用条件。
- [[KV Cache Sharing]] 把这种复用扩展到多个实例。
- 非 prefix reuse（例如对 prompt 中间片段进行重用）属于更广义的 KV reuse，不应都叫 prefix caching。

## 代价与适用边界

命中率取决于 workload 是否真的共享长前缀。缓存本身仍占 KV 容量，低重复 workload 可能主要付出元数据和容量成本而得不到计算复用。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 Automatic Prefix Caching。[[community/sgl-project/SGLang/SGLang|SGLang]] 的 RadixAttention / Radix Cache 以 radix tree 组织可复用 prefix KV。

## Sources

- https://docs.vllm.ai/en/stable/design/prefix_caching/
- https://docs.vllm.ai/en/v0.26.0/features/automatic_prefix_caching/
- https://docs.sglang.ai/
