---
type: concept
name: Request Routing
aliases:
  - Inference Request Routing
  - 请求路由
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Inference Scheduling
related_concepts:
  - Inference-Aware Routing
  - Load Balancing
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - Gateway API Inference Extension
  - KServe
  - MindIE-Motor
last_verified: 2026-09
---

# Request Routing

## 一句话定义

Request Routing 是为每个进入 serving 系统的推理请求选择目标模型实例、worker 或服务路径的过程。

## 解决的问题

当一个模型有多个 replica，或者服务包含 Prefill/Decode 等多个角色时，请求必须被送到正确的 endpoint。最基础策略可以是 round-robin 或 random，但 LLM 请求成本差异很大，简单策略通常无法利用缓存局部性或实时负载信息。

## 核心机制

Router 先得到候选 endpoint 集合，再根据可用性、模型/adapter、负载、KV cache、请求属性或拓扑约束过滤和打分，最后选择目标 endpoint 并把请求转发过去。

## 细分概念

- [[Inference-Aware Routing]]：让路由器理解 LLM serving 特有状态。
- [[KV-Aware Routing]]：根据可复用 KV/prefix 状态做路由。
- [[Load-Aware Routing]]：根据队列、并发、token load 等运行时负载做路由。

## 与 Load Balancing 的区别

Routing 是一次请求的“去哪儿”决策；[[Load Balancing]] 是多次 routing 决策形成的长期负载分布目标。一个 routing algorithm 可以同时实现 cache locality 和 load balancing，但两个概念不应合并。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]]、[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]]、[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 都包含独立的 LLM router。[[community/kubernetes-sigs/Gateway-API-Inference-Extension/Gateway-API-Inference-Extension|Gateway API Inference Extension]] 定义 InferencePool + Endpoint Picker 路由语义；[[community/kserve/KServe/KServe|KServe]] 的 LLMInferenceService 可通过 inference gateway/scheduler 进行 endpoint routing；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 的 Coordinator 负责 P/D worker 调度。

## Sources

- https://llm-d.ai/docs/dev/architecture/core/router/epp
- https://docs.nvidia.com/dynamo/latest/knowledge-base/modular-components/router/routing-concepts
- https://github.com/vllm-project/aibrix
- https://gateway-api-inference-extension.sigs.k8s.io/
- https://kserve.github.io/website/
- https://gitcode.com/Ascend/MindIE-Motor
