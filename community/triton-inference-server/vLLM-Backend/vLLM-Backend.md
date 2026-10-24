---
type: project
name: vLLM Backend
layer: distributed-serving
status: active
code_availability: public
repository: https://github.com/triton-inference-server/vllm_backend
docs: https://github.com/triton-inference-server/vllm_backend/blob/main/README.md
areas:
  - triton-backend
  - vllm-serving
  - inflight-batching
  - paged-attention
hardware:
  - nvidia
integrations:
  - "vLLM"
  - "Triton Inference Server"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# vLLM Backend

## 项目简介
vLLM Backend 是将 [[vLLM]] 接入 [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] 的 Python Backend。README 描述请求交给 vLLM 的 AsyncEngine，In-flight Batching 和 Paged Attention 由 vLLM 引擎负责。

## 组件职责
- Triton 提供 Server/模型生命周期及 API 接入。
- vLLM 执行大模型调度、KV Cache、Paged Attention 等核心计算工作。
- Backend 负责两者之间的请求/结果集成和容器部署；**不是单独推理 Kernel Runtime**。

## 研究价值
适合评估已有 vLLM 服务接入 Triton 平台的部署复杂度、可观测性和延迟附加开销。与 [[Dynamo]] 的分布式调度和 KV-Aware Routing 不是等价方案。

## 关联
[[vLLM]] · [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] · [[TensorRT-LLM-Backend]]

## Sources
- https://github.com/triton-inference-server/vllm_backend
- https://github.com/triton-inference-server/vllm_backend/blob/main/README.md
