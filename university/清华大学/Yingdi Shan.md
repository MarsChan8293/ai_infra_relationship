---
type: person
name: 闪英迪
english_name: Yingdi Shan
aliases: ["Yingdi Shan", "闪英迪"]
current_affiliations: ["Tsinghua University","MADSys Lab, Tsinghua University"]
schools:
  - "清华大学"
projects: [Seer]
areas: [distributed-systems, storage-systems, operating-systems, llm-serving]
roles: ["Assistant Researcher"]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/趋境科技/武永卫 Yongwei Wu","type":["same-lab","paper-coauthor","research-collaboration"],"project":"Seer","confidence":"high","evidence":["https://madsys.cs.tsinghua.edu.cn/","https://www.usenix.org/conference/osdi26/presentation/qin"]}'
  - '{"target":"university/清华大学/Mingxing Zhang","type":["paper-coauthor","research-collaboration"],"project":"Seer","confidence":"high","evidence":["https://www.usenix.org/conference/osdi26/presentation/qin"]}'
---
# 闪英迪（Yingdi Shan）

清华大学计算机系高性能计算研究所助理研究员、MADSys 研究人员，研究重点为分布式系统、存储系统与操作系统。2024 年加入清华大学计算机系，此前在中关村实验室从事操作系统内核相关研究。

## 教育与研究经历
- 2015：大连理工大学软件工程学士。
- 2022：[[university/清华大学/清华大学|清华大学]]计算机科学与技术博士。
- 2022–2024：中关村实验室助理研究员。
- 2024–至今：清华大学计算机系高性能计算研究所助理研究员；MADSys 个人主页将其列为 Research Assistant Professor。

## AI Infra 关系
- [[company/月之暗面/Seer|Seer]]：OSDI 2026 论文作者，与 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]、[[university/清华大学/Ruoyu Qin|Ruoyu Qin]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]共同参与 synchronous LLM RL rollout 系统研究。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：**MADSys 同实验室 / faculty 网络 + Seer 研究合作**。两人当前同处清华 MADSys systems 网络，并共同署名 Seer；这条边反映从传统 storage / distributed systems 向 RL serving 的研究延伸，不据此推断博士导师关系。
- 其传统研究主线是 storage / distributed systems，因此 Seer 构成从经典系统研究进入现代 LLM serving / RL infra 的明确连接点。

## 图谱意义
闪英迪提供了武永卫 / 章明星网络中另一条不同于 Mooncake/KTransformers 的系统人才支路：`storage & OS → RL rollout scheduling / speculative decoding`。

## Sources
- https://www.cs.tsinghua.edu.cn/info/1257/6372.htm
- https://madsys.cs.tsinghua.edu.cn/~yingdi-shan/
- https://madsys.cs.tsinghua.edu.cn/
- https://www.usenix.org/conference/osdi26/presentation/qin
