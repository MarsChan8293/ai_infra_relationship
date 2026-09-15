---
type: project
name: DualPath
companies: ["深度求索"]
company_relation: industry-academia-research-collaboration
layer: kv-cache
open_source: false
areas: [agentic-inference, llm-serving, kv-cache, disaggregated-serving, storage-io, scheduling]
last_verified: "2026-09"
---
# DualPath

## 项目简介
DualPath 是 SIGCOMM 2026 接收的 agentic LLM inference 系统，核心问题是多轮 agent workload 中大量 KV-Cache 从外部存储加载时，prefill 侧 storage NIC 饱和、decode 侧 storage NIC 闲置造成的 I/O 不平衡。

系统在传统 `storage → prefill` 路径之外增加 `storage → decode → prefill` 路径，并结合全局调度在 prefill / decode engines 之间动态平衡 KV-cache loading。论文报告 offline inference throughput 最高提升 1.87×，online serving throughput 平均提升约 1.96×。

## 作者 / 组织网络
SIGCOMM 2026 接收页面列出的作者与单位横跨北京大学、清华大学与 DeepSeek-AI：
- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：Tsinghua University, DeepSeek-AI；连接 MADSys 与 DeepSeek inference systems。
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：Tsinghua University；与 Shaoyuan Chen 再次形成论文合作边。
- Yongtong Wu、Yinmin Zhong：Peking University, DeepSeek-AI。
- Yixuan Tan、Panpan Huang：DeepSeek-AI。
- Rilin Huang、Xin Jin：Peking University。

## 图谱意义
DualPath 是章明星 BFS 中非常关键的二跳桥：`Mingxing Zhang → Shaoyuan Chen → DeepSeek`，而技术主题又与 Mooncake 的 KV-cache / disaggregated serving 路线直接相邻。它把清华 MADSys、北大 systems 与 DeepSeek production inference 放在同一个可核验项目网络里。

## Sources
- https://conferences.sigcomm.org/sigcomm/2026/accepted/
- https://conferences.sigcomm.org/sigcomm/2026/program/papers/
- https://arxiv.org/abs/2602.21548
