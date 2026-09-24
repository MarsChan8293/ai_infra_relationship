---
type: concept
name: Speculative Decoding
aliases:
  - Speculative Sampling
  - Spec Decode
  - 投机解码
  - 投机推理
domain: inference
topic: decoding
related_concepts:
  - Draft-Target Decoding
  - N-gram Speculation
  - Self-Speculative Decoding
  - Multi-token Prediction
projects:
  - vLLM
  - SGLang
last_verified: 2026-09
---

# Speculative Decoding

## 一句话定义

Speculative Decoding 先用更便宜的方法一次提出多个候选 token，再由目标模型并行验证，从而减少“每个输出 token 都必须单独跑一次昂贵 target forward”的串行瓶颈。

## 解决的问题

普通 autoregressive decode 每轮只确认一个 token，GPU 在低到中等 QPS、memory-bound 场景下常无法充分利用算力。投机解码把多步串行 decode 变成“快速 proposal + 一次批量 verification”。

## 核心机制

一个迭代通常包含：

1. proposer 生成若干 draft token。
2. target model 一次计算这些候选位置的 logits。
3. 按验证规则接受连续正确候选，并在第一个不接受的位置恢复到 target 分布。
4. 从新的已确认前缀继续下一轮。

关键性能变量是 proposer 成本、一次提出多少 token、acceptance rate 和 verification 开销。

## 主要细分

- [[Draft-Target Decoding]]：独立小 draft model + 大 target model。
- [[N-gram Speculation]]：从 prompt / 已有 token 模式中直接提出候选，无需额外神经网络。
- [[Self-Speculative Decoding]]：使用 target 模型自身的较便宜路径产生 draft。
- [[Multi-token Prediction]]：模型原生预测多个未来 token，可被用作 speculative proposer。
- EAGLE / DFlash / DSpark 等属于训练专用 proposer 的现代路线，后续可继续细分节点。

## 代价与适用边界

投机解码不是“候选越多越快”。当 proposer 太慢、acceptance rate 太低、batch/QPS 很高或 target verification 本身成为瓶颈时，收益会下降甚至为负。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 当前支持 EAGLE、MTP、Draft Model、N-Gram、Suffix、DFlash/DSpark 等多类 speculation method。[[community/sgl-project/SGLang/SGLang|SGLang]] 生态通过 SpecForge 训练并服务 EAGLE3、DFlash、DSpark 等 draft model。

## Sources

- https://docs.vllm.ai/en/latest/features/spec_decode/
- https://docs.vllm.ai/projects/speculators/en/stable/user_guide/getting_started/
- https://docs.sglang.ai/SpecForge/
