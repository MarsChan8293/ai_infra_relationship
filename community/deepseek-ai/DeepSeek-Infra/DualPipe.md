---
type: project
name: DualPipe
parent: DeepSeek-Infra
status: active
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
