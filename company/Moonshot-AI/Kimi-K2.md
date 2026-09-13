---
type: model-project
company: Moonshot AI
model: Kimi-K2
areas: [moe, agentic]
public_repo: true
---
# Kimi K2

## 项目简介
Kimi K2 是 Moonshot AI 的公开模型系列，采用 MoE 路线并强调 agentic 能力。对 AI Infra 图谱而言，它把模型侧的 MoE、长上下文和 agent workload 与 Moonshot 自研 communication / serving 系统连接起来。

## GitHub
https://github.com/MoonshotAI/Kimi-K2

## 主要维护者 / 组织
由 [[Moonshot-AI]] / MoonshotAI 组织公开维护。模型仓库与权重开放策略不自动等同于传统软件项目的 OSI 开源定义，因此本页记录为 public repository/model project。

## 本图谱人物
- [[Guanduo Chen]]：技术报告作者；Training Infra MTS
- [[吴育昕 Yuxin Wu]]：个人页列为 selected publication / Kimi Team
- [[杨植麟 Zhilin Yang]]：Moonshot 创始人与模型战略负责人

## Infra 关系
- MoE / EP 路线 → [[MoonEP]]
- KV / long-context serving → [[Mooncake]]
- 部署生态 → [[vLLM]] / [[SGLang]]

## Sources
- https://github.com/MoonshotAI/Kimi-K2
