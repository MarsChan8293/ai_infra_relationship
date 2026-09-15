---
type: project
name: Kubernetes
category: cloud-native-platform
layer: orchestration
open_source: true
repository: https://github.com/kubernetes/kubernetes
areas: [orchestration, scheduling, cloud-native, distributed-systems]
linked_people: []
last_verified: "2026-09"
---
# Kubernetes

## 项目定位
Kubernetes 是开源容器编排平台。在本图谱中只记录它与 AI Infra / LLM serving 的直接交叉，例如 [[llm-d]]、Inference Gateway、GPU workload orchestration 与生产推理平台，而不扩展成通用 cloud-native 人才图谱。

## AI Infra 连接
- [[llm-d]]：以 Kubernetes 为核心生产平台之一，把 inference engine、routing、KV-cache-aware scheduling 和 disaggregated serving 接入 cloud-native deployment 路径。
- 人物关联仅在人物页明确把 Kubernetes 作为其项目/社区主线时建立，不因为任职于云厂商自动推断 Kubernetes 参与。

## Sources
- https://kubernetes.io/
- https://github.com/kubernetes/kubernetes
