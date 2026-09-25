---
type: concept
name: PCIe
aliases:
  - PCI Express
  - Peripheral Component Interconnect Express
  - PCIe总线
domain: hardware
topic: interconnect
parent_concepts:
  - Hardware Interconnect
related_concepts:
  - NVLink
  - CXL Memory
  - NVMe SSD
projects:
  - NCCL
  - RCCL
  - VCCL
last_verified: 2026-09
---

# PCIe

## 一句话定义

PCIe 是 CPU、GPU/NPU、NIC、NVMe SSD 等设备最通用的高速 I/O interconnect，也是许多 accelerator server 的基础数据通路。

## 关键性能维度

- generation：Gen4 / Gen5 / Gen6。
- link width：x4 / x8 / x16。
- switch / root-complex topology。
- peer-to-peer capability。
- NUMA affinity。
- oversubscription。

标称 lane bandwidth 不是应用可得带宽，实际还受 protocol overhead、switch topology、DMA engine 和 concurrent traffic 影响。

## 在 AI Infra 中的位置

GPU↔CPU offload、NVMe I/O、NIC access、无专用高速链路时的 GPU P2P 都依赖 PCIe。[[CXL Memory]] 也建立在 PCIe physical/link infrastructure 上，但增加了 cache/memory protocol。

## 与 NVLink 的区别

[[NVLink]] 更专门面向 NVIDIA accelerator 间高带宽互联；PCIe 更通用、生态更广，但 GPU↔GPU 节点内带宽通常低于专用 link。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]] 根据 NVLink/PCIe topology 选择 collective 路径；[[community/ROCm/RCCL/RCCL|RCCL]] 明确支持 xGMI/PCIe；[[community/sii-research/VCCL/VCCL|VCCL]] 覆盖 PCIe、NVLink/NVSwitch、InfiniBand 与 TCP/IP 等多种路径。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/
- https://rocm.docs.amd.com/projects/rccl/en/latest/
- https://vccl-doc.readthedocs.io/en/latest/
