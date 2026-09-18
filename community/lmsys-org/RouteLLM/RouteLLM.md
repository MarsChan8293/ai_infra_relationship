---
type: project
name: RouteLLM
linked_people: []
companies: []
company_relation: community-led
layer: model-routing
open_source: true
repository: https://github.com/lm-sys/RouteLLM
areas: [llm-routing, inference-cost, model-selection, preference-learning, serving]
people:
  - "company/Inferact/Joseph Gonzalez"
  - "company/Inferact/Ion Stoica"
governance: LMSYS project
last_verified: "2026-09"
linked_companies: []
---
# RouteLLM

RouteLLM 是 LMSYS 的模型路由框架，目标是在强模型与较低成本模型之间学习 routing policy，并用 preference data 在质量与推理成本之间做可控权衡。

## AI Infra 价值
模型 routing 位于 serving 的“请求决策层”，与单个 inference engine 的 kernel / scheduler 优化不同。它直接决定每个请求被发送到哪个模型，因此能把系统优化从单模型吞吐扩展到 portfolio-level cost / quality optimization。

官方项目与文章提供多种 router 训练与评测路径，并报告在其 benchmark / target quality 设置下显著降低强模型调用成本。这里将其记录为实验结果，不把具体百分比泛化到所有业务流量。

## 图谱关系
[[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] 与 [[company/Inferact/Ion Stoica|Ion Stoica]] 是 RouteLLM 论文作者，使该项目继续落在 Berkeley / LMSYS systems 网络中。其他作者本轮不因单篇论文共同署名而批量建人物节点。

## Sources
- https://github.com/lm-sys/RouteLLM
- https://www.lmsys.org/projects/
- https://www.lmsys.org/blog/2024-07-01-routellm/
