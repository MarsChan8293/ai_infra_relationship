---
type: research-institution
name: MADSys
organization: 清华大学
aliases: ["MADSys Lab", "MADSys Group", "MADSys Lab, Tsinghua University"]
linked_people:
  - "community/kvcache-ai/KTransformers/Boxin Zhang"
  - "community/kvcache-ai/KTransformers/Hongtao Chen"
  - "community/kvcache-ai/KTransformers/Jianwei Dong"
  - "community/kvcache-ai/KTransformers/Jingqi Tang"
  - "community/kvcache-ai/KTransformers/Qingliang Ou"
areas: [machine-learning-systems, llm-inference, kv-cache, heterogeneous-inference, distributed-systems, rl-systems]
projects: [Mooncake, KTransformers, Seer]
website: https://madsys.cs.tsinghua.edu.cn/
last_verified: "2026-09"
---
# MADSys

## 机构定位
MADSys 是清华大学计算机系面向 Machine Learning / AI / Big Data Systems 的系统研究团队。在本图谱中，它是清华 systems 人才进入现代 LLM inference 基础设施的重要上游节点，尤其连接 memory/storage-centric inference、KV cache、异构执行、大规模 serving 与 RL rollout。

## AI Infra 主线
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：KVCache-centric disaggregated serving 与分布式缓存/传输系统。
- [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：CPU/GPU/NUMA 异构推理与本地超大模型执行。
- [[company/月之暗面/Seer|Seer]]：OSDI 2026 synchronous LLM RL rollout 系统；[[university/清华大学/Ruoyu Qin|Ruoyu Qin]]、[[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]、[[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]等连接 Moonshot AI 与清华系统研究网络。
- [[community/deepseek-ai/DualPath/DualPath|DualPath]]：SIGCOMM 2026 agentic LLM inference / KV-cache storage I/O 项目；由章明星与 MADSys 2026 博士 alumni [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] 等共同参与，形成与北大 systems / DeepSeek-AI 的交叉合作。

## 人才扩散
- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：MADSys 2026 Ph.D.；官方 alumni 页面列出的第一份工作为 Hangzhou DeepSeek Artificial Intelligence Co., Ltd。其后续公开项目包括 DualPath 与 DeepSpec。
- 团队人才还流向趋境科技等 AI Infra 公司。这里按公开 alumni 去向、项目作者和当前 affiliation 分别建边，不因共享实验室自动推断直属关系。

## 关系边界
`MADSys` affiliation 只表示人物与该研究团队存在公开可核验的研究、学生、导师或项目关系。共享实验室不自动推断具体导师、同期同学或直接合作，强关系仍需人物页的论文、项目或导师证据。

## Sources
- https://madsys.cs.tsinghua.edu.cn/
- https://madsys.cs.tsinghua.edu.cn/people/
- https://madsys.cs.tsinghua.edu.cn/publications/KTransformers
- https://www.usenix.org/conference/osdi26/presentation/qin
- https://conferences.sigcomm.org/sigcomm/2026/accepted/

<!-- BEGIN AUTO RESEARCH PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `current_affiliations:` 反向汇总，仅表示当前公开的研究机构 affiliation，不自动推断同组、导师、直属汇报或共同项目关系。

- [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Hongtao Chen|Hongtao Chen]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]]：[[清华大学]] / MADSys Lab

<!-- END AUTO RESEARCH PEOPLE -->
