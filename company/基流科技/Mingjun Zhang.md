---
type: person
name: Mingjun Zhang
aliases: [Mingjun Zhang]
current_affiliations: ["基流科技"]
schools:
  - "南京大学"
communities: [VCCL]
linked_companies:
  - "company/基流科技/基流科技"
projects: [VCCL, HetCCL, Expert-as-a-Service]
education: [南京大学]
roles: [AI Infra Engineer]
areas: [collective-communication, gpu-networking, distributed-training, moe-serving, distributed-serving]
last_verified: "2026-09"
relations:
  - '{"target":"company/基流科技/胡效赫 Xiaohe Hu","type":["paper-coauthor","coworker"],"confidence":"high","evidence":["https://github.com/Zhangmj0621","https://arxiv.org/abs/2510.00991","https://github.com/sii-research/VCCL","https://arxiv.org/abs/2509.17863"]}'
  - '{"target":"company/基流科技/Yanmin Jia","type":["paper-coauthor","coworker"],"confidence":"high","evidence":["https://github.com/Zhangmj0621","https://arxiv.org/abs/2510.00991","https://github.com/sii-research/VCCL","https://arxiv.org/abs/2605.31000","https://arxiv.org/abs/2509.17863"]}'
  - '{"target":"company/基流科技/He Liu","type":["paper-coauthor","coworker"],"confidence":"high","evidence":["https://github.com/Zhangmj0621","https://arxiv.org/abs/2510.00991","https://github.com/sii-research/VCCL","https://arxiv.org/abs/2605.31000","https://arxiv.org/abs/2509.17863"]}'
  - '{"target":"company/基流科技/Wenqi Xie","type":["paper-coauthor","coworker"],"confidence":"high","evidence":["https://github.com/Zhangmj0621","https://arxiv.org/abs/2510.00991","https://github.com/sii-research/VCCL"]}'
  - '{"target":"company/基流科技/Yan Zhang","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://arxiv.org/abs/2510.00991","https://arxiv.org/abs/2605.31000","https://arxiv.org/abs/2509.17863"]}'
---
# Mingjun Zhang

[[基流科技]] / Infrawaves AI infrastructure 工程节点，横跨 [[VCCL]]、[[company/基流科技/HetCCL|HetCCL]] 与 [[company/基流科技/Expert-as-a-Service|EaaS]]。

## 教育与技术经历
- [[南京大学]]：其 GitHub 个人主页直接标注 Nanjing University；该 GitHub 身份同时固定展示 VCCL、SGLang、Mooncake、vLLM、DeepEP 等 AI infra 项目。
- VCCL：论文第一作者；研究高效、高可靠、可观测 collective communication，并在生产训练集群部署。
- HetCCL：Infrawaves 作者之一，研究 mixed-vendor heterogeneous clusters 的跨硬件集合通信。
- EaaS：Infrawaves 作者之一，参与将高性能 P2P communication 延伸到大规模 MoE expert disaggregation / elastic serving。
- 公开 GitHub profile 重点关注 AI infra，并将 SGLang、VCCL、Mooncake、vLLM、DeepEP 相关项目列为 pinned repositories。

## 人物关系
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]]：**Infrawaves 同事 + VCCL / EaaS 论文合作者**。
- [[company/基流科技/Yanmin Jia|Yanmin Jia]]：**VCCL / HetCCL / EaaS 连续合作者**。
- [[company/基流科技/He Liu|He Liu]]：**VCCL / HetCCL / EaaS 连续合作者**。
- [[company/基流科技/Yan Zhang|Yan Zhang]]：**VCCL / HetCCL / EaaS 连续合作者**，共同把 communication 主线延伸到 MoE serving。
- [[company/基流科技/Wenqi Xie|Wenqi Xie]]：**Infrawaves 同事 + VCCL 论文合作者**。

## 图谱意义
Mingjun 原本只是“VCCL / collective communication”节点；EaaS 使他的公开轨迹首次出现明确的 serving 系统强边。因此后续 BFS 应优先从 EaaS 的跨机构作者与 communication runtime 继续，而不是仅从 pinned repositories 猜测 SGLang / vLLM 直接合作。

## Sources
- https://github.com/Zhangmj0621
- https://arxiv.org/abs/2510.00991
- https://arxiv.org/abs/2605.31000
- https://arxiv.org/abs/2509.17863
- https://github.com/sii-research/VCCL

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/基流科技/基流科技|基流科技（InfraWaves）]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
