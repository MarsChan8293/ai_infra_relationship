---
type: project
name: InfiniCCL
linked_people:
  - "community/InfiniTensor/baominghelly"
  - "community/InfiniTensor/GordonYang1"
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
layer: collective-communication
open_source: true
repository: https://github.com/InfiniTensor/InfiniCCL
areas: [collective-communication, distributed-systems, nccl, hccl, cncl, mpi, heterogeneous-compute]
people:
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
  - "community/InfiniTensor/baominghelly"
  - "community/InfiniTensor/GordonYang1"
last_verified: "2026-09"
linked_companies: []
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/InfiniTensor/baominghelly|baominghelly]]：[[InfiniCCL]]：Ascend HCCL backend、Cambricon CNCL backend。
- [[community/InfiniTensor/GordonYang1|GordonYang1]]：[[InfiniCCL]]：Send/Recv、AllGather、ReduceScatter、Broadcast、Scatter、Gather、Reduce、AllToAll 等多项 collective / P2P primitive。
- [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（Jiacheng Huang）]]：与 [[university/启元实验室/王豪杰 Haojie Wang|王豪杰]]、[[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]]、[[university/启元实验室/李映辉 Yinghui Li|李映辉]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫]] 共同署名《面向国产智能芯片的统一智能计算架构》。\n- GitHub `voltjia` 的直接工程轨迹横跨 [[community/InfiniTens...

<!-- END AUTO PROJECT PEOPLE -->
