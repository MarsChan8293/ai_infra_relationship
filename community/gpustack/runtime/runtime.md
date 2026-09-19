---
type: project
name: GPUStack Runtime
linked_people:
  - "community/gpustack/GPUStack/thxCode"
  - "community/gpustack/GPUStack/yxf0314"
layer: runtime
status: active
repository: https://github.com/gpustack/runtime
areas: [gpu-detection, workload-runtime, heterogeneous-accelerators, device-management, docker, kubernetes, podman]
hardware: [nvidia, amd, ascend, hygon, metax, mthreads, iluvatar, cambricon, t-head]
integrations: [GPUStack]
companies: ["GPUStack"]
last_verified: "2026-09"
linked_companies:
  - "company/GPUStack/GPUStack"
---
# GPUStack Runtime

GPUStack Runtime 是 [[community/gpustack/GPUStack/GPUStack|GPUStack]] 的异构加速器运行时层，提供统一的 GPU / NPU 资源探测与 GPU workload 管理接口。它把不同厂商的驱动、设备枚举和容器运行差异收敛成上层 GPUStack 可以消费的统一能力。

## AI Infra 位置

- 统一探测 NVIDIA、AMD、Ascend、Hygon、MetaX、Moore Threads、Iluvatar、Cambricon、T-Head 等加速器。
- 管理 Docker、Kubernetes 与实验性 Podman 工作负载。
- 处理设备健康、MIG / 分区、厂商运行时挂载等偏底层问题，是 GPUStack scheduler / worker 与硬件之间的重要适配层。

## 人物与关系

- [[community/gpustack/GPUStack/thxCode|thxCode]]：2026-08/09 持续修改 AMD、NVIDIA、Hygon、Ascend 等设备探测与健康检查，是当前 Runtime 最强的公开工程信号之一。
- [[community/gpustack/GPUStack/yxf0314|yxf0314]]：Ascend A5 多卡 HCCL / ranktable 问题的诊断参与者；后续修复 commit 明确引用其诊断。

## Sources

- https://github.com/gpustack/runtime
- https://github.com/gpustack/runtime/commit/fd62d22fa9728c8cbdb670a939b2be72f17b4869
- https://github.com/gpustack/runtime/commit/59187659fd5f535ef57563ffd03a0c2a73989b53
- https://github.com/gpustack/runtime/commit/55bbd00ec00173a7ad1c908c621658c1be0cbe9f

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/gpustack/GPUStack/thxCode|thxCode]]：https://github.com/gpustack/runtime/commit/fd62d22fa9728c8cbdb670a939b2be72f17b4869
- [[community/gpustack/GPUStack/yxf0314|yxf0314]]：GPUStack Runner / Runtime dependency 升级。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/GPUStack/GPUStack|GPUStack]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
