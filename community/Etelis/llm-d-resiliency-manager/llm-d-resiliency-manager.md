---
type: project
name: llm-d-resiliency-manager
linked_people: []
linked_concepts:
  - "concept/inference/reliability/Inference Fault Tolerance"
layer: distributed-serving
status: active
repository: https://github.com/Etelis/llm-d-resiliency-manager
docs: https://github.com/Etelis/llm-d-resiliency-manager/tree/main/docs
areas:
  - "fault-tolerance"
  - "failure-recovery"
  - "expert-parallel"
  - "rank-exclusion"
  - "routing-coordination"
  - "kubernetes"
integrations:
  - "llm-d"
  - "vLLM"
last_verified: "2026-10"
linked_companies: []
---
# llm-d-resiliency-manager
## 项目定位

llm-d-resiliency-manager 是针对 [[community/llm-d/llm-d/llm-d|llm-d]] Expert Parallel inference group 的实验性 recovery coordinator。它不是 llm-d 主仓库当前已合并的内置能力；README 明确写为 **proposed for llm-d incubation**，因此本图谱保留其独立 repo 身份。

## 恢复流程

当 worker 失败时，manager：

1. 暂停 routing；
2. 调用 [[community/vllm-project/vLLM/vLLM|vLLM]] fault-tolerance API 排除失败 rank；
3. 检查 surviving ranks 是否还能完成 inference；
4. 恢复 routing。

Pod replacement / group reset 仍由 LeaderWorkerSet 负责，因此它展示的是“container/group lifecycle”与“inference runtime membership recovery”之间的责任切分。

## 当前限制

官方 scope 当前是单个 group、DP=EP、TP=1，最多移除一个 non-master rank；依赖 redundant experts 和 supervisor 保持容器不因子进程失败而整体重启。仓库还明确说明尚未用真实 GPU workload + routing adapter 做完整验证。

该项目是 [[concept/inference/reliability/Inference Fault Tolerance|Inference Fault Tolerance]] 的直接样本，但现阶段应视为 experimental control-plane prototype，而不是已验证的生产 HA 方案。

## Sources

- https://github.com/Etelis/llm-d-resiliency-manager

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/reliability/Inference Fault Tolerance|Inference Fault Tolerance]]

<!-- END AUTO PROJECT CONCEPTS -->
