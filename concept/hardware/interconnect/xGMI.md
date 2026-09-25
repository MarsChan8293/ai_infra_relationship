---
type: concept
name: xGMI
aliases:
  - AMD xGMI
  - Infinity Fabric xGMI
  - xGMI Interconnect
domain: hardware
topic: interconnect
parent_concepts:
  - Hardware Interconnect
related_concepts:
  - PCIe
  - Collective Communication
projects:
  - RCCL
last_verified: 2026-09
---

# xGMI

## 一句话定义

xGMI 是 AMD GPU/accelerator 系统中的高速互联路径，用于 GPU 间高带宽 peer communication，并被 ROCm collective stack 用于节点内通信优化。

## 在 AI Infra 中的位置

在多 GPU inference/training 中，xGMI 承担的角色与 NVIDIA 系统中的专用 GPU interconnect 类似：让 tensor-parallel、data-parallel collective 和 P2P traffic 尽量避开较慢或共享程度更高的通用 I/O 路径。

## 性能关注点

- GPU topology。
- 每 GPU peer connectivity。
- aggregate/bisection bandwidth。
- P2P copy path。
- NUMA / PCIe fallback。
- collective scheduling。

## 与 PCIe 的关系

AMD GPU 节点通常同时存在 [[PCIe]] 与 xGMI。xGMI 用于高带宽 GPU peer path，PCIe 则承担更通用的 device/host/NIC/storage I/O。

## 项目实现

[[community/ROCm/RCCL/RCCL|RCCL]] 明确针对 xGMI / PCIe 拓扑优化 AMD GPU collective，并在跨节点场景进一步结合 RDMA/network transport。

## Sources

- https://rocm.docs.amd.com/projects/rccl/en/latest/
- https://github.com/ROCm/rocm-systems
