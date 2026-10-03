---
type: project
name: ModelSphere
layer: distributed-serving
status: active
repository: https://github.com/modelsphere/modelsphere
docs: https://github.com/modelsphere/modelsphere/tree/main/docs
areas:
  - "kubernetes"
  - "llm-serving"
  - "cache-aware-routing"
  - "autoscaling"
  - "pd-disaggregation"
  - "l3-kv-cache"
  - "dynamic-throttling"
  - "workload-driven-autotuning"
  - "heterogeneous-accelerators"
hardware:
  - "nvidia"
  - "ascend"
  - "iluvatar"
integrations:
  - "vLLM"
  - "SGLang"
last_verified: "2026-10"
---
# ModelSphere
## 项目定位

ModelSphere 是 Kubernetes 上的 LLM inference platform，重点在 engine 之上的部署、路由、扩缩、P/D、KV pool 与持续调优。它与 [[community/llm-d/llm-d/llm-d|llm-d]]、[[community/vllm-project/AIBrix/AIBrix|AIBrix]]、[[community/vllm-project/production-stack/vLLM Production Stack|vLLM Production Stack]] 处在相近的 production serving/control-plane 层，但当前治理和实现独立。

## 核心能力

- **Intelligent Auto Scaling**：按实时 demand 调整 replicas / compute，并支持高优先级模型资源优先级。
- **Quality-Aware Dynamic Throttling**：把 TTFT、output speed 等服务指标用于动态流控。
- **P/D Disaggregation**：官方明确列为 advanced serving architecture。
- **Unified L3 KV Cache Pool**：用于跨 serving instance 的 cache sharing / capacity efficiency。
- **Day-0 model deployment**：用可调优 deployment config 快速承接新模型。
- **Workload-Driven AutoTune**：空闲算力期间根据实际 workload 搜索 serving configuration。

因此该项目直接落在 [[concept/inference/scheduling/Autoscaling|Autoscaling]]、[[concept/inference/scheduling/KV-Aware Routing|KV-Aware Routing]] 与 [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]]。

## M-H-E 配置管理视角

ModelSphere 的价值不只是“拉起 Pod”。它显式需要管理模型、异构 accelerator 与 serving engine/config 的组合，当前 README 明确点名 [[community/vllm-project/vLLM/vLLM|vLLM]] 与 [[community/sgl-project/SGLang/SGLang|SGLang]]，并声称覆盖 NVIDIA、Huawei Ascend、Iluvatar CoreX 等 accelerator。其 model catalog / helm values 因而适合继续作为 M-H-E 配置管理样本深入分析。

## Sources

- https://github.com/modelsphere/modelsphere
