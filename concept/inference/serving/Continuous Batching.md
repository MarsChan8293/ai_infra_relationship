---
type: concept
name: Continuous Batching
aliases:
  - In-flight Batching
  - Iteration-level Batching
  - 连续批处理
domain: inference
topic: serving
related_concepts:
  - Chunked Prefill
  - Prefix Caching
projects:
  - vLLM
last_verified: 2026-09
---

# Continuous Batching

## 一句话定义

Continuous Batching 是在每个调度迭代中动态把新请求加入 batch、把已完成请求移出 batch，而不是等待一整个静态 batch 全部结束后再接收下一批请求。

## 解决的问题

LLM 请求的输入长度和输出长度差异很大。静态 batching 会被最慢请求拖住，已完成请求留下的 GPU 槽位无法及时被新请求利用。Continuous Batching 通过迭代级 admission/removal 提高设备利用率。

## 核心机制

Scheduler 持续维护 waiting、running 和 finished request 集合，在每次 forward 前依据 token budget、KV capacity 和优先级重新形成执行 batch。不同请求可以在不同时间进入和退出，因此 batch membership 会不断变化。

## 与相邻概念的区别

- [[Chunked Prefill]] 决定一个长 prefill 是否被拆成多个 token chunk，它可以作为 continuous scheduler 的一种工作单元。
- [[Prefix Caching]] 影响一个请求真正需要计算多少 prefill token，但不是 batching 策略。
- Continuous Batching 解决的是动态请求编排，不等于 kernel-level tensor batching。

## 代价与适用边界

更动态的调度提高吞吐和利用率，但 scheduler 需要同时考虑 KV 容量、token budget、prefill/decode 干扰和公平性。过大的 batch 也可能牺牲单请求 latency。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 将 continuous batching of incoming requests 列为核心 serving 能力，并由 scheduler 持续组织可执行请求。

## Sources

- https://docs.vllm.ai/en/stable/
