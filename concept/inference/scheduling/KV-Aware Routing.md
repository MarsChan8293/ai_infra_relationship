---
type: concept
name: KV-Aware Routing
aliases:
  - KV Cache-Aware Routing
  - Prefix-Cache Aware Routing
  - Prefix-Aware Routing
  - KV感知路由
  - 前缀缓存感知路由
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Inference-Aware Routing
related_concepts:
  - Prefix Caching
  - KV Cache Sharing
  - Load-Aware Routing
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - KServe
  - MindIE-Motor
last_verified: 2026-09
---

# KV-Aware Routing

## 一句话定义

KV-Aware Routing 根据各 worker 已持有的 [[KV Cache]] / prefix 状态选择请求目标，尽量把请求送到可以复用已有 KV 的实例。

## 解决的问题

分布式 serving 中，同一个长系统提示词或多轮会话可能被路由到不同 replica。若目标 worker 没有匹配 prefix，就必须重新 Prefill。普通 round-robin 会丢失这种计算局部性。

## 核心机制

Router 为请求 prefix 建立 hash/token 表示，并维护每个 worker 当前拥有的 KV block 或近似历史。到达新请求时计算 prefix overlap，再结合 worker 当前负载形成 cost/score，选择“缓存收益高且不过载”的 endpoint。

## 精确与近似

- 精确方案：消费 model server 的 KV lifecycle events，维护真实 KV index。
- 近似方案：根据历史路由结果推测 prefix 所在 worker，控制面更轻，但可能与真实 eviction 状态偏离。
- 实际系统通常还会叠加 [[Load-Aware Routing]]，避免所有相似请求挤到一个 cache-rich worker。

## 与相邻概念的区别

[[Prefix Caching]] 解决“能否复用前缀”；KV-aware routing 解决“哪个 worker 最值得复用”。[[KV Cache Sharing]] 则允许 KV 跨实例搬运，可能降低必须路由到原 owner 的约束。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]] 支持 approximate / precise prefix-cache aware routing；[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] router 使用 reusable KV state + active load；[[community/vllm-project/AIBrix/AIBrix|AIBrix]] gateway 支持 prefix-cache routing profile；[[community/kserve/KServe/KServe|KServe]] 可通过 inference gateway prefix-cache scorer 做 prefix-aware routing；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 的 KV Conductor / cache affinity 调度利用 KV event 与缓存匹配进行请求放置。

## Sources

- https://llm-d.ai/docs/dev/architecture/advanced/kv-management/prefix-cache-aware-routing
- https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/system-architecture/kv-aware-routing
- https://github.com/vllm-project/aibrix/blob/main/docs/source/production/gateway.rst
- https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-envoy-ai-gateway
- https://gitcode.com/Ascend/MindIE-Motor
