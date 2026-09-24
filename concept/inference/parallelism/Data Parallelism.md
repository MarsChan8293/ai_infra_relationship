---
type: concept
name: Data Parallelism
aliases:
  - DP
  - Replica Parallelism
  - 数据并行
domain: inference
topic: parallelism
parent_concepts:
  - Parallelism
related_concepts:
  - Expert Parallelism
projects:
  - vLLM
last_verified: 2026-09
---

# Data Parallelism

## 一句话定义

Inference Data Parallelism（DP）复制完整或逻辑完整的模型执行单元，把不同请求 / batch 分发给不同 replica 并行处理。

## 解决的问题

TP/PP 主要解决单个模型实例的容量或单请求并行，而 DP 主要横向扩展吞吐。当一组 GPU 已能承载一个 serving replica 时，可以再复制多份，把更多独立请求并行处理。

## 核心机制

Router / load balancer 把请求分配到不同 DP rank / replica。每个 replica 通常拥有独立 KV 状态和本地调度器；若叠加 EP/TP，则一个 DP replica 内部还可以由多个 rank 共同组成。

## 与训练 Data Parallel 的区别

训练 DP 通常需要同步 gradient；推理 DP 没有反向梯度同步，核心问题转为请求路由、负载均衡、KV locality、弹性扩缩和 replica 间资源利用率。

## 代价与适用边界

DP 会复制权重或逻辑模型实例，因此显存开销高于把同一份权重做纯模型并行。对高吞吐在线 serving 很自然，但单请求 latency 通常不会仅靠增加 DP 数而降低。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 data parallel deployment 与 internal/external load balancing 模式，并允许 DP 与 TP/EP 等组合。

## Sources

- https://docs.vllm.ai/en/latest/serving/data_parallel_deployment/
- https://docs.vllm.ai/en/latest/api/vllm/config/parallel/
