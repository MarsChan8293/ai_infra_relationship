---
type: project
name: VCCL
full_name: Venus Collective Communication Library
linked_concepts:
  - "concept/communication/collectives/AllGather"
  - "concept/communication/collectives/AllReduce"
  - "concept/communication/collectives/Collective Communication"
  - "concept/hardware/interconnect/Hardware Interconnect"
  - "concept/hardware/interconnect/NVLink"
  - "concept/hardware/interconnect/NVSwitch"
  - "concept/hardware/interconnect/PCIe"
  - "concept/communication/collectives/ReduceScatter"
status: active
linked_people:
  - "company/基流科技/He Liu"
  - "company/基流科技/Mingjun Zhang"
  - "company/基流科技/Wenqi Xie"
  - "company/基流科技/Yan Zhang"
  - "company/基流科技/Yanmin Jia"
  - "company/基流科技/胡效赫 Xiaohe Hu"
repository: https://github.com/sii-research/vccl
last_verified: "2026-09"
companies: ["基流科技"]
company_relation: industry-research-co-development
layer: communication
areas:
  - "collective-communication"
  - "accelerator-communication"
integrations: []
linked_companies:
  - "company/基流科技/基流科技"
---
# VCCL

Venus Collective Communication Library，面向大规模 GPU 训练集群的集合通信库，由 Shanghai Innovation Institute（SII）与 [[基流科技]] / Infrawaves 支持。

## 主要贡献公司
- [[company/基流科技/基流科技|基流科技 / InfraWaves]]：VCCL 的主要产业支持与作者网络来源；SII 是共同研究支持机构，因此不放入 `companies` 公司字段。

## 技术方向
- AllReduce / AllGather / Reduce / Broadcast / ReduceScatter / Send-Recv
- PCIe、NVLink / NVSwitch、InfiniBand Verbs 与 TCP/IP
- topology-aware scheduling、fault tolerance、flow telemetry
- 面向大规模训练的高可用与可观测 collective communication

## 核心人物网络
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]] — VCCL / collective communication 论文第一作者；后续继续进入 HetCCL / EaaS
- [[company/基流科技/Yanmin Jia|Yanmin Jia]] — Infrawaves collective communication；同时参与 HetCCL / EaaS
- [[company/基流科技/He Liu|He Liu]] — Infrawaves collective communication；VCCL / HetCCL / EaaS
- [[company/基流科技/Yan Zhang|Yan Zhang]] — VCCL 作者；后续连续参与 HetCCL / EaaS，是 communication → MoE serving 的桥人物
- [[company/基流科技/Wenqi Xie|Wenqi Xie]] — Infrawaves 公司管理 / 技术网络；VCCL 论文作者
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]] — 基流创始人 / CEO；VCCL 论文共同作者

## 生态连接
本轮补全后，VCCL 到 serving 的最强连接不再依赖 Mingjun Zhang 的 GitHub pinned repos，而是 [[company/基流科技/Expert-as-a-Service|EaaS]] 的论文强证据：胡效赫、Yanmin Jia、Yan Zhang、He Liu、Mingjun Zhang 同时出现在 MoE serving 系统作者网络中。

因此当前可建立：
VCCL → Infrawaves communication team → EaaS → MoE serving
的直接研究链路。

Mingjun Zhang 的公开 GitHub 同时关注 SGLang、Mooncake、vLLM、DeepEP 等项目，但仅凭 pinned repo 仍不写人物直接合作，具体边继续按 PR / 论文逐条确认。

## Sources
- https://github.com/sii-research/VCCL
- https://vccl-doc.readthedocs.io/en/latest/
- https://arxiv.org/abs/2510.00991
- https://arxiv.org/abs/2509.17863

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/基流科技/He Liu|He Liu]]：VCCL：Infrawaves 作者，参与大规模训练集群的 collective communication、fault tolerance 与 observability 研究。
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]]：[[南京大学]]：其 GitHub 个人主页直接标注 Nanjing University；该 GitHub 身份同时固定展示 VCCL、SGLang、Mooncake、vLLM、DeepEP 等 AI infra 项目。
- [[company/基流科技/Wenqi Xie|Wenqi Xie]]：VCCL：论文作者，系统覆盖 fault tolerance、observability、high-performance collective communication。
- [[company/基流科技/Yan Zhang|Yan Zhang]]：[[community/sii-research/VCCL/VCCL|VCCL]]：参与生产级大规模 GPU 集群 collective communication 系统研究。
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]：VCCL：Infrawaves 作者，参与大规模 GPU 训练集群集合通信的可靠性、性能和可观测性研究。
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]]：[[community/sii-research/VCCL/VCCL|VCCL]]：大规模 GPU 训练集群 collective communication 系统论文共同作者。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/基流科技/基流科技|基流科技（InfraWaves）]]：公司页与社区/项目页均有显式记录；关系：`industry-research-co-development`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/collectives/AllGather|AllGather]]
- [[concept/communication/collectives/AllReduce|AllReduce]]
- [[concept/communication/collectives/Collective Communication|Collective Communication]]
- [[concept/hardware/interconnect/Hardware Interconnect|Hardware Interconnect]]
- [[concept/hardware/interconnect/NVLink|NVLink]]
- [[concept/hardware/interconnect/NVSwitch|NVSwitch]]
- [[concept/hardware/interconnect/PCIe|PCIe]]
- [[concept/communication/collectives/ReduceScatter|ReduceScatter]]

<!-- END AUTO PROJECT CONCEPTS -->
