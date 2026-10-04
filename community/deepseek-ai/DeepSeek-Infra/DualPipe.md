---
type: project
name: DualPipe
parent: DeepSeek-Infra
linked_concepts:
  - "concept/inference/parallelism/Pipeline Parallelism"
status: active
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Chengqi Deng"
  - "community/deepseek-ai/DeepSeek-Infra/Jiashi Li"
  - "company/深度求索/梁文锋 Liang Wenfeng"
repository: https://github.com/deepseek-ai/DualPipe
docs: https://github.com/deepseek-ai/DualPipe
last_verified: "2026-10"
companies: ["深度求索"]
layer: training
areas:
  - "pipeline-parallelism"
  - "bidirectional-pipeline"
  - "pipeline-scheduling"
  - "computation-communication-overlap"
  - "dualpipev"
integrations: []
linked_companies:
  - "company/深度求索/深度求索"
code_availability: public
---
# DualPipe

## 项目简介
DualPipe 是 DeepSeek-V3 Technical Report 引入的双向 Pipeline Parallelism schedule，目标是在大模型训练中让 forward / backward computation 与 communication 充分重叠，同时降低 pipeline bubble。DeepSeek 2025 Open Source Week 将它列为 Day 4 “Optimized Parallelism Strategies” 的正式开源项目。

## 核心机制
DualPipe 让 micro-batch 沿两个相反方向通过 pipeline，在调度上安排 forward/backward chunks 相互覆盖；仓库同时包含由 DualPipe “cut-in-half” 推导出的 DualPipeV。其核心价值不是新的通信库，而是 pipeline schedule / execution order。

## 与其他 DeepSeek Infra 的关系
- [[profile-data]] 公开 DeepSeek V3/R1 training profile，并把 DualPipe 的 forward/backward overlap 作为可观察对象。
- [[DeepEP]] 解决 MoE EP communication；DualPipe 解决 pipeline schedule。两者都在“隐藏通信开销”上工作，但处于不同并行维度。
- 与 [[EPLB]] / [[LPLB]] 的 expert balancing 也不同：DualPipe 控制 stage/microbatch 时间调度，不负责 expert placement。

## 公开作者
仓库 README 明确写明由 [[Jiashi Li]]、[[Chengqi Deng]]、[[company/深度求索/梁文锋 Liang Wenfeng|Liang Wenfeng]] 创建/开发。

## Sources
- https://github.com/deepseek-ai/DualPipe
- https://github.com/deepseek-ai/open-infra-index
- https://arxiv.org/abs/2412.19437

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Chengqi Deng|Chengqi Deng]]：[[DualPipe]]：仓库 README 明确列为创建 / 开发者。
- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：[[DualPipe]]：仓库 README 明确列为创建 / 开发者。
- [[company/深度求索/梁文锋 Liang Wenfeng|梁文锋（Liang Wenfeng）]]：[[community/deepseek-ai/DeepSeek-Infra/DualPipe|DualPipe]]：仓库 README 明确列为创建 / 开发者。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/parallelism/Pipeline Parallelism|Pipeline Parallelism]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
