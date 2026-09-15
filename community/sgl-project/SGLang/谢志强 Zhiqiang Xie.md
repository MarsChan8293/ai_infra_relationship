---
type: person
name: 谢志强
english_name: Zhiqiang Xie
aliases: [谢志强, Zhiqiang Xie]
community: SGLang
schools:
  - "Stanford University"
  - "UC Berkeley"
  - "上海科技大学"
roles: [original-paper-author, kv-cache merge-oncall]
areas: [kv-cache, observability, llm-serving, systems]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/sgl-project/SGLang/郑连民 Lianmin Zheng","type":["paper-coauthor","open-source-collaboration","community-maintainer"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md"]}'
  - '{"target":"community/sgl-project/SGLang/尹良升 Liangsheng Yin","type":["paper-coauthor","open-source-collaboration","community-maintainer"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md"]}'
  - '{"target":"company/RadixArk/盛颖 Ying Sheng","type":["paper-coauthor","open-source-collaboration","research-collaboration"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://sites.google.com/view/yingsheng/home"]}'
---
# 谢志强（Zhiqiang Xie）

SGLang 原始论文作者、KV Cache 方向核心维护者，研究重点是大规模 ML systems、可观测性与可靠性。

## 教育经历
- [[上海科技大学]]：本科、硕士
- [[Stanford University]]：计算机博士在读，MAST Lab；导师 Christos Kozyrakis，并与 Kayvon Fatahalian 合作

## 研究 / 实习经历
- MPI-SWS、Microsoft Research Asia、AWS Shanghai AI Lab / DGL：早期系统研究实习
- Microsoft Research：LLM fault localization
- [[NVIDIA]] Research：大规模模型 serving memory management

## SGLang
- 原始论文作者
- KV Cache merge oncall
- HiCache 等分层 KV cache 工作

## 人物关系
- [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：**SGLang 原始论文合著者 + 当前系统模块协作者**。两人共同署名 2023/2024 SGLang 原始工作；截至 2026-09 郑连民负责 scheduler，谢志强负责 KV Cache merge oncall，属于 scheduler ↔ cache 的持续开源协作，不等同于公司同事。
- [[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升（Liangsheng Yin）]]：**SGLang 原始论文合著者 + scheduler/cache 协作者**。两人共同参与原始 SGLang 工作；当前尹良升负责 scheduler / speculative decoding，谢志强负责 KV Cache，因此在 serving runtime 的调度与缓存接口处存在持续模块交叉。
- [[RadixArk/盛颖 Ying Sheng|盛颖（Ying Sheng）]]：**SGLang co-creator / 原始论文合著网络**。两人共同署名 SGLang 原始技术工作，2023–2024 属同一项目核心研究网络。盛颖后于 2025 创办 [[RadixArk]]，公开资料未显示谢志强加入 RadixArk，因此不标记为公司同事。
- Christos Kozyrakis：**Stanford 博士导师**。谢志强在 Stanford MAST Lab 读博期间由其指导；该关系属于正式学术指导关系，与 SGLang 社区关系分开记录。Christos 当前不是仓库节点，因此本轮不为建立该边而新增普通节点。


## 学校关联
- [[university/UC Berkeley/UC Berkeley|UC Berkeley]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://zhiqiangxie.com/
- https://aclanthology.org/people/zhiqiang-xie/
- https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md
- https://arxiv.org/abs/2312.07104
- https://sites.google.com/view/yingsheng/home
