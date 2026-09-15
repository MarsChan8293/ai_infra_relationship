---
type: person
name: 秦若愚
english_name: Ruoyu Qin
aliases: ["Ruoyu Qin", "秦若愚"]
current_affiliations: ["Tsinghua University", "MADSys Lab, Tsinghua University", "月之暗面"]
schools:
  - "清华大学"
projects: [Mooncake, Seer]
areas: [llm-serving, kv-cache, distributed-systems, rl-rollout, speculative-decoding]
roles: ["PhD Student", "Research Intern"]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"university/清华大学/Mingxing Zhang","type":["mentor-network","research-collaboration"],"confidence":"high","evidence":["https://qinruoyu.com/","https://qinruoyu.com/static/media/cv-qinruoyu.pdf","https://www.cs.tsinghua.edu.cn/info/1247/6286.htm"]}'
  - '{"target":"university/清华大学/Yingdi Shan","type":["paper-coauthor","research-collaboration"],"project":"Seer","confidence":"high","evidence":["https://www.usenix.org/conference/osdi26/presentation/qin"]}'
---
# 秦若愚（Ruoyu Qin）

清华大学 MADSys 博士生，研究聚焦大规模分布式 LLM deployment、serving 与 RL rollout。个人主页与 CV 明确列出导师为 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]，并自 2023-09 起在 [[company/月之暗面/月之暗面|月之暗面（Moonshot AI）]] Infra Team 担任 Research Intern。

## 教育与经历
- [[university/清华大学/清华大学|清华大学]]：计算机科学与技术本科；后继续攻读博士，导师章明星。
- Moonshot AI Infra Team：2023-09–至今，Research Intern。

## AI Infra 项目
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：FAST 2025 第一作者，连接清华 MADSys 与真实 Kimi production serving workload。
- [[company/月之暗面/Seer|Seer]]：OSDI 2026 第一作者，面向 synchronous LLM RL rollout，通过 divided rollout、context-aware scheduling 与 grouped speculative decoding 降低长尾并提高吞吐。
- Prefill-as-a-Service：与 Weiran He、Yaoyu Wang、Zheming Li、Xinran Xu、Yongwei Wu、Weimin Zheng、Mingxing Zhang 等研究跨数据中心 prefill / KVCache。
- TENT：参与 disaggregated LLM serving 的高性能、韧性 data movement 研究。

## 人物关系
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：博士导师 + Mooncake / Seer 等论文合作者；个人主页和 CV 均有明确导师证据。
- [[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：Seer 共同作者，构成 Moonshot AI 与清华 systems 之间的 RL serving 合作网络。
- Moonshot/Kimi 工程团队：Mooncake、Seer 等项目提供项目级产学合作证据；没有公开细证据时不把秦若愚与每位 Moonshot 工程师自动写成直接同事。

## 图谱意义
秦若愚是章明星 BFS 的一条高密度人物桥：`MADSys → Mooncake → Moonshot AI Infra → Seer / RL rollout`，把存储系统、KV cache、production serving 与 RL inference 串成连续技术链。

## Sources
- https://qinruoyu.com/
- https://qinruoyu.com/static/media/cv-qinruoyu.pdf
- https://www.cs.tsinghua.edu.cn/info/1247/6286.htm
- https://www.usenix.org/conference/osdi26/presentation/qin
