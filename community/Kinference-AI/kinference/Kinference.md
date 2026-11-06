---
type: project
name: Kinference
linked_people: []
linked_companies: []
layer: gateway
status: active
repository: https://github.com/Kinference-AI/kinference
docs: https://kinference.ai/docs/getting-started/
areas:
  - kubernetes
  - llm-serving
  - request-routing
  - kv-aware-routing
  - load-aware-routing
  - block-level-kv-index
  - predicted-ttft
  - inference-policy
hardware:
  - nvidia
integrations:
  - "vLLM"
  - "Kubernetes"
  - "Buoyant Gateway"
last_verified: "2026-11"
code_availability: public
---
# Kinference

## 项目简介

Kinference 是面向 Kubernetes 与 [[community/vllm-project/vLLM/vLLM|vLLM]] 的开源 **inference control plane / KV-aware endpoint picker**。由 Buoyant 发起，主要使用 Rust（Apache-2.0）。它通过 gRPC API 接受网关送来的推理请求，基于路由策略、前缀缓存命中和 worker 负载选择 endpoint，并返回可选的改写请求体。**它不是 vLLM 计算引擎，也不负责直接代理 HTTP 响应流或提供跨设备 KV 共享存储池。**

## GitHub

https://github.com/Kinference-AI/kinference

## 主要维护者 / 组织

- **Buoyant, Inc.**：README 著作权与发起组织可核验；项目代码托管在 GitHub `Kinference-AI` 组织下。未据此推断个人维护者身份或其他企业关联。
- 配套网关样例：[Buoyant Gateway](https://github.com/BuoyantIO/gateway)。

## 核心实现

1. **真实 KV block 事件**：通过 ZMQ 订阅 vLLM KV cache events；当前 README 说明复用 NVIDIA Dynamo 的 `dynamo-kv-router` crate 来处理缓存事件。按 worker pool / block size 建立 Radix Tree，追踪缓存的 block 前缀以及淘汰变化。
2. **Token 级前缀匹配**：对请求 prompt tokenize，通过本地模式或 vLLM `/render` 获取 token 序列，再按 `kvBlockSize` 计算与各 worker KV 的前缀重合；tokenization 失败可退化为仅按负载选路。
3. **负载感知和延迟预测**：结合 vLLM `/metrics`、in-flight 请求、提前登记的 dispatched prefix 和缓存命中，估计各 worker 等待时间/TTFT；网关回传首 token/完成事件，用于比较预测与观测。
4. **策略与控制面**：Kubernetes `InferenceWorkerSet`、`InferencePool`、`InferencePolicy`、`InferenceProvider` 等 CRD；`kinfctl` 检查策略；可选本地/集群外 provider 路由。
5. **事件一致性与弹性**：ZMQ event sequence gap 使用 replay 修复；worker restart 按新 worker 视为冷缓存。架构文档设计了 controller leader election 与 per-replica routing，但 README 仍将多 replica 支持列为未完成，不能仅凭架构推断其生产就绪。

## 工程成熟度与约束（截至 2026-11-06）

- 官方明确声明 **Alpha**：尚无持续生产暴露，缺少限流、语义分类器、Anthropic `/v1/messages` 与完成验证的多副本能力。
- **现有路径重点围绕 vLLM**；未确认直接消费 vLLM-Ascend 或 MindIE 的 KV event 协议。因此“能通过 HTTP 访问某个推理服务”并不等于该后端可被精确 KV-aware 路由。
- 不直接提供模型生命周期管理、PD 分离部署、SLO autoscaler、模型权重热替换、跨 NVIDIA/Ascend 的 KV Cache 数据面。
- 官方相关资料在 `ARCHITECTURE.md`、`docs/request-flow.md`、`kinference.ai` 文档中；模型与硬件支持以实际版本测试为准。

## 与 ModelSphere / 其他项目的关系

- [[community/modelsphere/ModelSphere/ModelSphere|ModelSphere]]：同属 serving 基础设施。ModelSphere 的 CART 用**字符前缀 + 历史路由**推测 KV 亲和性，可作为 HTTP 代理，适配 vLLM/SGLang；Kinference 用**vLLM KV 事件 + token block + 预测延迟**选路，需要配套 Gateway。ModelSphere 平台范围更广（Operator、Console、AutoTune、恢复网关）。
- [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]]：复用其 `dynamo-kv-router` 组件读取/处理缓存事件，属于明确的代码依赖；不因此推断社区或人员隶属关系。
- [[community/llm-d/llm-d/llm-d|llm-d]] / [[community/vllm-project/AIBrix/AIBrix|AIBrix]]：同类请求感知路由/分布式 serving 生态，值得对比 endpoint scoring、KV event 兼容性和高可用方式。
- 技术概念：[[concept/inference/scheduling/Request Routing|Request Routing]]、[[concept/inference/scheduling/KV-Aware Routing|KV-Aware Routing]]、[[concept/inference/scheduling/Load-Aware Routing|Load-Aware Routing]]。

## 可复现实验建议

在相同 vLLM 版本、GPU、模型、prompt trace 下，比较 Kinference、ModelSphere CART 与 round-robin：p50/p95 TTFT、SLO Goodput、真实 prefix cache hit、worker 倾斜、缓存淘汰和路由开销。尤其要在长上下文和高 churn 下验证真实 KV 事件路由是否明显优于字符前缀近似。

## Sources

- https://github.com/Kinference-AI/kinference
- https://github.com/Kinference-AI/kinference/blob/main/ARCHITECTURE.md
- https://github.com/Kinference-AI/kinference/blob/main/docs/request-flow.md
- https://github.com/modelsphere/cache_aware_router
- https://kinference.ai/docs/getting-started/
