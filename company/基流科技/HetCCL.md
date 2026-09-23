---
type: project
name: HetCCL
linked_people:
  - "company/基流科技/He Liu"
  - "company/基流科技/Mingjun Zhang"
  - "company/基流科技/Yan Zhang"
  - "company/基流科技/Yanmin Jia"
layer: communication
status: unknown
areas:
  - collective-communication
  - heterogeneous-communication
  - mixed-vendor
  - rdma
  - distributed-training
companies: ["基流科技"]
last_verified: "2026-09"
linked_companies:
  - "company/基流科技/基流科技"
---
# HetCCL

HetCCL 是一项面向 mixed-vendor heterogeneous clusters 的集合通信系统研究，目标是在不同厂商 GPU / accelerator 共存的环境中提供高性能 collective communication。

该项目属于跨机构合作，并非基流科技单独拥有。论文作者来自北京大学、北京智源人工智能研究院、中国科学院计算技术研究所与 Infrawaves 等机构。

## 核心设计
- 通过高效 P2P transport 实现跨异构设备数据传输，避免 host-device memory copy 带来的额外开销。
- 对 AllReduce / ReduceScatter 等 combining collectives，引入 border-communicator 机制，在保留厂商原生 collective library reduction 能力的同时实现跨厂商组合。
- 用 hierarchical topology abstraction 把异构集群通信拆成 cluster-level primitives，优化跨 cluster 数据量与带宽利用。

## 基流科技作者网络
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]
- [[company/基流科技/Yan Zhang|Yan Zhang]]
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]]
- [[company/基流科技/He Liu|He Liu]]

这些人物同时与 [[community/sii-research/VCCL/VCCL|VCCL]] 网络发生重叠，构成“同构大规模训练 collective communication → 多厂商异构 collective communication”的连续技术主线。

## 公开结果
论文实现覆盖 4 类不同厂商设备，并报告异构通信带宽相对 Gloo 提升 17–19×，端到端 LLM 训练单步时间最高改善 16.9%。

## Sources
- https://arxiv.org/abs/2605.31000

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/基流科技/He Liu|He Liu]]：HetCCL：Infrawaves 作者，参与多厂商异构 GPU / accelerator collective communication。
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]]：HetCCL：Infrawaves 作者之一，研究 mixed-vendor heterogeneous clusters 的跨硬件集合通信。
- [[company/基流科技/Yan Zhang|Yan Zhang]]：[[company/基流科技/HetCCL|HetCCL]]：参与 mixed-vendor heterogeneous clusters 的跨设备 collective communication。
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]：HetCCL：Infrawaves 作者，面向多厂商异构加速器设计跨设备 collective communication。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/基流科技/基流科技|基流科技（InfraWaves）]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
