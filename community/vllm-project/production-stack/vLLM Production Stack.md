---
type: project
name: vLLM Production Stack
status: active
linked_people: []
repository: https://github.com/vllm-project/production-stack
docs: https://docs.vllm.ai/projects/production-stack
last_verified: "2026-09"
layer: distributed-serving
areas:
  - "vllm-production-deployment"
  - "kubernetes"
  - "request-routing"
  - "kv-cache-offloading"
  - "observability"
  - "helm"
integrations:
  - "vLLM"
  - "LMCache"
linked_companies: []
---
# vLLM Production Stack

## 项目简介
vLLM Production Stack 是 vLLM Project 下的生产部署参考栈，用于把单个 vLLM 实例扩展为 Kubernetes 上的分布式推理服务。它以 Helm 组织 serving engine、request router 与 observability stack，目标是在不改变上层 OpenAI-compatible API 使用方式的前提下增加多实例部署、请求路由、监控和 KV Cache offload。

它与 [[llm-d]]、[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]]、[[AIBrix]] 位于相邻的 distributed inference / serving 层，但定位更偏“vLLM 官方生产参考部署与组合栈”，而不是独立的通用分布式推理运行时。

## GitHub
https://github.com/vllm-project/production-stack

## 官方文档
https://docs.vllm.ai/projects/production-stack

## 主要维护者 / 组织
由 vLLM Project 社区维护。官方 README 提供 production-stack 社区会议，并列出 @ruizhang0101、@ApostaC、@YuhanLiu11、@Shaoting-Feng 等项目联系人。本节点只记录项目级治理事实，不仅凭联系人身份推断公司雇佣关系。

## 核心能力
- 通过 Helm 部署和管理多实例 vLLM serving。
- 提供 request router，支持模型路由、session-ID 路由，并持续演进 prefix/KV-aware routing。
- 通过 Prometheus + Grafana 提供 serving observability。
- 与 [[LMCache]] 集成实现 KV Cache offloading。
- 官方 roadmap 持续推进 autoscaling、disaggregated prefill 与更强的 router。

## 生态关系
- [[vLLM]]：核心 serving engine，Production Stack 直接构建在 vLLM 之上。
- [[LMCache]]：官方教程直接支持 KV Cache offloading。
- [[llm-d]]：同属 vLLM 生产化生态，但 llm-d 更偏大规模 distributed inference orchestration。
- [[KServe]] / [[AIBrix]]：同处 Kubernetes LLM serving/control-plane 邻近层，架构边界和治理路径不同。

## Sources
- https://github.com/vllm-project/production-stack
- https://docs.vllm.ai/projects/production-stack
