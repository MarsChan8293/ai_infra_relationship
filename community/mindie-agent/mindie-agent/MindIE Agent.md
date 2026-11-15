---
type: project
name: "MindIE Agent"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/mindie-agent/mindie-agent
docs: https://github.com/mindie-agent/mindie-agent/blob/main/docs/architecture.md
areas:
  - ascend-coding-agent
  - remote-npu-execution
  - inference-engineering
  - profiling-diagnostics
  - knowledge-reuse
  - agent-plugin
hardware:
  - ascend
last_verified: "2026-11"
---

# MindIE Agent

## 项目简介

面向昇腾推理工程的 Coding Agent 工具/Skill/知识生态，为 Codex、Claude Code、Kimi Code、DeepSeek Harness 等提供远端 NPU 开发、Profiling、故障分析与可追溯经验。

## 核心机制

使用 remote-dev 等组件执行远端操作，配合 profiler、debugger、coordinator、npu-top 和领域知识库；支持 vLLM-Ascend、MindIE、xLLM 等推理工程任务。它是优化 Agent 的工具/知识层，不是单独完整的演化搜索和独立 Judge。

## 昇腾适配与限制

直接聚焦 Ascend NPU，适配仍依赖目标机器的 CANN/驱动、设备权限、容器与框架版本；生产多机还需实验配额、隔离和回滚。开源组织为 mindie-agent，不能仅据名称推定与华为产品的法律或治理关系。

## 技术关系

[[concept/inference/agent/Agent Skill|Agent Skill]]、[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]；同组织 [[community/mindie-agent/mindie-bench/mindie-bench|mindie-bench]] 提供独立评测。与 [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] 的关联为工程适配支持。

## 维护组织与来源

上游组织：`mindie-agent`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/mindie-agent/mindie-agent
- https://github.com/mindie-agent/mindie-agent/blob/main/docs/architecture.md
- https://github.com/mindie-agent/remote-dev
