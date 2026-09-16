---
type: model-project
name: Grok-1
model: Grok-1
company: xAI
areas: [moe, open-weights, model-inference, jax]
public_repo: true
repository: https://github.com/xai-org/grok-1
open_weights: true
last_verified: "2026-09"
---
# Grok-1

## 项目简介

Grok-1 是 xAI 公开的 314B MoE 模型及 JAX reference implementation。官方仓库提供模型加载、checkpoint 与采样示例，是 xAI 当前最直接可核验的公开模型工程节点之一。

## AI Infra 边界

Grok-1 仓库 README 明确说明其中 MoE 实现以正确性验证为目标，并非高效 production inference implementation。因此本图谱把它作为 xAI 的公开模型/参考执行节点，不把它误写成 xAI 内部 production serving stack。

xAI 官方 GitHub 组织还公开 xAI SDK、protobuf、Grok Build 等项目，但它们分别偏 API 客户端、接口定义和 coding-agent tooling；本轮不为了填满项目数量而把这些全部扩成推理优化节点。

## Sources
- https://github.com/xai-org/grok-1
- https://github.com/xai-org
