---
type: project
name: Miles
companies: ["RadixArk"]
company_relation: company-led
layer: post-training-infrastructure
open_source: true
repository: https://github.com/radixark/miles
areas: [reinforcement-learning, post-training, distributed-training, rollout, sglang, weight-transfer]
people:
  - "company/RadixArk/朱邦华 Banghua Zhu"
last_verified: "2026-09"
---
# Miles

## 项目简介
Miles 是 RadixArk 面向大规模模型 post-training 的开源强化学习基础设施。官方项目将其定位为 enterprise-grade reinforcement learning framework：使用 [[SGLang]] 做高吞吐 rollout，以 Megatron-LM / FSDP2 等后端做训练，并覆盖异步 RL、P2P 权重更新、低精度训练、LoRA 与大规模 MoE 路由一致性。

## 组织与人物连接
- [[company/RadixArk/朱邦华 Banghua Zhu|朱邦华]]：个人主页明确将 Miles 与 SGLang 一起列为 RadixArk 团队构建的 open AI infra；其 CTO 职责覆盖公司整体 AI infrastructure 技术方向。
- [[RadixArk]]：官方仓库位于 `radixark/miles`，项目 README 明确以 RadixArk 品牌发布。

## 与推理基础设施的连接
Miles 的 rollout 层直接依赖 SGLang，并提供大模型 RL 训练到推理引擎之间的快速权重同步，因此它是“serving → post-training → serving”闭环的重要节点，而不只是训练框架。

## Sources
- https://github.com/radixark/miles
- https://banghua.me/
