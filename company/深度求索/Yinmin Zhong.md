---
type: person
name: Yinmin Zhong
current_affiliations: ["Peking University", "深度求索"]
schools:
  - "北京大学"
public_email: zhongyinmin@pku.edu.cn
projects: [DistServe, LoongServe]
areas: [llm-serving, rl-infra, distributed-systems, disaggregated-serving, training-systems]
roles: [PhD Candidate, Core System R&D Engineer]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu","type":["coworker","paper-coauthor","research-collaboration"],"confidence":"high","start":"2025-04","evidence":["https://www.yinminzhong.com/","https://interestinglsy.github.io/","https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin","https://arxiv.org/abs/2404.09526"]}'
  - '{"target":"university/北京大学/Xin Jin","type":["advisor","research-collaboration"],"confidence":"high","evidence":["https://www.yinminzhong.com/","https://xinjin.github.io/publications.html"]}'
---
# Yinmin Zhong

北京大学计算机学院博士生，同时自 2025-04 起在 DeepSeek RL Infra Team 担任 Core System R&D Engineer。研究长期聚焦高效训练与 serving 系统。

## 与刘胜与的关系
- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：DistServe、LoongServe、FastServe、RLHFuse 等多项北大 LLM systems 工作的长期共同作者。
- 两人的个人主页均明确显示 **2025-04 起在 DeepSeek**，因此可以建立有时间锚点的 coworker 边，而不仅是论文合作。
- 技术分工形成有价值的互补：刘胜与在 DeepSeek 进一步下沉到 attention / GEMM / TopK kernel，Yinmin Zhong 当前公开角色则明确在 RL Infra / distributed training-serving 系统侧。

## 项目
- [[community/LLMServe/DistServe/DistServe|DistServe]]：论文前两位作者为 Yinmin Zhong、Shengyu Liu。
- [[community/LoongServe/LoongServe/LoongServe|LoongServe]]：共同作者，长上下文 serving。
- RLHFuse：NSDI 2025，stage fusion 优化 RLHF training。
- DualPath：2026 DeepSeek-AI / PKU / Tsinghua 跨机构 inference network 的作者之一。

## Sources
- https://www.yinminzhong.com/
- https://www.yinminzhong.com/publications
- https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin
- https://arxiv.org/abs/2404.09526
