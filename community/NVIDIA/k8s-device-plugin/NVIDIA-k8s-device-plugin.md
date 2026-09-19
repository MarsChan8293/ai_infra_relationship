---
type: project
name: NVIDIA k8s-device-plugin
linked_people: []
layer: device-resource
status: active
repository: https://github.com/NVIDIA/k8s-device-plugin
docs: https://github.com/NVIDIA/k8s-device-plugin
areas:
  - "kubernetes-device-plugin"
  - "gpu-discovery"
  - "gpu-health"
  - "time-slicing"
  - "mps"
  - "kubernetes"
hardware:
  - "nvidia"
integrations:
  - "NVIDIA GPU Operator"
companies: ["NVIDIA"]
last_verified: "2026-09"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---
# NVIDIA k8s-device-plugin

> NVIDIA 官方 Kubernetes Device Plugin，用于向 kubelet 暴露并分配 GPU 资源。

## 核心能力

| 能力 | 说明 |
|---|---|
| GPU Discovery | 向 Kubernetes 报告节点 GPU |
| Allocate | 把选定设备注入容器 |
| Health | 跟踪 GPU 可用状态 |
| Sharing | 支持 time-slicing、MPS 等共享配置 |

## 边界

该项目负责 Kubernetes device plugin 语义，不承担完整驱动生命周期、Job 调度或 LLM serving。

## 集成与后端

- NVIDIA GPU Operator：常由 Operator 管理和部署。

## 关联项目

- 结构化设备分配：Kubernetes DRA。
- 异构共享设备层：HAMi。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/NVIDIA/k8s-device-plugin

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
