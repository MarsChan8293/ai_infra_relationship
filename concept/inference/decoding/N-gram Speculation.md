---
type: concept
name: N-gram Speculation
aliases:
  - N-gram Speculative Decoding
  - Prompt Lookup Decoding
  - Prompt Lookup Speculation
  - N-gram投机解码
domain: inference
topic: decoding
parent_concepts:
  - Speculative Decoding
related_concepts:
  - Draft-Target Decoding
projects:
  - vLLM
last_verified: 2026-09
---

# N-gram Speculation

## 一句话定义

N-gram Speculation 不使用额外 draft model，而是根据最近生成的 token 在 prompt 或已有上下文中寻找匹配 n-gram，并把匹配位置后面的 token 当作候选继续序列。

## 解决的问题

代码补全、文档问答、agent loop 等 workload 往往存在大量复制、模板和重复片段。既然候选可能已经出现在上下文里，就可以用廉价查找替代一次神经网络 draft forward。

## 核心机制

系统取当前尾部若干 token 作为 lookup key，在可搜索 token 序列中寻找相同片段，并提出其后续 token。Target model 仍负责最终 verification，因此该技术属于 [[Speculative Decoding]] 而不是普通缓存命中。

## 与相邻概念的区别

- 与 [[Prefix Caching]] 不同，Prefix Caching 复用的是已经计算好的 KV；N-gram speculation 复用的是“可能的输出 token 模式”。
- 与 [[Draft-Target Decoding]] 不同，它没有额外神经网络 draft model。
- Suffix Decoding 是更丰富的模式匹配路线，可同时利用 prompt 和历史 generation、频次信息以及动态 speculation length。

## 代价与适用边界

高度重复 workload 往往收益明显；开放式生成若很少出现可预测重复片段，lookup 命中和 acceptance rate 都会降低。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 当前 speculative config 提供 `ngram` proposer，并暴露 prompt lookup window 配置；同时也支持更丰富的 Suffix Decoding。

## Sources

- https://docs.vllm.ai/en/latest/features/spec_decode/
- https://docs.vllm.ai/en/stable/api/vllm/config/speculative/
- https://docs.vllm.ai/en/latest/features/speculative_decoding/suffix/
