---
type: concept
name: Inference-Aware Routing
aliases:
  - LLM-Aware Routing
  - Model-Aware Routing
  - 推理感知路由
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Request Routing
related_concepts:
  - KV-Aware Routing
  - Load-Aware Routing
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - Gateway API Inference Extension
  - KServe
last_verified: 2026-09
---

# Inference-Aware Routing

## 一句话定义

Inference-Aware Routing 是利用 LLM serving 特有的模型状态和请求特征，而不是只看网络连接数，来选择推理 endpoint 的路由方式。

## 解决的问题

传统 L4/L7 负载均衡通常假设请求成本相近，但 LLM 请求可能有完全不同的 prompt 长度、输出长度、KV prefix 命中、LoRA adapter、队列长度和 SLO。只看连接数很容易把“看起来空闲但实际要做大量 Prefill”的请求送错位置。

## 核心机制

Inference-aware router 会收集模型服务内部指标或请求属性，并将其转成 endpoint filter / score。常见信号包括 KV cache 命中、queue depth、running requests、token load、adapter availability 和预测 TTFT/ITL。

## 细分概念

- [[KV-Aware Routing]]：优先复用已有 KV/prefix。
- [[Load-Aware Routing]]：优先避开高队列、高 token load 或高并发 endpoint。
- 两者常被组合成一个 cost model，在 cache locality 与负载均衡之间做权衡。

## 代价与适用边界

更智能的路由需要 endpoint 暴露指标、事件或 tokenizer 信息。若状态更新不及时，router 可能依据过期信息做出错误选择，因此 freshness 与控制面开销是重要边界。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]] EPP 以 KV、队列、running requests 等状态打分；[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] router 结合 cache overlap 和 projected load；[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 提供 LLM-specific routing；[[community/kubernetes-sigs/Gateway-API-Inference-Extension/Gateway-API-Inference-Extension|Gateway API Inference Extension]] 通过 EPP 标准化 inference-aware endpoint selection；[[community/kserve/KServe/KServe|KServe]] 可使用该类 scheduler/routing 机制。

## Sources

- https://llm-d.ai/docs/dev/architecture/core/router/epp
- https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/system-architecture/kv-aware-routing
- https://github.com/vllm-project/aibrix
- https://gateway-api-inference-extension.sigs.k8s.io/
- https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-envoy-ai-gateway
