---
type: infra-project
name: Checkpoint Engine
company: 月之暗面
areas: [reinforcement-learning, weight-transfer, checkpoint-loading, distributed-training, inference-serving, rdma]
layer: training-serving-data-plane
open_source: true
repository: https://github.com/MoonshotAI/checkpoint-engine
related_projects: [Mooncake, SGLang, vLLM, Kimi-K2]
last_verified: "2026-09"
---
# Checkpoint Engine

## 项目简介
Checkpoint Engine 是 Moonshot AI 开源的模型权重更新中间件，用于训练/RL 流程向在线 inference engine 高效更新模型权重。官方 README 给出的 Kimi-K2 生产路径可在数千 GPU 上完成 1T 参数模型更新，并同时支持 broadcast 与 P2P 两类更新模式。

## Mooncake 关系
P2P 更新路径直接依赖 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake Transfer Engine]]，从已有 inference instance 的 CPU 内存向新加入实例的 GPU 发送权重。Mooncake/TENT 的 2026 论文也把 Checkpoint Engine 作为 RL parameter-update 场景之一，说明两者已经形成生产级训练 ↔ 推理数据平面关系。

## Serving 生态
- [[vLLM]]：官方 README 的主要 inference engine 测试路径之一。
- [[SGLang]]：Checkpoint Engine 提供专门的分布式 checkpoint loading / weight-update 集成路径。
- [[Kimi-K2]]：项目 README 明确以 Kimi-K2 千卡/千 GPU 级权重更新作为生产案例。

## Sources
- https://github.com/MoonshotAI/checkpoint-engine
- https://github.com/kvcache-ai/Mooncake
- https://arxiv.org/abs/2604.00368
