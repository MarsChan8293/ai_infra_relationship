---
type: project
name: GPUStack
layer: distributed-serving
status: active
repository: https://github.com/gpustack/gpustack
docs: https://docs.gpustack.ai/latest/
areas: [gpu-cluster, model-serving, inference-orchestration, heterogeneous-compute, model-gateway, distributed-inference, scheduler, maas, gpuaas, observability]
hardware: [nvidia, amd, ascend, hygon, metax, mthreads, iluvatar, cambricon, t-head]
integrations: [vLLM, SGLang, TensorRT-LLM, LMCache, "GPUStack Runtime", "GPUStack Runner", "GPUStack Operator", "GPUStack Community Inference Backends", "GGUF Parser"]
companies: ["GPUStack"]
last_verified: "2026-09"
---
# GPUStack

GPUStack 是面向生产环境的开源 GPU cluster manager / distributed model-serving control plane。它在底层异构 accelerator 与 [[community/vllm-project/vLLM/vLLM|vLLM]]、[[community/sgl-project/SGLang/SGLang|SGLang]]、[[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] 等推理引擎之间提供资源管理、调度、部署、gateway、可观测性和 API 层。

## 2026 架构定位

当前官方仓库把 GPUStack 定义为同时覆盖 AI model serving 与 GPU instance provisioning 的 GPU cluster manager：

- 单一 control plane 管理 on-prem、Kubernetes 与 cloud 中的多个 GPU cluster。
- 根据资源情况调度 GPU，并配置 / 选择 inference engine。
- vLLM / SGLang / TensorRT-LLM 作为可插拔 inference engine，同时允许 custom backend。
- 支持 [[community/LMCache/LMCache/LMCache|LMCache]] / HiCache 等扩展 KV cache，并提供 speculative decoding。
- 提供高可用、load balancing、Grafana / Prometheus monitoring、authentication 与 access control。
- 对外提供 OpenAI-compatible model API，并支持按需 SSH GPU instance。

## 子项目

### [[community/gpustack/runtime/runtime|GPUStack Runtime]]

异构 accelerator detection 与 workload runtime 层，把九类 GPU / NPU 厂商的设备信息与容器运行环境统一给上层。

### [[community/gpustack/runner/runner|GPUStack Runner]]

推理 backend 镜像供应链，维护不同 CUDA / ROCm / CANN / DTK / MACA / MUSA 等软件栈上的 vLLM、SGLang、MindIE 组合。

### [[community/gpustack/gpustack-operator/gpustack-operator|GPUStack Operator]]

Kubernetes 设备资源控制器，覆盖 Kueue 调度、GPU sharing、software slicing、MIG / vendor partitioning，并继续向 KV cache / distributed serving 资源编排扩展。

### [[community/gpustack/community-inference-backends/community-inference-backends|GPUStack Community Inference Backends]]

让社区 upstream engine 通过标准 spec 接入 GPUStack，而不要求进入 core。当前包含 llama.cpp、TensorRT-LLM、TokenSpeed、TEI、MinerU 等多类 backend。

### [[community/gpustack/gguf-parser-go/gguf-parser-go|GGUF Parser]]

模型部署前的 GGUF resource planning 工具，覆盖 metadata、RAM / VRAM、device placement 与实验性 max-TPS 估算。

## 关键人物

- [[company/GPUStack/秦小康|秦小康]]：GPUStack CEO。
- [[company/GPUStack/Yinlin Li|Yinlin Li / linyinli]]：cloud-native / Ascend / community backend 方向。
- [[community/gpustack/GPUStack/thxCode|thxCode]]：Runtime / Runner / Operator 跨项目工程核心节点。
- [[community/gpustack/GPUStack/gitlawr|gitlawr]]：control-plane / shared KV cache 方向。
- [[community/gpustack/GPUStack/yxf0314|yxf0314]]：vLLM distributed serving / worker / Ascend 方向。

## 人物关系

[[community/gpustack/GPUStack/thxCode|thxCode]] ↔ [[community/gpustack/GPUStack/yxf0314|yxf0314]] 已有可直接核验的 technical collaboration：Ascend A5 多卡 HCCL / ranktable 问题由 yxf0314 参与诊断，后续 Runtime 修复明确引用该诊断，并由 thxCode 收敛实现。对应人物页已写入 reciprocal typed edge。

## 历史边界：llama-box

GPUStack 早期曾以 llama-box 承接 llama.cpp / GGUF 等 backend；从 v2.0.0 起官方 migration 文档明确不再支持 llama-box，转向 containerized custom backend / community backend 模式。因此本轮不把 archived llama-box 当作当前核心子项目扩张，但保留其作为 GPUStack → [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] 历史关系线索。

## Sources

- https://github.com/gpustack/gpustack
- https://docs.gpustack.ai/latest/
- https://github.com/gpustack/runtime
- https://github.com/gpustack/runner
- https://github.com/gpustack/gpustack-operator
- https://github.com/gpustack/community-inference-backends
- https://github.com/gpustack/gguf-parser-go
