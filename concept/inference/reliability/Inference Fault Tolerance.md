---
type: concept
name: Inference Fault Tolerance
aliases:
  - Serving Resiliency
  - Inference Failure Recovery
  - 推理故障容错
  - 在线推理故障恢复
domain: inference
topic: reliability
related_concepts:
  - Inference Scheduling
  - Request Routing
  - Load Balancing
  - P-D Disaggregation
projects:
  - "llm-d-resiliency-manager"
last_verified: 2026-10
---

# Inference Fault Tolerance

## 一句话定义

Inference Fault Tolerance 指在线推理服务在 worker、rank、pod 或通信成员失效后，尽量保持请求入口、服务状态和剩余算力可用，并通过隔离、重路由、成员收缩或状态恢复避免整组服务完全重启。

## 与普通 Kubernetes 自愈的区别

Kubernetes / LeaderWorkerSet 可以负责 Pod 或 group 生命周期，但模型并行推理还存在 rank membership、collective、KV/请求状态和 router 可见性等运行时问题。真正的 inference fault tolerance 往往需要控制面与 engine runtime 协同，而不是只依赖重新拉起容器。

## 典型恢复链路

`detect failure → pause / drain routing → update surviving membership → validate engine health → restore routing`

对于 TP / EP / DP 等并行组，是否允许缩容运行取决于模型切分、冗余专家、通信拓扑和 engine 的 fault-tolerance API。

## 项目实现

[[community/Etelis/llm-d-resiliency-manager/llm-d-resiliency-manager|llm-d-resiliency-manager]] 针对 llm-d Expert Parallel group 做实验性在线恢复：失败后暂停 routing，通过 vLLM FT API 排除失效 rank，验证 survivor inference，再恢复 routing；Pod replacement 仍交给 LeaderWorkerSet。

## Sources

- https://github.com/Etelis/llm-d-resiliency-manager
