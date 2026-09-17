---
type: person
name: 何家傲
english_name: Jiaao He
aliases: ["Jiaao He", "Rick Ho", "laekov", "何家傲"]
current_affiliations: ["ByteDance"]
schools:
  - "清华大学"
linked_companies:
  - "company/字节跳动/字节跳动"
projects: [FastDecode, FastMoE, GLM-130B]
areas: [llm-serving, distributed-training, moe, heterogeneous-inference, sparse-systems]
roles: [Research Scientist]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/清程极智/翟季冬 Jidong Zhai","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://laekov.com.cn/cv/","https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-journalscorrabs-2403-11421/"]}'
---
# 何家傲（Jiaao He）

当前：[[company/字节跳动/字节跳动|字节跳动]] Research Scientist on Infrastructure，2025-03–至今。

## 教育与研究经历
- [[清华大学]]：本科 2020、计算机博士 2025。
- PACMAN Lab：2017–2025；个人 CV 明确列出 Advisor: [[company/清程极智/翟季冬 Jidong Zhai|Jidong Zhai]]。
- 曾任清华 Student Cluster Competition Team 队长。

## AI Infra 关系
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：**博士导师 + 系统论文长期合作者**。合作覆盖 [[community/thu-pacman/FastMoE/FastMoE|FastMoE]] / FasterMoE / SmartMoE 与 [[university/清华大学/FastDecode|FastDecode]]。
- [[university/清华大学/FastDecode|FastDecode]]：面向 LLM serving 的 CPU/GPU heterogeneous pipeline，针对 KV cache 占用导致 GPU batch size 受限的问题，把 memory-bound attention/KV-cache 路径下沉到多节点 CPU 侧。
- [[community/thu-pacman/FastMoE/FastMoE|FastMoE]] / FasterMoE / SmartMoE：形成从 MoE distributed training 到现代 LLM systems 的连续研究轨迹。
- [[university/清华大学/GLM-130B|GLM-130B]]：官方项目页把何家傲列入 PACMAN contributors，连接 MoE / distributed training 与 100B 级模型训练系统协作。

## 图谱意义
何家傲是 PACMAN 从超算/HPC、MoE distributed training 向 LLM inference serving 迁移的关键人物，并在博士毕业后直接进入字节基础设施研究网络。

## Sources
- https://laekov.com.cn/cv/
- https://pacman.cs.tsinghua.edu.cn/~zjd/people/
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/fastmoe/
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/fastermoe/
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-journalscorrabs-2403-11421/
- https://keg.cs.tsinghua.edu.cn/glm-130b/zh/posts/glm-130b/

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/字节跳动/字节跳动|字节跳动]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
