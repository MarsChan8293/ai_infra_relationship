---
type: project
name: Humanize
layer: runtime
status: active
repository: https://github.com/humanfia/humanize
docs: https://docs.humanfia.ai/humanize/
last_verified: "2026-10"
areas:
  - "agent-harness"
  - "agent-flow"
  - "coding-agent-orchestration"
  - "multi-backend-agent"
  - "deepseek-harness"
  - "agent-client-protocol"
  - "workflow-runtime"
code_availability: public
integrations:
  - "DeepSeek Harness"
---

# Humanize

## 项目简介

Humanize（CLI 为 `hmz`）是 humanfia 开源的 agent flow system，用于把多个 coding-agent / model backend 编排为可执行 flow。它位于模型 serving 之上，核心对象是 agent、flow、backend、工作目录与运行权限，而不是 LLM kernel 或 serving scheduler。

## Agent Harness 定位

Humanize 属于 [[concept/inference/agent/Agent Harness|Agent Harness]]：它负责把不同 agent backend 放进统一 flow，并提供 CLI / TUI 运行面。官方文档和代码中存在明确的 harness abstraction，能够驱动 Claude Code、Codex、Kimi Code、DeepSeek Harness 等 coding-agent backend，也可以通过 LiteLLM 直接调用模型。

其中 DeepSeek Harness 是直接、可核验的 backend：项目提供 `[dsh]` extra，并在 flow/reference 文档中把 `dsh` 映射为 `DeepSeekHarnessAgent`。因此这里建立到 [[community/deepseek-ai/DeepSeek-Harness/DeepSeek-Harness|DeepSeek Harness]] 的 integration 关系。

## 与 DSH 的层次关系

Humanize 与 DeepSeek Harness 不是替代关系。DSH 自身提供 agent runtime、plugin tree、session、tool、sandbox、MCP/ACP 等能力；Humanize 更偏上层 flow orchestration，可以把 DSH 与其他 agent backend 作为同一工作流中的可选执行器。

```text
Humanize flow
  ├─ Claude Code
  ├─ Codex
  ├─ Kimi Code
  ├─ DeepSeek Harness
  └─ LiteLLM / ACP backend
```

## 安全边界

Humanize 官方文档明确提示 flow 中的 agent 会绕过交互式 approvals，并可能直接编辑文件、执行命令和提交代码，因此建议先在 scratch repository 中运行。这个设计更适合自动化 agent flow，但意味着权限隔离、workspace 边界和外部输入信任模型必须由部署者明确控制。

## 与 Agent Skill 的关系

Humanize 解决的是“如何运行和编排 agent”，而 [[concept/inference/agent/Agent Skill|Agent Skill]] 解决的是“agent 在某个领域应该知道什么、按什么步骤工作”。因此 Humanize 可以承载 AI Infra Skill，但其自身不等同于性能优化知识库。

## Sources

- https://github.com/humanfia/humanize
- https://github.com/humanfia/humanize/blob/main/README.md
- https://github.com/humanfia/humanize/blob/main/docs/reference/flows.md
- https://github.com/humanfia/humanize/blob/main/docs/reference/agents.md
- https://github.com/humanfia/humanize/blob/main/docs/index.md
