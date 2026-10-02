---
type: project
name: "XGrammar"
linked_people: []
layer: "structured-generation"
status: active
repository: https://github.com/mlc-ai/xgrammar
docs: https://xgrammar.mlc.ai/
areas:
  - "structured-generation"
  - "constrained-decoding"
  - "llm-inference"
  - "speculative-decoding"
last_verified: "2026-10"
linked_companies: []
---
# XGrammar

XGrammar 是 Catalyst 官方研究页面列出的高效、灵活、可移植 LLM structured generation engine。MLSys 2025 论文作者包括 [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇]] 与 [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航]]。

## AI Infra 位置

- 面向 constrained / structured generation，减少 grammar-guided decoding 的运行时开销。
- 通过预处理 context-independent token、persistent stack 与 grammar computation / GPU execution overlap 降低运行时开销。
- MLSys 2025 论文报告 grammar processing 相比既有方案可超过 10× 加速，并在 H100 低延迟 inference 场景实现接近 zero-overhead 的 structured generation。
- 以独立 runtime / library 形式接入 LLM inference stacks，而不是模型服务框架本身。

## Sources

- https://catalyst.cs.cmu.edu/projects/xgrammar.html
- https://github.com/mlc-ai/xgrammar
- https://xgrammar.mlc.ai/
- https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html
