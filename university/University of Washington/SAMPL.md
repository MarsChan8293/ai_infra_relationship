---
type: research-institution
name: "SAMPL"
aliases: ["SAMPL Research Group"]
organization: "University of Washington"
areas: [machine-learning-systems, ai-infrastructure, llm-serving, gpu-kernels, compilers, quantization]
people:
  - "community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye"
  - "community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai"
  - "community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen"
  - "community/sgl-project/SGLang/郑连民 Lianmin Zheng"
projects:
  - FlashInfer
website: https://sampl.cs.washington.edu/
country: "USA"
city: "Seattle, WA"
last_verified: "2026-09"
---
# SAMPL

SAMPL 是 University of Washington Paul G. Allen School 的跨学科 machine learning systems research group，研究跨越 framework、compiler、specialized hardware、training / inference 与 programming abstractions。官方页面说明该组由 Sampa、Syslab、PLSE、EFESLab 与 CMU Catalyst 等研究网络协作组成。

## 与 AI Infra 图谱最相关的项目

- [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]]：面向 LLM serving 的高性能 GPU operator / attention engine。
- **Punica**：multi-tenant LoRA serving。
- **Atom**：面向高吞吐 LLM serving 的 low-bit quantization。
- **Fiddler**：MoE inference 的 CPU-GPU orchestration。
- **SparseTIR / TVM**：把 compiler / IR 路线与 inference kernels、deployment 连接起来。

## 已有图谱桥梁

- [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：FlashInfer、SparseTIR 等 SAMPL 项目公开参与者。
- [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航（Ruihang Lai）]]：FlashInfer / SparseTIR 研究网络。
- [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇（Tianqi Chen）]]：SAMPL 官方 faculty 列表中的 CMU faculty，也是 TVM / FlashInfer 等项目桥梁。
- [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：SAMPL TVM Stack 页面列出的项目参与者，进一步连接 SGLang / LMSYS。

这里的 `people` 只表示官方 SAMPL 页面或其项目页能够直接验证的研究参与，不把跨校 faculty collaboration 推断为 UW 雇佣关系。

## Sources
- https://sampl.cs.washington.edu/
- https://sampl.cs.washington.edu/research.html
- https://sampl.cs.washington.edu/projects/flashinfer.html
- https://sampl.cs.washington.edu/projects/punica.html
- https://sampl.cs.washington.edu/projects/tvm.html
