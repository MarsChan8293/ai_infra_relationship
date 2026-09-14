---
type: project
name: VCCL
full_name: Venus Collective Communication Library
layer: collective-communication
open_source: true
---
# VCCL

Venus Collective Communication Library，面向大规模 GPU 训练集群的集合通信库，由 Shanghai Innovation Institute（SII）与 [[基流科技]] / Infrawaves 支持。

## 技术方向
- AllReduce / AllGather / Reduce / Broadcast / ReduceScatter / Send-Recv
- PCIe、NVLink / NVSwitch、InfiniBand Verbs 与 TCP/IP
- topology-aware scheduling、fault tolerance、flow telemetry
- 面向大规模训练的高可用与可观测 collective communication

## 核心人物网络
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]] — VCCL / collective communication 论文第一作者；AI infra 工程网络
- [[company/基流科技/Yanmin Jia|Yanmin Jia]] — Infrawaves collective communication；同时参与 HetCCL
- [[company/基流科技/He Liu|He Liu]] — Infrawaves collective communication；VCCL / HetCCL 网络
- [[company/基流科技/Wenqi Xie|Wenqi Xie]] — Infrawaves 技术团队 / 公司 executive director；VCCL 论文作者
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]] — 基流创始人 / CEO；VCCL 论文共同作者

## 生态连接
Mingjun Zhang 的公开 GitHub 同时活跃/关注 [[SGLang]]、[[Mooncake]]、[[vLLM]]、DeepEP 等项目，因此 VCCL 是“集群网络 / collective communication → LLM serving / expert parallel / KV cache”之间的重要底层桥。仅凭 GitHub pinned repo 不写人物直接合作，具体边仍按 PR / 论文逐条确认。

## Sources
- https://github.com/sii-research/VCCL
- https://vccl-doc.readthedocs.io/en/latest/
- https://arxiv.org/abs/2510.00991
