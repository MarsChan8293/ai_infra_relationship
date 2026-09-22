---
type: research-institution
name: "Catalyst Group"
aliases: ["CMU Catalyst", "CMU Automated Learning Systems Group"]
organization: "Carnegie Mellon University"
linked_people: []
areas: [machine-learning-systems, ai-infrastructure, llm-serving, compilers, gpu-systems, speculative-decoding, structured-generation]
projects:
  - "FlexFlow Serve"
  - "XGrammar"
  - "Mirage Persistent Kernel"
projects: [XGrammar, FlexFlow Serve, Mirage Persistent Kernel]
people:
  - "community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen"
  - "community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai"
  - "community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye"
website: https://catalyst.cs.cmu.edu/
country: "USA"
city: "Pittsburgh, PA"
last_verified: "2026-09"
---
# Catalyst Group

Catalyst 是 Carnegie Mellon University 的跨学科 machine learning + systems research group，官方定位是通过跨 stack optimization 自动化高效 learning systems。其成员跨 Machine Learning Department、Computer Science Department 与 Electrical & Computer Engineering Department。

## AI Infra 主线

- [[university/Carnegie Mellon University/FlexFlow Serve|FlexFlow Serve]] / SpecInfer：低延迟、高性能 generative LLM serving，包含 tree-based speculative inference、CPU offloading 与 quantization。
- [[university/Carnegie Mellon University/XGrammar|XGrammar]]：高效 structured generation engine。
- **TidalDecode**：面向 LLM decoding 的 sparse attention。
- **MLC LLM**：compiler-accelerated cross-hardware LLM deployment。
- [[university/Carnegie Mellon University/Mirage Persistent Kernel|Mirage Persistent Kernel]]：把 LLM inference mega-kernelization 与 compiler/runtime 结合。
- **Helix**：Catalyst publication network 中的 heterogeneous GPU/network LLM serving system。

## 与现有图谱的桥梁

- [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇（Tianqi Chen）]]：Catalyst faculty。
- [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航（Ruihang Lai）]]：Catalyst PhD student。
- [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：Catalyst 官方 people 页面列为 visiting student。
- UW [[university/University of Washington/SAMPL|SAMPL]] 官方页面明确将 CMU Catalyst 列为协作来源之一，因此两组之间存在公开的组织级研究协作线索。

上述成员身份按 Catalyst 当前公开页面记录；不会据此推断任意两名成员必然存在直接共同项目。

## Canonical project nodes

- [[university/Carnegie Mellon University/Catalyst Group/XGrammar|XGrammar]]：structured generation / constrained decoding engine。
- [[university/Carnegie Mellon University/Catalyst Group/FlexFlow Serve|FlexFlow Serve]]：低延迟、高性能 LLM serving，包含 speculative inference、CPU offload 与 quantization。
- [[university/Carnegie Mellon University/Catalyst Group/Mirage Persistent Kernel|Mirage Persistent Kernel]]：把 LLM inference tensor programs mega-kernelize 的 compiler + runtime 路线。

这些项目由 Catalyst 官方 research 页面直接列出；项目节点只编码明确研究归属，不因页面归属推断所有作者的雇佣或治理关系。

## Sources
- https://catalyst.cs.cmu.edu/
- https://catalyst.cs.cmu.edu/research.html
- https://catalyst.cs.cmu.edu/projects/flexflow%20serve.html
- https://catalyst.cs.cmu.edu/projects/xgrammar.html
