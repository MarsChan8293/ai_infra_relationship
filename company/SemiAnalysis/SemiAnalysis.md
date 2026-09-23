---
type: company
name: SemiAnalysis
aliases: ["SemiAnalysisAI"]
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
