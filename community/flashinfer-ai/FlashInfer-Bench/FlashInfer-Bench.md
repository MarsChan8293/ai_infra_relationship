---
type: project
name: "FlashInfer-Bench"
linked_people:
  - "community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen"
  - "community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye"
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
  - "concept/inference/optimization/Agentic Inference Optimization"
layer: "optimization-harness"
status: active
repository: https://github.com/flashinfer-ai/flashinfer-bench
docs: https://bench.flashinfer.ai/
areas:
  - "agentic-kernel-optimization"
  - "kernel-benchmark"
  - "correctness-validation"
  - "production-deployment"
  - "llm-inference"
  - "self-improving-ai-systems"
hardware:
  - "nvidia"
integrations:
  - "FlashInfer"
  - "SGLang"
  - "vLLM"
last_verified: "2026-10"
linked_companies: []
---

# FlashInfer-Bench

FlashInfer-Bench 是 FlashInfer 社区构建的 benchmark suite 与 production workflow，用于把 **AI-generated GPU kernel** 从生成、正确性验证、性能评测一路连接到真实 LLM inference engine 的部署。

## 核心闭环

```text
Kernel Definition / Workload
        ↓
Agent-generated Implementation
        ↓
Correctness Evaluation
        ↓
Performance Benchmark
        ↓
Best Candidate Selection
        ↓
apply() Dynamic Substitution
        ↓
SGLang / vLLM Production Validation
```

其核心数据契约是 FlashInfer Trace：统一描述 kernel definition、workload、implementation 与 evaluation，使 Agent、benchmark harness 和 production system 之间能够复用同一套任务表示。

## AI Infra 价值

FlashInfer-Bench 同时连接两层优化：

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]：为 AI Kernel Agent 提供真实 workload、correctness gate、benchmark 与 leaderboard。
- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]：通过 `apply()` 动态替换机制把候选 kernel 注入 SGLang / vLLM，要求局部 kernel 优化回到真实 serving 系统中验证。

因此它不是单纯的 microbenchmark，而是 **kernel generation → evaluation → deployment** 的闭环 Harness。

## 论文与项目

FlashInfer-Bench 论文发表于 MLSys 2026；官方仓库由 `flashinfer-ai` 维护，并提供 FlashInfer Trace 数据集与 MLSys 2026 AI Kernel Generation Contest 的评测基础设施。

## Sources

- https://github.com/flashinfer-ai/flashinfer-bench
- https://arxiv.org/abs/2601.00227
- https://proceedings.mlsys.org/paper_files/paper/2026/hash/37e44c4b5321605735be9761f9b758fc-Abstract-Conference.html
