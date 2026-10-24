---
type: project
name: TensorRT-LLM Backend
layer: distributed-serving
status: maintenance
code_availability: public
repository: https://github.com/triton-inference-server/tensorrtllm_backend
docs: https://github.com/triton-inference-server/tensorrtllm_backend/blob/main/README.md
areas:
  - triton-backend
  - model-serving
  - inflight-batching
  - tensorrt-llm
hardware:
  - nvidia
integrations:
  - "TensorRT-LLM"
  - "Triton Inference Server"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# TensorRT-LLM Backend

## 项目简介
TensorRT-LLM Backend 是 [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] 对 [[TensorRT-LLM]] 的 Serving 接入层，提供模型配置、部署样例与 Runtime 集成，不是另一个独立的 Tensor/GEMM 推理引擎。

## 维护与代码迁移
当前 README **明确说明 Backend 的源代码和测试已经转移至 [[TensorRT-LLM]] 仓库中的 `triton_backend/` 目录**。本仓库仍保留公开说明与入口；`status: maintenance` 仅表达本文档对它作为独立主开发路径的保守判断，并非直接依据 GitHub Archived 状态。
- 实际代码： https://github.com/NVIDIA/TensorRT-LLM/tree/main/triton_backend
- 文档入口： https://github.com/triton-inference-server/tensorrtllm_backend

## 价值与边界
Triton 负责服务/部署和 Backend 容器接入；Paged Attention、In-flight Batching、TP/PP/EP 等实际推理能力需要以 TensorRT-LLM 版本为准。不要把 Backend 当作与 TensorRT-LLM 平行的第三套引擎。

## 关联
[[TensorRT-LLM]] · [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]]

## Sources
- https://github.com/triton-inference-server/tensorrtllm_backend
- https://github.com/NVIDIA/TensorRT-LLM/tree/main/triton_backend
