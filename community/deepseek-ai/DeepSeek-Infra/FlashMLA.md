---
type: project
name: FlashMLA
parent: DeepSeek-Infra
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Jiashi Li"
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
companies: ["深度求索"]
company_relation: company-led
layer: attention-kernels
open_source: true
linked_companies:
  - "company/深度求索/深度求索"
---
# FlashMLA

## 项目简介
FlashMLA 是 DeepSeek 面向 Multi-head Latent Attention（MLA）与相关 sparse/efficient attention 路径的 GPU kernel 项目，把 DeepSeek 模型架构中的 attention 特性下沉为可复用、高性能实现。

## GitHub
https://github.com/deepseek-ai/FlashMLA

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。原始公开作者节点包括 [[Jiashi Li]] 与 [[刘胜与 Shengyu Liu]]。

## 生态关系
[[FlashInfer]] · [[vLLM]] · [[SGLang]] · [[DeepGEMM]]。FlashMLA 是模型特定 attention kernel 与通用 serving kernel 生态之间的连接点。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：[[FlashMLA]]：2025 公开作者
- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：[[FlashMLA]]：高性能 MLA decoding kernels；公开作者 / 核心技术贡献

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
