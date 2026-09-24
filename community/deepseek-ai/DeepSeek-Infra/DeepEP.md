---
type: project
name: DeepEP
parent: DeepSeek-Infra
linked_concepts:
  - "concept/communication/collectives/All-to-All"
  - "concept/communication/collectives/Collective Communication"
  - "concept/inference/parallelism/Expert Parallelism"
  - "concept/communication/data-movement/RDMA"
status: active
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Chengqi Deng"
  - "community/deepseek-ai/DeepSeek-Infra/Jiashi Li"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/Liang Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Liyue Zhang"
  - "community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu"
  - "community/deepseek-ai/DeepSeek-Infra/Zhean Xu"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
repository: https://github.com/deepseek-ai/DeepEP
docs: https://github.com/deepseek-ai/DeepEP
last_verified: "2026-09"
companies: ["深度求索"]
company_relation: company-led
layer: communication
linked_companies:
  - "company/深度求索/深度求索"
areas:
  - "expert-parallel"
  - "all-to-all"
  - "moe-dispatch"
  - "moe-combine"
  - "low-latency"
hardware:
  - "nvidia"
integrations:
  - "NCCL"
---
# DeepEP

## 项目简介
DeepEP 是 DeepSeek 面向 MoE Expert Parallel 的高性能通信库，优化 token dispatch/combine、跨 GPU/节点通信与低延迟/高吞吐 EP 路径，是模型 MoE 架构下沉到系统通信层的典型项目。

## GitHub
https://github.com/deepseek-ai/DeepEP

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。原始公开作者网络已记录 [[赵成钢 Chenggang Zhao]]、[[Shangyan Zhou]]、[[Liyue Zhang]]、[[Chengqi Deng]]、[[Zhean Xu]]、[[Yuxuan Liu]]、[[Kuai Yu]]、[[Jiashi Li]]、[[Liang Zhao]]。

## 生态关系
[[vLLM]] · [[SGLang]] · [[NIXL]] · [[DeepGEMM]] · [[MoonEP]]。MoonEP 官方 acknowledgments 将 DeepEP 列为 inspiration，属于项目级技术关系，不自动推出人物直接合作。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Chengqi Deng|Chengqi Deng]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：[[DeepEP]]：2025 原始公开作者
- [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]]：项目关联；人物页已明确记录该项目。
- [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Liyue Zhang|Liyue Zhang]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou|Shangyan Zhou]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu|Yuxuan Liu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：[[DeepEP]]：2025 公开项目原始作者

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/collectives/All-to-All|All-to-All]]
- [[concept/communication/collectives/Collective Communication|Collective Communication]]
- [[concept/inference/parallelism/Expert Parallelism|Expert Parallelism]]
- [[concept/communication/data-movement/RDMA|RDMA]]

<!-- END AUTO PROJECT CONCEPTS -->
