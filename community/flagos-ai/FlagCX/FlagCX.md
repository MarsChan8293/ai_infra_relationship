---
type: project
name: FlagCX
linked_concepts:
  - "concept/communication/collectives/AllGather"
  - "concept/communication/collectives/AllReduce"
  - "concept/communication/collectives/Collective Communication"
status: active
linked_people:
  - "community/flagos-ai/FlagCX/MC952-arch"
  - "community/flagos-ai/FlagCX/mikethegoblin"
  - "community/flagos-ai/FlagOS/敖玉龙 Yulong Ao"
  - "community/flagos-ai/FlagOS/曹州"
companies: []
company_relation: community-led
layer: communication
repository: https://github.com/flagos-ai/FlagCX
areas:
  - "collective-communication"
  - "heterogeneous-computing"
  - "distributed-training"
  - "distributed-inference"
  - "heterogeneous-communication"
integrations: []
last_verified: "2026-09"
linked_companies: []
---
# FlagCX

## 项目简介
FlagCX 是 FlagOS 的统一集合通信库，面向不同 AI 芯片提供多框架、多硬件的通信抽象与高效跨芯通信能力。对大模型推理而言，它连接 tensor/pipeline/expert parallel 等分布式执行与底层多种硬件通信栈。

## GitHub
https://github.com/flagos-ai/FlagCX

## 主要维护者 / 组织
当前官方 `MAINTAINERS.md` 可确认 `MC952-arch`、`Caozhou1995`、`aoyulong` 等维护者。[[敖玉龙 Yulong Ao]] 2026 年公开资料明确负责 FlagCX；[[曹州]] 同时出现在 FlagCX 与 FlagScale 维护网络中。

## 生态关系
[[FlagOS]] · [[FlagScale]] · [[FlagGems]] · [[vllm-plugin-FL]] · [[sglang-plugin-FL]]。这里的连接是通信层与框架/插件的技术依赖关系。

## Sources
- https://github.com/flagos-ai/FlagCX
- https://github.com/flagos-ai/FlagCX/blob/main/MAINTAINERS.md
- https://hub.baai.ac.cn/view/55412
- https://hub.baai.ac.cn/view/46246

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/flagos-ai/FlagCX/MC952-arch|MC952-arch]]：https://raw.githubusercontent.com/flagos-ai/FlagCX/main/MAINTAINERS.md
- [[community/flagos-ai/FlagCX/mikethegoblin|mikethegoblin]]：https://raw.githubusercontent.com/flagos-ai/FlagCX/main/MAINTAINERS.md
- [[community/flagos-ai/FlagOS/敖玉龙 Yulong Ao|敖玉龙（Yulong Ao）]]：[[FlagCX]]：**开源项目维护**；当前官方 MAINTAINERS 列表包含 `aoyulong`，智源官方资料同时明确其负责该统一通信库。
- [[community/flagos-ai/FlagOS/曹州|曹州]]：[[FlagCX]]：**开源项目维护**；官方 MAINTAINERS 同样列出 `Caozhou1995`。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/collectives/AllGather|AllGather]]
- [[concept/communication/collectives/AllReduce|AllReduce]]
- [[concept/communication/collectives/Collective Communication|Collective Communication]]

<!-- END AUTO PROJECT CONCEPTS -->
