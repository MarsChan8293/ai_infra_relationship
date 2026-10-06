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
  - "Request Routing"
  - "Autoscaling"
  - "P-D Disaggregation"
projects:
  - "llm-d"
  - "NVIDIA Dynamo"
  - "AIBrix"
  - "MindIE-Motor"
  - "AgentInfer"
  - "vllm-rlt"
  - "GPUStack"
  - "Ray Serve"
  - "vLLM Production Stack"
last_verified: 2026-10
---

# Inference Scheduling

## 一句话定义

Inference Scheduling 是在多个请求、worker、资源池和推理阶段之间决定“谁先执行、在哪执行、用多少资源”的控制机制。

## 解决的问题

LLM 请求具有输入长度、输出长度、KV 命中、模型/LoRA、优先级和延迟目标等巨大差异。只按到达顺序或简单轮询分配请求，很容易造成某些 worker 排队、KV 复用丢失、Prefill/Decode 相互干扰或资源配比失衡。

## 核心机制

推理调度通常包含三层决策：

1. 请求级：哪个请求先被处理；
2. worker 级：请求应该发送到哪个 replica / endpoint，由 [[Request Routing]] 承担；
3. 资源级：需要多少 worker、哪类硬件以及 P/D 等不同角色如何配比。

容量估算（过去单列为 Capacity Planning）属于资源级调度的一部分：根据 arrival rate、输入/输出 token 分布、单实例吞吐和 SLO 估算 replica 数与 P:D 比例。负载均衡则是连续 routing 决策形成的运行结果，不再维护独立 canonical node。

## 与相邻概念的区别

- [[Request Routing]] 决定单个请求的目标 endpoint，并承担负载均衡目标。
- [[Autoscaling]] 改变 endpoint 数量；其 desired replicas 可以来自容量估算模型。
- Engine 内部的 [[Continuous Batching]] 也是调度，但作用域是一个 engine 内部的执行 batch。
- [[P-D Disaggregation]] 改变 worker 角色划分，调度器需要进一步决定 P:D 资源配比。

## 代价与适用边界

调度器越了解模型内部状态，决策可能越好，但需要采集更多指标、KV 状态和预测数据。状态同步开销过大或信息过时时，复杂调度未必优于简单策略。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]] 的 Router/EPP 与 autoscaling 路径覆盖 endpoint scoring、队列/token backlog 和 serving capacity；[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] 在 frontend/router 中进行 worker 选择与弹性伸缩；[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 提供 gateway/routing/autoscaling；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 由 Coordinator 负责 P/D 实例调度并公开容量估算指标。

[[community/gpustack/GPUStack/GPUStack|GPUStack]] 明确提供异构 GPU/NPU 资源调度与 distributed model-serving control plane；[[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]] 提供 replica scheduling/routing/autoscaling；[[community/vllm-project/production-stack/vLLM Production Stack|vLLM Production Stack]] 以多实例 vLLM + request router 组成 Kubernetes production serving。

## Sources

- https://llm-d.ai/docs/architecture/core/router/epp/scheduling
- https://docs.nvidia.com/dynamo/latest/knowledge-base/modular-components/router/routing-concepts
- https://github.com/vllm-project/aibrix
- https://gitcode.com/Ascend/MindIE-Motor
