---
type: project
name: FlashInfer
layer: gpu-kernels
open_source: true
---
# FlashInfer

## 项目简介
FlashInfer 是面向 LLM serving 的高性能 GPU kernel 库，覆盖 attention、GEMM、MoE、sampling、通信与 JIT 等路径。它位于 inference engine 与 CUDA/GPU 执行层之间，价值在于把常见推理算子做成可复用、高性能的 kernel 组件。

## GitHub
https://github.com/flashinfer-ai/flashinfer

## 主要维护者 / 组织
由 flashinfer-ai 社区维护。已记录的 full-codebase approvers 包括 [[叶子豪 Zihao Ye]]、[[aleozlx]]、[[Jingfan Sun]]、[[Yang Xu]]、[[Brian K. Ryu]]；这些关系表示同一代码库维护权限，不自动推断公司同事。

## 生态关系
[[vLLM]] · [[SGLang]] · [[TensorRT-LLM]] · [[Together AI]] · [[NVIDIA]] · [[DeepGEMM]] · [[FlashMLA]]
