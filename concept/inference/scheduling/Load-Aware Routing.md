---
type: concept
name: Load-Aware Routing
aliases:
  - Least-Loaded Routing
  - Load-Sensitive Routing
  - 负载感知路由
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Inference-Aware Routing
related_concepts:
  - KV-Aware Routing
  - Load Balancing
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - Gateway API Inference Extension
last_verified: 2026-09
---

# Load-Aware Routing

## 一句话定义

Load-Aware Routing 根据 endpoint 当前队列、并发请求、token backlog、KV 使用率或预测延迟等实时负载信号选择目标 worker。

## 解决的问题

LLM 请求成本高度不均匀，同样一个“活跃连接”可能对应 10 token 输出，也可能对应超长 reasoning。只按连接数或 round-robin 分流，容易把昂贵请求叠到同一个 worker 上。

## 核心机制

Router 周期性或事件驱动地获取 worker 状态，把 queue depth、running requests、token load、KV utilization、estimated TTFT/ITL 等信号转换成 score，再优先选择预计完成成本较低的 endpoint。

## 与 KV-Aware Routing 的关系

[[KV-Aware Routing]] 倾向把请求送到已有 prefix 的 worker；load-aware routing 倾向避开拥塞 worker。实际系统常把两者组合：先争取 cache locality，但当缓存 owner 过载时切换到负载更低的节点。

## 与 Load Balancing 的区别

Load-aware routing 是实现 [[Load Balancing]] 的一种 request-level 策略。Load balancing 是目标，load-aware routing 是利用实时运行状态实现该目标的方法之一。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]] 支持 queue depth、running requests、token load 和 latency scorer；[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] 提供 least-loaded、power-of-two 以及 cache+load cost model；[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 面向 LLM-aware load balancing；[[community/kubernetes-sigs/Gateway-API-Inference-Extension/Gateway-API-Inference-Extension|Gateway API Inference Extension]] 允许 EPP 根据 endpoint metrics 做智能选择。

## Sources

- https://llm-d.ai/docs/well-lit-paths/foundations/optimized-baseline
- https://llm-d.ai/docs/architecture/core/router/epp/scheduling
- https://docs.nvidia.com/dynamo/latest/knowledge-base/modular-components/router/routing-concepts
- https://github.com/vllm-project/aibrix
- https://gateway-api-inference-extension.sigs.k8s.io/api-types/inferencepool/
