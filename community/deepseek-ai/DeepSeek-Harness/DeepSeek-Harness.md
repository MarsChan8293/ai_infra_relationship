---
type: project
name: DeepSeek Harness
status: active
repository: https://github.com/deepseek-ai/deepseek-harness
docs: https://deepseek-harness.github.io/deepseek-harness/
last_verified: "2026-10"
companies: ["深度求索"]
layer: runtime
areas:
  - "agent-harness"
  - "plugin-runtime"
  - "agent-loop"
  - "tool-orchestration"
  - "session-runtime"
  - "mcp"
  - "acp"
  - "sandbox"
  - "llm-adapters"
integrations:
  - "Cordis"
---
# DeepSeek Harness

## 项目简介
DeepSeek Harness（`dsh`）是 DeepSeek 在 2026 年开源的 agent harness，官方定位是 **Everything is a Plugin**。它不是 inference engine，也不是 MaaS scheduler；它负责 agent runtime：model adapter、tool registry、session log、agent loop、sandbox、MCP/ACP、Web/SDK/headless surfaces 都通过可组合 plugin tree 组织。

## 架构核心：Cordis plugin tree
DSH 基于 [[community/cordiverse/Cordis/Cordis|Cordis]]。插件向共享 context 注入 service、typed event 与可回滚 effect。官方架构文档明确说明：model adapter、tool registry、session log、agent loop 本身也都是插件，因此扩展方式是挂载/替换 plugin，而不是修改一个不可替换的 privileged core。

## Profiles / Bundles
官方当前 shipping profiles 包括：
- **web**：完整浏览器应用。
- **headless**：无 server 的 one-shot runner。
- **sdk / sdk-minimal**：JSON-RPC / SDK 运行面。
- **acp**：automation-only ACP server。
- Desktop application 复用同一 dsh runtime，并维护 desktop profile。

Profile 由 ordered bundles + profile patch + home patch + optional overlay 组成；这让“部署一个 agent”更接近配置/组合一个 runtime graph，而不是写死单体应用。

## Agent runtime
一次 turn 可以包含多次 model step 与 tool call。Session log 是 model-visible context 的 durable source of truth，agent/step/tool/system/user/assistant 等事件被记录后再投影为模型历史。DSH 同时保留 live event seam，用于运行中 interception / streaming / capability replacement。

## Tool / protocol 边界
- **MCP**：外部 MCP server 的 tools 被转换成普通 Harness tools，并经过 cancellation、permission、result logging 等统一管线。
- **ACP**：允许 trusted program 以进程外协议创建/恢复持久 agent session、选择模型、挂载 MCP server、提交/取消工作；也可作为 out-of-process subagent backend。
- **Sandbox**：本地 Linux bwrap/Landlock、macOS Seatbelt、Windows restricted token，以及 SSH remote backend；filesystem 与 subprocess 各自在正确 seam 上执行 policy。
- **LLM adapters**：provider/model route 可替换，支持动态 model id 与 reasoning-effort metadata。

## 与 AI Infra control plane 的关系
DSH 更像 agent-facing runtime/control plane，而 [[MindIE-Motor]]、llm-d、KServe 等更偏 inference serving / workload orchestration。当前 DeepSeek Harness 仓库中未发现对 MindIE 的官方直接集成，因此这里不建立 `integration` 强边；后续若接入 MindIE-Motor，更合理的边界是 DSH 负责 agent/session/tool state，上层通过明确 adapter/plugin 调用 serving control plane。

## 状态
官方 README 将项目标记为 **developer preview**，并明确提示 compatibility-breaking changes 仍会发生。项目活跃，但当前不应按稳定 API 平台理解。

## Sources
- https://github.com/deepseek-ai/deepseek-harness
- https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md
- https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/mcp.md
- https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/acp/acp
