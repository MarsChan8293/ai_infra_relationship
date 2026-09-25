---
type: project
name: Megatron-LM
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
companies:
  - NVIDIA
last_verified: "2026-09"
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
