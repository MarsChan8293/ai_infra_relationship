---
type: project
name: GPUStack Operator
linked_people:
  - "community/gpustack/GPUStack/thxCode"
layer: device-resource
status: active
repository: https://github.com/gpustack/gpustack-operator
docs: https://docs.gpustack.ai/gpustack-operator/
areas: [kubernetes, accelerator-scheduling, gpu-sharing, gpu-slicing, hardware-partitioning, kueue, device-management, kv-cache]
hardware: [nvidia, amd, ascend, hygon, metax, mthreads, iluvatar, cambricon, t-head]
integrations: [GPUStack]
companies: ["GPUStack"]
last_verified: "2026-09"
linked_companies:
  - "company/GPUStack/GPUStack"
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/gpustack/GPUStack/thxCode|thxCode]]：https://github.com/gpustack/gpustack-operator/commit/c25422d1fc780e8ded68ee4c5d778bc6d267da30

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/GPUStack/GPUStack|GPUStack]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
