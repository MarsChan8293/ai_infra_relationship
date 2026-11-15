---
type: project
name: "xLLM Workflow"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/xLLM-AI/xllm-workflow
docs: https://github.com/xLLM-AI/xllm-workflow/blob/main/docs/architecture/skill-map.md
areas:
  - ascend-inference-engineering
  - agentic-optimization-loop
  - profiling-analysis
  - accuracy-validation
  - benchmark-protocol
  - experiment-lifecycle
hardware:
  - ascend
last_verified: "2026-11"
---

# xLLM Workflow

## 项目简介

面向昇腾大模型 Serving 的 Agent-ready 工程优化工作流，以 xLLM 为完整主路径，组织源码修改、Profiling、性能/精度验证与历史经验记录。

## 核心机制

`xllm-npu-sota-loop` 按 Research → Learn → Code → Review → Validate → Record 迭代；`xllm-experiment-lifecycle` 管理实验恢复和证据；eval-runner、profiler、benchmark、accuracy-debug 与代码评审 Skill 提供测量约束。

## 昇腾适配与限制

原生适用于 xLLM 的 NPU 推理优化。官方说明 vLLM-Ascend 和 SGLang 目前仅支持实验 Adapter 或 Artifact 分析，不是完整主路径。README 表示尚无 LICENSE，公开源码复用前需确认版权授权。

## 技术关系

[[community/xLLM-AI/xLLM/xLLM|xLLM]]、[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]、[[concept/inference/agent/Agent Skill|Agent Skill]]；与 InferRSI 为方法学互补而非已实现的接口集成。

## 维护组织与来源

上游组织：`xLLM-AI`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/xLLM-AI/xllm-workflow
- https://github.com/xLLM-AI/xllm-workflow/blob/main/docs/architecture/skill-map.md
- https://github.com/xLLM-AI/xllm-workflow/blob/main/README.md
