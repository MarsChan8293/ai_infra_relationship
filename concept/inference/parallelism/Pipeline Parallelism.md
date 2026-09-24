---
type: concept
name: Pipeline Parallelism
aliases:
  - PP
  - Pipeline Model Parallelism
  - 流水线并行
domain: inference
topic: parallelism
parent_concepts:
  - Parallelism
related_concepts:
  - Tensor Parallelism
projects:
  - vLLM
last_verified: 2026-09
---

# Pipeline Parallelism

## 一句话定义

Pipeline Parallelism（PP）沿模型深度把不同 Transformer layers 分给多个 stage / device，activation 在 stage 之间依次传递。

## 解决的问题

当模型整体放不进单卡，而又不希望每一层都做高频 collective 时，PP 可以让每个 rank 只保存一部分层，显著降低单设备权重占用。

## 核心机制

第一个 stage 接收输入并执行自己负责的层，然后把 activation 发送给下一 stage；最后一个 stage 产生输出。训练中通常通过 microbatch 填充 pipeline；推理中则重点关注 stage 负载均衡、请求流水和跨 stage activation transfer。

## 与相邻概念的区别

- [[Tensor Parallelism]] 是层内并行，PP 是层间切分。
- PP 的通信频率通常低于逐层 TP collective，但 stage 不均衡会形成 pipeline bubble。
- TP 与 PP 可以组合，形成跨节点 PP、节点内 TP 等拓扑。

## 代价与适用边界

如果不同 stage 的计算量不均匀，最慢 stage 会限制吞吐。小 batch / 低并发时 pipeline 难以填满，额外 P2P 传输和 bubble 可能抵消收益。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 `pipeline_parallel_size`，并在 distributed inference / parallelism scaling 文档中把 PP 作为跨设备部署选项。

## Sources

- https://docs.vllm.ai/en/latest/serving/parallelism_scaling/
- https://docs.vllm.ai/en/latest/api/vllm/config/parallel/
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
