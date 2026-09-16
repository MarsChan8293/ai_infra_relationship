---
type: research-institution
name: IPADS
organization: 上海交通大学
aliases: ["Institute of Parallel and Distributed Systems", "上海交通大学并行与分布式系统研究所"]
areas: [operating-systems, distributed-systems, ai-infrastructure, llm-serving, resource-management, gpu-systems]
people:
  - "university/上海交通大学/Haibo Chen"
  - "university/上海交通大学/Rong Chen"
  - "university/上海交通大学/Xingda Wei"
  - "university/上海交通大学/Rongxin Cheng"
projects:
  - KunServe
website: https://ipads.sjtu.edu.cn/
country: China
city: Shanghai
last_verified: "2026-09"
---
# IPADS

IPADS（Institute of Parallel and Distributed Systems，并行与分布式系统研究所）是上海交通大学的系统研究机构。其官方 research statement 覆盖操作系统、分布式系统、数据库、体系结构、编译与人工智能的交叉系统研究，并公开列出 PowerInfer 等开源系统。

## AI Infra 主线
近年来 IPADS 的一条明确主线是从传统 OS / distributed systems 延伸到 AI training、LLM serving、GPU resource management 与 KV cache / memory management。

核心人物包括：
- [[university/上海交通大学/Haibo Chen|Haibo Chen]]
- [[university/上海交通大学/Rong Chen|Rong Chen]]
- [[university/上海交通大学/Xingda Wei|Xingda Wei]]
- [[university/上海交通大学/Rongxin Cheng|Rongxin Cheng]]

## 代表项目
- [[university/上海交通大学/KunServe|KunServe]]：面向 LLM serving 内存过载的 parameter-centric memory management。
- 相关研究网络还覆盖 BlitzScale、PhoenixOS、XSched、KV cache study、AITurbo 等系统方向；这些线索后续由 planner 按独立 action 再决定是否建节点。

## Sources
- https://ipads.sjtu.edu.cn/
- https://www.cs.sjtu.edu.cn/en/jiaoshiml/chenrong.html
- https://www.cs.sjtu.edu.cn/en/jiaoshiml/weixingda.html
