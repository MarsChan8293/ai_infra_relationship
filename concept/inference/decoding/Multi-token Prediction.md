---
type: concept
name: Multi-token Prediction
aliases:
  - Multi-Token Prediction
  - MTP
  - Multi Token Prediction
  - 多Token预测
  - 多词元预测
domain: inference
topic: decoding
related_concepts:
  - Speculative Decoding
  - Draft-Target Decoding
projects:
  - vLLM
last_verified: 2026-09
---

# Multi-token Prediction

## 一句话定义

Multi-token Prediction（MTP）让模型或附加预测模块一次预测多个未来 token / 未来位置，而不是只训练或执行单一步 next-token prediction。

## 解决的问题

标准 autoregressive decode 具有强串行依赖。若模型能低成本给出多个未来 token 的高质量候选，就可以把这些候选送入 [[Speculative Decoding]] verification，一次确认多个 token。

## 核心机制

不同模型的 MTP 结构并不相同。常见做法是在 backbone hidden state 之上增加一个或多个 next-n predictor/head，产生多个未来位置候选。Serving runtime 再把这些预测作为 proposer 输出，由 target/backbone 验证并决定接受长度。

## 与相邻概念的区别

MTP 是“模型如何产生多个未来预测”的能力；Speculative Decoding 是“如何提出并验证多个候选”的推理协议。MTP 常作为后者的 proposer，但也可能被用于训练目标或其他推理优化，因此不把它建模为严格子概念。

## 代价与适用边界

MTP 的收益取决于 predictor 额外算力、候选准确率、可接受 token 数以及 runtime 是否能高效做 verification。不同模型的 MTP 权重结构不能假设通用。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 当前把 MTP 作为 speculative method，并包含多种模型专用 MTP draft implementation。

## Sources

- https://docs.vllm.ai/en/latest/features/spec_decode/
- https://docs.vllm.ai/en/latest/api/vllm/config/speculative/
- https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_v2_mtp/
