---
type: concept
name: Inference Scheduling
aliases:
  - LLM Inference Scheduling
  - 推理调度
  - LLM推理调度
domain: scheduling
topic: inference-scheduling
related_concepts:
  - Request Routing
  - Load Balancing
  - Autoscaling
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - MindIE-Motor
last_verified: 2026-09
---

# Inference Scheduling

## 一句话定义

Inference Scheduling 是在多个请求、worker、资源池和推理阶段之间决定“谁先执行、在哪执行、用多少资源”的控制机制。

## 解决的问题

LLM 请求具有输入长度、输出长度、KV 命中、模型/LoRA、优先级和延迟目标等巨大差异。只按到达顺序或简单轮询分配请求，很容易造成某些 worker 排队、KV 复用丢失、Prefill/Decode 相互干扰或资源配比失衡。

## 核心机制

推理调度通常包含三层决策：

1. 请求级：哪个请求先被处理。
2. worker 级：请求应该发送到哪个 replica / endpoint。
3. 资源级：需要多少 worker、哪类硬件以及 P/D 等不同角色如何配比。

因此 [[Request Routing]]、[[Load Balancing]]、[[Autoscaling]] 都属于 inference scheduling 的不同控制环节。

## 与相邻概念的区别

- Routing 决定单个请求的目标 endpoint。
- Load balancing 关注一段时间内工作如何在多个 endpoint 之间分布。
- Autoscaling 改变 endpoint 数量，而不是仅在已有 endpoint 中选一个。
- Engine 内部的 [[Continuous Batching]] 也是调度，但作用域是一个 engine 内部的执行 batch。

## 代价与适用边界

调度器越了解模型内部状态，决策可能越好，但需要采集更多指标、KV 状态和预测数据。状态同步开销过大或信息过时时，复杂调度未必优于简单策略。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]] 的 Router/EPP 负责 endpoint scoring、请求优先级与分布式 serving 调度；[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] 在 frontend/router 中进行 worker 选择；[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 提供 gateway/routing/autoscaling；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 由 Coordinator 负责 P/D 实例调度和负载均衡。

## Sources

- https://llm-d.ai/docs/architecture/core/router/epp/scheduling
- https://docs.nvidia.com/dynamo/latest/knowledge-base/modular-components/router/routing-concepts
- https://github.com/vllm-project/aibrix
- https://gitcode.com/Ascend/MindIE-Motor
