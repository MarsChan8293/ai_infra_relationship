---
type: concept
name: Draft-Target Decoding
aliases:
  - Draft Model Speculative Decoding
  - Draft-and-Verify
  - Draft Target
  - 草稿模型投机解码
domain: inference
topic: decoding
parent_concepts:
  - Speculative Decoding
related_concepts:
  - Multi-token Prediction
  - Self-Speculative Decoding
projects:
  - vLLM
  - SGLang
last_verified: 2026-09
---

# Draft-Target Decoding

## 一句话定义

Draft-Target Decoding 使用一个比目标模型更便宜的 proposer / draft model 先生成候选 token，再由 target model 批量验证这些候选。

## 解决的问题

它试图用“小模型多走几步 + 大模型一次验证”替代“大模型一步一步串行 decode”，降低 target model forward 的次数。

## 核心机制

Draft 必须足够快，同时生成的 token 又要与 target 高度一致。Target 对整段候选做 verification，连续接受的 token 可以一次提交；出现不匹配后按正确采样规则回退并继续。

传统路线可直接使用一个较小的独立语言模型；现代 EAGLE、DFlash、DSpark 等会训练专门的 proposer，以更高 acceptance rate 和更低 proposer cost 替代普通小模型。

## 与相邻概念的区别

- [[Speculative Decoding]] 是总类。
- [[Self-Speculative Decoding]] 不需要独立 auxiliary draft model。
- [[N-gram Speculation]] 不运行额外神经网络 proposer。
- [[Multi-token Prediction]] 可以承担 draft/proposal 角色，但其“预测多个未来 token”的模型结构本身并不等同于完整 draft-target verification 协议。

## 代价与适用边界

Draft 太大时自身成本吃掉收益；太小时候选质量低、acceptance rate 下降。部署还会增加 draft 权重显存、KV 状态和调度复杂度。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 的 speculative config 支持 `draft_model`、EAGLE、DFlash、DSpark 等 model-based proposer。[[community/sgl-project/SGLang/SGLang|SGLang]] 的 SpecForge 面向 EAGLE3、DFlash、DSpark 等 draft model 的训练与导出。

## Sources

- https://docs.vllm.ai/en/latest/features/spec_decode/
- https://docs.vllm.ai/en/latest/features/speculative_decoding/eagle/
- https://docs.sglang.ai/SpecForge/
