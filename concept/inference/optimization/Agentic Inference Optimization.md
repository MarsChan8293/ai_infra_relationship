---
type: concept
name: Agentic Inference Optimization
aliases:
  - AI Infra Optimization Agent
  - Autonomous Inference Optimization
  - Agentic AI Infra Optimization
  - 智能体推理优化
domain: inference
topic: optimization
related_concepts:
  - Agentic Kernel Optimization
  - Agent Harness
  - Agent Skill
  - Inference Scheduling
  - Parallelism
  - KV Cache Management
  - Autotuning
projects:
  - "MetaInfer"
  - "RoofLang"
  - "GEAK"
  - "Hyperloom"
  - "CANNBot"
  - "FlashInfer-Bench"
last_verified: 2026-10
---

# Agentic Inference Optimization

## 一句话定义

Agentic Inference Optimization 把推理性能工程从一次性的人工分析，转化为由 AI agent 在可验证控制环中持续执行的自动优化过程：先建立 baseline 和性能证据，再诊断瓶颈、修改框架配置或源码、重新运行 correctness 与 benchmark，并只保留被真实测量证明有效的候选。

## 核心闭环

典型工作流不是“让模型给出优化建议”，而是：

```text
Baseline
  ↓
Profile / Observe
  ↓
Diagnose
  ↓
Plan
  ↓
Modify Config / Source
  ↓
Build / Restart
  ↓
Correctness
  ↓
Benchmark
  ↓
Keep / Revert
  ↓
Memory / Next Iteration
```

其中 Agent 适合承担诊断、规划、代码修改和候选生成；Harness / Evaluator 则负责 baseline、执行、正确性、性能测量、promotion 和 rollback。性能结论必须来自真实评测，而不是模型自我判断。

## 优化对象

Agentic Inference Optimization 的搜索空间可以覆盖多个层级：

- **Framework configuration**：batch、并发、并行度、cache、graph mode、attention backend 等。
- **Framework source**：scheduler、model runner、KV path、通信 overlap、host/runtime overhead。
- **System architecture**：TP / DP / EP / PP、P/D disaggregation、placement、routing、cache lifecycle。
- **Kernel / operator**：当瓶颈下沉到算子层时进入 [[Agentic Kernel Optimization]]。
- **Hardware-specific backend**：根据 NVIDIA CUDA 或 Ascend CANN / AscendC 的 profiler、compiler 与 runtime 反馈选择不同优化动作。

## Agent Harness 与 Agent Skill 在闭环中的位置

[[concept/inference/agent/Agent Harness|Agent Harness]] 提供 session、tool、permission、sandbox、model backend 和 durable execution 等运行时能力；[[concept/inference/agent/Agent Skill|Agent Skill]] 提供 profiler guide、benchmark procedure、capacity rule、incident recipe 等领域知识。二者都可以成为优化系统的组成部分，但单独存在时都不等于完整的 agentic optimization：是否属于本概念，关键看是否具备可测量、可验证、可 promotion / rollback 的优化闭环。

## 与传统 Autotuning 的区别

传统 [[Autotuning]] 往往在预定义参数空间内做搜索，例如 tile size、block size、并行度或 batch 参数。Agentic Inference Optimization 的动作空间更开放，可以同时修改配置、源码、算法结构与 kernel，并使用 profiling、compiler diagnostics、历史实验和代码上下文形成新的假设。

因此两者不是替代关系：Autotuning 可以作为 Agentic Optimization 内部的一个确定性搜索器。

## 与 Agentic Kernel Optimization 的关系

[[Agentic Kernel Optimization]] 是更底层的代码优化闭环。Inference Agent 应先判断性能瓶颈是否真的来自 kernel，再决定是否下钻；kernel microbenchmark 的局部提升也必须回到真实 serving workload 做端到端验证。

## 项目实现

[[community/MetaInfer/MetaInfer|MetaInfer]] 直接把 LLM 用于 inference framework generation、model porting 与 kernel optimize → benchmark 循环，是当前仓库中最直接的 AI-for-AI-Infra 实现之一。

[[community/yzygitzh/RoofLang/RoofLang|RoofLang]] 把 workload、hardware、placement、parallelism、KV lifecycle 与 graph transformation 暴露给 persistent optimizer agent，并通过 analytical simulation 搜索 throughput / interactivity 的系统设计空间。它更偏 architecture search，而不是直接修改现有 serving engine，但属于同一类“让 agent 闭环优化推理系统”的机制。

[[community/flashinfer-ai/FlashInfer-Bench/FlashInfer-Bench|FlashInfer-Bench]] 连接 AI-generated kernel 与真实 serving engine：先用 FlashInfer Trace 和 benchmark harness 做 correctness / performance evaluation，再通过 `apply()` 把最佳实现动态替换进 SGLang / vLLM。它因此是 kernel-level agent optimization 向 production inference validation 过渡的关键桥梁。

## 设计原则

- **Measurement is ground truth**：性能晋级由 Harness 决定。
- **Correctness before performance**：任何候选先过正确性 gate。
- **Deterministic control plane**：预算、超时、状态机、rollback 和 promotion 不交给 LLM 自由决定。
- **Evidence compounding**：成功与失败实验都应进入 Recipe / Memory。
- **Hierarchical optimization**：先定位 framework / communication / scheduler / kernel 哪一层是瓶颈，再进入对应 optimizer。
- **Hardware-aware but interface-stable**：上层保留统一 TaskSpec / Evaluator，底层由 NVIDIA / Ascend adapter 提供 profiler、compiler 与 benchmark 能力。

## Sources

- https://github.com/MetaInfer/MetaInfer
- https://github.com/yzygitzh/rooflang
- https://github.com/NVlabs/kda
- https://github.com/LancerLab/croqtile
- https://github.com/flashinfer-ai/flashinfer-bench
- https://arxiv.org/abs/2601.00227
