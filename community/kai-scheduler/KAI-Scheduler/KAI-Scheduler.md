---
type: project
name: KAI-Scheduler
layer: scheduler
status: active
repository: https://github.com/kai-scheduler/KAI-Scheduler
docs: https://github.com/kai-scheduler/KAI-Scheduler
areas:
  - "queue"
  - "quota"
  - "fair-share"
  - "gang-scheduling"
  - "preemption"
  - "topology-aware-scheduling"
  - "kubernetes"
integrations:
  - "HAMi"
  - "Kubernetes DRA"
last_verified: "2026-09"
---
# KAI-Scheduler

> 面向 AI/GPU 工作负载的 Kubernetes 调度器。

## 核心能力

| 能力 | 说明 |
|---|---|
| Queue / Quota | 进行多租户队列和资源治理 |
| Fair-share | 在队列之间进行公平资源分配 |
| Gang Scheduling | 面向分布式 AI workload 成组调度 |
| Topology-aware | 把 GPU/节点拓扑纳入 placement |

## 边界

KAI-Scheduler 负责 Pod/Job placement，不做 LLM request routing，也不执行设备隔离。

## 集成与后端

- HAMi：设备共享/隔离侧的组合路径。
- Kubernetes DRA：结构化设备资源表达与分配框架。

## 关联项目

- Batch 调度：Volcano。
- Job admission：Kueue。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/kai-scheduler/KAI-Scheduler
