---
type: person
name: Shu Liu
aliases: ["Shu Liu", "Shu Lynn Liu"]
current_affiliations: ["UC Berkeley","Sky Computing Lab"]
schools:
  - "UC Berkeley"
projects: [Jenga, MoE-Lightning]
areas: [llm-systems, moe-inference, ai-systems, distributed-systems, agent-systems]
roles: [PhD Student]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/Inferact/Ion Stoica","type":["advisor","paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://shulynnliu.com/","https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/31876.html"]}'
  - '{"target":"university/UC Berkeley/Shiyi Cao","type":["paper-coauthor","research-collaboration"],"project":"MoE-Lightning","confidence":"high","evidence":["https://doi.org/10.1145/3669940.3707267","https://sky.cs.berkeley.edu/publications/"]}'
---
# Shu Liu

UC Berkeley CS 博士生、[[university/UC Berkeley/Sky Computing Lab|Sky Computing Lab]] 成员，个人主页明确列出导师为 [[company/Inferact/Ion Stoica|Ion Stoica]]。研究从 LLM systems / distributed systems 延伸到 self-improving agents 与 AI-driven systems research。

## AI Infra 关系
- [[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025 作者，参与异构 LLM serving memory management 研究。
- [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]]：ASPLOS 2025 作者，与 [[university/UC Berkeley/Shiyi Cao|Shiyi Cao]] 等共同研究 memory-constrained GPU 上的高吞吐 MoE inference。
- LLM query optimization：2025 Berkeley report 与 Ion Stoica、Joseph Gonzalez、Matei Zaharia 等共同研究 relational data analytics 中昂贵 LLM inference 的优化。
- ADRS / SkyDiscover：进一步把 AI 用作 systems optimization / discovery 工具，研究系统开始从“为 AI 做基础设施”反向走向“让 AI 发现系统优化”。

## 图谱意义
Shu Liu 是 `Jenga → MoE inference → AI-driven systems / agents` 的桥节点，也体现 Ion Stoica / Sky 最新一代研究方向的变化。

## 学校关联
- [[university/UC Berkeley/UC Berkeley|UC Berkeley]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://shulynnliu.com/
- https://arxiv.org/abs/2503.18292
- https://doi.org/10.1145/3669940.3707267
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/31876.html
- https://sky.cs.berkeley.edu/project/adrs/
- https://sky.cs.berkeley.edu/people/
