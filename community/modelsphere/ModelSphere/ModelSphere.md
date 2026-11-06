---
type: project
name: ModelSphere
linked_people: []
linked_concepts:
  - "concept/inference/scheduling/Autoscaling"
  - "concept/inference/kv-cache/KV Cache Management"
  - "concept/inference/kv-cache/KV Cache Sharing"
  - "concept/inference/scheduling/KV-Aware Routing"
  - "concept/inference/serving/P-D Disaggregation"
  - "concept/inference/scheduling/Request Routing"
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
last_verified: "2026-11"
linked_companies: []
code_availability: public
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

## 关键组件与工程边界（2026-11 核查）

- **路由数据面**：`llm-openresty` 负责 API 层入口与 session affinity；`cache_aware_router`（CART）是 Rust HTTP 反向代理，支持 vLLM、SGLang 等 OpenAI-compatible serving。
- **CART 缓存亲和**：按请求中的**字符前缀**维护本地 Radix Tree（记录历史路由到哪个 worker），按匹配长度/比例选择候选，并根据 in-flight 请求数和过载阈值退回低负载 worker；它不是消费 vLLM KV lifecycle events 的精确 KV block 索引。
- **CART 生产限制**：路由状态为进程本地，推荐每个 backend pool 单活；配置热加载更新 worker 列表后将重建 Radix Tree；当前仓库说明 metrics endpoint 尚未实现。
- **资源控制**：`llm-operator` / `slo-scaler-decision-gen` 负责 replica 扩缩与 SLO 决策；并不等同运行中 MoE EP 重切分。
- **故障续接**：`continuation_gateway` 可根据已输出文本在健康实例重新发起补全，属于文本级续接，不能视为原进程 KV 迁移或 logits 逐位一致。
- **性能调优**：`llm-autotune` 是单独的预览版调参组件；统一 L3 KV pool 与异构 P/D 在平台 README 有描述，跨 NVIDIA–Ascend 直接共享 KV 的端到端兼容性仍需单独验收。

## 与 Kinference 的差异

[[community/Kinference-AI/kinference/Kinference|Kinference]] 聚焦 Kubernetes/vLLM 请求路由决策，消费实际 KV block events + engine metrics，并对 endpoint 预测 TTFT；ModelSphere 则覆盖入口、CART、Operator、AutoTune、Console 与恢复网关等完整平台能力。**二者处于不同抽象层，CART 与 Kinference 可做同负载 A/B 对照，不能把与普通负载均衡的收益视作二者直接性能差距。**

## 组件源码

- https://github.com/modelsphere/cache_aware_router
- https://github.com/modelsphere/llm-operator
- https://github.com/modelsphere/continuation_gateway
- https://github.com/modelsphere/llm-autotune

## Sources

- https://github.com/modelsphere/modelsphere

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/scheduling/Autoscaling|Autoscaling]]
- [[concept/inference/kv-cache/KV Cache Management|KV Cache Management]]
- [[concept/inference/kv-cache/KV Cache Sharing|KV Cache Sharing]]
- [[concept/inference/scheduling/KV-Aware Routing|KV-Aware Routing]]
- [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]]
- [[concept/inference/scheduling/Request Routing|Request Routing]]

<!-- END AUTO PROJECT CONCEPTS -->
