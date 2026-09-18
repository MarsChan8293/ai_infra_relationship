---
type: project
name: InfiniCCL
layer: collective-communication
open_source: true
repository: https://github.com/InfiniTensor/InfiniCCL
areas: [collective-communication, distributed-systems, nccl, hccl, cncl, mpi, heterogeneous-compute]
people:
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
  - "community/InfiniTensor/baominghelly"
  - "community/InfiniTensor/GordonYang1"
last_verified: "2026-09"
---
# InfiniCCL

InfiniCCL 是 [[InfiniCore]] 的统一 collective communication 层，面向多种 accelerator / communication backend 提供一致的分布式通信接口。

## 活跃工程线
- [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（voltjia）]]：2026-09 直接推进 NCCL point-to-point 与 AllGather 等能力。
- [[GordonYang1]]：集中贡献 Send/Recv、AllGather、ReduceScatter、Broadcast、Scatter、Gather、Reduce、AllToAll 等 CCL primitives。
- [[baominghelly]]：补充 Ascend HCCL 与 Cambricon CNCL backend。

这形成九源栈很清晰的一条国产异构通信边：

`InfiniCCL → NCCL / HCCL / CNCL / RCCL / MPI → InfiniLM / InfiniTrain`

## Sources
- https://github.com/InfiniTensor/InfiniCCL
- https://github.com/InfiniTensor/InfiniCCL/pull/58
- https://github.com/InfiniTensor/InfiniCCL/pull/59
- https://github.com/InfiniTensor/InfiniCCL/pull/73
- https://github.com/InfiniTensor/InfiniCCL/pull/72
- https://github.com/InfiniTensor/InfiniCCL/pull/65
