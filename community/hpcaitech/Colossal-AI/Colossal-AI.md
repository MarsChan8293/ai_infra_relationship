---
type: project
name: Colossal-AI
companies: ["潞晨科技"]
company_relation: company-originated
layer: distributed-training
open_source: true
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
