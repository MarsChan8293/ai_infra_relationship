---
type: project
name: TransferQueue
layer: post-training-data-plane
open_source: true
repository: https://github.com/Ascend/TransferQueue
areas: [post-training, reinforcement-learning, streaming-data, distributed-data, npu, rdma, hccs]
people:
  - "community/Ascend/TransferQueue/荣程浩 Chenghao Rong"
related_projects: ["YuanRong DataSystem", "veRL", "Mooncake"]
last_verified: "2026-09"
---
# TransferQueue

## 项目简介
TransferQueue 是面向大模型 post-training / reinforcement learning 的高性能异步数据存储与传输模块。它把样本级数据管理、流式调度与可插拔 storage backend 从训练控制器中解耦出来，形成训练与 rollout 之间的数据平面。

## openYuanRong 关系
TransferQueue 在 2025 年引入可插拔 KV storage backend 时，首个可用 backend 即 [[community/openEuler/openYuanRong/YuanRong DataSystem|openYuanRong DataSystem]]。当前官方文档提供完整的 YuanRong 集成：CPU 数据可经 TCP/RDMA 传输，Ascend NPU tensor 可以通过 HCCS 与远程 H2D/D2H 路径移动。

这条边比“兼容一个存储库”更强：openYuanRong DataSystem 实际承担 TransferQueue 的 storage/data-movement backend，因此把 openYuanRong 直接连到 Ascend RL / post-training 数据流。

## veRL 连接
TransferQueue 已进入 veRL 数据流并支持 streaming dataloader / async training 场景；openYuanRong 也存在作为 veRL 可选分布式框架的 RFC。这里分别记录“已落地 TransferQueue backend”与“框架级 RFC”，不把 RFC 自动视作完全落地。

## 维护者
- [[community/Ascend/TransferQueue/荣程浩 Chenghao Rong|荣程浩（Chenghao Rong）]]：openEuler 2026 openYuanRong Meetup 明确称其为 Transfer Queue 社区 Maintainer，并分享 TransferQueue 基于 openYuanRong 的实践。

## Sources
- https://github.com/Ascend/TransferQueue
- https://github.com/Ascend/TransferQueue/blob/main/docs/storage_backends/openyuanrong_datasystem.md
- https://www.openeuler.org/zh/news/20260728-openYuanrong%20Meetup/20260728-openYuanrong%20Meetup.html
- https://github.com/verl-project/verl/blob/main/docs/data/transfer_queue.md
