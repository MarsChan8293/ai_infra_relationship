---
type: project
name: "ShinkaEvolve"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/SakanaAI/ShinkaEvolve
docs: https://sakanaai.github.io/ShinkaEvolve/
areas:
  - llm-guided-program-evolution
  - evolutionary-search
  - agentic-code-mutation
  - candidate-archive
  - parallel-evaluation
last_verified: "2026-11"
---

# ShinkaEvolve

## 项目简介

Sakana AI 的通用 LLM 程序进化框架，结合 LLM 代码变异、候选种群、独立 Evaluator 与结果档案，支持跨轮演进；本身不是推理 Serving 引擎。

## 核心机制

候选程序可在本地或 Slurm 环境并行评测，维护优胜代码的档案并在不同进化分支间传播有效方案；支持 Coding Agent 相关 Skill。适合把 Scheduler/KV/路由策略设为可修改源码，通过固定性能和正确性脚本形成长期搜索。

## 昇腾适配与限制

与硬件解耦，暂无原生 vLLM-Ascend/CANN 集成证据；要在 910B/910C/950 上运行需自建 NPU 任务执行器、CANN 镜像、资源租约和正确性门禁。它能提供搜索策略，不自动保证多机推理实验可靠性。

## 技术关系

[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]。与 [[community/smth-fun/SEIS/SEIS|SEIS]] 具有程序进化方法共性，但没有已核实的直接集成。

## 维护组织与来源

上游组织：`SakanaAI`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/SakanaAI/ShinkaEvolve
- https://sakanaai.github.io/ShinkaEvolve/
- https://github.com/SakanaAI/ShinkaEvolve/tree/main/examples
