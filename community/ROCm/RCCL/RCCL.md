---
type: project
name: RCCL
linked_people: []
linked_concepts:
  - "concept/communication/collectives/All-to-All"
  - "concept/communication/collectives/AllGather"
  - "concept/communication/collectives/AllReduce"
  - "concept/communication/collectives/Collective Communication"
  - "concept/hardware/interconnect/Hardware Interconnect"
  - "concept/hardware/interconnect/PCIe"
  - "concept/communication/data-movement/Point-to-Point Transfer"
  - "concept/communication/data-movement/RDMA"
  - "concept/communication/collectives/ReduceScatter"
  - "concept/hardware/interconnect/xGMI"
layer: communication
status: active
repository: https://github.com/ROCm/rocm-systems
docs: https://rocm.docs.amd.com/projects/rccl/en/latest/
areas:
  - "all-reduce"
  - "all-gather"
  - "reduce-scatter"
  - "all-to-all"
  - "point-to-point"
hardware:
  - "amd"
integrations:
companies: ["AMD"]
last_verified: "2026-09"
linked_companies:
  - "company/AMD/AMD"
---
# RCCL

> AMD ROCm 面向多 GPU、多节点的集合通信库。

## 核心能力

| 能力 | 说明 |
|---|---|
| Collectives | 覆盖 AllReduce、AllGather、AllToAll 等原语 |
| xGMI / PCIe | 优化 AMD GPU 节点内高速互联 |
| RDMA / Network | 支持跨节点 InfiniBand、RoCE 等通信路径 |
| P2P | 支持 GPU 到 GPU 点到点通信 |

## 边界

RCCL 位于通信层，不负责模型执行、Serving 或调度策略。

## 集成与后端

V0.1 将框架使用 RCCL 的关系记录在关联区，不自动把所有 ROCm 使用者标为强集成。

## 关联项目

- 通信对照：NCCL、VCCL、FlagCX。
- AMD 推理引擎路径：vLLM、SGLang。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前 ROCm RCCL 官方文档为快照。

## 直接来源

- https://rocm.docs.amd.com/projects/rccl/en/latest/
- https://github.com/ROCm/rocm-systems

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/AMD/AMD|AMD]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/collectives/All-to-All|All-to-All]]
- [[concept/communication/collectives/AllGather|AllGather]]
- [[concept/communication/collectives/AllReduce|AllReduce]]
- [[concept/communication/collectives/Collective Communication|Collective Communication]]
- [[concept/hardware/interconnect/Hardware Interconnect|Hardware Interconnect]]
- [[concept/hardware/interconnect/PCIe|PCIe]]
- [[concept/communication/data-movement/Point-to-Point Transfer|Point-to-Point Transfer]]
- [[concept/communication/data-movement/RDMA|RDMA]]
- [[concept/communication/collectives/ReduceScatter|ReduceScatter]]
- [[concept/hardware/interconnect/xGMI|xGMI]]

<!-- END AUTO PROJECT CONCEPTS -->
