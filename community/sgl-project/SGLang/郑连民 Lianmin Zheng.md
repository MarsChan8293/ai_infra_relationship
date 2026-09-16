---
type: person
name: 郑连民
english_name: Lianmin Zheng
aliases: [郑连民, Lianmin Zheng]
current_affiliations: ["UCLA"]
schools:
  - "UC Berkeley"
  - "上海交通大学"
  - "UCLA"
communities: [SGLang, LMSYS]
roles: [SGLang creator, scheduler merge-oncall, Assistant Professor]
areas: [llm-serving, distributed-systems, compilers, evaluation]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/RadixArk/盛颖 Ying Sheng","type":["paper-coauthor","open-source-collaboration","research-collaboration"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://sites.google.com/view/yingsheng/home"]}'
  - '{"target":"community/sgl-project/SGLang/尹良升 Liangsheng Yin","type":["paper-coauthor","open-source-collaboration","community-maintainer"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md"]}'
  - '{"target":"community/sgl-project/SGLang/谢志强 Zhiqiang Xie","type":["paper-coauthor","open-source-collaboration","community-maintainer"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md"]}'
  - '{"target":"company/Inferact/Ion Stoica","type":["advisor","paper-coauthor","research-collaboration"],"project":"SGLang","end":"2024","confidence":"high","evidence":["https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/31234.html","https://arxiv.org/abs/2312.07104"]}'
  - '{"target":"company/Inferact/Joseph Gonzalez","type":["advisor","paper-coauthor","research-collaboration"],"project":"SGLang","end":"2024","confidence":"high","evidence":["https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/31234.html","https://arxiv.org/abs/2312.07104"]}'
---
# 郑连民（Lianmin Zheng）

SGLang 第一作者 / 核心创建者之一，也是 LMSYS.org 联合创始人。2026-07 起任 [[UCLA]] Computer Science Assistant Professor。

## 教育经历
- [[上海交通大学]]：ACM 荣誉班本科
- [[UC Berkeley]]：计算机博士，导师 [[Inferact/Ion Stoica|Ion Stoica]]、[[Inferact/Joseph Gonzalez|Joseph Gonzalez]]

## 工作与研究
- Berkeley 期间参与 Alpa、TVM/Ansor、FastChat、Chatbot Arena、SGLang 等系统
- 曾在 [[xAI]] 负责 Grok inference 基础设施
- [[UCLA]]：Computer Science Assistant Professor，2026-07–至今

## SGLang
- 2023 年夏天参与启动 SGLang，2024-01 项目公开
- 原始论文第一作者
- 当前官方 maintainer 列表中负责 Scheduler merge oncall

## 人物关系
- [[RadixArk/盛颖 Ying Sheng|盛颖（Ying Sheng）]]：**SGLang 共同创建者 / 长期系统研究合作者**。两人从 2023 年夏天共同启动 SGLang；项目于 2024-01 公开。盛颖公开回忆指出 2024 年夏天两人与尹良升、Yineng Zhang 多次一起 debug serving 系统。该关系首先是开源/研究合作，不因双方曾出现 xAI 履历就自动扩写成同事关系。
- [[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升（Liangsheng Yin）]]：**LMSYS/SGLang 研究与开源合作者**。尹良升从 2023 年起在 LMSYS/SGLang 网络中与郑连民、盛颖工作；2024 年夏天三人有明确的共同 debug 记录。当前郑连民负责 Scheduler merge oncall，尹良升负责 Scheduler + speculative decoding，属于持续的核心维护协作。
- [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强（Zhiqiang Xie）]]：**SGLang 原始论文合著者 + 当前社区维护协作者**。两人共同署名 2023/2024 SGLang 原始工作；截至 2026-09，郑连民负责 scheduler，谢志强负责 KV Cache merge oncall，属于 scheduler ↔ cache 的系统层协作，而非已确认的公司同事关系。
- [[Inferact/Ion Stoica|Ion Stoica]]：**UC Berkeley 博士导师 / 学生**。郑连民 Berkeley 博士阶段由 Ion Stoica 与 Joseph Gonzalez 指导；该 Berkeley systems 谱系连接 Alpa、FastChat、SGLang，同时通过 Ion 的其他学生连接 [[vLLM]] 与 [[Ray]]。
- [[Inferact/Joseph Gonzalez|Joseph Gonzalez]]：**UC Berkeley 博士导师 / 学生**。Joseph 与 Ion Stoica 共同指导郑连民，其 ML systems / model serving 研究网络后来延伸到 SGLang；Joseph 同时是 [[Inferact]] founding member，因此形成 Berkeley systems → vLLM / SGLang 两支 inference 生态的桥梁。

## Sources
- https://lmzheng.net/
- https://www2.eecs.berkeley.edu/Pubs/Dissertations/Faculty/jegonzal.html
- https://www2.eecs.berkeley.edu/Pubs/Dissertations/Faculty/stoica.html
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/31234.html
- https://arxiv.org/abs/2312.07104
- https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md
- https://www.cs.ucla.edu/ucla-computer-science-welcomes-six-faculty-members-v1/
