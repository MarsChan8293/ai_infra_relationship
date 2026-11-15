---
type: project
name: "InferRSI"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/InferMatrixLab/InferRSI
docs: https://github.com/InferMatrixLab/InferRSI/blob/main/docs/quickstart.md
areas:
  - agentic-inference-optimization
  - controlled-benchmark
  - correctness-gate
  - performance-evidence
  - optimization-campaign
  - skill-library
last_verified: "2026-11"
---

# InferRSI

## 项目简介

推理优化 CLI 工作台，面向 Coding Agent 提供可控 baseline/candidate 实验、独立正确性与性能验收、实验记录和优化知识检索；不是新的 Serving Engine。

## 核心机制

依赖用户或外部 Agent 提供候选源码、Benchmark 与质量检查脚本；保留固定协议 A/B 或 AB/BA 测试、迭代 Campaign、结果证据及历史经验。Skill Library 按硬件/框架/推理引擎/方法/工作流组织，包含 Ascend Profiling、模型适配及 vLLM KV 生命周期等专题。

## 昇腾适配与限制

拥有昇腾相关 Skill 与案例，不等于已完成所有 NPU 设备适配；910B/910C/950 需要独立提供远端执行、数值门禁与性能脚本，区分真实测量收益和候选方法论。

## 技术关系

[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]、[[concept/inference/agent/Agent Harness|Agent Harness]]、[[concept/inference/agent/Agent Skill|Agent Skill]]；与 [[community/OpenRSI-Foundation/RSI-Harness/RSI-Harness|RSI-Harness]] 的 Work/Judge 隔离和 [[community/smth-fun/SEIS/SEIS|SEIS]] 的源码进化为互补思路，不能推断已有集成。

## 维护组织与来源

上游组织：`InferMatrixLab`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/InferMatrixLab/InferRSI
- https://github.com/InferMatrixLab/InferRSI/blob/main/docs/quickstart.md
- https://github.com/InferMatrixLab/InferRSI/blob/main/src/inferrsi/knowledge/data/skill_library/README.md
