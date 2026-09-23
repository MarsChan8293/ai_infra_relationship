---
type: project
name: Expert-as-a-Service
linked_people:
  - "company/基流科技/He Liu"
  - "company/基流科技/Mingjun Zhang"
  - "company/基流科技/Yan Zhang"
  - "company/基流科技/Yanmin Jia"
  - "company/基流科技/胡效赫 Xiaohe Hu"
layer: distributed-serving
status: unknown
areas:
  - moe-serving
  - expert-disaggregation
  - elastic-serving
  - fault-tolerance
  - p2p-communication
companies: ["基流科技"]
last_verified: "2026-09"
linked_companies:
  - "company/基流科技/基流科技"
---
# Expert-as-a-Service（EaaS）

Expert-as-a-Service（EaaS）是一项面向大规模 Mixture-of-Experts（MoE）模型推理的分布式 serving 系统研究。它不是基流科技单独拥有的产品，而是由多家机构共同完成的跨组织系统工作；基流科技 / Infrawaves 有多名作者参与，因此在本图谱中作为公司通向 inference serving 的强项目边。

## 核心设计
- 将 MoE expert 模块解耦为独立、无状态的服务单元，降低传统单体 serving 架构中 expert 资源绑定带来的弹性与容错问题。
- 通过细粒度 expert 级资源伸缩，使资源分配能够随 serving traffic 动态变化。
- 使用高性能、CPU-free 的 P2P 通信路径降低 expert 间数据移动开销。
- 通过服务解耦获得更强的故障隔离与容错能力。

## 基流科技作者网络
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]]
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]
- [[company/基流科技/Yan Zhang|Yan Zhang]]
- [[company/基流科技/He Liu|He Liu]]
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]]

这五名 Infrawaves 作者把公司原有的高性能网络 / collective communication 能力直接接到了 MoE serving 系统层。相较只从 GitHub pinned repository 推测上层关联，这条边由论文共同署名与机构 affiliation 直接支撑。

## 图谱意义
EaaS 形成一条清晰的技术路径：

[[community/sii-research/VCCL/VCCL|VCCL]] / [[company/基流科技/HetCCL|HetCCL]]
→ 高性能 GPU / heterogeneous communication
→ EaaS 的 CPU-free P2P 数据路径
→ MoE expert disaggregation
→ elastic / fault-tolerant serving

因此，基流科技不应只被建模为“AI 集群网络公司”，还应被视为与大规模 MoE inference infrastructure 有直接研究交集的节点。

## 公开结果
论文报告：在模拟硬件故障下，EaaS 的吞吐下降低于 2%；通过按 serving traffic 动态适配 expert 资源，最多节省 37.5% 的计算资源。SC26 官方日程当前也已列出该工作。

## Sources
- https://arxiv.org/abs/2509.17863
- https://sc26.conference-program.com/presentation/?id=pap132&sess=sess235

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/基流科技/He Liu|He Liu]]：项目关联；人物页已明确记录该项目。
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]]：项目关联；人物页已明确记录该项目。
- [[company/基流科技/Yan Zhang|Yan Zhang]]：[[company/基流科技/Expert-as-a-Service|Expert-as-a-Service（EaaS）]]：参与大规模 MoE serving，系统采用 expert disaggregation、细粒度弹性与 CPU-free P2P communication。
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]：项目关联；人物页已明确记录该项目。
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]]：[[company/基流科技/Expert-as-a-Service|Expert-as-a-Service（EaaS）]]：与 Yanmin Jia、Yan Zhang、He Liu、Mingjun Zhang 等共同参与大规模 MoE serving 系统研究，将公司网络系统能力直接接入 expert disaggregation、elastic serving 与 fault tolerance。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/基流科技/基流科技|基流科技（InfraWaves）]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
