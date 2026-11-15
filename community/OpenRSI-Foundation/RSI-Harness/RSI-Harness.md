---
type: project
name: "RSI-Harness"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/OpenRSI-Foundation/OpenRSI-Index
docs: https://github.com/OpenRSI-Foundation/OpenRSI-Index/tree/main/RSI-Harness
areas:
  - recursive-self-improvement
  - agent-experiment-harness
  - isolated-judge
  - long-horizon-optimization
  - distributed-experiment
last_verified: "2026-11"
---

# RSI-Harness

## 项目简介

OpenRSI Index 的长周期自主改进实验框架，实际源码位于主仓的 RSI-Harness/ 子目录。独立承载多轮 Agent 任务、冻结候选和可审计 Judge，不是仅有论文的展示仓。

## 核心机制

Work 容器持久运行 Coding Agent；通过 `rsi-submit` 快照提交候选；干净 Judge 环境加载任务私有测试并评分；反馈返回 Work 继续迭代，按评分方向选最佳有效候选。使用 Harbor 任务格式，提供 Docker 及部分 Slurm/LSF/Kubernetes/PBS/PJM 执行支持。

## 昇腾适配与限制

官方 GPU 本地依赖 NVIDIA，未确认原生昇腾 NPU；需要实现 CANN/设备挂载、910B/910C 卡级租约、真机 vLLM-Ascend Benchmark 和 KV/logits 精度 Judge。`vllm-in-judge` 示例的目标是使用 vLLM 评估 Agent 任务，并非自动优化 vLLM Scheduler。

## 技术关系

[[concept/inference/agent/Agent Harness|Agent Harness]]、[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]；其 SGLang-Omni 多模态任务与 [[community/sgl-project/SGLang/SGLang|SGLang]] 为研究关联，未确认与 [[community/InferMatrixLab/InferRSI/InferRSI|InferRSI]] 直接集成。

## 维护组织与来源

上游组织：`OpenRSI-Foundation`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/OpenRSI-Foundation/OpenRSI-Index
- https://github.com/OpenRSI-Foundation/OpenRSI-Index/tree/main/RSI-Harness
- https://github.com/OpenRSI-Foundation/OpenRSI-Index/tree/main/rsi-tasks/SGNOMI
