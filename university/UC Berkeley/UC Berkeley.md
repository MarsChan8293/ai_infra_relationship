---
type: school
name: UC Berkeley
aliases: ["University of California, Berkeley"]
---
# UC Berkeley

## AI Infra 总览
UC Berkeley 的 AI Infra 影响力具有非常连续的“systems lab → open-source project → startup/company”结构。AMPLab/RISELab/Sky Computing Lab 一脉把 distributed systems、cloud computing 与 ML systems 研究不断外溢到 Ray、Ray Serve、vLLM、SGLang、Anyscale、Databricks、Inferact，并向 OpenAI、Meta 等模型公司输送 serving systems 人才。

## 导师枢纽
- [[Ion Stoica]]：Berkeley systems / Sky Computing Lab 核心教授与 director；是 Woosuk Kwon 的博士导师之一，也是 Lianmin Zheng、Simon Mo、Xiaoxuan Liu 等多个 AI systems 节点的导师/共同导师网络核心。
- [[Joseph Gonzalez]]：Berkeley systems + ML systems faculty；与 Ion Stoica 共同指导 Lianmin Zheng、Simon Mo 等，并参与 [[Inferact]] founding network。

## vLLM：论文系统 → 开源 engine → Inferact
- [[Woosuk Kwon]]：Berkeley PhD 2021–2025，advisor Ion Stoica；vLLM creator；后任 [[Inferact]] cofounder/CTO。
- [[Simon Mo]]：Berkeley systems 研究者，博士导师网络包括 Ion Stoica / Joseph Gonzalez；经历 [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]]、[[vLLM]]，后任 Inferact cofounder/CEO。
- [[游凯超 Kaichao You]]：清华博士背景，2019 RISELab visiting、2024 Sky Lab visiting；后成为 vLLM Project Lead 与 Inferact cofounder/Chief Scientist。公开资料不足以把 Ion/Joseph 写成其正式博士导师。
- [[乔一凡 Yifan Qiao]]：Berkeley Sky Lab postdoc，与 Ion Stoica / Joseph Gonzalez 合作；2026 加入 Inferact founding MTS。

这条链的关键不是“Berkeley 校友很多”，而是同一批人把研究 prototype、开源治理和 startup engineering 连成了持续组织网络。

## SGLang：另一条 serving engine 路线
[[郑连民 Lianmin Zheng]] 的 Berkeley 博士由 Ion Stoica 与 Joseph Gonzalez 指导，其工作从 Alpa/Ansor、LLM evaluation 延伸到 [[SGLang]]。SGLang 的 RadixAttention / serving systems 网络又连接 [[盛颖 Ying Sheng]]、[[尹良升 Liangsheng Yin]]、[[谢志强 Zhiqiang Xie]]，并进一步形成 [[RadixArk]] 产业节点。

## 跨校人才桥：清华 / 北大 → Berkeley → 模型公司
- [[Chen Zhang]]：清华 BS/PhD → 2024 Berkeley visiting / Sky Lab → [[Meta]]，持续参与 vLLM/Jenga/PrefillOnly。
- [[柳晓萱 Xiaoxuan Liu]]：Berkeley PhD，advisor network 包含 Alvin Cheung 与 Ion Stoica；参与 vLLM、TurboSpec、Jenga，后进入 [[OpenAI]]。
- [[游凯超 Kaichao You]]：清华 → Berkeley visiting → vLLM/Inferact。

因此 Berkeley 在图谱中更像一个“系统人才放大器”：吸收不同学校的强系统学生，通过 Sky/RISE 的共同项目形成协作网络，再流向开源社区、创业公司和 frontier labs。

## Ray / Anyscale / Databricks 的历史底座
[[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]]、[[Anyscale]] 与 Berkeley Ray 系谱相连；[[Databricks]] 则可追溯到更早的 AMPLab/Spark 创业网络。这说明 vLLM/SGLang 并非孤立现象，而是 Berkeley 长期把系统研究开源并商业化的延续。

## 关键项目
[[vLLM]] · [[SGLang]] · [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]] · Ray · [[Inferact]] · [[Anyscale]] · [[Databricks]]

## Sources
- https://sky.cs.berkeley.edu/
- https://www2.eecs.berkeley.edu/Faculty/Homepages/stoica.html
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-107.html
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/EECS-2024-158.html
- https://inferact.ai/
- https://liuxiaoxuanpku.github.io/
- https://yifanqiao.com/
