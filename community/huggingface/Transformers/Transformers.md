---
type: project
name: Transformers
linked_people: []
linked_concepts:
  - "concept/inference/decoding/Self-Speculative Decoding"
layer: runtime
status: active
repository: https://github.com/huggingface/transformers
docs: https://huggingface.co/docs/transformers/
areas:
  - model-runtime
  - text-generation
  - assisted-generation
  - speculative-decoding
companies: ["Hugging Face"]
last_verified: "2026-09"
linked_companies:
  - "company/Hugging Face/Hugging Face"
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

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/decoding/Self-Speculative Decoding|Self-Speculative Decoding]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Hugging Face/Hugging Face|Hugging Face]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
