---
type: project
name: Colossal-AI
linked_people:
  - "community/hpcaitech/Colossal-AI/Hongxin Liu"
  - "community/sgl-project/SGLang/Shenggui Li"
  - "company/字节跳动/方佳瑞 Jiarui Fang"
  - "company/潞晨科技/Haichen Huang"
  - "company/潞晨科技/尤洋 Yang You"
companies: ["潞晨科技"]
company_relation: company-originated
layer: distributed-training
open_source: true
linked_companies:
  - "company/潞晨科技/潞晨科技"
---
# Colossal-AI

## 项目简介
Colossal-AI 是由 [[潞晨科技]] 发起的大规模 AI 训练/推理系统，覆盖 data / tensor / pipeline / sequence parallelism、ZeRO、异构内存、MoE、checkpoint 与 RL/LLM 训练等方向。

## 主要贡献公司
- [[company/潞晨科技/潞晨科技|潞晨科技]]：项目发起方与长期核心工程组织，是本图谱中 Colossal-AI 最强的公司级归属边。

## 核心人物网络
- [[company/潞晨科技/尤洋 Yang You|尤洋（Yang You）]] — HPC-AI Tech 创始人；Colossal-AI 创业/研究核心
- [[company/潞晨科技/Haichen Huang|Haichen Huang]] — 当前 HPC-AI 工程师；Elixir / large-scale LLM training
- [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]] — 原始系统作者；持续活跃于 release、ZeRO、FP8、checkpoint 等维护
- [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞（Jiarui Fang）]] — 前 HPC-AI CTO / Colossal-AI lead；当前 ByteDance AI infra
- [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]] — Colossal-AI 早期核心作者/MLSys startup founding member；当前 SGLang Core Dev、SpecForge Lead

## BFS 主线
[[潞晨科技]] → Colossal-AI → 分布式训练 / 异构内存 / 自动并行；随后人才分别流向 [[字节跳动]] AI infra 与 [[SGLang]] speculative decoding / serving，构成训练系统到推理系统的人才桥。

## Sources
- https://github.com/hpcaitech/ColossalAI
- https://openreview.net/pdf?id=WO3qJC2TOG
- https://colossalai.org/docs/concepts/colossalai_overview/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]]：Colossal-AI 原始系统论文作者之一，论文时期 affiliation 为 [[潞晨科技]]。
- [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]]：[[Colossal-AI]]：原始系统作者之一，参与早期文档、系统设计与开源工程。
- [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞（Jiarui Fang）]]：[[潞晨科技]]：CTO，2022-02–2023-03；负责 Colossal-AI 等大规模训练系统。
- [[company/潞晨科技/Haichen Huang|Haichen Huang]]：[[Colossal-AI]]：原始系统论文作者之一；参与 MoE、异构训练与训练系统文档/实现。
- [[company/潞晨科技/尤洋 Yang You|尤洋（Yang You）]]：[[潞晨科技]]：创始人，公司围绕 Colossal-AI 提供大模型训练、微调、推理与企业级平台。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/潞晨科技/潞晨科技|潞晨科技]]：公司页与社区/项目页均有显式记录；关系：`company-originated`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
