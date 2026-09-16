---
type: project
name: Ladder Residual
companies: ["Together AI"]
company_relation: research-collaboration
layer: tensor-parallel-inference
open_source: true
repository: https://github.com/mayank31398/ladder-residual-inference
areas: [llm-inference, tensor-parallelism, communication-overlap, distributed-inference]
people:
  - "university/浙江大学/Jue Wang"
last_verified: "2026-09"
---
# Ladder Residual

## 项目简介
Ladder Residual 是针对大模型 Tensor Parallel inference 的架构/系统协同方案，通过调整 residual 路径，让通信与计算更容易重叠，从而降低 TP 的通信瓶颈。论文发表于 ICML 2025，并公开 inference benchmarking 代码。

论文报告在 8 卡 TP 的 70B Transformer 场景中获得约 29% 端到端推理加速。它的价值在于不只调 runtime，而是通过模型结构重新安排通信依赖，使系统层更容易隐藏 collective latency。

## 人物与组织
- [[university/浙江大学/Jue Wang|Jue Wang]]：论文作者，当前任职 Together AI。
- [[company/Together AI/Together AI|Together AI]]：Jue Wang 当前所属公司；该项目同时包含 Princeton / MIT / Together AI 等多机构作者，因此这里标记为 research collaboration，而不是公司独占项目。

## Sources
- https://proceedings.mlr.press/v267/zhang25bg.html
- https://arxiv.org/abs/2501.06589
- https://github.com/mayank31398/ladder-residual-inference
- https://juewang.me/
