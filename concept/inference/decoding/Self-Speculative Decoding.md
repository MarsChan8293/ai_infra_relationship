---
type: concept
name: Self-Speculative Decoding
aliases:
  - Self Speculative Decoding
  - Self-Drafting
  - 自投机解码
domain: inference
topic: decoding
parent_concepts:
  - Speculative Decoding
related_concepts:
  - Draft-Target Decoding
projects:
  - Transformers
last_verified: 2026-09
---

# Self-Speculative Decoding

## 一句话定义

Self-Speculative Decoding 让 target LLM 自己提供一个更便宜的 drafting 路径，再由完整 target 路径验证，而不是额外部署一个独立 draft model。

## 解决的问题

传统 [[Draft-Target Decoding]] 需要寻找、训练并部署一个与 target 足够匹配的辅助模型，还会占用额外权重和运行时内存。Self-speculation 尝试直接复用 target 自身结构。

## 核心机制

经典 Draft & Verify 做法是在 drafting 阶段跳过部分中间层，以较低成本连续提出候选；verification 阶段再由完整模型对 draft token 并行验证。其他 self-drafting 方案也可能使用 early-exit 或 target 内部轻量路径。

## 与相邻概念的区别

“Self” 的关键不是 proposer 和 target 名字相同，而是 draft 能力直接来自 target 模型自身或其子网络，不需要独立 auxiliary LLM。EAGLE/MTP 等若存在独立训练的 draft module，应按其实际结构区分，不能全部泛称 self-speculative。

## 代价与适用边界

省掉独立 draft model 并不等于 draft 免费。若浅层输出质量不足，acceptance rate 会下降；不同模型也未必天然适合 early exit，需要训练策略或层选择。

## 项目实现

[[community/huggingface/Transformers/Transformers|Transformers]] 官方 assisted decoding 文档直接提供 Self-speculative decoding：同一个 target 模型的中间层通过 `assistant_early_exit` 产生候选，随后由剩余层验证或修正；源码使用 `EarlyExitCandidateGenerator` 实现该路径。

## Sources

- https://aclanthology.org/2024.acl-long.607/
- https://aclanthology.org/2024.acl-long.681/
- https://github.com/huggingface/transformers/blob/main/docs/source/en/assisted_decoding.md
- https://github.com/huggingface/transformers/blob/main/src/transformers/generation/candidate_generator.py
