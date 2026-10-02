---
type: project
name: Megatron-LM
linked_people: []
linked_concepts:
  - "concept/inference/parallelism/Sequence Parallelism"
layer: training
status: active
repository: https://github.com/NVIDIA/Megatron-LM
docs: https://docs.nvidia.com/megatron-core/developer-guide/latest/
areas:
  - distributed-training
  - tensor-parallel
  - sequence-parallel
  - context-parallel
  - expert-parallel
hardware:
  - nvidia
companies: ["NVIDIA"]
last_verified: "2026-09"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---

# Megatron-LM

## 项目简介

Megatron-LM / Megatron Core 是 NVIDIA 面向大模型训练与模型并行的开源基础设施，覆盖 Tensor Parallelism、Pipeline Parallelism、Sequence Parallelism、Context Parallelism、Expert Parallelism 等组合。

## 与 Sequence Parallelism 的关系

Megatron-LM 直接实现 `sequence_parallel` 配置与执行路径。官方代码和文档明确描述 TP + Sequence Parallelism 会引入 activation AllGather / ReduceScatter，并在 LayerNorm、embedding、通信 overlap 等路径中使用 sequence-parallel 标记。

这正对应本仓库对经典 Megatron-style Sequence Parallelism 的定义：在 TP 基础上沿 sequence 维分片部分 activation，减少复制的 activation memory，而不是把整个长上下文 attention 都等同于 Context Parallelism。

## Sources

- https://github.com/NVIDIA/Megatron-LM
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
- https://github.com/NVIDIA/Megatron-LM/blob/main/megatron/core/transformer/moe/README.md
- https://github.com/NVIDIA/Megatron-LM/blob/main/megatron/core/fusions/fused_layer_norm.py

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/parallelism/Sequence Parallelism|Sequence Parallelism]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
