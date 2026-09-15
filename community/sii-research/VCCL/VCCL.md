---
type: project
name: VCCL
full_name: Venus Collective Communication Library
linked_people:
  - "company/基流科技/He Liu"
  - "company/基流科技/Mingjun Zhang"
  - "company/基流科技/Wenqi Xie"
  - "company/基流科技/Yanmin Jia"
companies: ["基流科技"]
company_relation: industry-research-co-development
layer: collective-communication
open_source: true
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/基流科技/He Liu|He Liu]]：VCCL：Infrawaves 作者，参与大规模训练集群的 collective communication、fault tolerance 与 observability 研究。
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]]：[[南京大学]]：其 GitHub 个人主页直接标注 Nanjing University；该 GitHub 身份同时固定展示 VCCL、SGLang、Mooncake、vLLM、DeepEP 等 AI infra 项目，可与本人物节点稳定对应。
- [[company/基流科技/Wenqi Xie|Wenqi Xie]]：VCCL：论文作者，系统覆盖 fault tolerance、observability、high-performance collective communication。
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]：VCCL：Infrawaves 作者，参与大规模 GPU 训练集群集合通信的可靠性、性能和可观测性研究。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/基流科技/基流科技|基流科技（InfraWaves）]]：公司页与社区/项目页均有显式记录；关系：`industry-research-co-development`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
