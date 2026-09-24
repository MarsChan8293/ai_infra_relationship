---
type: project
name: Gateway API Inference Extension
linked_people: []
linked_concepts:
  - "concept/inference/scheduling/Inference-Aware Routing"
  - "concept/inference/scheduling/Load Balancing"
  - "concept/inference/scheduling/Load-Aware Routing"
  - "concept/inference/scheduling/Request Routing"
layer: distributed-serving
status: active
repository: https://github.com/kubernetes-sigs/gateway-api-inference-extension
docs: https://gateway-api-inference-extension.sigs.k8s.io/
areas:
  - "inference-pool"
  - "inference-aware-routing"
  - "gateway-api"
  - "multi-cluster-routing"
  - "kubernetes"
integrations:
  - "KServe"
  - "llm-d"
last_verified: "2026-09"
linked_companies: []
---
# Gateway API Inference Extension

> 为 Kubernetes Gateway API 增加面向生成式推理的端点选择与路由语义。

## 核心能力

| 能力 | 说明 |
|---|---|
| InferencePool | 把推理 Pod 与路由扩展组织成 Gateway backend |
| Inference-aware Routing | 根据推理负载与指标选择端点 |
| Gateway API | 沿用 Kubernetes Gateway API 资源模型 |
| 多集群方向 | 支持导入远端 InferencePool 的能力演进 |

## 边界

它定义路由/API 扩展，不执行模型计算，也不承担 GPU/Pod 资源调度。

## 集成与后端

- KServe：LLMInferenceService 使用该类 inference routing 基础设施。
- llm-d：同属 Kubernetes inference-aware routing 生态。

## 关联项目

- Kubernetes LLM 基础设施：AIBrix。
- 更上层的模型 Gateway：LiteLLM。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://gateway-api-inference-extension.sigs.k8s.io/
- https://github.com/kubernetes-sigs/gateway-api-inference-extension

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/scheduling/Inference-Aware Routing|Inference-Aware Routing]]
- [[concept/inference/scheduling/Load Balancing|Load Balancing]]
- [[concept/inference/scheduling/Load-Aware Routing|Load-Aware Routing]]
- [[concept/inference/scheduling/Request Routing|Request Routing]]

<!-- END AUTO PROJECT CONCEPTS -->
