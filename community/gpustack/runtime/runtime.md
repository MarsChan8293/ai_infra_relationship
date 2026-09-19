---
type: project
name: GPUStack Runtime
layer: runtime
status: active
repository: https://github.com/gpustack/runtime
areas: [gpu-detection, workload-runtime, heterogeneous-accelerators, device-management, docker, kubernetes, podman]
hardware: [nvidia, amd, ascend, hygon, metax, mthreads, iluvatar, cambricon, t-head]
integrations: [GPUStack]
companies: ["GPUStack"]
last_verified: "2026-09"
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
