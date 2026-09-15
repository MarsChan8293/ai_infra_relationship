---
type: person
name: 尹良升
english_name: Liangsheng Yin
aliases: [尹良升, Liangsheng Yin]
community: SGLang
schools:
  - "UC Berkeley"
  - "上海交通大学"
roles: [maintainer, scheduler merge-oncall, speculative-decoding merge-oncall]
areas: [llm-serving, scheduling, speculative-decoding]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/sgl-project/SGLang/郑连民 Lianmin Zheng","type":["paper-coauthor","open-source-collaboration","community-maintainer"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md"]}'
  - '{"target":"company/RadixArk/盛颖 Ying Sheng","type":["paper-coauthor","open-source-collaboration","research-collaboration"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://sites.google.com/view/yingsheng/home"]}'
  - '{"target":"community/sgl-project/SGLang/谢志强 Zhiqiang Xie","type":["paper-coauthor","open-source-collaboration","community-maintainer"],"project":"SGLang","start":"2023","confidence":"high","evidence":["https://arxiv.org/abs/2312.07104","https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md"]}'
---
# 尹良升（Liangsheng Yin）

SGLang 核心维护者与原始论文作者之一，长期负责 scheduler、serving runtime 与 speculative decoding 等方向。

## 教育经历
- [[上海交通大学]]：ACM / 致远相关计算机培养体系，本科，2021 起
- 个人主页标注为 incoming [[UC Berkeley]] PhD student

## 研究 / 社区经历
- LMSYS：2023 起 Research Intern / research collaborator，与郑连民、盛颖等共同开发 SGLang
- [[SGLang]]：原始论文作者；Scheduler merge oncall；Speculative decoding merge oncall

## 人物关系
- [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：**LMSYS/SGLang 研究与开源合作者**。2023 起在同一 LMSYS/SGLang 技术网络工作；盛颖公开回忆 2024 年夏天尹良升与郑连民、盛颖、Yineng Zhang 多次共同 debug。当前两人共同负责 scheduler 相关维护边界。
- [[RadixArk/盛颖 Ying Sheng|盛颖（Ying Sheng）]]：**SGLang 共同开发者**。2023 起参与同一 SGLang 核心开发网络；2024 年夏天有明确共同 debug 记录。盛颖后于 2025 创办 RadixArk，尹良升当前公开资料并未显示加入 RadixArk，因此不标记为公司同事。
- [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强（Zhiqiang Xie）]]：**SGLang 原始论文合著者 + 当前模块协作者**。两人共同署名 SGLang 原始工作；截至 2026-09，尹良升负责 scheduler / speculative decoding，谢志强负责 KV Cache，属于 scheduler ↔ cache 的系统级社区协作。
- [[Yineng Zhang]]：**SGLang 早期核心开发合作者**。2024 年夏天与郑连民、盛颖、尹良升一起进行高强度 debugging；Yineng 后主要在 Together AI / inference 方向发展，当前不与尹良升标记为公司同事。该关系保留为 prose 候选，本轮未因同一维护网络自动升级 typed relation。

## Sources
- https://www.lsyin.me/
- https://github.com/sgl-project/sglang/blob/main/.github/MAINTAINER.md
- https://arxiv.org/abs/2312.07104
- https://sites.google.com/view/yingsheng/home
