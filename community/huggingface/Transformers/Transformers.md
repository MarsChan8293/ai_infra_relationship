---
type: project
name: Transformers
layer: runtime
status: active
repository: https://github.com/huggingface/transformers
docs: https://huggingface.co/docs/transformers/
areas:
  - model-runtime
  - text-generation
  - assisted-generation
  - speculative-decoding
companies:
  - Hugging Face
last_verified: "2026-09"
---

# Transformers

## 项目简介

Transformers 是 Hugging Face 维护的开源模型与推理/训练库。除模型实现外，其 generation runtime 提供 assisted generation / speculative decoding，包括使用 target 模型中间层作为 proposer 的 self-speculative decoding。

## 与 Self-Speculative Decoding 的关系

官方 assisted decoding 文档单独定义 **Self-speculative decoding**：使用同一个模型的中间层提出候选 token，命中时提前退出，随后由剩余层验证或修正。API 通过 `assistant_early_exit` 暴露这一能力，源码中的 `EarlyExitCandidateGenerator` 也明确说明候选由 “the model itself” 通过 early exit 产生。

这属于 target 模型自身的廉价 drafting 路径，不是额外部署独立 draft LLM。

## Sources

- https://github.com/huggingface/transformers
- https://github.com/huggingface/transformers/blob/main/docs/source/en/assisted_decoding.md
- https://github.com/huggingface/transformers/blob/main/src/transformers/generation/candidate_generator.py
- https://github.com/huggingface/transformers/blob/main/src/transformers/generation/configuration_utils.py
