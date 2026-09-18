---
type: project
name: S-LoRA
companies: []
company_relation: research-community
layer: adapter-serving
open_source: true
repository: https://github.com/S-LoRA/S-LoRA
areas: [llm-serving, lora, adapter-serving, memory-management, batching, cuda-kernels]
people:
  - "company/RadixArk/盛颖 Ying Sheng"
  - "university/UC Berkeley/Shiyi Cao"
  - "university/UC Berkeley/Shuo Yang"
  - "company/RadixArk/朱邦华 Banghua Zhu"
  - "community/sgl-project/SGLang/郑连民 Lianmin Zheng"
  - "company/Inferact/Joseph Gonzalez"
  - "company/Inferact/Ion Stoica"
governance: "LMSYS/Berkeley research project; upstream repository is archived"
last_verified: "2026-09"
---
# S-LoRA

S-LoRA 是面向大量 LoRA adapters 并发服务的 LMSYS / Berkeley research system。它针对 adapter weights 与 KV cache 共同挤压 GPU memory 的问题，提出统一内存管理与异构 batching 路线。

## AI Infra 价值
- Unified Paging 同时管理 adapter weights 与 KV cache，减少高并发多 adapter serving 下的碎片与内存压力。
- 通过定制 CUDA kernels 处理不同 adapter rank / request shape 的 heterogeneous batching。
- 研究把 LoRA 从“单模型微调工件”推进为可大规模多租户服务的 runtime / memory-management 问题。
- 官方文章报告在其评测设置下相对基线可提升吞吐并扩大可并发服务的 adapter 数量；这些数字只作为论文实验结论，不外推到所有部署。

## 图谱关系
S-LoRA 作者网络同时包含 [[company/RadixArk/盛颖 Ying Sheng|Ying Sheng]]、[[university/UC Berkeley/Shiyi Cao|Shiyi Cao]]、[[university/UC Berkeley/Shuo Yang|Shuo Yang]]、[[company/RadixArk/朱邦华 Banghua Zhu|Banghua Zhu]]、[[community/sgl-project/SGLang/郑连民 Lianmin Zheng|Lianmin Zheng]]、[[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] 与 [[company/Inferact/Ion Stoica|Ion Stoica]]。这使其成为 LMSYS 从 Berkeley research 到后续 SGLang / RadixArk 人才网络的一枚很干净的中间节点。

当前 GitHub repository 已 archived，因此把它建模为历史上重要的 research project，而不是仍在高速演进的 production-serving 主干。

## Sources
- https://www.lmsys.org/blog/2023-11-15-slora/
- https://github.com/S-LoRA/S-LoRA
- https://arxiv.org/abs/2311.03285
