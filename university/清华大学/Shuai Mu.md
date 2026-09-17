---
type: person
name: Shuai Mu
aliases: ["Shuai Mu", "穆帅"]
current_affiliations: ["Stony Brook University"]
schools:
  - "清华大学"
areas: [distributed-systems, databases, consensus, replication, concurrency-control]
roles: [Associate Professor]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/趋境科技/武永卫 Yongwei Wu","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://mpaxos.com/cv.pdf"]}'
  - '{"target":"university/清华大学/Kang Chen","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://mpaxos.com/cv.pdf"]}'
  - '{"target":"company/清程极智/郑纬民 Weimin Zheng","type":["mentor-network","paper-coauthor"],"confidence":"high","evidence":["https://mpaxos.com/cv.pdf"]}'
---
# Shuai Mu

Stony Brook University 计算机系副教授，研究分布式系统、多核系统、数据库与容错复制。

## 清华学术谱系
Shuai Mu 的公开 CV 明确记录其 2015 年获得清华大学计算机博士学位，并写明：`Advisor: Yongwei Wu, Kang Chen; Supervisor: Weimin Zheng`。

因此在本图谱中可以建立以下高置信度关系：
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：博士导师。
- [[university/清华大学/Kang Chen|陈康（Kang Chen）]]：博士导师。
- [[company/清程极智/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]]：博士阶段 supervisor / 上游学术指导网络，不等同于 degree advisor。

## 研究合作
Shuai Mu 与武永卫、陈康、郑纬民共同署名 HPDC 2014 的 `When Paxos Meets Erasure Code`，以及更早的云存储工作。这说明师生关系之外还存在直接的分布式存储 / 一致性系统研究合作。

## 图谱意义
Shuai Mu 是武永卫早期 systems 人才培养网络中非常清晰的一条外溢支路：

`清华 distributed/storage systems → consensus / transactions → Stony Brook distributed systems`

这条支路不直接属于当前 LLM serving，但对理解武永卫团队在可靠分布式系统、存储与一致性方向的技术底座很有价值。

## Sources
- https://mpaxos.com/
- https://mpaxos.com/cv.pdf
