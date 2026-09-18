---
type: research-institution
name: IPADS
organization: 上海交通大学
aliases: ["Institute of Parallel and Distributed Systems", "上海交通大学并行与分布式系统研究所"]
linked_people:
  - "university/上海交通大学/Rong Chen"
areas: [operating-systems, distributed-systems, ai-infrastructure, llm-serving, resource-management, gpu-systems, kv-cache]
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

IPADS（Institute of Parallel and Distributed Systems，并行与分布式系统研究所）是上海交通大学的系统研究机构。其官方 research statement 覆盖操作系统、分布式系统、数据库、体系结构、编译与人工智能的交叉系统研究，并形成了越来越密集的 AI Infra / LLM serving 研究线。

## AI Infra 主线
IPADS 的优势是从 OS、cluster、resource management 与 heterogeneous hardware 出发切入 AI infrastructure，而不是围绕单一 inference engine 展开。

核心人物包括：
- [[university/上海交通大学/Haibo Chen|Haibo Chen]]
- [[university/上海交通大学/Rong Chen|Rong Chen]]
- [[university/上海交通大学/Xingda Wei|Xingda Wei]]
- [[university/上海交通大学/Rongxin Cheng|Rongxin Cheng]]

## 代表项目 / 工作
- [[university/上海交通大学/KunServe|KunServe]]：面向 LLM serving 内存过载的 parameter-centric memory management。
- **PowerInfer**：SOSP 2024，本地 consumer-GPU LLM inference，采用 locality-aware CPU-GPU hybrid execution。
- **BlitzScale**：OSDI 2025，面向大模型 serving 的快速 live autoscaling。
- **KVCache Cache in the Wild**：ATC 2025，从大型云环境刻画并优化 KV cache。
- 相关研究网络还包括 PhoenixOS、XSched、PipeLLM、AITurbo 等系统方向；是否独立建项目节点由后续 EXPAND / DISCOVER 决定。

## Sources
- https://ipads.sjtu.edu.cn/
- https://ipads.sjtu.edu.cn/pub/members/haibo_chen
- https://ipads.se.sjtu.edu.cn/_media/publications/song-sosp24.pdf
- https://www.cs.sjtu.edu.cn/en/jiaoshiml/chenrong.html
- https://www.cs.sjtu.edu.cn/en/jiaoshiml/weixingda.html

<!-- BEGIN AUTO RESEARCH PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `current_affiliations:` 反向汇总，仅表示当前公开的研究机构 affiliation，不自动推断同组、导师、直属汇报或共同项目关系。

- [[university/上海交通大学/Rong Chen|Rong Chen]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。

<!-- END AUTO RESEARCH PEOPLE -->
