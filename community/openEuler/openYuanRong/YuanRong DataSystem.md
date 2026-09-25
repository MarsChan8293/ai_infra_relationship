---
type: project
name: YuanRong DataSystem
aliases: [openYuanRong DataSystem, yuanrong-datasystem]
linked_people: []
linked_concepts:
  - "concept/storage/Distributed Storage"
  - "concept/memory/HBM"
  - "concept/hardware/interconnect/HCCS"
  - "concept/memory/Memory Hierarchy"
  - "concept/memory/Memory Pooling"
  - "concept/storage/NVMe SSD"
  - "concept/storage/Remote Object Store"
  - "concept/storage/Storage Tiering"
layer: distributed-data-cache
open_source: true
repository: https://github.com/openyuanrong/datasystem
areas: [distributed-cache, kv-cache, hbm, dram, ssd, rdma, hccs, npu, data-transfer]
related_projects: ["openYuanRong", "YuanRong TransferEngine", "TransferQueue", "vLLM-Ascend", "vLLM-Omni"]
last_verified: "2026-09"
linked_companies: []
---
# YuanRong DataSystem

## 项目简介
YuanRong DataSystem 是 [[community/openEuler/openYuanRong/openYuanRong|openYuanRong]] 的分布式数据系统。官方项目把它定位为近计算的异构多级缓存：利用集群 HBM、DRAM 与 SSD 构建 pooled cache，并提供 Object / Stream / KV 等数据语义与跨节点数据移动。

## AI Infra 连接
- [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]：官方 KV Pool 文档已经支持 YuanRong 作为 storage backend，复用 AscendStoreConnector backend abstraction。
- [[community/Ascend/TransferQueue/TransferQueue|TransferQueue]]：首个可插拔 KV storage backend 即 openYuanRong DataSystem；在 NPU 场景支持 HCCS、RDMA 与远程 H2D / D2H 路径。
- [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]]：`YuanrongConnector` 使用 DataSystem 作为跨节点分布式 KV store。

这几条关系都属于明确的软件集成，不据此推断项目维护者之间的人际关系。

## Sources
- https://github.com/openyuanrong/datasystem
- https://pypi.org/project/openyuanrong-datasystem/
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_pool.html
- https://github.com/Ascend/TransferQueue/blob/main/docs/storage_backends/openyuanrong_datasystem.md
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/disaggregated_inference/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/storage/Distributed Storage|Distributed Storage]]
- [[concept/memory/HBM|HBM]]
- [[concept/hardware/interconnect/HCCS|HCCS]]
- [[concept/memory/Memory Hierarchy|Memory Hierarchy]]
- [[concept/memory/Memory Pooling|Memory Pooling]]
- [[concept/storage/NVMe SSD|NVMe SSD]]
- [[concept/storage/Remote Object Store|Remote Object Store]]
- [[concept/storage/Storage Tiering|Storage Tiering]]

<!-- END AUTO PROJECT CONCEPTS -->
