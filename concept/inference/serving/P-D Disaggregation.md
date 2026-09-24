---
type: concept
name: P-D Disaggregation
aliases:
  - PD Disaggregation
  - P/D Disaggregation
  - Prefill-Decode Disaggregation
  - Prefill Decode Disaggregation
  - PD分离
  - 预填充解码分离
domain: inference
topic: serving
parent_concepts:
  - Disaggregated Serving
related_concepts:
  - KV Cache Transfer
  - Chunked Prefill
projects:
  - vLLM
  - SGLang
  - LMCache
  - Mooncake
  - Dynamo
last_verified: 2026-09
---

# P-D Disaggregation

## 一句话定义

P-D Disaggregation 把 LLM 的 Prefill 和 Decode 放到不同 worker / GPU 资源池执行，由 Prefill 计算初始 KV，再把 KV 交给 Decode 继续逐 token 生成。

## 解决的问题

Prefill 通常更偏计算密集，Decode 则更受 KV 容量、内存带宽和并发影响。统一调度时，长 prefill 还可能干扰正在进行的 decode，抬高 inter-token latency。拆分后两种阶段可以使用不同的副本数、并行策略和硬件配置。

## 核心机制

一次典型请求包含三步：

1. Prefill worker 处理 prompt 并生成 [[KV Cache]]。
2. 通过 [[KV Cache Transfer]] 将对应 KV 送往 Decode worker。
3. Decode worker 从该状态继续 autoregressive generation。

Router 还需要完成 P/D worker 选择、容量匹配、handoff metadata 管理和失败处理。

## 与相邻概念的区别

- [[Disaggregated Serving]] 是上位架构，P/D 是其中一种具体切分。
- [[Chunked Prefill]] 仍可在统一 engine 内把大 prefill 切片调度，不要求 P/D 使用不同 worker。
- P/D 本身不意味着吞吐一定提高，收益取决于 workload、资源配比和 KV transfer 成本。

## 代价与适用边界

核心新增成本是 KV 传输和两个资源池的碎片化。网络较慢、prompt 很短或负载较低时，transfer/handoff 可能比阶段隔离带来的收益更大。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 experimental Disaggregated Prefilling 与多种 KV connector。[[community/sgl-project/SGLang/SGLang|SGLang]] 支持 Mooncake、NIXL 等 transfer backend。[[community/LMCache/LMCache/LMCache|LMCache]] 可作为 vLLM 的 KV transfer layer。[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 提供 Transfer Engine 和 KVCache-centric P/D 架构。[[community/ai-dynamo/Dynamo/Dynamo|Dynamo]] 负责 P/D worker pool、路由和 NIXL transfer orchestration。

## Sources

- https://docs.vllm.ai/en/latest/features/disagg_prefill/
- https://docs.sglang.ai/backend/pd_disaggregation.html
- https://docs.lmcache.ai/getting_started/quickstart/disaggregated_prefill.html
- https://kvcache-ai.github.io/Mooncake/
- https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving
