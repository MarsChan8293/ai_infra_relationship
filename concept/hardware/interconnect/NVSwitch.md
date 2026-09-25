---
type: concept
name: NVSwitch
aliases:
  - NVIDIA NVSwitch
  - NVLink Switch
  - NVLink Switch Fabric
domain: hardware
topic: interconnect
parent_concepts:
  - Hardware Interconnect
related_concepts:
  - NVLink
  - Collective Communication
projects:
  - NCCL
  - VCCL
last_verified: 2026-09
---

# NVSwitch

## 一句话定义

NVSwitch 是面向 NVLink 的交换芯片/fabric，把多块 NVIDIA GPU 连接成高带宽、近似全互联的节点内或机架级拓扑。

## 解决的问题

纯 point-to-point NVLink 的连接数会受到 GPU link 数量限制。NVSwitch 通过交换 fabric 扩展可达性，使 collective 和 tensor-parallel traffic 不必完全依赖固定直连拓扑。

## 核心影响

- 更高的 bisection bandwidth。
- 更均匀的 GPU↔GPU reachability。
- collective topology 更规则。
- 减少部分 traffic 经 PCIe/host bridge 绕行。
- 大规模系统仍需结合跨节点 NIC/RDMA fabric。

## 与 NVLink 的区别

[[NVLink]] 是 link/protocol；NVSwitch 是交换 fabric。可以把它理解为“高速道路”和“交换枢纽”的不同层级。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]] 对 NVLink/NVSwitch 系统进行 topology-aware collective planning；[[community/sii-research/VCCL/VCCL|VCCL]] 明确覆盖 NVLink/NVSwitch 并进行 topology-aware scheduling。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/
- https://vccl-doc.readthedocs.io/en/latest/
