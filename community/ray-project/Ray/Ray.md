---
type: project
name: Ray
linked_people:
  - "company/Inferact/Ion Stoica"
  - "company/RadixArk/Qiaolin Yu"
  - "university/UC Berkeley/Philipp Moritz"
  - "university/UC Berkeley/Robert Nishihara"
repository: https://github.com/ray-project/ray
open_source: true
areas: [ai-infrastructure, distributed-computing, machine-learning-systems, training, serving]
last_verified: "2026-09"
linked_companies: []
---
# Ray

## 项目简介
Ray 是起源于 UC Berkeley RISELab 的分布式执行框架，最初针对机器学习工作负载中的通用 distributed execution 问题，后来扩展到 training、RL、data processing 与 model serving。

## Berkeley 起源
- [[university/UC Berkeley/Philipp Moritz|Philipp Moritz]]：2019 Berkeley 博士论文主题即 Ray，导师 Michael Jordan 与 [[company/Inferact/Ion Stoica|Ion Stoica]]。
- [[university/UC Berkeley/Robert Nishihara|Robert Nishihara]]：Ray creator；其正式博士导师为 Michael Jordan，与 Ion 的关系是 research / open-source collaboration。
- [[company/Inferact/Ion Stoica|Ion Stoica]]：Berkeley faculty / Ray research network / Anyscale co-founder。

因此这条谱系应建模为：
`UC Berkeley RISELab → Ray → Anyscale`

## AI Infra 生态
- [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]]：把 Ray actor / distributed execution 基础设施延伸到 production model serving。
- [[company/Anyscale/Anyscale|Anyscale]]：由 Ray creators 创办的商业平台，是 Ray 最直接的产业化节点。
- Simon Mo 等人物又把 Ray Serve / Anyscale production serving 经验带入 Berkeley vLLM / Inferact 网络。
- [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]] 等后续工程人才体现 Ray core 人才继续流向新一代 inference startups。

## 治理变化
2025 Ray 加入 PyTorch Foundation。该变化意味着 Ray 的开源治理不应简单等同于 Anyscale 公司所有权；Anyscale 仍是核心商业与工程生态节点，但社区治理需要与公司关系分开建模。

## Sources
- https://github.com/ray-project/ray
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-124.html
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-30.html
- https://www.anyscale.com/press/founders-of-open-source-project-ray-launch-anyscale-with-usd-20-6m-in-funding-to-democratize-distributed-programmingfounders-of-open-source-project-ray-launch-anyscale-with-usd-20-6m-in-funding-to-democratize-distributed-programming
- https://www.anyscale.com/blog/ray-by-anyscale-joins-pytorch-foundation

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/Inferact/Ion Stoica|Ion Stoica]]：[[university/UC Berkeley/Philipp Moritz|Philipp Moritz]]：正式博士学生，博士论文即 Ray distributed execution engine；后共同创办 Anyscale。
- [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]]：[[Anyscale]]：Ray Core Software Engineer，2025-06–2025-12
- [[university/UC Berkeley/Philipp Moritz|Philipp Moritz]]：[[community/ray-project/Ray/Ray|Ray]]：面向机器学习生态的通用分布式执行引擎，博士研究与开源项目直接重合。
- [[university/UC Berkeley/Robert Nishihara|Robert Nishihara]]：共同创建 / 推动 [[community/ray-project/Ray/Ray|Ray]]；

<!-- END AUTO PROJECT PEOPLE -->
