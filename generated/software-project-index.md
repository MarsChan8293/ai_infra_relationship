# Software Project Index

Automatically generated from every canonical Markdown node with `type: project` under `company/`, `community/`, and `university/`.

- Projects: 165
- Source roots: community 140 · company 12 · university 13
- Fine-grained `layer` metadata is preserved in the table; portal sections fold those layers into a stable navigation taxonomy.
- Concepts are not included; they remain in `ai_infra_docs/software/concepts`.

## Browse by technology layer

| Layer | Projects |
| --- | ---: |
| [Inference Engine](#inference-engine) | 25 |
| [Distributed Serving](#distributed-serving) | 21 |
| [Gateway / Routing](#gateway) | 2 |
| [KV Cache](#kv-cache) | 10 |
| [Storage](#storage) | 2 |
| [Communication / Data Movement](#communication) | 14 |
| [Runtime / Framework](#runtime) | 27 |
| [Kernel / Operator](#kernel) | 10 |
| [Compiler / DSL](#compiler) | 8 |
| [Training / Post-training](#training) | 14 |
| [Scheduler / Orchestration](#scheduler) | 8 |
| [Device / Resource](#device-resource) | 6 |
| [Benchmark / Profiling](#benchmark) | 4 |
| [Ecosystem](#ecosystem) | 2 |
| [Inference Optimization](#optimization) | 6 |
| [Other](#other) | 6 |

## inference-engine

**Inference Engine** · 25 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/thu-pacman/Chitu/Chitu]] | inference-engine |  | llm-serving, inference-engine, heterogeneous-compute, quantization, distributed-serving | `thu-pacman` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Chitu) |
| [[university/浙江大学/FloE]] | moe-inference |  | llm-inference, moe, memory-optimization, parameter-offload, pcie | `university:浙江大学` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FloE) |
| [[community/FlashML-org/FreeToken/FreeToken]] | edge-moe-serving |  | llm-inference, moe-inference, edge-inference, cpu-gpu-coexecution, expert-caching | `FlashML-org` | 0 | 3 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FreeToken) |
| [[university/浙江大学/HMI]] | multi-tenant-inference |  | multi-tenant-serving, memory-management, parameter-swapping, prefetch, pipeline | `university:浙江大学` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HMI) |
| [[community/InfiniTensor/InfiniLM]] | inference-engine |  | llm-inference, paged-attention, cuda-graph, tensor-parallel, pipeline-parallel | `InfiniTensor` | 0 | 7 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniLM) |
| [[community/InfiniTensor/InfiniTensor]] | inference-engine |  | inference-engine, tensor-compiler, hardware-backend, heterogeneous-compute, cuda-graph | `InfiniTensor` | 0 | 7 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniTensor) |
| [[community/kvcache-ai/KTransformers/KTransformers]] | inference-engine | active | heterogeneous-inference, cpu-gpu-offload, moe-inference | `kvcache-ai` | 0 | 18 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KTransformers) |
| [[company/Together AI/Ladder Residual]] | tensor-parallel-inference |  | llm-inference, tensor-parallelism, communication-overlap, distributed-inference | `company:Together AI` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Ladder%20Residual) |
| [[community/ModelTC/LightLLM/LightLLM]] | inference-engine | active | llm-serving, distributed-inference, token-generation | `ModelTC` | 0 | 9 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LightLLM) |
| [[university/香港中文大学/LiveServe]] | realtime-multimodal-serving |  | realtime-serving, multimodal-serving, kv-cache, scheduling, audio-serving | `university:香港中文大学` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LiveServe) |
| [[community/ggml-org/llama.cpp/llama.cpp]] | inference-engine | active | llm-inference, vlm-inference, local-inference, edge-inference, quantization | `ggml-org` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=llama.cpp) |
| [[community/InternLM/LMDeploy/LMDeploy]] | inference-engine |  | llm-inference, model-serving, quantization, cuda-kernels, kv-cache | `InternLM` | 0 | 3 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LMDeploy) |
| [[community/Ascend/MindIE-LLM/MindIE-LLM]] | inference-engine | active | llm-inference, ascend-inference | `Ascend` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MindIE-LLM) |
| [[community/Ascend/MindIE-SD/MindIE-SD]] | inference-engine | active | diffusion-inference, ascend-inference | `Ascend` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MindIE-SD) |
| [[university/UC Berkeley/MoE-Lightning]] | inference-engine |  | moe-inference, heterogeneous-inference, cpu-gpu-offloading, memory-optimization | `university:UC Berkeley` | 0 | 3 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MoE-Lightning) |
| [[community/ollama/Ollama/Ollama]] | local-inference-platform |  | local-inference, hybrid-inference, model-serving, model-management, gguf | `ollama` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Ollama) |
| [[company/Intel/OpenVINO GenAI]] | genai-inference-library |  | llm-inference, genai, continuous-batching, kv-cache, speculative-decoding | `company:Intel` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=OpenVINO%20GenAI) |
| [[community/sgl-project/SGLang/SGLang]] | inference-engine | active | continuous-batching, radix-attention, prefix-caching, tensor-parallel, expert-parallel | `sgl-project` | 5 | 31 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=SGLang) |
| [[community/siliconflow/SiliconLLM/SiliconLLM]] | llm-inference-engine |  |  | `siliconflow` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=SiliconLLM) |
| [[community/interestingLSY/swiftLLM/swiftLLM]] | research-llm-inference-engine |  | llm-serving, inference-engine, triton, paged-attention, scheduling | `interestingLSY` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=SwiftLLM) |
| [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM]] | inference-engine | active | tensorrt-engine, quantization, speculative-decoding, tensor-parallel, expert-parallel | `NVIDIA` | 1 | 10 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TensorRT-LLM) |
| [[community/vllm-project/vLLM/vLLM]] | inference-engine | active | continuous-batching, paged-kv-cache, prefix-caching, speculative-decoding, tensor-parallel | `vllm-project` | 8 | 29 | 6 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM) |
| [[community/vllm-project/vLLM-Ascend/vLLM-Ascend]] | inference-engine | active | ascend-inference, vllm-backend | `vllm-project` | 1 | 17 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM-Ascend) |
| [[community/vllm-project/vLLM-Omni/vLLM-Omni]] | multimodal-serving |  | multimodal-inference, disaggregated-inference, diffusion-serving, realtime-serving, data-transfer | `vllm-project` | 0 | 7 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM-Omni) |
| [[community/xLLM-AI/xLLM/xLLM]] | inference-engine | active | llm-inference, heterogeneous-inference, chinese-ai-accelerators, service-engine-decoupling, kv-cache | `xLLM-AI` | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=xLLM) |

## distributed-serving

**Distributed Serving** · 21 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/vllm-project/AIBrix/AIBrix]] | distributed-serving | active | llm-infrastructure, model-serving, autoscaling, request-routing, kubernetes | `vllm-project` | 1 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=AIBrix) |
| [[community/bentoml/BentoML/BentoML]] | distributed-serving | active | model-serving, api-service, autoscaling, packaging | `bentoml` | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=BentoML) |
| [[company/月之暗面/checkpoint-engine]] | distributed-serving | active | reinforcement-learning, weight-transfer, checkpoint-loading, distributed-training, inference-serving | `company:月之暗面` | 3 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Checkpoint%20Engine) |
| [[community/LLMServe/DistServe/DistServe]] | disaggregated-llm-serving |  | llm-serving, prefill-decode-disaggregation, scheduling, slo, distributed-inference | `LLMServe` | 0 | 3 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DistServe) |
| [[company/基流科技/Expert-as-a-Service]] | distributed-serving | unknown | moe-serving, expert-disaggregation, elastic-serving, fault-tolerance, p2p-communication | `company:基流科技` | 0 | 5 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Expert-as-a-Service) |
| [[community/lmsys-org/FastChat/FastChat]] | llm-serving |  | llm-serving, openai-compatible-api, model-serving, distributed-serving, evaluation | `lmsys-org` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FastChat) |
| [[university/清华大学/FastDecode]] | distributed-serving |  | llm-serving, heterogeneous-inference, kv-cache, cpu-gpu-pipeline | `university:清华大学` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FastDecode) |
| [[university/Carnegie Mellon University/Catalyst Group/FlexFlow Serve]] | distributed-serving | active | llm-serving, speculative-decoding, distributed-inference, cpu-offload, quantization | `university:Carnegie Mellon University` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlexFlow%20Serve) |
| [[community/kubernetes-sigs/Gateway-API-Inference-Extension/Gateway-API-Inference-Extension]] | distributed-serving | active | inference-pool, inference-aware-routing, gateway-api, multi-cluster-routing, kubernetes | `kubernetes-sigs` | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Gateway%20API%20Inference%20Extension) |
| [[community/gpustack/GPUStack/GPUStack]] | distributed-serving | active | gpu-cluster, model-serving, inference-orchestration, heterogeneous-compute, model-gateway | `gpustack` | 9 | 5 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GPUStack) |
| [[community/kserve/KServe/KServe]] | distributed-serving | active | kubernetes-model-serving, llm-inference-service, autoscaling, inference-routing, kubernetes | `kserve` | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KServe) |
| [[university/上海交通大学/KunServe]] | llm-serving |  | llm-serving, memory-management, kv-cache, resource-management, elasticity | `university:上海交通大学` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KunServe) |
| [[community/BerriAI/LiteLLM/LiteLLM]] | distributed-serving | active | llm-gateway, provider-routing, rate-limiting, cost-tracking, openai-compatible-proxy | `BerriAI` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LiteLLM) |
| [[community/llm-d/llm-d/llm-d]] | distributed-serving | active | request-routing, kv-aware-routing, pd-disaggregation, worker-pool-orchestration, kubernetes | `llm-d` | 4 | 15 | 5 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=llm-d) |
| [[community/LoongServe/LoongServe/LoongServe]] | long-context-llm-serving |  | llm-serving, long-context, sequence-parallelism, kv-cache, scheduling | `LoongServe` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LoongServe) |
| [[community/ai-dynamo/Dynamo/Dynamo]] | distributed-serving | active | distributed-inference, disaggregated-serving, kv-aware-routing, cache-management, autoscaling | `ai-dynamo` | 4 | 11 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVIDIA%20Dynamo) |
| [[community/ray-project/Ray-Serve/Ray-Serve]] | distributed-serving | active | distributed-serving, autoscaling, multi-model, pd-disaggregation, prefix-aware-routing | `ray-project` | 2 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Ray%20Serve) |
| [[community/lmsys-org/S-LoRA/S-LoRA]] | adapter-serving |  | llm-serving, lora, adapter-serving, memory-management, batching | `lmsys-org` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=S-LoRA) |
| [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server]] | distributed-serving | active | model-serving, dynamic-batching, multi-framework-serving | `triton-inference-server` | 1 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Triton%20Inference%20Server) |
| [[community/vllm-project/production-stack/vLLM Production Stack]] | distributed-serving | active | vllm-production-deployment, kubernetes, request-routing, kv-cache-offloading, observability | `vllm-project` | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM%20Production%20Stack) |
| [[community/xLLM-AI/xLLM-service/xLLM-service]] | distributed-serving | active | cluster-serving, request-scheduling, pd-disaggregation, epd-disaggregation, online-offline-scheduling | `xLLM-AI` | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=xLLM-service) |

## gateway

**Gateway / Routing** · 2 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/deepseek-recipe]] | serving-api-adapter |  | llm-serving, api-protocol, prompt-encoding, response-parsing, rust | `deepseek-ai` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=deepseek-recipe) |
| [[community/lmsys-org/RouteLLM/RouteLLM]] | model-routing |  | llm-routing, inference-cost, model-selection, preference-learning, serving | `lmsys-org` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=RouteLLM) |

## kv-cache

**KV Cache** · 10 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DualPath/DualPath]] | kv-cache |  | agentic-inference, llm-serving, kv-cache, disaggregated-serving, storage-io | `deepseek-ai` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DualPath) |
| [[community/taco-project/FlexKV/FlexKV]] | distributed-kv-cache |  | kv-cache, distributed-storage, multi-level-cache, rdma, data-movement | `taco-project` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlexKV) |
| [[community/vllm-project/Jenga/Jenga]] | heterogeneous-memory-management |  | llm-serving, memory-management, kv-cache, heterogeneous-models | `vllm-project` | 0 | 5 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Jenga) |
| [[community/thu-pacman/Lethe/Lethe]] | kv-cache-optimization |  | llm-serving, kv-cache, reasoning-models, cache-pruning, memory-efficiency | `thu-pacman` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Lethe) |
| [[community/LMCache/LMCache/LMCache]] | kv-cache | active | kv-cache, distributed-kv-cache, offloading, storage-backend, p2p | `LMCache` | 3 | 19 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LMCache) |
| [[community/Deep-Spark/lmcache-iluvatar/lmcache-iluvatar]] | kv-cache-hardware-plugin |  |  | `Deep-Spark` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=lmcache-iluvatar) |
| [[community/Ascend/MemCache/MemCache]] | kv-cache |  | kv-cache, distributed-storage, prefix-cache, memory-pooling, disaggregated-serving | `Ascend` | 0 | 14 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MemCache) |
| [[community/kvcache-ai/Mooncake/Mooncake]] | kv-cache | active | kv-cache, disaggregated-serving, rdma, data-movement, distributed-storage | `kvcache-ai` | 2 | 21 | 2 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Mooncake) |
| [[community/xPU-IO/Tutti/Tutti]] | kv-cache |  | kv-cache, gpu-storage, nvme, ssd-offload, llm-serving | `xPU-IO` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Tutti) |
| [[community/openEuler/openYuanRong/YuanRong DataSystem]] | distributed-data-cache |  | distributed-cache, kv-cache, hbm, dram, ssd | `openEuler` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=YuanRong%20DataSystem) |

## storage

**Storage** · 2 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/3FS]] | storage | active | distributed-file-system, high-throughput-storage, linux | `deepseek-ai` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=3FS) |
| [[university/厦门大学/GeminiFS]] | gpu-storage |  | gpu-storage, filesystem, nvme, direct-storage, ml-systems | `university:厦门大学` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GeminiFS) |

## communication

**Communication / Data Movement** · 14 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/DeepEP]] | communication | active | expert-parallel, all-to-all, moe-dispatch, moe-combine, low-latency | `deepseek-ai` | 1 | 9 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepEP) |
| [[community/flagos-ai/FlagCX/FlagCX]] | communication | active | collective-communication, heterogeneous-computing, distributed-training, distributed-inference, heterogeneous-communication | `flagos-ai` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagCX) |
| [[company/基流科技/HetCCL]] | communication | unknown | collective-communication, heterogeneous-communication, mixed-vendor, rdma, distributed-training | `company:基流科技` | 0 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HetCCL) |
| [[community/InfiniTensor/InfiniCCL]] | collective-communication |  | collective-communication, distributed-systems, nccl, hccl, cncl | `InfiniTensor` | 0 | 3 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniCCL) |
| [[community/Ascend/MemFabric/MemFabric]] | communication |  | memory-pooling, data-movement, disaggregated-serving, kv-cache, rdma | `Ascend` | 0 | 6 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MemFabric) |
| [[company/月之暗面/MoonEP]] | communication | active | expert-parallelism, communication, moe | `company:月之暗面` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MoonEP) |
| [[community/MetaX-MACA/MXDeepEP/MXDeepEP]] | moe-expert-parallel-communication |  |  | `MetaX-MACA` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MXDeepEP) |
| [[community/NVIDIA/NCCL/NCCL]] | communication | active | all-reduce, all-gather, reduce-scatter, broadcast, point-to-point | `NVIDIA` | 3 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NCCL) |
| [[community/ai-dynamo/NIXL/NIXL]] | communication | active | point-to-point-transfer, memory-storage-abstraction, plugin-backends, gpu-direct, storage | `ai-dynamo` | 3 | 9 | 2 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NIXL) |
| [[community/ROCm/RCCL/RCCL]] | communication | active | all-reduce, all-gather, reduce-scatter, all-to-all, point-to-point | `ROCm` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=RCCL) |
| [[community/kvcache-ai/Mooncake/TENT]] | data-movement |  | data-movement, rdma, heterogeneous-interconnect, fault-tolerance, disaggregated-serving | `kvcache-ai` | 0 | 5 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TENT) |
| [[community/OpenUCX/UCX/UCX]] | communication | active | rdma, tcp, shared-memory, gpu-memory, communication-abstraction | `OpenUCX` | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=UCX) |
| [[community/sii-research/VCCL/VCCL]] | communication | active | collective-communication, accelerator-communication | `sii-research` | 0 | 6 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=VCCL) |
| [[community/openEuler/openYuanRong/YuanRong TransferEngine]] | npu-data-transfer |  | data-transfer, rdma, roce, npu, kv-transfer | `openEuler` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=YuanRong%20TransferEngine) |

## runtime

**Runtime / Framework** · 27 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/Ascend/CANN/CANN]] | ai-compute-software-stack |  |  | `Ascend` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=CANN) |
| [[community/NVIDIA/CUTLASS/CUTLASS]] | runtime | active | gemm, cute, cuda-templates, python-dsl | `NVIDIA` | 1 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=CUTLASS) |
| [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM]] | runtime | active | gemm, fp8, fp4, moe-kernels, jit | `deepseek-ai` | 1 | 11 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepGEMM) |
| [[community/Deep-Spark/DeepSparkInference/DeepSparkInference]] | inference-model-and-runtime-integration |  |  | `Deep-Spark` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepSparkInference) |
| [[community/flagos-ai/FlagAttention/FlagAttention]] | runtime | active | attention, triton, kernels, llm-inference, heterogeneous-computing | `flagos-ai` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagAttention) |
| [[community/flagos-ai/FlagGems/FlagGems]] | runtime | active | triton, kernels, heterogeneous-computing, performance-optimization, operator-library | `flagos-ai` | 0 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagGems) |
| [[community/Dao-AILab/FlashAttention/FlashAttention]] | runtime | active | exact-attention, io-aware-attention, memory-efficient-attention | `Dao-AILab` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashAttention) |
| [[community/flashinfer-ai/FlashInfer/FlashInfer]] | runtime | active | attention-kernels, paged-attention, lora-kernels, kernel-generation | `flashinfer-ai` | 2 | 11 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashInfer) |
| [[community/deepseek-ai/DeepSeek-Infra/FlashMLA]] | runtime | active | attention-kernels, mla-optimization | `deepseek-ai` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashMLA) |
| [[community/ggml-org/ggml/ggml]] | tensor-runtime |  | tensor-runtime, local-inference, edge-inference, quantization, gguf | `ggml-org` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ggml) |
| [[community/gpustack/runner/runner]] | runtime | active | inference-runtime, container-images, backend-packaging, heterogeneous-inference, vllm | `gpustack` | 4 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GPUStack%20Runner) |
| [[community/gpustack/runtime/runtime]] | runtime | active | gpu-detection, workload-runtime, heterogeneous-accelerators, device-management, docker | `gpustack` | 1 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GPUStack%20Runtime) |
| [[community/Deep-Spark/iluvatar-corex-ixrt/iluvatar-corex-ixrt]] | inference-runtime |  |  | `Deep-Spark` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=iluvatar-corex-ixrt) |
| [[community/InfiniTensor/InfiniCore]] | heterogeneous-compute |  | heterogeneous-compute, runtime, operators, collective-communication, hardware-backend | `InfiniTensor` | 0 | 6 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniCore) |
| [[community/InfiniTensor/InfiniRT]] | hardware-runtime |  | runtime, device-abstraction, memory-management, heterogeneous-compute, cuda | `InfiniTensor` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniRT) |
| [[community/Ascend/MindIE-Motor/MindIE-Motor]] | runtime | active | inference-runtime, ascend-runtime | `Ascend` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MindIE-Motor) |
| [[community/sgl-project/mini-SGLang/mini-SGLang]] | llm-serving-runtime |  | llm-serving, radix-cache, chunked-prefill, overlap-scheduling, tensor-parallelism | `sgl-project` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=mini-SGLang) |
| [[company/Intel/OpenVINO]] | inference-runtime-toolkit |  | inference-runtime, llm-inference, genai, cpu, gpu | `company:Intel` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=OpenVINO) |
| [[community/openEuler/openYuanRong/openYuanRong]] | distributed-compute-runtime |  | serverless, distributed-runtime, scheduling, distributed-data, ai-infrastructure | `openEuler` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=openYuanRong) |
| [[community/Ascend/ops-transformer/ops-transformer]] | runtime | active | transformer-operators, ascend-kernels | `Ascend` | 0 | 3 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ops-transformer) |
| [[community/flagos-ai/sglang-plugin-FL/sglang-plugin-FL]] | runtime | active | sglang, heterogeneous-inference, hardware-backend, llm-serving, sglang-plugin | `flagos-ai` | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=sglang-plugin-FL) |
| [[community/lightseekorg/TokenSpeed/TokenSpeed]] | runtime | active | inference-optimization, performance-tooling | `lightseekorg` | 0 | 1 | 4 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TokenSpeed) |
| [[community/MooreThreads/torch_musa/torch_musa]] | deep-learning-framework-backend |  |  | `MooreThreads` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=torch_musa) |
| [[community/MetaX-MACA/vLLM-metax/vLLM-metax]] | llm-serving-hardware-backend |  |  | `MetaX-MACA` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vLLM-metax) |
| [[community/MooreThreads/vllm-musa/vllm-musa]] | llm-serving-hardware-backend |  |  | `MooreThreads` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vllm-musa) |
| [[community/flagos-ai/vllm-plugin-FL/vllm-plugin-FL]] | runtime | active | vllm, heterogeneous-inference, hardware-backend, llm-serving, vllm-plugin | `flagos-ai` | 1 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=vllm-plugin-FL) |
| [[company/Intel/xFasterTransformer]] | cpu-llm-inference-runtime |  | llm-inference, cpu, xeon, distributed-inference, quantization | `company:Intel` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=xFasterTransformer) |

## kernel

**Kernel / Operator** · 10 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/QingCheng-AI/ascend-kernel/ascend-kernel]] | kernel |  | ascend, kernels, llm-inference, heterogeneous-compute | `QingCheng-AI` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ascend-kernel) |
| [[community/deepseek-ai/DeepSeek-Infra/DeepSelect]] | sparse-attention-topk-kernels |  | topk, sparse-attention, sampling, cuda, gpu-kernels | `deepseek-ai` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepSelect) |
| [[community/Tencent/HPC-Ops/HPC-Ops]] | kernel |  | llm-inference, kernels, attention, moe, gemm | `Tencent` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HPC-Ops) |
| [[community/InfiniTensor/InfiniOps]] | gpu-kernels |  | operator-library, gpu-kernels, attention, kv-cache, quantization | `InfiniTensor` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniOps) |
| [[community/MooreThreads/MATE/MATE]] | gpu-operator-kernel-library |  |  | `MooreThreads` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=MATE) |
| [[community/MetaX-MACA/mcoplib/mcoplib]] | gpu-operator-kernel-library |  |  | `MetaX-MACA` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=mcoplib) |
| [[community/InfiniTensor/ntops]] | gpu-kernels |  | gpu-kernels, llm-operators, ninetoothed, kernel-dsl | `InfiniTensor` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ntops) |
| [[community/thu-pacman/QFactory/QFactory]] | quantized-serving-kernel-optimization |  | llm-serving, quantization, kernel-generation, ai-compiler | `thu-pacman` | 0 | 3 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=QFactory) |
| [[community/deepseek-ai/DeepSeek-Infra/TileKernels]] | gpu-kernels |  | gpu-kernels, tilelang, moe, quantization, fp8 | `deepseek-ai` | 0 | 7 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TileKernels) |
| [[company/爱特思/国产化人工智能算力平台异构并行加速项目]] | operator-optimization |  | domestic-ai-compute, operator-optimization, kernel, heterogeneous-compute, model-training | `company:爱特思` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=%E5%9B%BD%E4%BA%A7%E5%8C%96%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E7%AE%97%E5%8A%9B%E5%B9%B3%E5%8F%B0%E5%BC%82%E6%9E%84%E5%B9%B6%E8%A1%8C%E5%8A%A0%E9%80%9F%E9%A1%B9%E7%9B%AE) |

## compiler

**Compiler / DSL** · 8 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/LancerLab/Croqtile/Croqtile]] | compiler | active | kernel-dsl, gpu-kernels, ai-native-programming, symbolic-shapes, compile-time-verification | `LancerLab` | 0 | 3 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Croqtile) |
| [[community/deepseek-ai/DeepSeek-Infra/DeepJIT]] | compiler | active | jit-compilation, kernel-generation | `deepseek-ai` | 0 | 3 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepJIT) |
| [[community/flagos-ai/FlagTree/FlagTree]] | compiler | active | compiler, triton, heterogeneous-computing, multi-backend, kernel-dsl | `flagos-ai` | 0 | 8 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagTree) |
| [[university/Carnegie Mellon University/Catalyst Group/Mirage Persistent Kernel]] | kernel-compiler-runtime | active | llm-inference, persistent-kernel, megakernel, compiler, gpu-runtime | `university:Carnegie Mellon University` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Mirage%20Persistent%20Kernel) |
| [[community/InfiniTensor/NineToothed]] | compiler |  | compiler, kernel-dsl, triton, tilelang, gpu-kernels | `InfiniTensor` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NineToothed) |
| [[community/siliconflow/OneDiff/OneDiff]] | diffusion-inference-compiler |  |  | `siliconflow` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=OneDiff) |
| [[community/tile-ai/TileLang/TileLang]] | compiler | active | kernel-dsl, kernel-generation | `tile-ai` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TileLang) |
| [[community/triton-lang/Triton/Triton]] | compiler | active | gpu-kernel-dsl, compiler, jit, mlir | `triton-lang` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Triton) |

## training

**Training / Post-training** · 14 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/thu-pacman/BaGuaLu/BaGuaLu]] | distributed-training |  | distributed-training, parallelism, communication, moe, activation-memory | `thu-pacman` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=BaGuaLu) |
| [[community/hpcaitech/Colossal-AI/Colossal-AI]] | training | active | distributed-training, parallelism, large-model-training | `hpcaitech` | 0 | 5 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Colossal-AI) |
| [[community/thu-pacman/FastMoE/FastMoE]] | distributed-moe-training |  | moe, distributed-training, all-to-all-communication, load-balancing, large-model-training | `thu-pacman` | 0 | 5 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FastMoE) |
| [[community/flagos-ai/FlagScale/FlagScale]] | training | active | distributed-training, heterogeneous-training, llm-inference, auto-tuning, large-model-training | `flagos-ai` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagScale) |
| [[company/面壁智能/ForgeTrain]] | training | active | llm-training, cuda-kernels, triton, distributed-training, performance-optimization | `company:面壁智能` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ForgeTrain) |
| [[university/清华大学/GLM-130B]] | pretraining-system-model-codesign |  | foundation-models, large-scale-pretraining, distributed-training, heterogeneous-hardware, inference-efficiency | `university:清华大学` | 0 | 8 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GLM-130B) |
| [[community/InfiniTensor/InfiniTrain]] | distributed-training |  | distributed-training, tensor-parallel, pipeline-parallel, sequence-parallel, zero | `InfiniTensor` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InfiniTrain) |
| [[community/radixark/Miles/Miles]] | post-training-infrastructure |  | reinforcement-learning, post-training, distributed-training, rollout, sglang | `radixark` | 0 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Miles) |
| [[community/Oneflow-Inc/OneFlow/OneFlow]] | training | active | deep-learning-framework, distributed-training, tensor-runtime | `Oneflow-Inc` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=OneFlow) |
| [[company/月之暗面/Seer]] | rl-rollout-serving |  | llm-serving, reinforcement-learning, rollout, scheduling, speculative-decoding | `company:月之暗面` | 0 | 3 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Seer) |
| [[community/vllm-project/Speculators/Speculators]] | speculative-decoding-training |  | speculative-decoding, online-training, hidden-state-transfer, vllm, distributed-training | `vllm-project` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Speculators) |
| [[community/lightseekorg/TorchSpec/TorchSpec]] | speculative-decoding-training |  | speculative-decoding, distributed-training, hidden-state-transfer, vllm, sglang | `lightseekorg` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TorchSpec) |
| [[community/Ascend/TransferQueue/TransferQueue]] | post-training-data-plane |  | post-training, reinforcement-learning, streaming-data, distributed-data, npu | `Ascend` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TransferQueue) |
| [[community/verl-project/VeRL-Omni/VeRL-Omni]] | multimodal-rl-post-training |  | reinforcement-learning, post-training, multimodal, diffusion, rollout | `verl-project` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=VeRL-Omni) |

## scheduler

**Scheduler / Orchestration** · 8 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSeek-Infra/EPLB]] | expert-parallel-load-balancing |  | moe, expert-parallel, load-balancing, inference, distributed-systems | `deepseek-ai` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=EPLB) |
| [[community/kai-scheduler/KAI-Scheduler/KAI-Scheduler]] | scheduler | active | queue, quota, fair-share, gang-scheduling, preemption | `kai-scheduler` | 2 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KAI-Scheduler) |
| [[university/华南理工大学/Kairos]] | cluster-scheduling |  | deep-learning-scheduling, gpu-cluster, ai-compute-management, deterministic-scheduling, preemption | `university:华南理工大学` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kairos) |
| [[community/cloud-native/Kubernetes/Kubernetes]] | orchestration |  | orchestration, scheduling, cloud-native, distributed-systems | `cloud-native` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kubernetes) |
| [[community/kubernetes-sigs/Kueue/Kueue]] | scheduler | active | job-queueing, admission-control, cluster-queue, fair-sharing, multi-cluster | `kubernetes-sigs` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kueue) |
| [[community/deepseek-ai/DeepSeek-Infra/LPLB]] | moe-load-balancing |  | moe, expert-parallel, load-balancing, gpu-systems, nvshmem | `deepseek-ai` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=LPLB) |
| [[company/基流科技/Venus]] | scheduler | active | cluster-scheduling, inference-serving, post-training, elastic-scaling, fault-tolerance | `company:基流科技` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Venus) |
| [[community/volcano-sh/Volcano/Volcano]] | scheduler | active | batch-scheduling, gang-scheduling, queue, preemption, backfill | `volcano-sh` | 0 | 8 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Volcano) |

## device-resource

**Device / Resource** · 6 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/gpustack/gpustack-operator/gpustack-operator]] | device-resource | active | kubernetes, accelerator-scheduling, gpu-sharing, gpu-slicing, hardware-partitioning | `gpustack` | 1 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GPUStack%20Operator) |
| [[community/Project-HAMi/HAMi/HAMi]] | device-resource | active | gpu-sharing, memory-isolation, device-plugin, heterogeneous-accelerators, topology-aware-allocation | `Project-HAMi` | 2 | 4 | 5 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HAMi) |
| [[community/cloud-native/Kubernetes-DRA/Kubernetes-DRA]] | device-resource | active | resource-claim, device-class, resource-slice, structured-device-allocation, kubernetes | `cloud-native` | 3 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kubernetes%20DRA) |
| [[community/NVIDIA/GPU-Operator/NVIDIA-GPU-Operator]] | device-resource | active | gpu-driver-lifecycle, container-toolkit, device-plugin, dcgm, gpu-feature-discovery | `NVIDIA` | 2 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVIDIA%20GPU%20Operator) |
| [[community/NVIDIA/k8s-device-plugin/NVIDIA-k8s-device-plugin]] | device-resource | active | kubernetes-device-plugin, gpu-discovery, gpu-health, time-slicing, mps | `NVIDIA` | 1 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVIDIA%20k8s-device-plugin) |
| [[university/华南理工大学/异构计算平台并行加速解决方案]] | heterogeneous-compute-platform |  | heterogeneous-compute, operator-optimization, ai-model-deployment, openEuler, hpc | `university:华南理工大学` | 0 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=%E5%BC%82%E6%9E%84%E8%AE%A1%E7%AE%97%E5%B9%B3%E5%8F%B0%E5%B9%B6%E8%A1%8C%E5%8A%A0%E9%80%9F%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88) |

## benchmark

**Benchmark / Profiling** · 4 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/flagos-ai/FlagPerf/FlagPerf]] | benchmark | active | benchmark, ai-hardware, training, inference, heterogeneous-computing | `flagos-ai` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagPerf) |
| [[community/gpustack/gguf-parser-go/gguf-parser-go]] | benchmark | active | gguf, memory-estimation, throughput-estimation, model-profiling, resource-planning | `gpustack` | 2 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GGUF%20Parser) |
| [[community/SemiAnalysisAI/InferenceX/InferenceX]] | benchmark | active | llm-inference, agentic-inference, continuous-benchmarking, performance-per-dollar, performance-per-watt | `SemiAnalysisAI` | 4 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=InferenceX) |
| [[community/deepseek-ai/DeepSeek-Infra/profile-data]] | systems-profiling |  | profiling, moe, expert-parallel, prefill, decode | `deepseek-ai` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=profile-data) |

## ecosystem

**Ecosystem** · 2 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/flagos-ai/FlagRelease/FlagRelease]] | ecosystem | active | model-porting, deployment, heterogeneous-inference, release-engineering, software-release | `flagos-ai` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlagRelease) |
| [[community/gpustack/community-inference-backends/community-inference-backends]] | ecosystem | active | inference-backend, backend-marketplace, model-serving, extensibility, heterogeneous-inference | `gpustack` | 4 | 1 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GPUStack%20Community%20Inference%20Backends) |

## optimization

**Inference Optimization** · 6 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/deepseek-ai/DeepSpec/DeepSpec]] | speculative-decoding |  | llm-inference, speculative-decoding, draft-model, inference-acceleration | `deepseek-ai` | 0 | 4 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=DeepSpec) |
| [[community/lmsys-org/Lookahead-Decoding/Lookahead-Decoding]] | speculative-decoding |  | speculative-decoding, parallel-decoding, llm-inference, latency-optimization | `lmsys-org` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Lookahead%20Decoding) |
| [[community/Ascend/msModelSlim/msModelSlim]] | optimization | active | model-compression, quantization | `Ascend` | 0 | 0 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=msModelSlim) |
| [[community/yzygitzh/RoofLang/RoofLang]] | optimization | active | inference-optimization, system-architecture-search, graph-ir, roofline-modeling, discrete-event-simulation | `yzygitzh` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=RoofLang) |
| [[community/sgl-project/SpecForge/SpecForge]] | speculative-decoding |  | speculative-decoding, draft-model-training, llm-inference, distributed-training | `sgl-project` | 0 | 1 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=SpecForge) |
| [[university/Carnegie Mellon University/Catalyst Group/XGrammar]] | structured-generation | active | structured-generation, constrained-decoding, llm-inference, speculative-decoding | `university:Carnegie Mellon University` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=XGrammar) |

## other

**Other** · 6 projects

| Project | Exact layer | Status | Areas | Upstream / source | Integrations | People | Companies | Graph |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [[community/sail-sg/EnvPool/EnvPool]] | other |  | ai-infrastructure | `sail-sg` | 0 | 0 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=EnvPool) |
| [[community/Project-HAMi/ascend-device-plugin/ascend-device-plugin]] | other |  | ascend, kubernetes, accelerator-scheduling, device-plugin, heterogeneous-computing | `Project-HAMi` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HAMi%20Ascend%20Device%20Plugin) |
| [[community/ray-project/Ray/Ray]] | other |  | ai-infrastructure, distributed-computing, machine-learning-systems, training, serving | `ray-project` | 0 | 4 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Ray) |
| [[community/deepseek-ai/DeepSeek-Infra/smallpond]] | distributed-data-processing |  | data-processing, distributed-query, duckdb, 3fs, parquet | `deepseek-ai` | 0 | 2 | 1 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=smallpond) |
| [[community/apache/Spark/Spark]] | other |  | distributed-computing, data-processing, cluster-computing, ai-data-platform | `apache` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Spark) |
| [[community/tile-ai/TileScale/TileScale]] | other |  | ai-infrastructure | `tile-ai` | 0 | 2 | 0 | [Graph](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=TileScale) |

## Unmapped fine-grained layers

These project layers currently fold into `other`. Keeping this list visible makes taxonomy cleanup explicit rather than silently losing detail.

- `other`: 5
- `distributed-data-processing`: 1

