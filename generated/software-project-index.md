# Software Project Index

Generated from research/software-project-migration.json and canonical Project v3 frontmatter.

- Projects: 59
- Concepts: not included; they remain in ai_infra_docs/software/concepts.

## inference-engine

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] | active | heterogeneous-inference, cpu-gpu-offload, moe-inference | 0 | 18 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KTransformers) |
| [[community/ModelTC/LightLLM/LightLLM|LightLLM]] | active | llm-serving, distributed-inference, token-generation | 0 | 9 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LightLLM) |
| [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] | active | llm-inference, vlm-inference, local-inference, edge-inference, quantization | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=llama.cpp) |
| [[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]] | active | llm-inference, ascend-inference | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MindIE-LLM) |
| [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | active | diffusion-inference, ascend-inference | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MindIE-SD) |
| [[community/sgl-project/SGLang/SGLang|SGLang]] | active | continuous-batching, radix-attention, prefix-caching, tensor-parallel, expert-parallel | 5 | 31 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=SGLang) |
| [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] | active | tensorrt-engine, quantization, speculative-decoding, tensor-parallel, expert-parallel | 1 | 10 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TensorRT-LLM) |
| [[community/vllm-project/vLLM/vLLM|vLLM]] | active | continuous-batching, paged-kv-cache, prefix-caching, speculative-decoding, tensor-parallel | 8 | 29 | 6 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM) |
| [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] | active | ascend-inference, vllm-backend | 1 | 17 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM-Ascend) |

## distributed-serving

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/vllm-project/AIBrix/AIBrix|AIBrix]] | active | llm-infrastructure, model-serving, autoscaling, request-routing, kubernetes | 1 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=AIBrix) |
| [[community/bentoml/BentoML/BentoML|BentoML]] | active | model-serving, api-service, autoscaling, packaging | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=BentoML) |
| [[community/kubernetes-sigs/Gateway-API-Inference-Extension/Gateway-API-Inference-Extension|Gateway API Inference Extension]] | active | inference-pool, inference-aware-routing, gateway-api, multi-cluster-routing, kubernetes | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Gateway%20API%20Inference%20Extension) |
| [[community/kserve/KServe/KServe|KServe]] | active | kubernetes-model-serving, llm-inference-service, autoscaling, inference-routing, kubernetes | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KServe) |
| [[community/BerriAI/LiteLLM/LiteLLM|LiteLLM]] | active | llm-gateway, provider-routing, rate-limiting, cost-tracking, openai-compatible-proxy | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LiteLLM) |
| [[community/llm-d/llm-d/llm-d|llm-d]] | active | request-routing, kv-aware-routing, pd-disaggregation, worker-pool-orchestration, kubernetes | 4 | 15 | 5 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=llm-d) |
| [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] | active | distributed-inference, disaggregated-serving, kv-aware-routing, cache-management, autoscaling | 4 | 11 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVIDIA%20Dynamo) |
| [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]] | active | distributed-serving, autoscaling, multi-model, pd-disaggregation, prefix-aware-routing | 2 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Ray%20Serve) |
| [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] | active | model-serving, dynamic-batching, multi-framework-serving | 1 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Triton%20Inference%20Server) |

## kv-cache

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/LMCache/LMCache/LMCache|LMCache]] | active | kv-cache, distributed-kv-cache, offloading, storage-backend, p2p | 3 | 19 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LMCache) |
| [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] | active | kv-cache, disaggregated-serving, rdma, data-movement, distributed-storage | 2 | 21 | 2 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Mooncake) |

## storage

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | active | distributed-file-system, high-throughput-storage, linux | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=3FS) |

## communication

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] | active | expert-parallel, all-to-all, moe-dispatch, moe-combine, low-latency | 1 | 9 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepEP) |
| [[community/flagos-ai/FlagCX/FlagCX|FlagCX]] | active | collective-communication, heterogeneous-computing, distributed-training, distributed-inference, heterogeneous-communication | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagCX) |
| [[community/NVIDIA/NCCL/NCCL|NCCL]] | active | all-reduce, all-gather, reduce-scatter, broadcast, point-to-point | 3 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NCCL) |
| [[community/ai-dynamo/NIXL/NIXL|NIXL]] | active | point-to-point-transfer, memory-storage-abstraction, plugin-backends, gpu-direct, storage | 3 | 9 | 2 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NIXL) |
| [[community/ROCm/RCCL/RCCL|RCCL]] | active | all-reduce, all-gather, reduce-scatter, all-to-all, point-to-point | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=RCCL) |
| [[community/OpenUCX/UCX/UCX|UCX]] | active | rdma, tcp, shared-memory, gpu-memory, communication-abstraction | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=UCX) |
| [[community/sii-research/VCCL/VCCL|VCCL]] | active | collective-communication, accelerator-communication | 0 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=VCCL) |

## runtime

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]] | active | gemm, cute, cuda-templates, python-dsl | 1 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=CUTLASS) |
| [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] | active | gemm, fp8, fp4, moe-kernels, jit | 1 | 11 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepGEMM) |
| [[community/flagos-ai/FlagAttention/FlagAttention|FlagAttention]] | active | attention, triton, kernels, llm-inference, heterogeneous-computing | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagAttention) |
| [[community/flagos-ai/FlagGems/FlagGems|FlagGems]] | active | triton, kernels, heterogeneous-computing, performance-optimization, operator-library | 0 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagGems) |
| [[community/Dao-AILab/FlashAttention/FlashAttention|FlashAttention]] | active | exact-attention, io-aware-attention, memory-efficient-attention | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashAttention) |
| [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] | active | attention-kernels, paged-attention, lora-kernels, kernel-generation | 2 | 11 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashInfer) |
| [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] | active | attention-kernels, mla-optimization | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashMLA) |
| [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | active | inference-runtime, ascend-runtime | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MindIE-Motor) |
| [[community/Ascend/ops-transformer/ops-transformer|ops-transformer]] | active | transformer-operators, ascend-kernels | 0 | 3 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ops-transformer) |
| [[community/flagos-ai/sglang-plugin-FL/sglang-plugin-FL|sglang-plugin-FL]] | active | sglang, heterogeneous-inference, hardware-backend, llm-serving, sglang-plugin | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=sglang-plugin-FL) |
| [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | active | inference-optimization, performance-tooling | 0 | 1 | 4 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TokenSpeed) |
| [[community/flagos-ai/vllm-plugin-FL/vllm-plugin-FL|vllm-plugin-FL]] | active | vllm, heterogeneous-inference, hardware-backend, llm-serving, vllm-plugin | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vllm-plugin-FL) |

## compiler

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]] | active | jit-compilation, kernel-generation | 0 | 3 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepJIT) |
| [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] | active | compiler, triton, heterogeneous-computing, multi-backend, kernel-dsl | 0 | 8 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagTree) |
| [[community/tile-ai/TileLang/TileLang|TileLang]] | active | kernel-dsl, kernel-generation | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TileLang) |
| [[community/triton-lang/Triton/Triton|Triton]] | active | gpu-kernel-dsl, compiler, jit, mlir | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Triton) |

## training

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/hpcaitech/Colossal-AI/Colossal-AI|Colossal-AI]] | active | distributed-training, parallelism, large-model-training | 0 | 5 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Colossal-AI) |
| [[community/flagos-ai/FlagScale/FlagScale|FlagScale]] | active | distributed-training, heterogeneous-training, llm-inference, auto-tuning, large-model-training | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagScale) |
| [[community/Oneflow-Inc/OneFlow/OneFlow|OneFlow]] | active | deep-learning-framework, distributed-training, tensor-runtime | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=OneFlow) |

## scheduler

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/kai-scheduler/KAI-Scheduler/KAI-Scheduler|KAI-Scheduler]] | active | queue, quota, fair-share, gang-scheduling, preemption | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KAI-Scheduler) |
| [[community/kubernetes-sigs/Kueue/Kueue|Kueue]] | active | job-queueing, admission-control, cluster-queue, fair-sharing, multi-cluster | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kueue) |
| [[community/volcano-sh/Volcano/Volcano|Volcano]] | active | batch-scheduling, gang-scheduling, queue, preemption, backfill | 0 | 8 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Volcano) |

## device-resource

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/Project-HAMi/HAMi/HAMi|HAMi]] | active | gpu-sharing, memory-isolation, device-plugin, heterogeneous-accelerators, topology-aware-allocation | 2 | 4 | 5 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HAMi) |
| [[community/cloud-native/Kubernetes-DRA/Kubernetes-DRA|Kubernetes DRA]] | active | resource-claim, device-class, resource-slice, structured-device-allocation, kubernetes | 3 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kubernetes%20DRA) |
| [[community/NVIDIA/GPU-Operator/NVIDIA-GPU-Operator|NVIDIA GPU Operator]] | active | gpu-driver-lifecycle, container-toolkit, device-plugin, dcgm, gpu-feature-discovery | 2 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVIDIA%20GPU%20Operator) |
| [[community/NVIDIA/k8s-device-plugin/NVIDIA-k8s-device-plugin|NVIDIA k8s-device-plugin]] | active | kubernetes-device-plugin, gpu-discovery, gpu-health, time-slicing, mps | 1 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVIDIA%20k8s-device-plugin) |

## benchmark

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/flagos-ai/FlagPerf/FlagPerf|FlagPerf]] | active | benchmark, ai-hardware, training, inference, heterogeneous-computing | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagPerf) |

## ecosystem

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]] | active | ai-infrastructure, kernel-optimization, communication, storage | 0 | 22 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepSeek%20Infra) |
| [[community/flagos-ai/FlagOS/FlagOS|FlagOS]] | active | heterogeneous-computing, llm-training, llm-inference, ai-compiler, kernels | 0 | 8 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagOS) |
| [[community/flagos-ai/FlagRelease/FlagRelease|FlagRelease]] | active | model-porting, deployment, heterogeneous-inference, release-engineering, software-release | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagRelease) |

## optimization

| Project | Status | Areas | Integrations | People | Companies | Graph |
| --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | active | model-compression, quantization | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=msModelSlim) |

