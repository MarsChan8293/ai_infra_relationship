---
type: project
name: "mindie-bench"
layer: benchmark
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/mindie-agent/mindie-bench
docs: https://github.com/mindie-agent/mindie-bench/blob/main/README.md
areas:
  - ascend-agent-benchmark
  - isolated-evaluation
  - correctness-gate
  - performance-gate
  - behavioral-oracle
  - npu-resource-lease
hardware:
  - ascend
last_verified: "2026-11"
---

# mindie-bench

## 项目简介

独立评估昇腾 Coding Agent 工程表现的 Benchmark/Judge，重点在隔离执行、密封 Oracle、NPU 任务完成率与精度/性能验收，不是直接负责生成推理优化 Patch 的引擎。

## 核心机制

包含独立 Host Runner、行为测试、remote NPU 槽位、G0–G4 消融与经验复用评估；官方任务范围覆盖 910B、910C、950DT，部分 vLLM-Ascend 及算子任务要求数值精度、ACLGraph、显存与真实服务热态性能。区分 completed_pass、completed_fail、infra_failed、unknown。

## 昇腾适配与限制

原生昇腾验收框架，但尚须针对 DeepSeek/vLLM-Ascend 的 Scheduler、KV、EP/TP、PD 自定义真实 Bench 与 logits/KV Golden Tests；官方列出卡型不等于所有任务均完成全卡型验证。

## 技术关系

与 [[community/mindie-agent/mindie-agent/MindIE Agent|MindIE Agent]] 属同一开源生态但职责互补；可作为 [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]] 的独立 Judge 层。

## 维护组织与来源

上游组织：`mindie-agent`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/mindie-agent/mindie-bench
- https://github.com/mindie-agent/mindie-bench/blob/main/README.md
- https://github.com/mindie-agent/mindie-bench/blob/main/docs/rsi-inference.md
