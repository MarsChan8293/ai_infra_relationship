---
type: project
name: NVIDIA Dynamo
governance: company-led
company: NVIDIA
companies: [NVIDIA]
company_relation: company-led
layer: distributed-inference-orchestration
open_source: true
---
# NVIDIA Dynamo

## 项目简介
Dynamo 是数据中心尺度的分布式 inference serving framework，负责把多个推理 worker、路由、KV/data movement、缓存和弹性伸缩组织成完整 serving 系统。它重点覆盖 PD disaggregation、KV-aware routing、multi-tier cache、autoscaling、Kubernetes operator 与 fault tolerance，并支持多种 engine。

## GitHub
https://github.com/ai-dynamo/dynamo

## 主要贡献公司
- [[company/NVIDIA/NVIDIA|NVIDIA]]：项目发起与主要工程组织；在 ai-dynamo 组织下开放开发。

## 主要维护者 / 组织
由 NVIDIA 发起并在 ai-dynamo 组织下开放开发，仓库明确面向 vLLM、SGLang、TensorRT-LLM 等后端。

## 生态关系
- Engines：[[vLLM]] · [[SGLang]] · [[TensorRT-LLM]]
- Data movement：[[NIXL]]
- Company：[[NVIDIA]]
- Kubernetes：承载大规模部署与 operator 能力。
