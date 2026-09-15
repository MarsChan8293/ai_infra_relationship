---
type: project
name: SpecForge
linked_people:
  - "community/sgl-project/SGLang/Shenggui Li"
companies: []
company_relation: community-led
layer: speculative-decoding
open_source: true
repository: https://github.com/sgl-project/SpecForge
areas: [speculative-decoding, draft-model-training, llm-inference, distributed-training]
last_verified: "2026-09"
---
# SpecForge

## 项目定位
SpecForge 是 SGLang 团队维护的 speculative decoding 训练框架，目标是训练可直接接入 [[SGLang]] serving 的 draft models，并覆盖在线/离线、colocated/disaggregated 等训练与推理拓扑。

## AI Infra 价值
- 把 speculative decoding 从单一算法实现推进为可维护的训练/服务一体化工程框架。
- 与 [[SGLang]] serving stack 直接兼容，减少 draft model 到生产推理的额外移植成本。
- 2026 持续扩展 DFlash、DFlash2、Domino、DSpark 等方法，并支持更完整的 disaggregated training / inference 路径。

## 生态关系
SpecForge 属于 SGLang 生态项目，并被 LMSYS 作为旗舰项目持续推广。人物关系以对应人物页的 `projects:` / `communities:` 和公开作者/维护记录为准，不因为同属 SGLang 生态自动推断长期同事关系。

## Sources
- https://github.com/sgl-project/SpecForge
- https://github.com/sgl-project/SpecForge/blob/main/README.md

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]]：[[SGLang]]：当前 Core Dev；进一步负责 SpecForge，聚焦 speculative decoding / serving systems。

<!-- END AUTO PROJECT PEOPLE -->
