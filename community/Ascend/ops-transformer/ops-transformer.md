---
type: project
name: ops-transformer
linked_people:
  - "community/Ascend/ops-transformer/Konstantin Berestizshevsky"
  - "community/Ascend/ops-transformer/tangkaidi"
  - "community/Ascend/ops-transformer/wangchao661"
companies: ["华为"]
company_relation: company-led
layer: npu-kernels
hardware: [Ascend]
open_source: true
linked_companies:
  - "company/华为/华为"
---
# ops-transformer

## 项目简介
CANN 面向 Transformer 与大模型场景的算子库，包含 attention、MoE 与推理相关 NPU kernel。

## GitCode
https://gitcode.com/cann/ops-transformer

## GitHub
未确认官方 GitHub canonical repository；本节点以官方 GitCode 仓库作为源码来源。

## 主要贡献公司
- [[company/华为/华为|华为]]：CANN / Ascend 算子栈的主要开发与维护公司节点。

## 推理优化人物
[[Konstantin Berestizshevsky]] · [[tangkaidi]] · [[wangchao661]]

## 生态关系
[[vLLM-Ascend]] · [[MindIE-LLM]]

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]]：2026 年在 CANN `ops-transformer` 贡献 Quest-based block-sparse attention predictor 的 AscendC kernel。
- [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]]：2026 年在 CANN `ops-transformer` 推进 A5 推理 `BlockSparseAttention` 的 BSND input layout 支持，使推理算子 layout 能力继续向训练侧已有格式对齐。
- [[community/Ascend/ops-transformer/wangchao661|wangchao661]]：2026 年在 CANN `ops-transformer` 的 experimental attention 路径为 `BlockSparseAttention` 增加 MXFP4 能力，并扩展相关 aclnn 接口参数。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
