---
type: project
name: KServe
linked_people: []
linked_concepts:
  - "concept/inference/scheduling/Autoscaling"
  - "concept/inference/scheduling/Inference-Aware Routing"
  - "concept/inference/scheduling/KV-Aware Routing"
  - "concept/inference/scheduling/Load Balancing"
  - "concept/inference/scheduling/Request Routing"
layer: distributed-serving
status: active
repository: https://github.com/kserve/kserve
docs: https://kserve.github.io/website/
areas:
  - "kubernetes-model-serving"
  - "llm-inference-service"
  - "autoscaling"
  - "inference-routing"
  - "kubernetes"
integrations:
  - "vLLM"
  - "Gateway API Inference Extension"
last_verified: "2026-09"
linked_companies: []
---
# KServe

> Kubernetes 原生模型服务控制面，覆盖传统 InferenceService 与 LLMInferenceService。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| InferenceService | 标准化模型部署与服务入口 | [S1] |
| LLMInferenceService | 面向生成式 AI 的 LLM serving API | [S1] |
| 多节点 / 分离式工作负载 | 可表达多节点并行与 Prefill/Decode 分离 | [S1] |
| Gateway 集成 | 通过 Kubernetes Gateway 体系暴露和路由服务 | [S1] |

## 边界

KServe 主要负责 Kubernetes 模型服务生命周期和 API 编排，不负责底层 LLM kernel 与单 worker 执行优化。

## 集成与后端

- vLLM：KServe 生成式推理 runtime 的主要高性能后端之一。
- Gateway API Inference Extension：LLMInferenceService 路由基础设施之一。

## 关联项目

- 分布式推理编排：llm-d。
- 另一条分布式服务路线：Ray Serve。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- [S1] https://kserve.github.io/website/
- [S2] https://github.com/kserve/kserve

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/scheduling/Autoscaling|Autoscaling]]
- [[concept/inference/scheduling/Inference-Aware Routing|Inference-Aware Routing]]
- [[concept/inference/scheduling/KV-Aware Routing|KV-Aware Routing]]
- [[concept/inference/scheduling/Load Balancing|Load Balancing]]
- [[concept/inference/scheduling/Request Routing|Request Routing]]

<!-- END AUTO PROJECT CONCEPTS -->
