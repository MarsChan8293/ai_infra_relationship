---
type: project
name: "AKG Agents"
linked_people: []
layer: optimization
status: active
repository: https://github.com/mindspore-ai/akg
docs: https://github.com/mindspore-ai/akg/tree/master/akg_agents
areas: ["agentic-kernel-optimization", "multi-agent", "kernel-generation", "autonomous-research", "triton-ascend", "swft", "kernel-verifier"]
hardware: ["ascend", "nvidia", "cpu"]
companies: ["华为"]
last_verified: "2026-10"
---

# AKG Agents

AKG Agents 是 MindSpore AKG 项目中的 LLM-powered multi-agent collaboration framework，面向 AI Infra 与高性能代码生成/优化。

## 核心能力

公开实现包括 ReAct Agent、Skill / Tools / SubAgent、LangGraph workflow、Trace 和 registry。当前主要 production scenario 是 multi-backend / multi-DSL kernel code generation；2026 年加入 AutoResearch workflow，以 KernelVerifier 作为评测闭环进行 agent-driven iterative deep optimization。

AKG 主仓将其作为 AKG-AGENT 子项目公开，并覆盖 Triton-Ascend 等 Ascend kernel 路线。

## Sources

- https://github.com/mindspore-ai/akg
- https://github.com/mindspore-ai/akg/tree/master/akg_agents
