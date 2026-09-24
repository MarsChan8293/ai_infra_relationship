---
type: concept
name: Chunked Prefill
aliases:
  - Prefill Chunking
  - Chunked Prompt Prefill
  - 分块预填充
domain: inference
topic: serving
related_concepts:
  - Continuous Batching
  - P-D Disaggregation
projects:
  - vLLM
last_verified: 2026-09
---

# Chunked Prefill

## 一句话定义

Chunked Prefill 把一个很长的 prompt prefill 切成多个较小 token chunk，使它不必在一次调度迭代中完整执行。

## 解决的问题

长 prefill 是大块计算工作，若一次性执行，可能长时间占据 GPU 并阻塞正在 decode 的请求，造成较差的 inter-token latency 和调度尾延迟。

## 核心机制

Scheduler 为一次迭代设置 token budget，只处理长 prompt 的一部分 token，并在后续迭代继续。这样 prefill chunk 可以和 decode token 一起进入 [[Continuous Batching]]，在计算密集的 prefill 和内存带宽敏感的 decode 之间形成更细粒度的调度。

## 与相邻概念的区别

- Chunked Prefill 仍可由同一个 engine 完成 Prefill 与 Decode。
- [[P-D Disaggregation]] 则把两阶段放入不同实例/资源池，并需要 KV handoff。
- 两者都能减轻长 prefill 对 decode 的干扰，但控制手段和系统成本不同。

## 代价与适用边界

chunk 太大时仍会明显阻塞 decode；chunk 太小时则会增加调度、kernel launch 和状态管理开销。最优 chunk size 与模型、硬件、并发和输入长度分布有关。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 Chunked Prefill；其文档说明 V1 中该能力默认启用，并用于把大型 prefill 切分后与 decode 请求共同 batching。

## Sources

- https://docs.vllm.ai/en/v0.10.2/configuration/optimization.html
- https://docs.vllm.ai/en/latest/features/disagg_prefill/
