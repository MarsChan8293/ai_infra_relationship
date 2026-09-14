---
type: model-project
company: 月之暗面
model: Kimi-K3
areas: [multimodal, long-context, agentic]
public_repo: true
---
# Kimi K3

## 项目简介
Kimi K3 是 Moonshot AI 2026 年公开的 frontier-model 项目。官方仓库将其描述为 2.8T 参数模型，并强调 Kimi Delta Attention、Attention Residuals、原生视觉与 1M context。它把超长上下文、多模态和 agentic workload 同时推到 serving 系统前台。

## GitHub
https://github.com/MoonshotAI/Kimi-K3

## 主要维护者 / 组织
由 [[月之暗面]] / MoonshotAI 组织公开维护。该仓库于 2026-07 创建，是当前 Kimi K3 的 canonical GitHub 项目入口。

## 本图谱人物
[[杨植麟 Zhilin Yang]] · [[Guanduo Chen]]

## 系统关系
- 长上下文 → KV cache 容量、传输与复用压力，可连接 [[Mooncake]] / [[NIXL]]。
- agentic / multimodal workload → routing、batching 与 heterogeneous serving，可连接 [[vLLM]] / [[SGLang]]。
- Moonshot 自研 MoE communication 路线 → [[MoonEP]]。

## Sources
- https://github.com/MoonshotAI/Kimi-K3
