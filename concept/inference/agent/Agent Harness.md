---
type: concept
name: Agent Harness
aliases:
  - Agent Runtime Harness
  - Agent Execution Harness
  - 智能体运行时框架
domain: inference
topic: agent-runtime
related_concepts:
  - Agentic Inference Optimization
  - Agent Skill
projects:
  - DeepSeek Harness
  - Humanize
last_verified: "2026-10"
---
# Agent Harness

## 一句话定义
Agent Harness 是承载 LLM agent 运行生命周期的 runtime / control layer：负责 model call、tool registry、session/context、permissions/sandbox、subagent/protocol integration 与 durable execution state，而不是模型推理 kernel 本身。

## 与普通 Agent Framework 的区别
“Agent framework”常泛指 prompt、graph 或 workflow SDK；Harness 更强调运行时契约，例如工具调用如何授权、session 如何持久化、失败/重试如何记录、外部 protocol 如何进入 agent loop，以及不同 model/tool backend 是否可以被替换。

## 与 Agent Skill 的区别
[[concept/inference/agent/Agent Skill|Agent Skill]] 封装领域知识、执行步骤和证据规则；Harness 则负责把 agent 真正运行起来。可以把两者理解为“Skill 决定某类任务怎么做，Harness 决定 agent 如何执行、授权、持久化和组合”。

## 项目实现
[[community/deepseek-ai/DeepSeek-Harness/DeepSeek-Harness|DeepSeek Harness]] 把 model adapter、tool registry、session log、agent loop 等都做成 Cordis plugin，并提供 MCP、ACP、sandbox、Web/headless/SDK 等运行面，是典型的 Agent Harness 实现。

[[community/humanfia/humanize/humanize|Humanize]] 把 Claude Code、Codex、Kimi Code、DeepSeek Harness、LiteLLM / ACP 等 backend 组织成可执行 agent flow，更偏多 backend flow orchestration；其中 DeepSeek Harness 是其直接支持的 backend。

## 与 AI Infra 的边界
Agent Harness 位于模型 serving 之上。它可以调用 vLLM、MindIE、SGLang 等推理服务，但“能调用某个 API”不等于项目级 integration；强边仍需 adapter/plugin 或官方文档证据。

Agent Harness 也不自动等于 [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]：只有当 runtime 进一步包含可验证的 baseline、measurement、correctness、promotion / rollback 等控制环时，才构成完整的 autonomous optimization system。

## Sources
- https://github.com/deepseek-ai/deepseek-harness
- https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md
- https://github.com/humanfia/humanize
- https://docs.humanfia.ai/humanize/
