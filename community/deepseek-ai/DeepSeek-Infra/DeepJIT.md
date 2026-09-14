---
type: project
name: DeepJIT
parent: DeepSeek-Infra
companies: ["深度求索"]
company_relation: company-led
layer: kernel-jit
open_source: true
---
# DeepJIT

## 项目简介
DeepJIT 是 DeepSeek 在 2026 年开源的轻量 xPU kernel JIT compilation/runtime library，使用 C++20，目标是为 NVIDIA CUDA GPU 与 Huawei Ascend NPU 等平台提供更统一的 kernel 动态编译与加载能力。

## GitHub
https://github.com/deepseek-ai/DeepJIT

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。当前公开主要作者节点包括 [[guyan364]]、[[kurisu6912]]、[[LyricZhao]]。

## 生态关系
[[vLLM-Ascend]] · [[DeepGEMM]] · CUDA · Ascend/CANN。它补的是 kernel toolchain/JIT 层，而不是完整 serving runtime。
