---
type: project
name: FlashInfer
linked_concepts:
  - "concept/kernel/attention/Attention Kernel"
  - "concept/kernel/attention/FlashAttention"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/gemm/Grouped GEMM"
  - "concept/kernel/programming/JIT Kernel Compilation"
  - "concept/kernel/optimization/Kernel Fusion"
  - "concept/kernel/attention/PagedAttention"
status: active
linked_people:
  - "community/flashinfer-ai/FlashInfer/aleozlx"
  - "community/flashinfer-ai/FlashInfer/Brian K. Ryu"
  - "community/flashinfer-ai/FlashInfer/Jingfan Sun"
  - "community/flashinfer-ai/FlashInfer/Wuwei Lin"
  - "community/flashinfer-ai/FlashInfer/Yang Xu"
  - "community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye"
  - "community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai"
  - "community/flashinfer-ai/FlashInfer/陈乐群 Lequn Chen"
  - "community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen"
  - "community/NVIDIA/TensorRT-LLM/Brian Nguyen"
  - "community/sgl-project/SGLang/Yineng Zhang"
repository: https://github.com/flashinfer-ai/flashinfer
docs: https://docs.flashinfer.ai/
last_verified: "2026-09"
companies: []
company_relation: community-led-with-industry-contributors
layer: runtime
linked_companies: []
areas:
  - "attention-kernels"
  - "paged-attention"
  - "lora-kernels"
  - "kernel-generation"
hardware:
  - "nvidia"
integrations:
  - "vLLM"
  - "SGLang"
---
# FlashInfer

## 项目简介
FlashInfer 是面向 LLM serving 的高性能 GPU kernel 库，覆盖 attention、GEMM、MoE、sampling、通信与 JIT 等路径。它位于 inference engine 与 CUDA/GPU 执行层之间，价值在于把常见推理算子做成可复用、高性能的 kernel 组件。

## GitHub
https://github.com/flashinfer-ai/flashinfer

## 主要贡献公司
FlashInfer 起源于学术/开源社区并采用社区治理。NVIDIA、Together AI 等产业节点与作者/维护者网络存在直接连接，但当前不把任何单一公司写成项目主要归属；公司边继续按具体 maintainer 任职与持续代码贡献逐条建立。

## 主要维护者 / 组织
由 flashinfer-ai 社区维护。已记录的 full-codebase approvers 包括 [[叶子豪 Zihao Ye]]、[[aleozlx]]、[[Jingfan Sun]]、[[Yang Xu]]、[[Brian K. Ryu]]；这些关系表示同一代码库维护权限，不自动推断公司同事。

## 生态关系
[[vLLM]] · [[SGLang]] · [[TensorRT-LLM]] · [[Together AI]] · [[NVIDIA]] · [[DeepGEMM]] · [[FlashMLA]]

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]]：[[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 两人共同拥有全代码库审批权限并覆盖多个 kernel 模块。
- [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]]：[[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 两人共同承担全代码库审批与核心 kernel review。
- [[community/flashinfer-ai/FlashInfer/Jingfan Sun|Jingfan Sun]]：[[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：**NVIDIA 同事 + FlashInfer Full Codebase Approver 同僚**。截至 2026-09 两人均在 NVIDIA 并承担 FlashInfer 全代码库审批；叶子豪偏 creator/compiler/kernel 架构，Jingfan Sun 偏 GPU kernel、MoE/EP 和性能工程。首次在...
- [[community/flashinfer-ai/FlashInfer/Wuwei Lin|Wuwei Lin]]：Project source / contributor context: https://github.com/flashinfer-ai/flashinfer
- [[community/flashinfer-ai/FlashInfer/Yang Xu|Yang Xu]]：[[FlashInfer]]：Full Codebase Approver
- [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：[[FlashInfer]]：创建者、核心维护者
- [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航（Ruihang Lai）]]：Carnegie Mellon University：计算机博士生，导师 [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇（Tianqi Chen）]]、Todd Mowry
- [[community/flashinfer-ai/FlashInfer/陈乐群 Lequn Chen|陈乐群（Lequn Chen）]]：Project source / contributor context: https://github.com/flashinfer-ai/flashinfer
- [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇（Tianqi Chen）]]：Project source / contributor context: https://github.com/flashinfer-ai/flashinfer
- [[community/NVIDIA/TensorRT-LLM/Brian Nguyen|Brian Nguyen]]：[[TensorRT-LLM]]：FlashInfer decode / CUDA Graph 集成活跃贡献者
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：[[FlashInfer]]：MLSys 2025 论文作者；论文获 MLSys 2025 Best Paper Award。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/attention/Attention Kernel|Attention Kernel]]
- [[concept/kernel/attention/FlashAttention|FlashAttention]]
- [[concept/kernel/gemm/GEMM|GEMM]]
- [[concept/kernel/gemm/Grouped GEMM|Grouped GEMM]]
- [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]]
- [[concept/kernel/optimization/Kernel Fusion|Kernel Fusion]]
- [[concept/kernel/attention/PagedAttention|PagedAttention]]

<!-- END AUTO PROJECT CONCEPTS -->
