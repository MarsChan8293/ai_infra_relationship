---
type: project
name: Jenga
organization: Tsinghua University / UC Berkeley
linked_people:
  - "community/vllm-project/vLLM/Chen Zhang"
  - "company/清程极智/翟季冬 Jidong Zhai"
layer: heterogeneous-memory-management
areas: [llm-serving, memory-management, kv-cache, heterogeneous-models]
people:
  - "community/vllm-project/vLLM/Chen Zhang"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/Inferact/Woosuk Kwon"
  - "community/vllm-project/vLLM/游凯超 Kaichao You"
  - "community/vllm-project/vLLM/李卓翰 Zhuohan Li"
  - "company/清程极智/翟季冬 Jidong Zhai"
  - "company/Inferact/Joseph Gonzalez"
  - "company/Inferact/Ion Stoica"
last_verified: "2026-09"
linked_companies: []
---
# Jenga

## 项目简介
Jenga 是 SOSP 2025 的 LLM serving memory-management 系统，面向现代模型中 embedding dimensions、attention 结构与访问模式逐渐异构化后产生的显存碎片和缓存策略问题。

Jenga 使用两级 memory allocator，并允许针对不同 layer / token dependency 表达不同 caching / eviction 策略。论文实现基于 [[community/vllm-project/vLLM/vLLM|vLLM]]；公开结果显示 GPU memory utilization 最高提升 79.6%，serving throughput 最高提升 4.92×、平均 1.80×。

## 人物网络
论文作者网络把清华 PACMAN 与 Berkeley / vLLM serving 直接连在一起：
- [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]：第一作者；清华 PACMAN 博士 → Berkeley → Meta。
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：清华作者与 Chen Zhang 博士导师。
- [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：University of Chicago / LMCache / TensorMesh 系统网络。
- [[company/Inferact/Woosuk Kwon|Woosuk Kwon]]、[[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]、[[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰（Zhuohan Li）]]：vLLM / Berkeley serving 网络。
- [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]]、[[company/Inferact/Ion Stoica|Ion Stoica]]：Berkeley Sky systems faculty 网络。

## 图谱意义
Jenga 是从翟季冬出发最关键的二跳桥之一：`翟季冬 → Chen Zhang → Jenga → vLLM / Berkeley → Inferact / TensorMesh / Meta`。它证明 PACMAN 与现代开源 LLM serving 社区之间存在直接论文合作，而不只是学生毕业后的职业迁移。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-confsosp-zhang-dlkmwlyllz-25/
- https://arxiv.org/abs/2503.18292
- https://sky.cs.berkeley.edu/publications/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]：[[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025 第一作者；连接清华 PACMAN 与 Berkeley / vLLM serving 系统网络
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：[[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025，与 [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]、[[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰]]、[[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超]]、Woosuk Kwon、Zhuohan Li、Joseph Gon...

<!-- END AUTO PROJECT PEOPLE -->
