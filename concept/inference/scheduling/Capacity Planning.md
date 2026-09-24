---
type: concept
name: Capacity Planning
aliases:
  - Inference Capacity Planning
  - LLM Capacity Planning
  - 容量规划
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Inference Scheduling
related_concepts:
  - Autoscaling
  - P-D Disaggregation
projects:
  - llm-d
  - MindIE-Motor
last_verified: 2026-09
---

# Capacity Planning

## 一句话定义

Capacity Planning 是根据请求速率、输入/输出 token 分布、模型吞吐和 SLO，估计需要多少推理实例以及不同角色之间应如何配比。

## 解决的问题

“GPU 利用率 80%”无法直接回答需要几个 Prefill worker、几个 Decode worker，也无法告诉平台在流量翻倍时要提前准备多少实例。对于 [[P-D Disaggregation]]，P 和 D 的资源需求甚至会随输入/输出比例变化。

## 核心机制

容量模型通常把 workload 拆成到达率、平均/分位输入 token、输出 token 和目标延迟，再结合单实例 prefill tokens/s、decode tokens/s 或经验性能曲线推导所需 replica 数。在线系统还可以持续学习实际吞吐，修正静态 benchmark 的偏差。

## 与 Autoscaling 的区别

[[Autoscaling]] 是执行闭环；Capacity Planning 是估算模型。前者可以使用后者的结果作为 desired replicas，也可以采用更直接的 queue/SLO 控制律。

## P/D 场景

P/D 分离后，Prefill 更偏 FLOPs-bound，Decode 更偏 memory-bandwidth-bound。容量规划因此不仅要算总实例数，还要估算 P:D 比例，并在 workload 输入/输出结构变化时重新调整。

## 项目实现

[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] Coordinator 已公开容量规划指标设计，根据入口流量与 P/D 单实例在线吞吐推导所需实例数量。[[community/llm-d/llm-d/llm-d|llm-d]] 的 autoscaling 体系使用 queue、token backlog、KV pressure 与 latency SLO 推导 serving capacity / desired replicas。

## Sources

- https://gitcode.com/Ascend/MindIE-Motor/pull/946
- https://llm-d.ai/docs/dev/architecture/advanced/autoscaling
- https://llm-d.ai/docs/well-lit-paths/foundations/workload-autoscaling
