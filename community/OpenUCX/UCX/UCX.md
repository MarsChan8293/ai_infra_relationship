---
type: project
name: UCX
linked_people: []
linked_concepts:
  - "concept/communication/data-movement/Point-to-Point Transfer"
  - "concept/communication/data-movement/RDMA"
layer: communication
status: active
repository: https://github.com/openucx/ucx
docs: https://openucx.readthedocs.io/en/master/
areas:
  - "rdma"
  - "tcp"
  - "shared-memory"
  - "gpu-memory"
  - "communication-abstraction"
  - "network"
hardware:
  - "cpu"
  - "nvidia"
  - "amd"
integrations:
  - "NIXL"
last_verified: "2026-09"
linked_companies: []
---
# UCX

> 面向高带宽、低延迟网络的通用通信框架与传输抽象。

## 核心能力

| 能力 | 说明 |
|---|---|
| RDMA | 支持 InfiniBand、RoCE 等 RDMA 网络 |
| 多 Transport | 统一 TCP、shared memory、GPU 等传输路径 |
| 通信原语 | 提供面向上层框架的通信 API |
| 硬件抽象 | 根据可用硬件选择合适数据路径 |

## 边界

UCX 是底层通信框架，不理解 LLM 请求、KV 生命周期或 Kubernetes workload 语义。

## 集成与后端

- NIXL：UCX 是 NIXL 支持的数据传输 backend 之一。

## 关联项目

- 集合通信与异构通信对照：VCCL。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前 OpenUCX 官方资料为快照。

## 直接来源

- https://github.com/openucx/ucx
- https://openucx.readthedocs.io/en/master/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/data-movement/Point-to-Point Transfer|Point-to-Point Transfer]]
- [[concept/communication/data-movement/RDMA|RDMA]]

<!-- END AUTO PROJECT CONCEPTS -->
