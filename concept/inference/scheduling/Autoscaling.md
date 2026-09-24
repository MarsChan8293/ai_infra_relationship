---
type: concept
name: Autoscaling
aliases:
  - Inference Autoscaling
  - LLM Autoscaling
  - 自动扩缩容
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Inference Scheduling
related_concepts:
  - Load Balancing
  - Capacity Planning
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - KServe
  - MindIE-Motor
last_verified: 2026-09
---

# Autoscaling

## 一句话定义

Autoscaling 根据推理负载自动增加或减少 model server / worker 数量，使 serving capacity 跟随需求变化。

## 解决的问题

固定副本数必须在“高峰不够”和“低谷浪费 GPU”之间取舍。传统 CPU/GPU utilization 又未必能反映 LLM 是否即将排队，因为 continuous batching 下 GPU 很容易长期保持高利用率。

## 核心机制

LLM autoscaler 更适合使用 queue depth、running requests、token backlog、KV cache pressure、TTFT/TPOT SLO 或推导出的 desired replicas 作为信号。控制回路通常包括观测、容量估计、期望 replica 数计算和实际扩缩容执行。

## 与 Capacity Planning 的关系

[[Capacity Planning]] 估计“当前/未来需要多少资源”，Autoscaling 把这种估计变成在线闭环动作。Capacity Planning 可以离线进行，也可以实时为 HPA/KEDA 等 autoscaler 提供指标。

## 代价与适用边界

LLM worker 启动通常需要加载大权重，scale-up 延迟远高于普通 Web Pod。过于激进的扩缩会产生冷启动和抖动，因此 hysteresis、cooldown、预热和模型缓存都很重要。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]] 提供基于 EPP/KEDA 的 queue、token backlog 和 SLO-aware autoscaling；[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] 将 autoscaling 作为分布式 inference 核心能力；[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 提供 LLM app-tailored autoscaler；[[community/kserve/KServe/KServe|KServe]] 的 LLMInferenceService 支持 WVA/KEDA/HPA 路径；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 暴露容量规划指标供 HPA/外部控制器消费。

## Sources

- https://llm-d.ai/docs/dev/architecture/advanced/autoscaling
- https://docs.nvidia.com/dynamo/
- https://github.com/vllm-project/aibrix
- https://kserve.github.io/website/docs/next/model-serving/generative-inference/llmisvc/autoscaling/llmisvc-autoscaling-examples
- https://gitcode.com/Ascend/MindIE-Motor
