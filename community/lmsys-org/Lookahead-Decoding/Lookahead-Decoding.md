---
type: project
name: Lookahead Decoding
companies: []
company_relation: research-community
layer: speculative-decoding
open_source: true
repository: https://github.com/hao-ai-lab/LookaheadDecoding
areas: [speculative-decoding, parallel-decoding, llm-inference, latency-optimization]
people:
  - "company/Inferact/Ion Stoica"
governance: "LMSYS-listed research project; code hosted by Hao AI Lab"
last_verified: "2026-09"
---
# Lookahead Decoding

Lookahead Decoding 是 LMSYS 项目页收录的 exact parallel decoding 研究路线，由 Yichao Fu、Peter Bailis、Ion Stoica、Hao Zhang 等作者提出。它利用 Jacobi iteration 生成并缓存 n-gram，再通过 verification 提前接受多个未来 token，从而减少严格串行的自回归解码步骤。

## AI Infra 价值
- 不要求额外训练 draft model，也不依赖外部 datastore。
- 与典型 speculative decoding 一样优化 decoding latency，但候选生成机制来自 Jacobi iteration / n-gram trajectory。
- 官方文章报告在其测试模型与 workloads 上约 1.5x–2.3x 的 wall-clock latency reduction；这里仅记录论文/项目实验结论。

## 图谱关系
[[company/Inferact/Ion Stoica|Ion Stoica]] 同时是该工作的作者与 LMSYS current advisor，因此构成明确的人物桥。代码托管在 hao-ai-lab/LookaheadDecoding，不能因为被 LMSYS 项目页收录就改写成 lm-sys GitHub org 所有。

## Sources
- https://www.lmsys.org/projects/
- https://www.lmsys.org/blog/2023-11-21-lookahead-decoding/
- https://github.com/hao-ai-lab/LookaheadDecoding
