---
type: infra-project
name: Checkpoint Engine
company: 月之暗面
linked_people:
  - "company/月之暗面/checkpoint-engine/HubertZhang"
  - "company/月之暗面/checkpoint-engine/weixiao-huang"
areas: [reinforcement-learning, weight-transfer, checkpoint-loading, distributed-training, inference-serving, rdma]
layer: training-serving-data-plane
open_source: true
repository: https://github.com/MoonshotAI/checkpoint-engine
related_projects: [Mooncake, SGLang, vLLM, Kimi-K2]
last_verified: "2026-09"
linked_companies:
  - "company/月之暗面/月之暗面"
---
# Checkpoint Engine

## 项目简介
Checkpoint Engine 是 Moonshot AI 开源的模型权重更新中间件，用于训练/RL 流程向在线 inference engine 高效更新模型权重。官方 README 给出的 Kimi-K2 生产路径可在数千 GPU 上完成 1T 参数模型更新，并同时支持 broadcast 与 P2P 两类更新模式。

## Mooncake 关系
P2P 更新路径直接依赖 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake Transfer Engine]]，从已有 inference instance 的 CPU 内存向新加入实例的 GPU 发送权重。Mooncake/TENT 的 2026 论文也把 Checkpoint Engine 作为 RL parameter-update 场景之一，说明两者已经形成生产级训练 ↔ 推理数据平面关系。

## Serving 生态
- [[community/vllm-project/vLLM/vLLM|vLLM]]：官方 README 的主要 inference engine 测试路径之一。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：Checkpoint Engine 提供专门的分布式 checkpoint loading / weight-update 集成路径。
- Kimi-K2：项目 README 明确以 Kimi-K2 千卡/千 GPU 级权重更新作为生产案例。

## 维护信号
- [[company/月之暗面/checkpoint-engine/HubertZhang|HubertZhang]]：官方 PR 页面把 PR #80 标记为 **Collaborator**；2026 年持续发布 v0.3.4、v0.4.0、v0.4.1、v0.4.2，并直接修改 RDMA / EFA、ParameterServer 与 weight-update 核心路径，因此可建立高置信项目维护边。
- [[company/月之暗面/checkpoint-engine/weixiao-huang|weixiao-huang]]：发布 `v0.4.2-rc0`。当前没有稳定 Collaborator / CODEOWNERS / MAINTAINERS 证据，因此只记录 release-publishing / collaboration 信号，不与 HubertZhang 等强度处理。

GitHub 项目身份不能单独推出 Moonshot AI 雇佣关系；人物节点因此保持 handle-first。

## Sources
- https://github.com/MoonshotAI/checkpoint-engine
- https://github.com/MoonshotAI/checkpoint-engine/pulls
- https://github.com/MoonshotAI/checkpoint-engine/releases
- https://github.com/kvcache-ai/Mooncake
- https://arxiv.org/abs/2604.00368

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/月之暗面/月之暗面|月之暗面]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/月之暗面/checkpoint-engine/HubertZhang|HubertZhang]]：[[company/月之暗面/checkpoint-engine|Checkpoint Engine]]：GitHub Collaborator，且持续发布 v0.3.4、v0.4.0、v0.4.1、v0.4.2 等版本。
- [[company/月之暗面/checkpoint-engine/weixiao-huang|weixiao-huang]]：[[company/月之暗面/checkpoint-engine|Checkpoint Engine]]：2026 年 release publishing 活动，可作为后续治理核验线索。

<!-- END AUTO PROJECT PEOPLE -->
