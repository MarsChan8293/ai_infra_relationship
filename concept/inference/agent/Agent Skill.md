---
type: concept
name: Agent Skill
aliases:
  - Agent Skills
  - Coding Agent Skill
  - Domain Skill
  - 智能体技能
domain: inference
topic: agent-knowledge
related_concepts:
  - Agent Harness
  - Agentic Inference Optimization
  - Agentic Kernel Optimization
projects:
  - AI-Infra-Auto-Driven-SKILLS
  - Ascend Agent Skills
last_verified: "2026-10"
---

# Agent Skill

## 一句话定义

Agent Skill 是可被 coding agent / agent runtime 按需装载的**领域知识与操作流程单元**：把任务判断、工具使用、验证步骤、证据规则和常见故障模式封装成可复用上下文，使通用模型获得某个 AI Infra 子领域的工程操作能力。

## 核心机制

典型 Skill 不负责长期运行 agent，而是提供一组可移植的执行约束：

```text
Task
  ↓
Skill selection
  ↓
Domain instructions / evidence rules
  ↓
Tool calls / code changes / benchmark
  ↓
Validation
  ↓
Structured result
```

Skill 的价值在于把一次性 prompt 变成版本化、可审查、可复用的工程知识单元。对于 AI Infra，内容可以覆盖 serving benchmark、capacity planning、profiling、kernel 开发、模型 Day-0 支持、故障排查和精度/性能验证。

## 与 Agent Harness 的区别

[[concept/inference/agent/Agent Harness|Agent Harness]] 管理 agent 的生命周期与执行环境，例如 session、model backend、tools、permissions、sandbox、protocol 和 durable state；Agent Skill 管理的是**任务知识与操作策略**。两者通常组合：Harness 决定“怎么跑”，Skill 决定“这类任务怎么做”。

## 与 Agentic Optimization 的关系

Agent Skill 可以为 [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]] 和 [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]] 提供 domain knowledge、profiling guide、benchmark rule 与 repair recipe，但 Skill 本身不必实现自动搜索、候选 promotion 或 keep/revert 控制环。

## 项目实现

[[community/BBuf/AI-Infra-Auto-Driven-SKILLS/AI-Infra-Auto-Driven-SKILLS|AI-Infra-Auto-Driven-SKILLS]] 把 serving benchmark、capacity planning、profiler 分析、model Day-0 support、code review、incident triage 与模型 PR 历史封装为普通 `SKILL.md` 目录，是跨推理框架的 AI Infra Skill layer。

[[community/Ascend/agent-skills/Ascend Agent Skills|Ascend Agent Skills]] 把 AscendC、Catlass、Triton-Ascend、profiling、精度验证和性能优化经验封装为 coding-agent 可消费的 Skill，是硬件/后端专用 Domain Skill 的代表。

## 设计原则

- Skill 应显式声明适用对象、前置条件和验证方式；
- 性能结论必须绑定 hardware / model / precision / workload / revision；
- Skill 应保留 correctness 与 safety gate，而不是只优化单一指标；
- 平台专用知识与通用 orchestration 分层，避免把 NVIDIA / Ascend 特定命令写死在通用 Harness；
- Skill 与 Runtime 解耦，使同一知识单元可以被多个 coding-agent / harness 复用。

## Sources

- https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS
- https://github.com/Ascend/agent-skills
