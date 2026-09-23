---
type: company
name: SemiAnalysis
aliases: ["SemiAnalysisAI"]
linked_people:
  - "community/SemiAnalysisAI/InferenceX/Bryan Shan"
  - "community/SemiAnalysisAI/InferenceX/Cam Quilici"
  - "community/SemiAnalysisAI/InferenceX/Dylan Patel"
  - "community/SemiAnalysisAI/InferenceX/Kimbo Chen"
areas:
  - "semiconductor-research"
  - "ai-infrastructure"
  - "llm-inference"
  - "inference-benchmarking"
  - "gpu-architecture"
  - "datacenter-economics"
projects:
  - "InferenceX"
people:
  - "Dylan Patel"
  - "Kimbo Chen"
  - "Bryan Shan"
  - "Cam Quilici"
last_verified: "2026-09"
linked_projects:
  - "community/SemiAnalysisAI/InferenceX/InferenceX"
---
# SemiAnalysis

SemiAnalysis 是一家独立的半导体与 AI 研究机构，覆盖从半导体制造、封装、芯片设计、网络、数据中心，到 AI 模型、训练与推理基础设施的完整链条。对本仓库最重要的不是其媒体属性，而是它已经形成了可直接进入 AI Infra 图谱的工程与 benchmark 能力。

## 为什么进入 AI Infra 图谱

- 覆盖 AI model frameworks、training / inference infrastructure、performance 与 cost。
- 维护开源组织 [SemiAnalysisAI](https://github.com/SemiAnalysisAI)，公开发布推理 benchmark、GPU 微架构测试和 compiler fuzzing 项目。
- 核心开源项目 [[community/SemiAnalysisAI/InferenceX/InferenceX|InferenceX]] 持续测量真实硬件上的 LLM / agentic inference 表现，形成硬件、serving framework、模型与成本之间的可审计连接。

## 核心 AI Infra 项目

- [[community/SemiAnalysisAI/InferenceX/InferenceX|InferenceX]]：原名 InferenceMAX，持续 benchmark SGLang、vLLM、TensorRT-LLM、NVIDIA Dynamo 等 serving stack，并覆盖 NVIDIA、AMD、Google TPU 等硬件。
- SemiAnalysisAI 还公开维护 Blackwell microbenchmark 与 FuzzX 等工程项目；这些项目当前作为候选扩展节点保留，本轮不把它们与 InferenceX 混成同一实体。

## 关键人物

- [[community/SemiAnalysisAI/InferenceX/Dylan Patel|Dylan Patel]]：Founder、CEO、Chief Analyst。
- [[community/SemiAnalysisAI/InferenceX/Kimbo Chen|Kimbo Chen]]：长期参与 GPU architecture、inference performance 与 InferenceX 研究。
- [[community/SemiAnalysisAI/InferenceX/Bryan Shan|Bryan Shan]]：InferenceX / agentic inference 研究与 benchmark 工作。
- [[community/SemiAnalysisAI/InferenceX/Cam Quilici|Cam Quilici]]：InferenceX / AgentX 研究与 benchmark 工作。

## 图谱边界

SemiAnalysis 的文章经常分析 NVIDIA、AMD、Huawei、Google、OpenAI 等厂商，也会 benchmark SGLang、vLLM、TensorRT-LLM、Dynamo 等项目。**被分析、被 benchmark、提供算力或被引用，不自动等于组织合作或治理关系**。这些关系只在 InferenceX 项目页按“被测 stack / 硬件”描述，不升级为公司级强边。

## Sources

- https://semianalysis.com/about/
- https://semianalysis.com/dylan-patel/
- https://github.com/SemiAnalysisAI
- https://github.com/SemiAnalysisAI/InferenceX
- https://inferencex.semianalysis.com/about

<!-- BEGIN AUTO COMPANY PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `current_affiliations:` 与/或 `public_email` 企业域名规则反向汇总。邮箱域名证据表示可核验的组织关联，但不会单独推断当前任职、职级、直属汇报或团队归属。

- [[community/SemiAnalysisAI/InferenceX/Bryan Shan|Bryan Shan]]：人物页 `current_affiliations:` 明确记录。
- [[community/SemiAnalysisAI/InferenceX/Cam Quilici|Cam Quilici]]：人物页 `current_affiliations:` 明确记录。
- [[community/SemiAnalysisAI/InferenceX/Dylan Patel|Dylan Patel]]：人物页 `current_affiliations:` 明确记录。
- [[community/SemiAnalysisAI/InferenceX/Kimbo Chen|Kimbo Chen]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO COMPANY PEOPLE -->

<!-- BEGIN AUTO COMPANY COMMUNITY LINKS -->
## 社区 / 开源项目关联（自动汇总）

以下关系由公司页与社区/项目页的显式元数据双向汇总。员工个人参与不会自动升级为公司官方关系。

- [[community/SemiAnalysisAI/InferenceX/InferenceX|InferenceX]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMPANY COMMUNITY LINKS -->
