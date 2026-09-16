---
type: project
name: KunServe
layer: llm-serving
open_source: true
repository: https://github.com/SJTU-IPADS/kunserve
areas: [llm-serving, memory-management, kv-cache, resource-management, elasticity]
people:
  - "university/上海交通大学/Rongxin Cheng"
  - "university/上海交通大学/Xingda Wei"
  - "university/上海交通大学/Rong Chen"
  - "university/上海交通大学/Haibo Chen"
last_verified: "2026-09"
---
# KunServe

## 项目简介
KunServe 是上海交通大学 IPADS 的 LLM serving 系统研究项目，提出 parameter-centric memory management：在服务过载时，不只围绕 KV cache 做丢弃/迁移/交换，而是选择性释放跨 GPU 复制的模型参数空间，并通过 remote attention、KV cache exchange 与在线计划减少排队和尾延迟。

官方 `SJTU-IPADS/kunserve` 仓库同时公开 KunServe 的 Python orchestration / Ray / scheduling experiments，以及用于高性能 dense Transformer inference 的 FlashTransformer C++/CUDA backend，定位于 LLM serving research 与 reproducible evaluation。

## 人物与机构
- [[university/上海交通大学/IPADS|IPADS]]：论文作者 affiliation 明确为 Institute of Parallel and Distributed Systems, Shanghai Jiao Tong University；canonical repository 也位于 `SJTU-IPADS` GitHub organization。
- [[university/上海交通大学/Rongxin Cheng|Rongxin Cheng]]、Yuxin Lai、[[university/上海交通大学/Xingda Wei|Xingda Wei]]、[[university/上海交通大学/Rong Chen|Rong Chen]]、[[university/上海交通大学/Haibo Chen|Haibo Chen]]：EuroSys 2026 版本作者网络。

## 图谱意义
KunServe 把 SJTU 的 OS / resource-management 研究直接连到 LLM serving 的 GPU memory、KV cache 与弹性调度问题，是本仓库中“传统 systems → inference infrastructure”非常清晰的一条桥。

## Sources
- https://github.com/SJTU-IPADS/kunserve
- https://arxiv.org/abs/2412.18169
- https://ipads.se.sjtu.edu.cn/_media/publications/kunserve-eurosys26.pdf
- https://ipads.se.sjtu.edu.cn/pub/members/rong_chen
