---
type: project
name: TensorRT-LLM
governance: company-led
companies: ["NVIDIA"]
company_relation: company-led
layer: inference-runtime
open_source: true
---
# TensorRT-LLM

## 项目简介
TensorRT-LLM 是 NVIDIA 面向 LLM inference 的 runtime、kernel 与模型执行栈，深度结合 CUDA/TensorRT，对 NVIDIA GPU 上的 attention、GEMM、MoE、量化、speculative decoding、KV cache 与多 GPU 执行做系统级优化。

## GitHub
https://github.com/NVIDIA/TensorRT-LLM

## 主要贡献公司
- [[company/NVIDIA/NVIDIA|NVIDIA]]：项目主导维护公司。

## 主要维护者 / 组织
由 [[NVIDIA]] 主导维护。仓库人物页按公开长期贡献/维护证据建模，不把所有 NVIDIA 员工自动纳入核心项目组。

## 生态关系
[[Dynamo]] · [[FlashInfer]] · [[NIXL]] · [[vLLM]] · [[SGLang]] · [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]]。TensorRT-LLM 是 NVIDIA-specialized engine/runtime，而 Dynamo 更偏跨 engine 的集群级 serving 编排。
