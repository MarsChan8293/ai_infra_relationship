---
type: project
name: "msModeling"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/Ascend/msmodeling
docs: https://github.com/Ascend/msmodeling/blob/main/docs/en/user_guide/msmodeling_optix_user_guide.md
areas:
  - ascend-performance-modeling
  - serving-autotuning
  - agent-closed-loop-optimization
  - parallelism-search
  - serving-simulation
  - pso-search
hardware:
  - ascend
last_verified: "2026-11"
---

# msModeling

## 项目简介

昇腾官方开源的建模与服务性能优化项目。除 TensorCast / Serving 仿真外，内置 OptiX 面向真实 Serving 环境的自动寻优，是昇腾推理系统 RSI 的配置搜索基础。

## 核心机制

Serving 模拟在延迟/SLO 约束下搜索 PP、PD 及 Batch/并行策略；OptiX 通过 PSO、Early Rejection 和 AI Agent 闭环探索实际 vLLM、MindIE Serving 参数，提供优化器、插件与可恢复配置。仓库代码包含 optix/optimizer、plugins、serve_plan 等模块。

## 昇腾适配与限制

原生面向 Ascend，但主要是参数、部署计划与并行配置优化，并未核实能够任意自主改写 vLLM-Ascend Scheduler/KV 源码。910B/910C 的性能结果仍须真机校准。官方提及 MindIE 引擎支持不应自动等价为已集成 MindIE-Motor 控制面。

## 技术关系

[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]、[[concept/compiler/Autotuning|Autotuning]]、[[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]。与 [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] 是不同仓库/目标。

## 维护组织与来源

上游组织：`Ascend`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/Ascend/msmodeling
- https://github.com/Ascend/msmodeling/blob/main/docs/en/user_guide/msmodeling_optix_user_guide.md
- https://github.com/Ascend/msmodeling/blob/main/README_EN.md
