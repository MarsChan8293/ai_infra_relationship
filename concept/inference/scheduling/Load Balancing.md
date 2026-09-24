---
type: concept
name: Load Balancing
aliases:
  - Inference Load Balancing
  - LLM Load Balancing
  - 负载均衡
domain: scheduling
topic: inference-scheduling
parent_concepts:
  - Inference Scheduling
related_concepts:
  - Request Routing
  - Load-Aware Routing
  - Autoscaling
projects:
  - llm-d
  - NVIDIA Dynamo
  - AIBrix
  - Gateway API Inference Extension
  - KServe
  - MindIE-Motor
last_verified: 2026-09
---

# Load Balancing

## 一句话定义

Load Balancing 是让推理工作在多个 replica / worker 之间形成合理分布，避免部分节点过载而另一些节点闲置。

## 解决的问题

LLM serving 的请求持续时间和 token 数差异巨大，均匀分配“请求个数”并不等于均匀分配“计算与显存压力”。同时，过度追求均匀又可能破坏 KV cache locality，因此需要在负载和复用之间权衡。

## 核心机制

常见策略包括 round-robin、random、power-of-two、least-loaded、queue-aware、token-aware 和 KV-aware cost model。控制器可以把多个信号组合成 worker score，并设置过载阈值或 affinity 规则。

## 与相邻概念的区别

- [[Request Routing]] 是每次请求的 endpoint 选择动作。
- [[Load-Aware Routing]] 是直接根据实时负载完成路由。
- [[Autoscaling]] 改变 worker 数量；load balancing 只在当前 worker 集合上重新分配工作。
- KV locality 会让“最均匀”不一定是“最高吞吐”，因此 LLM load balancing 通常不是简单平均。

## 项目实现

[[community/llm-d/llm-d/llm-d|llm-d]]、[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]]、[[community/vllm-project/AIBrix/AIBrix|AIBrix]] 都实现 LLM-specific worker selection。[[community/kubernetes-sigs/Gateway-API-Inference-Extension/Gateway-API-Inference-Extension|Gateway API Inference Extension]] 的目标之一就是标准化 inference workload 的 optimized load-balancing；[[community/kserve/KServe/KServe|KServe]] 通过 inference gateway 路由；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] Coordinator 提供大规模推理服务的负载均衡。

## Sources

- https://llm-d.ai/docs/well-lit-paths/foundations/optimized-baseline
- https://docs.nvidia.com/dynamo/latest/knowledge-base/modular-components/router/routing-concepts
- https://github.com/vllm-project/aibrix
- https://gateway-api-inference-extension.sigs.k8s.io/
- https://kserve.github.io/website/
- https://gitcode.com/Ascend/MindIE-Motor
