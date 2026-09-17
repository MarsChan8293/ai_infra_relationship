---
type: person
name: 陈康
english_name: Kang Chen
aliases: ["Kang Chen", "陈康"]
current_affiliations: ["Peking University"]
schools:
  - "清华大学"
  - "北京大学"
areas: [distributed-systems, storage-systems, rdma, disaggregated-memory, graph-systems, systems-software]
roles: [Professor]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/趋境科技/武永卫 Yongwei Wu","type":["same-lab","research-collaboration","paper-coauthor"],"confidence":"high","evidence":["https://madsys.cs.tsinghua.edu.cn/author/kang-chen/","https://madsys.cs.tsinghua.edu.cn/publication/"]}'
  - '{"target":"university/清华大学/Shuai Mu","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://mpaxos.com/cv.pdf"]}'
  - '{"target":"university/清华大学/Weichao Guo","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://weichaoguo.github.io/"]}'
---
# 陈康（Kang Chen）

北京大学计算机学院教授。此前长期在清华大学计算机系高性能计算研究所 / MADSys 从事分布式存储、RDMA、NVM / disaggregated memory、图计算等研究；MADSys 主页记录其于 2026 年转至北京大学，北京大学计算机学院当前官方页面列其为教授、研究方向为系统软件。

## 与武永卫的关系
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：长期处于同一清华 systems / MADSys 研究网络，在分布式存储、RDMA、图计算等方向有持续论文合作。
- 两人还共同指导过 [[university/清华大学/Shuai Mu|Shuai Mu]]。Shuai Mu 的公开 CV 明确写明其清华博士阶段 `Advisor: Yongwei Wu, Kang Chen; Supervisor: Weimin Zheng`，因此这里可以建立高置信度的共同指导网络，但不据此推断陈康与武永卫之间存在导师关系。

## 人才网络
- [[university/清华大学/Shuai Mu|Shuai Mu]]：清华博士阶段共同导师之一；二人亦共同署名 HPDC 2014 等系统论文。
- [[university/清华大学/Weichao Guo|Weichao Guo]]：清华系统研究网络的长期论文合作者，覆盖存储、OS 与高性能系统方向。

## 图谱意义
陈康与武永卫共同构成清华传统 distributed/storage systems 人才培养网络的重要一支。这条路线向后连接 Shuai Mu、Weichao Guo 等系统人才，并与 MADSys 后续的 disaggregated memory、KV cache / LLM serving 研究形成技术谱系上的连续性。

## Sources
- https://cs.pku.edu.cn/info/1062/6300.htm
- https://madsys.cs.tsinghua.edu.cn/author/kang-chen/
- https://madsys.cs.tsinghua.edu.cn/publication/
- https://mpaxos.com/cv.pdf
- https://weichaoguo.github.io/
