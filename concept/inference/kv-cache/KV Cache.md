---
type: concept
name: KV Cache
aliases:
  - Key-Value Cache
  - KV缓存
domain: inference
topic: kv-cache
related_concepts:
  - KV Cache Management
  - Prefix Caching
projects:
  - vLLM
  - SGLang
last_verified: 2026-09
---

# KV Cache

## 一句话定义

KV Cache 是自回归 Transformer 推理时保存历史 token 的 attention Key/Value 状态的缓存，使后续 token 不必重新计算完整前缀的 K/V。

## 解决的问题

如果每生成一个 token 都重新计算整个历史序列，decode 的重复计算会随上下文不断放大。KV Cache 用显存或其他存储空间换取计算复用，是现代 LLM serving 的基础状态。

## 核心机制

Prefill 阶段批量处理输入 token 并生成初始 KV；Decode 阶段每一步只计算新增 token 的 K/V，同时读取历史 KV 完成 attention。随着上下文、batch 和并发增长，KV Cache 会逐渐成为容量、带宽和调度的重要约束。

## 细分与相邻概念

- [[KV Cache Management]]：如何分配、复用、迁移、回收 KV。
- [[Prefix Caching]]：跨请求复用相同前缀对应的 KV。
- [[KV Cache Offloading]]：把部分 KV 从主加速器内存移到更便宜的存储层。
- [[KV Cache Transfer]]：在 worker、设备或存储层之间移动 KV 数据。

## 代价与适用边界

KV Cache 能显著减少重复计算，但会消耗与序列长度、层数、KV head 数和数据类型相关的存储空间。长上下文和高并发场景通常需要把“是否能算”进一步转化为“KV 能否高效放置和移动”的系统问题。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 把 KV 内存管理作为核心 serving 能力，并提供 prefix caching、KV connector、offloading 等机制。[[community/sgl-project/SGLang/SGLang|SGLang]] 通过 RadixAttention / Radix Cache 对可复用前缀 KV 进行管理。

## Sources

- https://docs.vllm.ai/en/stable/
- https://docs.sglang.ai/
