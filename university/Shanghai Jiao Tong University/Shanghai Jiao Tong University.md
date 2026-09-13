---
type: school
name: Shanghai Jiao Tong University
aliases: [SJTU, 上海交通大学]
---
# Shanghai Jiao Tong University

## AI Infra 总览
上海交大的 AI Infra 网络至少有两支需要分开观察：IPADS 的 Modern AI Infrastructure / OS & distributed systems 路线，以及 NNE-Lab/LightLLM 的 LLM inference framework 路线。它们同属 SJTU，但没有证据时不能把两边人物写成同实验室或直接共事。

## IPADS：Modern AI Infrastructure
IPADS 长期系统研究在 LLM 时代快速转向 serving scalability、resource management、KV cache 与 memory management。[[Rong Chen]] 的官方主页明确把 “Modern AI Infrastructure（与 [[Xingda Wei]] 合作，2020–）”列为研究方向。

### 核心 faculty
- [[Haibo Chen]]：IPADS / OS 与系统研究核心教授，近期作者网络覆盖 KunServe 等 LLM infrastructure 工作。
- [[Rong Chen]]：高性能、可扩展 AI systems；Modern AI Infrastructure 研究线核心。
- [[Xingda Wei]]：scalable AI infrastructure、autoscaling、resource management 核心 faculty。

### 代表项目/论文簇
- KunServe：[[Rongxin Cheng]]、Yuxin Lai、[[Xingda Wei]]、[[Rong Chen]]、[[Haibo Chen]]；关注 LLM serving overload 下 parameter-centric memory management。
- BlitzServing / BlitzScale：面向 serving elasticity 与快速 scaling。
- KVCache-at-cloud：研究云上 KV cache 的行为与系统设计。
- LMetric、PhoenixOS、ProMoE 等：把 workload measurement、resource management、OS/runtime 与 MoE serving 串联起来。

这条线的特点是从 OS/cluster/resource-management 角度切入 AI Infra，而不是从某个单一 inference engine 出发。

## NNE-Lab / LightLLM / TokenFlow
另一支更贴近 LLM serving framework 与 decoding system。[[Fan Wu]] 是 NNE-Lab / distributed systems faculty 网络核心；[[Junyi Chen]] 2024–至今在 SJTU NNE-Lab 读 CS 硕士，公开主页显示导师为 Fan Wu 与 Shengzhong Liu，并有 SenseTime Research 大模型系统经历、[[LightLLM]] core contributor 经历，2026 进入 Xiaohongshu RED AI-Infra Training Framework Team 并参与开源 post-training framework Relax。

Junyi Chen 还与 Fan Wu、Shengzhong Liu 等共同参与 TokenFlow 等系统研究，因此他是 SJTU 学术、LightLLM 社区与产业 AI Infra 之间非常清晰的桥梁。

## 两支网络的关系
IPADS 更偏 OS、resource management、elastic serving、memory/parameter management；NNE-Lab/LightLLM 更偏 serving framework、structured/constrained decoding 与模型执行工具链。两边可能在学校和会议社区内相遇，但当前图谱不把“同校”升级成“同门/直接合作”。

## Sources
- https://ipads.se.sjtu.edu.cn/~rongchen/
- https://ipads.se.sjtu.edu.cn/~wxd/
- https://ipads.se.sjtu.edu.cn/
- https://cs.sjtu.edu.cn/~fwu/
- https://junyi-chen.github.io/
