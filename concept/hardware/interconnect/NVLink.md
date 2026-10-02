---
type: concept
name: NVLink
aliases:
  - NVIDIA NVLink
  - NVLink Interconnect
domain: hardware
topic: interconnect
parent_concepts:
  - Hardware Interconnect
related_concepts:
  - NVSwitch
  - PCIe
  - Collective Communication
projects:
  - NCCL
  - VCCL
  - TENT
last_verified: 2026-09
---

# NVLink

## 一句话定义

NVLink 是 NVIDIA 面向 GPU/accelerator 的高带宽低延迟互联，用于节点内或特定系统中的 GPU↔GPU / GPU↔CPU 数据交换。

## 为什么比“总带宽”更重要

模型并行通信并不只看单条 link 速率，还取决于：

- GPU 间实际拓扑。
- 每 GPU 可用 link 数。
- 是否经过 [[NVSwitch]]。
- collective algorithm。
- concurrent traffic。
- peer memory access 与 copy engine 行为。

## 与 PCIe 的关系

NVLink 通常作为专用高速路径补充 [[PCIe]]，而不是替代所有 PCIe I/O。NIC、NVMe 和很多 host-device control path 仍然依赖 PCIe。

## 与 Collective 的关系

[[Collective Communication]] library 会把 ring/tree/channel 映射到 NVLink topology，以减少经过慢速 PCIe 或跨 NUMA 路径的流量。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]] 进行 NVLink-aware collective；[[community/sii-research/VCCL/VCCL|VCCL]] 支持 NVLink/NVSwitch topology；[[community/kvcache-ai/Mooncake/TENT|TENT]] 把 NVLink 与 RDMA/multi-rail 等异构路径统一纳入动态 data-movement scheduling。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/
- https://vccl-doc.readthedocs.io/en/latest/
- https://arxiv.org/abs/2604.00368
