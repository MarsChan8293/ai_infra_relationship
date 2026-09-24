---
type: concept
name: Tensor Parallelism
aliases:
  - TP
  - Tensor Model Parallelism
  - 张量并行
domain: inference
topic: parallelism
parent_concepts:
  - Parallelism
related_concepts:
  - Sequence Parallelism
  - Context Parallelism
projects:
  - vLLM
last_verified: 2026-09
---

# Tensor Parallelism

## 一句话定义

Tensor Parallelism（TP）在单个 Transformer layer 内把权重张量和对应矩阵计算切到多个设备上，并通过 collective communication 合并中间结果。

## 解决的问题

当一个 layer 的权重或计算无法由单卡高效承载时，TP 可以让多个 GPU/NPU 同时参与同一层的 forward，而不是把整层放在一个设备上。

## 核心机制

常见做法是对线性层做 column-parallel / row-parallel 切分，每个 rank 保存部分权重并计算部分输出，再通过 AllReduce、AllGather 或 ReduceScatter 等 collective 恢复后续算子需要的数据布局。Attention head 和 MLP projection 也可按兼容维度切分。

## 与相邻概念的区别

- [[Pipeline Parallelism]] 沿模型深度切不同 layer，TP 则在同一 layer 内切 tensor。
- [[Sequence Parallelism]] 常与 TP 组合，用 sequence 维进一步降低 replicated activation。
- [[Context Parallelism]] 面向更完整的长上下文计算/状态分片，不等同于传统 TP 附带的 sequence parallel。

## 代价与适用边界

TP 的优势是每层都能用多设备并行，但几乎每层都会引入通信。高带宽 NVLink/NVSwitch/HCCS 等互联通常比跨节点低带宽网络更适合高 TP。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 通过 `tensor_parallel_size` 配置 TP，并可和 PP、DP、EP、CP 等组合。

## Sources

- https://docs.vllm.ai/en/latest/serving/parallelism_scaling/
- https://docs.vllm.ai/en/latest/api/vllm/config/parallel/
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
