---
type: concept
name: HCCS
aliases:
  - Huawei Cache Coherence System
  - High-speed Cache Coherent System
  - 昇腾HCCS
domain: hardware
topic: interconnect
parent_concepts:
  - Hardware Interconnect
related_concepts:
  - RDMA
  - Point-to-Point Transfer
  - HBM
projects:
  - TransferQueue
  - YuanRong DataSystem
last_verified: 2026-09
---

# HCCS

## 一句话定义

HCCS 是华为昇腾系统中的高速设备互联路径，用于 NPU/节点内高速数据交换，并可作为上层 tensor/data transfer 的硬件通道之一。

## 在 AI Infra 中的位置

对于 Ascend 分布式推理、RL/post-training 和 KV/参数搬运，数据路径可能在 HCCS、RDMA、Host memory 等通道之间选择。HCCS 更偏节点内或特定系统拓扑的 accelerator high-speed path，而 [[RDMA]] 更偏跨节点网络传输。

## 关键关注点

- 实际拓扑和可达设备。
- device-to-device bandwidth。
- H2D / D2H / remote copy 的路径选择。
- 与 HBM/Host memory 的 locality。
- 上层 runtime 是否能异步 overlap compute。
- 多路径/多 rail 调度。

## 项目实现

[[community/Ascend/TransferQueue/TransferQueue|TransferQueue]] 的 YuanRong backend 文档明确支持 Ascend NPU tensor 经 HCCS 与远程 H2D/D2H 路径移动；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 的 AI data plane 也明确覆盖 HCCS、RDMA 与多级缓存。

## Sources

- https://github.com/Ascend/TransferQueue/blob/main/docs/storage_backends/openyuanrong_datasystem.md
- https://github.com/openyuanrong/datasystem
