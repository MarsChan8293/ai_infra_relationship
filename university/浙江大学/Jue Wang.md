---
type: person
name: Jue Wang
aliases: [Jue Wang]
current_affiliations: ["浙江大学","Together AI"]
schools:
  - "浙江大学"
linked_companies:
  - "company/Together AI/Together AI"
projects:
  - HMI
  - FloE
  - Ladder Residual
areas: [llm-inference, tensor-parallelism, moe-inference, multi-tenant-serving]
last_verified: "2026-09"
relations:
  - '{"target":"university/浙江大学/Lidan Shou","type":["mentor-network"],"confidence":"medium","evidence":["https://juewang.me/about/","https://juewang.me/","https://arxiv.org/abs/2504.17449"]}'
  - '{"target":"university/浙江大学/Huan Li","type":["research-collaboration"],"confidence":"medium","evidence":["https://juewang.me/about/","https://juewang.me/","https://arxiv.org/abs/2504.17449"]}'
  - '{"target":"university/浙江大学/Zheng Li","type":["paper-coauthor"],"confidence":"high","evidence":["https://juewang.me/about/","https://juewang.me/","https://arxiv.org/abs/2504.17449"]}'
---
# Jue Wang

浙江大学校友，2014–2018 年在浙大完成本科，2018–2023 年在浙江大学计算机系攻读博士，导师为 [[Lidan Shou]]。个人主页显示当前为 [[Together AI]] Principal Research Scientist，研究集中于高效、低成本 LLM algorithms and systems。

## Inference systems 研究
- [[university/浙江大学/HMI|HMI]]：与 [[Huan Li]]、[[Lidan Shou]] 等合作，研究 multi-tenant pretrained-model inference 的内存与资源复用。
- [[university/浙江大学/FloE|FloE]]：ICML 2025，参与显存受限 GPU 上的 MoE inference 系统研究，连接 expert compression / parameter movement 与系统优化。
- [[company/Together AI/Ladder Residual|Ladder Residual]]：ICML 2025，通过重新设计 residual path 让 Tensor Parallel communication 与计算重叠，加速 distributed inference。
- 此外个人主页还列出 SonicSampler、Kitty、Self-Spec 等 inference 方向工作。

## 人物关系
- [[Lidan Shou]]：博士导师；之后仍在 HMI、FloE 等论文网络中持续合作。
- [[Huan Li]]：浙江大学研究网络与 HMI 合作者。
- [[Zheng Li]]：FloE 共同作者。
- [[Together AI]]：当前产业研究节点，将浙大 systems 学术网络连接到生产级大模型训练 / 推理公司。

## 图谱意义
Jue Wang 是浙江大学 AI Infra 网络里很典型的 **“校内 systems training → 国际 AI infra 公司”** 人才流动节点。相比纯模型研究，其公开工作更靠近 parallelism、resource sharing、memory/data movement 与 inference architecture。

## 学校关联
- [[university/浙江大学/浙江大学|浙江大学]]：本科、博士与长期研究网络。

## Sources
- https://juewang.me/about/
- https://juewang.me/
- https://arxiv.org/abs/2504.17449
- https://proceedings.mlr.press/v267/zhou25j.html
- https://proceedings.mlr.press/v267/zhang25bg.html

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/Together AI/Together AI|Together AI]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
