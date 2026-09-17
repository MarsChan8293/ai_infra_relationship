---
type: person
name: 章明星
english_name: Mingxing Zhang
aliases: ["Mingxing Zhang", "章明星"]
current_affiliations: ["Tsinghua University","MADSys Lab, Tsinghua University"]
schools:
  - "清华大学"
projects: [Mooncake, KTransformers, Seer, DualPath]
areas: [storage-systems, distributed-systems, llm-serving, kv-cache, heterogeneous-inference]
roles: ["Associate Professor"]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/趋境科技/武永卫 Yongwei Wu","type":["student","paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://www.ccf.org.cn/Focus/2018-11-12/654739.shtml","https://madsys.cs.tsinghua.edu.cn/publication/"]}'
  - '{"target":"university/清华大学/Ruoyu Qin","type":["mentor-network","research-collaboration"],"confidence":"medium","evidence":["https://www.cs.tsinghua.edu.cn/info/1247/6286.htm"]}'
  - '{"target":"company/深度求索/Shaoyuan Chen","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://sigops.org/s/conferences/sosp/2025/accepted.html","https://conferences.sigcomm.org/sigcomm/2026/accepted/"]}'
  - '{"target":"university/清华大学/Yingdi Shan","type":["paper-coauthor","research-collaboration"],"project":"Seer","confidence":"high","evidence":["https://www.usenix.org/conference/osdi26/presentation/qin"]}'
---
# 章明星（Mingxing Zhang）

清华大学计算机系副教授、MADSys 系统研究 faculty。研究从分布式/存储系统延伸到现代 LLM serving、KV cache infrastructure、异构推理与 RL rollout，是清华 systems 人才进入 AI Infra 的关键枢纽之一。

## 经历
- 2017：[[university/清华大学/清华大学|清华大学]]计算机科学与技术博士。
- 2017–2022：深信服创新研究院，曾任 Chief Algorithm Expert / Head of Sangfor Innovation Institute。
- 2022–至今：回到清华大学计算机系任教；官方 faculty 页面当前列为 Associate Professor。

## 学术谱系
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：**博士导师 + 长期 systems / AI Infra 合作者**。CCF 2018 优秀博士学位论文奖公示明确列出章明星博士论文《大规模图数据的高效计算》的培养单位为清华大学、导师为武永卫。毕业后两人仍持续共同署名 Mooncake、KTransformers 等工作，因此这条边同时具有正式 `student/advisor` 与长期 `research-collaboration` 两层含义。
- 这条关系把当前 AI Infra 人才链清晰串成：`武永卫 → 章明星 → Ruoyu Qin`。其中 [[university/清华大学/Ruoyu Qin|Ruoyu Qin]] 是章明星指导网络中的下一代研究者，不直接标记为武永卫学生。

## AI Infra 关系
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：FAST 2025 论文作者与研究导师网络核心；清华官方报道明确将 [[university/清华大学/Ruoyu Qin|Ruoyu Qin]] 列为其指导学生。
- [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025 论文作者，连接 MADSys 与 CPU/GPU hybrid MoE inference。
- [[company/月之暗面/Seer|Seer]]：OSDI 2026 论文作者，与 Ruoyu Qin、[[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]等共同把 MADSys 技术路线延伸到 synchronous LLM RL rollout 与 speculative decoding。
- [[community/deepseek-ai/DualPath/DualPath|DualPath]]：SIGCOMM 2026 作者；与 [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]、北大 systems / DeepSeek-AI 作者网络合作研究 agentic LLM inference 的 disaggregated KV-cache storage I/O。

## 人才扩散
- [[university/清华大学/Ruoyu Qin|Ruoyu Qin]]：Mooncake 第一作者；清华官方报道支持指导关系，后进一步进入 Moonshot AI Infra / Seer 研究网络。
- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：KTransformers 与 DualPath 共同作者；MADSys 2026 博士 alumni，第一份工作公开列为 DeepSeek，形成 `MADSys → DeepSeek` 的强人才迁移边。
- [[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]：清华 MADSys / 存储系统研究人员，与章明星共同署名 Seer。

## 图谱意义
章明星所在路线把传统 storage / distributed systems 的设计问题直接推入 LLM serving 热路径。沿这一节点 BFS 可以同时进入两条高价值支路：

`武永卫 → 章明星 → Ruoyu Qin → Moonshot AI Infra → Seer`

以及

`武永卫 → 章明星 → KTransformers → Shaoyuan Chen → DeepSeek → DualPath / DeepSpec`。

## 学校关联
- [[university/清华大学/清华大学|清华大学]]：博士与当前任职机构。

## Sources
- https://www.ccf.org.cn/Focus/2018-11-12/654739.shtml
- https://www.cs.tsinghua.edu.cn/csen/info/1301/4666.htm
- https://madsys.cs.tsinghua.edu.cn/
- https://madsys.cs.tsinghua.edu.cn/publication/
- https://www.cs.tsinghua.edu.cn/info/1247/6286.htm
- https://sigops.org/s/conferences/sosp/2025/accepted.html
- https://www.usenix.org/conference/osdi26/presentation/qin
- https://conferences.sigcomm.org/sigcomm/2026/accepted/
