---
type: person
name: Zan Zong
current_affiliations: ["Tsinghua University","PACMAN Lab, Tsinghua University"]
schools:
  - "清华大学"
projects: [UltraAttn, FlowPrefill, SmartMoE]
roles: [Postdoc]
areas: [llm-serving, attention, prefill-scheduling, distributed-training, high-performance-computing]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/清程极智/翟季冬 Jidong Zhai","type":["same-lab","paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/author/zan-zong/","https://pacman.cs.tsinghua.edu.cn/~zjd/"]}'
---
# Zan Zong

PACMAN 人物页记录其研究从 distributed DNN / HPC 延伸到 LLM attention 与 serving scheduling。

## AI Infra / 项目贡献
- **UltraAttn**：SC 2025，Zan Zong 为论文作者；系统通过 hierarchical context-tiling 做 attention parallelization。
- **FlowPrefill**：PACMAN 作者页将其列为 Zan Zong 的最新研究之一，针对 LLM serving 中 preemption 与 prefill scheduling granularity 解耦，以缓解 head-of-line blocking。
- **SmartMoE**：PACMAN 作者页明确列入其成果，属于其较早的稀疏 MoE / distributed training 路线。
- 此外还参与 heterogeneous / geo-distributed large-model training 与 pipeline parallelism 等研究。

这条轨迹把 PACMAN 的 distributed training / MoE 研究进一步连到 attention parallelism 与 serving prefill scheduling，形成一条清晰的训练系统 → 推理热路径人才支线。

## 学校关联
- [[university/清华大学/清华大学|清华大学]]：已有教育、任职或研究关联；具体阶段以一手页面为准。

## 后续核验
PACMAN 当前 people 页面另有 alumni / first-job 信号，可能意味着现有 `current_affiliations` / `roles` 已出现时间漂移。该问题不在本次 `project_contribution` DISCOVER action 内直接改写，留给 VERIFY 对 current affiliation 做单独核验，避免把项目发现顺手升级成职业状态判断。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/author/zan-zong/
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-confsc-yang-z-0-lhyz-25/
