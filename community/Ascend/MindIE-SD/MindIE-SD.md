---
type: project
name: MindIE-SD
status: active
linked_people: []
last_verified: "2026-09"
companies: ["华为"]
company_relation: company-led
layer: inference-engine
hardware:
  - "ascend"
areas:
  - "diffusion-inference"
  - "ascend-inference"
integrations: []
linked_companies:
  - "company/华为/华为"
---
# MindIE-SD

## 项目简介
MindIE-SD 是昇腾侧推理组件。本图谱只保留与大模型推理优化直接相关的 MoE、EP/TP 通信、dispatcher 与量化路径，不扩展一般模型适配。

## GitCode
https://gitcode.com/Ascend/MindIE-SD

## GitHub
未确认官方 GitHub canonical repository；本节点以官方 GitCode 仓库作为源码来源。

## 主要贡献公司
- [[company/华为/华为|华为]]：Ascend/MindIE 官方技术栈的主要开发与维护公司节点。

## 推理优化人物
- [[betta18]]：2026 年处理 MoE dispatcher 路由选择与 W8A8 dynamic quant 精度对齐，并利用 `top_k` 与 EP size 关系决定 static / dynamic dispatcher。

## 生态关系
[[vLLM-Ascend]] · [[MindIE-LLM]] · [[msModelSlim]]

## Sources
- https://gitcode.com/Ascend/MindIE-SD/tree/master/tests/layers

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
