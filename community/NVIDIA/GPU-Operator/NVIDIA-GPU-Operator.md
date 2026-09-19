---
type: project
name: NVIDIA GPU Operator
layer: device-resource
status: active
repository: https://github.com/NVIDIA/gpu-operator
docs: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/
areas:
  - "gpu-driver-lifecycle"
  - "container-toolkit"
  - "device-plugin"
  - "dcgm"
  - "gpu-feature-discovery"
  - "kubernetes"
hardware:
  - "nvidia"
integrations:
  - "NVIDIA k8s-device-plugin"
  - "Kubernetes DRA"
companies:
  - "NVIDIA"
last_verified: "2026-09"
---
# NVIDIA GPU Operator

> 自动管理 Kubernetes NVIDIA GPU 节点软件栈的 Operator。

## 核心能力

| 能力 | 说明 |
|---|---|
| Driver Lifecycle | 部署和维护 NVIDIA GPU Driver |
| Container Toolkit | 配置 GPU 容器运行时 |
| Device Plugin | 集成 Kubernetes GPU 设备暴露 |
| Monitoring / Labels | 集成 DCGM、GFD 等节点能力 |

## 边界

GPU Operator 负责 NVIDIA GPU 节点软件生命周期，不负责 AI workload queue、LLM serving 或模型 kernel。

## 集成与后端

- NVIDIA k8s-device-plugin：Operator 管理的软件组件之一。
- Kubernetes DRA：GPUCluster 路线使用 DRA 进行设备分配。

## 关联项目

- 模型 serving：Triton Inference Server。
- 异构设备共享路线：HAMi。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前 NVIDIA 官方文档为快照。

## 直接来源

- https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/
- https://github.com/NVIDIA/gpu-operator
