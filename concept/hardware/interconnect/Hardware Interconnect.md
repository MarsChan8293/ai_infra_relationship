---
type: concept
name: Hardware Interconnect
aliases:
  - Accelerator Interconnect
  - Device Interconnect
  - 硬件互联
  - 加速器互联
domain: hardware
topic: interconnect
related_concepts:
  - PCIe
  - NVLink
  - HCCS
  - xGMI
  - RDMA
  - CXL Memory
projects:
  - NCCL
  - RCCL
  - VCCL
  - TENT
  - MemFabric
  - TransferQueue
last_verified: 2026-09
---

# Hardware Interconnect

## 一句话定义

Hardware Interconnect 是连接 CPU、GPU/NPU、内存、NIC 与交换芯片的数据通路，决定节点内和节点间可获得的带宽、延迟、拓扑与一致性语义。

## 为什么它是 AI Infra 的核心变量

模型并行、KV transfer、参数更新和异构内存池都需要搬运大量 tensor。相同的软件 collective 或 transfer engine，落在不同互联上可能有完全不同的性能上限。

## 主要类别

- [[PCIe]]：通用 CPU/device I/O 总线。
- [[NVLink]] / [[NVSwitch]]：NVIDIA GPU 高带宽互联与交换 fabric。
- [[HCCS]]：Ascend 节点内/超节点高速互联路径。
- [[xGMI]]：AMD GPU/accelerator 高速互联。
- [[CXL Memory]]：基于 PCIe physical layer 扩展 cache/memory semantics。
- [[RDMA]]：更偏网络 transport 语义，常通过 NIC 连接跨节点设备。

## 软件如何利用它

Collective library 会做 topology-aware ring/tree/channel planning；数据移动层会选择 P2P、RDMA、shared memory 或高速 device link；scheduler 还可能根据拓扑决定 placement。

## 项目实现

[[community/NVIDIA/NCCL/NCCL|NCCL]]、[[community/ROCm/RCCL/RCCL|RCCL]]、[[community/sii-research/VCCL/VCCL|VCCL]] 根据互联拓扑优化 collective；[[community/kvcache-ai/Mooncake/TENT|TENT]] 在异构互联上动态调度 transfer；[[community/Ascend/MemFabric/MemFabric|MemFabric]] 与 [[community/Ascend/TransferQueue/TransferQueue|TransferQueue]] 暴露 Ascend 多种节点内/跨节点数据通路。

## Sources

- https://docs.nvidia.com/deeplearning/nccl/
- https://rocm.docs.amd.com/projects/rccl/en/latest/
- https://vccl-doc.readthedocs.io/en/latest/
- https://arxiv.org/abs/2604.00368
- https://gitcode.com/Ascend/memfabric_hybrid
- https://github.com/Ascend/TransferQueue
