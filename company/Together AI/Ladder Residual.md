---
type: project
name: Ladder Residual
linked_people:
  - "university/浙江大学/Jue Wang"
companies: ["Together AI"]
company_relation: research-collaboration
layer: tensor-parallel-inference
open_source: true
repository: https://github.com/mayank31398/ladder-residual-inference
areas: [llm-inference, tensor-parallelism, communication-overlap, distributed-inference]
people:
  - "university/浙江大学/Jue Wang"
last_verified: "2026-09"
linked_companies:
  - "company/Together AI/Together AI"
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[university/浙江大学/Jue Wang|Jue Wang]]：[[company/Together AI/Ladder Residual|Ladder Residual]]：ICML 2025，通过重新设计 residual path 让 Tensor Parallel communication 与计算重叠，加速 distributed inference。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Together AI/Together AI|Together AI]]：公司页与社区/项目页均有显式记录；关系：`research-collaboration`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
