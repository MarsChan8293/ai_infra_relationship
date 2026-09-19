---
type: project
name: GPUStack Operator
layer: device-resource
status: active
repository: https://github.com/gpustack/gpustack-operator
docs: https://docs.gpustack.ai/gpustack-operator/
areas: [kubernetes, accelerator-scheduling, gpu-sharing, gpu-slicing, hardware-partitioning, kueue, device-management, kv-cache]
hardware: [nvidia, amd, ascend, hygon, metax, mthreads, iluvatar, cambricon, t-head]
integrations: [GPUStack]
companies: ["GPUStack"]
last_verified: "2026-09"
---
# GPUStack Operator

GPUStack Operator 是 [[community/gpustack/GPUStack/GPUStack|GPUStack]] 在 Kubernetes 上的 accelerator resource control plane。它发现节点上的加速器、归一化设备能力，并在 Kueue 之上形成可调度的资源链。

## AI Infra 位置

- whole-device 独占与 shared allocation
- software slicing：为 workload 设置独立 compute / VRAM budget
- hardware partitioning：包括 NVIDIA MIG，以及 Hygon / T-Head 的对应硬件分区能力
- 多厂商 device manager 与资源池抽象
- 2026 年的工程主线已经继续向 KV cache / distributed serving 资源编排延伸

这使 Operator 不只是“安装 GPUStack 的 Helm chart”，而是 GPUStack 设备资源与推理 workload 调度体系的独立核心组件。

## 人物

- [[community/gpustack/GPUStack/thxCode|thxCode]]：2026-09 仍在高频修改 Operator，包括设备资源、Kueue、KV cache、Mooncake / shared-store 等路径。

## Sources

- https://github.com/gpustack/gpustack-operator
- https://github.com/gpustack/gpustack-operator/commit/c25422d1fc780e8ded68ee4c5d778bc6d267da30
