---
type: project
name: NVIDIA Dynamo
linked_people:
  - "community/ai-dynamo/Dynamo/Alec Flowers"
  - "community/ai-dynamo/Dynamo/Ishan Dhanani"
  - "community/ai-dynamo/Dynamo/Julien Mancuso"
  - "community/ai-dynamo/Dynamo/Karen Chung"
  - "community/ai-dynamo/Dynamo/Matej Kosec"
  - "community/ai-dynamo/Dynamo/Ryan McCormick"
  - "community/ai-dynamo/Dynamo/Stefan Schimanski"
  - "community/ai-dynamo/Dynamo/Sungsoo Ha"
  - "community/ai-dynamo/NIXL/Adit Ranadive"
  - "community/kvcache-ai/Mooncake/马腾 Teng Ma"
  - "community/triton-inference-server/Triton-Inference-Server/Yingge He"
governance: company-led
companies: ["NVIDIA"]
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/ai-dynamo/Dynamo/Alec Flowers|Alec Flowers]]：[[Dynamo]]：frontend、vLLM sidecar、agentic protocol 相关工程
- [[community/ai-dynamo/Dynamo/Ishan Dhanani|Ishan Dhanani]]：[[Dynamo]]：distributed / agentic inference
- [[community/ai-dynamo/Dynamo/Julien Mancuso|Julien Mancuso]]：[[Dynamo]]：Kubernetes/operator 相关活跃贡献者
- [[community/ai-dynamo/Dynamo/Karen Chung|Karen Chung]]：[[Dynamo]]：核心工程与社区活动
- [[community/ai-dynamo/Dynamo/Matej Kosec|Matej Kosec]]：[[Dynamo]]：核心工程贡献者
- [[community/ai-dynamo/Dynamo/Ryan McCormick|Ryan McCormick]]：Project source / contributor context: https://github.com/ai-dynamo/dynamo
- [[community/ai-dynamo/Dynamo/Stefan Schimanski|Stefan Schimanski]]：[[NVIDIA]] Dynamo Engineering
- [[community/ai-dynamo/Dynamo/Sungsoo Ha|Sungsoo Ha]]：[[Dynamo]]：recipes 与大模型部署优化方向活跃贡献者
- [[community/ai-dynamo/NIXL/Adit Ranadive|Adit Ranadive]]：Project source / contributor context: https://github.com/ai-dynamo/nixl
- [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾（Teng Ma）]]：社区贡献关联；人物页已明确记录该社区。
- [[community/triton-inference-server/Triton-Inference-Server/Yingge He|Yingge He]]：[[Dynamo]] 生态协作

<!-- END AUTO PROJECT PEOPLE -->
