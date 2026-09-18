---
type: research-institution
name: "MAST Lab"
aliases: ["Stanford Multi-scale Architectures & Systems Team", "Stanford MAST"]
organization: "Stanford University"
areas: [computer-systems, ai-infrastructure, llm-serving, kv-cache, cloud-systems, resilient-serving]
people:
  - "community/sgl-project/SGLang/谢志强 Zhiqiang Xie"
projects:
  - SGLang
website: https://mast.stanford.edu/
country: "USA"
city: "Stanford, CA"
last_verified: "2026-09"
---
# MAST Lab

Stanford MAST（Multi-scale Architectures & Systems Team）由 Christos Kozyrakis 领导，长期研究 computer architecture 与 computer systems。当前 active research themes 已明确包含 **AI Efficiency** 与 **Scale-out AI systems**。

## AI Infra 主线

- **Contextra**（OSDI 2026）：hierarchical context caching for long-context LLM serving；系统构建在 [[SGLang]] 上，针对 KV cache loading、GPU/CPU memory layout 与 cache-aware scheduling。
- **RaidServe**（MLSys 2026）：面向 GPU failure / irregular availability 的高性能 resilient tensor-parallel serving。
- **Regulating Branch Parallelism in LLM Serving**：面向 LLM serving branch parallelism。
- **AI Metropolis**（MLSys 2025）：使用 out-of-order execution 提升 LLM multi-agent simulation 的系统效率。

## 人才桥梁

[[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强（Zhiqiang Xie）]] 是当前 MAST PhD student，并直接连接 SGLang 社区，因此 MAST 是 Stanford systems research 与仓库现有 SGLang / RadixArk 网络之间的高价值桥梁。

Contextra “built on SGLang”表示工程依赖与共同技术生态，不等价于 MAST 对 SGLang 的治理或所有权。

## Sources
- https://mast.stanford.edu/
- https://mast.stanford.edu/pubs/strata/
- https://mast.stanford.edu/pubs/raidserve/
