---
type: project
name: "AKG Agents"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/mindspore-ai/akg
docs: https://github.com/mindspore-ai/akg/tree/master/akg_agents
areas: ["agentic-kernel-optimization", "multi-agent", "kernel-generation", "autonomous-research", "triton-ascend", "swft", "kernel-verifier"]
hardware: ["ascend", "nvidia", "cpu"]
companies: ["华为"]
last_verified: "2026-10"
linked_companies:
  - "company/华为/华为"
code_availability: public
---

# AKG Agents

AKG Agents 是 MindSpore AKG 项目中的 LLM-powered multi-agent collaboration framework，面向 AI Infra 与高性能代码生成/优化。

## 核心能力

公开实现包括 ReAct Agent、Skill / Tools / SubAgent、LangGraph workflow、Trace 和 registry。当前主要 production scenario 是 multi-backend / multi-DSL kernel code generation；2026 年加入 AutoResearch workflow，以 KernelVerifier 作为评测闭环进行 agent-driven iterative deep optimization。

AKG 主仓将其作为 AKG-AGENT 子项目公开，并覆盖 Triton-Ascend 等 Ascend kernel 路线。

## Sources

- https://github.com/mindspore-ai/akg
- https://github.com/mindspore-ai/akg/tree/master/akg_agents

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
