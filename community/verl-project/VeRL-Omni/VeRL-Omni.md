---
type: project
name: VeRL-Omni
linked_people:
  - "community/vllm-project/vLLM-Omni/Yongxiang Huang"
layer: multimodal-rl-post-training
open_source: true
repository: https://github.com/verl-project/verl-omni
areas: [reinforcement-learning, post-training, multimodal, diffusion, rollout, distributed-training, ascend]
people:
  - "community/vllm-project/vLLM-Omni/Yongxiang Huang"
related_projects: ["vLLM-Omni", "openYuanRong"]
last_verified: "2026-09"
linked_companies: []
---
# VeRL-Omni

## 项目简介
VeRL-Omni 是 verl 项目下专门面向 diffusion 与 omni-modality generative models 的 RL post-training 框架。项目从 verl 内部的 multimodal generation RL 工作演化而来，2026 年独立成仓库。

## 与 vLLM-Omni 的关系
VeRL-Omni 官方 README 明确把 [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]] 作为高性能 rollout backend，用于 multimodal / diffusion generation，并通过 rollout routing、request-level / step-wise batching、embed caching 等减少 RL rollout 成本。2026-08 v0.2.0 进一步强调 faster diffusion RL 与稳定的 Qwen3-Omni training。

## 与 openYuanRong / Ascend 的关系
- 项目 citation 直接包含 `openYuanRong Team`，表明双方存在项目级共建/作者关系；这里记录为 project collaboration，不展开为所有成员之间的人际关系。
- README 已提供 Ascend NPU support，形成 `vLLM-Omni rollout → VeRL-Omni training → Ascend` 的多模态 RL 路径。

## 治理
官方 governance 当前列出两位 Lead Maintainer：
- [[community/vllm-project/vLLM-Omni/Yongxiang Huang|Yongxiang Huang / @SamitHuang]]
- Xibin Wu / `@wuxibin89`

Active committers 再按 trainer、worker、rollout/agent loop、reward 与 pipeline 分工。这里只纳入与 vLLM-Omni 搜索直接形成高价值 bridge 的 Yongxiang Huang，避免把整个治理 roster 批量灌入图谱。

## Sources
- https://github.com/verl-project/verl-omni
- https://github.com/verl-project/verl-omni/blob/main/docs/community/governance.md
- https://verl-project.github.io/posts/2026-08-17-verl-omni-v0-2-0/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/vllm-project/vLLM-Omni/Yongxiang Huang|Yongxiang Huang]]：https://github.com/verl-project/verl-omni/blob/main/docs/community/governance.md

<!-- END AUTO PROJECT PEOPLE -->
