---
type: concept
name: Parallelism
aliases:
  - Model Parallelism
  - 分布式并行
  - 并行切分
domain: inference
topic: parallelism
related_concepts:
  - Tensor Parallelism
  - Pipeline Parallelism
  - Data Parallelism
  - Expert Parallelism
  - Sequence Parallelism
  - Context Parallelism
projects:
  - vLLM
last_verified: 2026-09
---

# Parallelism

## 一句话定义

Parallelism 是把模型、请求、token、专家或计算阶段拆到多个设备 / worker 上协同执行，用更多硬件换取容量、吞吐或单请求性能。

## 解决的问题

单卡可能放不下模型，也可能无法满足目标吞吐和延迟。不同并行维度分别切模型权重、层、请求副本、MoE expert 或 sequence/context，因此解决的是不同瓶颈。

## 主要细分

- [[Tensor Parallelism]]：在单层内部切 tensor / weight / matmul。
- [[Pipeline Parallelism]]：沿模型深度把不同层切成多个 stage。
- [[Data Parallelism]]：复制模型，把不同请求 / 数据分给不同 replica。
- [[Expert Parallelism]]：把 MoE experts 分布到不同 rank。
- [[Sequence Parallelism]]：经典做法只对部分 activation 沿 sequence 维切分。
- [[Context Parallelism]]：面向长上下文，把更完整的 sequence/context 计算与状态跨 rank 分片。

这些维度可以组合，例如 TP × PP、DP × EP、TP × CP。真正的代价通常落在 collective communication、P2P activation transfer、负载均衡和同步上。

## 代价与适用边界

并行度不是越大越好。增加 rank 会降低每个设备的本地工作量，但同时提高通信、同步和调度成本。最佳切分取决于模型结构、互联带宽、batch/QPS、上下文长度和显存。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 当前支持 tensor、pipeline、data、expert 与 context parallelism，并允许按模型与硬件拓扑组合配置。

## Sources

- https://docs.vllm.ai/en/stable/
- https://docs.vllm.ai/en/latest/serving/parallelism_scaling/
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
