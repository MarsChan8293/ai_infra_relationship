---
type: project
name: msModelSlim
status: active
last_verified: "2026-09"
linked_people: []
companies: ["华为"]
company_relation: company-led
layer: optimization
hardware:
  - "ascend"
areas:
  - "model-compression"
  - "quantization"
integrations: []
linked_companies:
  - "company/华为/华为"
---
# msModelSlim

## 项目简介
msModelSlim 是昇腾侧模型压缩与量化工具链。本图谱重点跟踪与推理性能直接相关的 W8A8、W4A8、MXFP8、MXFP4、MoE 与 MTP 量化实现，以及这些量化产物与 MindIE / vLLM-Ascend 的部署连接。

截至 2026-09，公开 MR 已覆盖 Step-3.5-Flash 的 MoE W8A8 + MTP 量化，以及 DeepSeek-V4-Pro 的 W4A8 / W8A8 等低比特路径。对本图谱而言，它是 Ascend quantization 人才向 serving runtime 输出能力的主要入口。

## GitCode
https://gitcode.com/Ascend/msmodelslim

## GitHub
未确认官方 GitHub canonical repository；本节点以官方 GitCode 仓库作为源码来源。

## 主要贡献公司
- [[company/华为/华为|华为]]：Ascend 模型压缩/量化官方工具链的主要开发与维护公司节点。

## 生态关系
[[MindIE-LLM]] · [[MindIE-SD]] · [[vLLM-Ascend]]

## Sources
- https://gitcode.com/Ascend/msmodelslim/tree/master/lab_practice/step_3_5_flash
- https://gitcode.com/Ascend/msmodelslim/tree/master/msmodelslim/model

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
