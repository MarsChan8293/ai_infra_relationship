---
type: person
name: 郑立言
english_name: Liyan Zheng
aliases: ["Liyan Zheng", "郑立言"]
current_affiliations: ["ByteDance Seed"]
schools:
  - "清华大学"
projects: [InfiniTensor]
areas: [llm-systems, distributed-training, compiler-optimization, inference-engine, reliability]
roles: [LLM System Researcher]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/清程极智/翟季冬 Jidong Zhai","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://wintersurf.github.io/","https://pacman.cs.tsinghua.edu.cn/~zjd/projects/einnet/"]}'
---
# 郑立言（Liyan Zheng）

当前：[[company/字节跳动/字节跳动|字节跳动]] Seed，LLM System Researcher。

## 教育与研究经历
- [[清华大学]]：计算机博士；个人主页明确列出导师为 [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]。
- PACMAN 研究主线覆盖大规模 LLM training、编译优化与长期运行可靠性。

## AI Infra 关系
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：**博士导师 + 长期论文合作者**。两人共同参与 EinNet、Vapro 等系统工作。
- [[community/InfiniTensor/InfiniTensor|InfiniTensor]]：公开个人主页列为其核心项目；项目由 EinNet 等 tensor-program optimization 研究线演化而来，当前定位为面向 GPU / AI accelerators 的高性能推理引擎。
- ByteDance Seed：当前从事 LLM systems，技术方向与 Seed Infrastructures 的 distributed training、high-performance inference、heterogeneous compilation 主线高度一致。

## 图谱意义
郑立言把 PACMAN 的 tensor compiler / performance optimization 谱系连接到 ByteDance Seed 的现代 LLM infrastructure，是“清华编译与 HPC → 大模型训练/推理系统”的直接人才迁移节点。

## Sources
- https://wintersurf.github.io/
- https://pacman.cs.tsinghua.edu.cn/~zjd/people/
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/einnet/
- https://seed.bytedance.com/en/direction/infrastructures
