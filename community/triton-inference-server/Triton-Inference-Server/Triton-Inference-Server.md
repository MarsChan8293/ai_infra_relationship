---
type: project
name: Triton Inference Server
linked_people:
  - "community/triton-inference-server/Triton-Inference-Server/Akhil Saraswathi"
  - "community/triton-inference-server/Triton-Inference-Server/Faradawn Yang"
  - "community/triton-inference-server/Triton-Inference-Server/Sai Kiran Polisetty"
  - "community/triton-inference-server/Triton-Inference-Server/Yingge He"
companies: ["NVIDIA"]
company_relation: company-led
layer: production-inference-server
open_source: true
---
# Triton Inference Server

## 项目简介
Triton Inference Server 是 NVIDIA 的通用 production inference server，支持多种 framework/backend、动态 batching、并发模型执行、metrics 与 cloud/datacenter/edge 部署。它早于当前 LLM-specialized serving 热潮，是 NVIDIA production inference 栈的重要基础层。

## GitHub
https://github.com/triton-inference-server/server

## 主要贡献公司
- [[company/NVIDIA/NVIDIA|NVIDIA]]：项目发起与主要维护公司。

## 主要维护者 / 组织
由 [[NVIDIA]] / Triton Inference Server 社区维护，具体 backend 通常分布在多个仓库与子项目中。

## 生态关系
[[TensorRT-LLM]] · [[Dynamo]] · [[NVIDIA]]。在本图谱中它代表较通用的模型服务器层，TensorRT-LLM 代表 LLM runtime，Dynamo 代表数据中心级 orchestration。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/triton-inference-server/Triton-Inference-Server/Akhil Saraswathi|Akhil Saraswathi]]：[[Triton-Inference-Server]]：CI / Torch AOTI 贡献者
- [[community/triton-inference-server/Triton-Inference-Server/Faradawn Yang|Faradawn Yang]]：Project source / contributor context: https://github.com/triton-inference-server/server
- [[community/triton-inference-server/Triton-Inference-Server/Sai Kiran Polisetty|Sai Kiran Polisetty]]：[[Triton-Inference-Server]]：当前活跃工程贡献者
- [[community/triton-inference-server/Triton-Inference-Server/Yingge He|Yingge He]]：[[Triton-Inference-Server]]：Torch AOTI / QA integration 活跃贡献者

<!-- END AUTO PROJECT PEOPLE -->
