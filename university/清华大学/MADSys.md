---
type: research-institution
name: MADSys
organization: 清华大学
aliases: ["MADSys Lab", "MADSys Group", "MADSys Lab, Tsinghua University"]
linked_people:
  - "community/kvcache-ai/KTransformers/Boxin Zhang"
  - "community/kvcache-ai/KTransformers/Chen Lin"
  - "community/kvcache-ai/KTransformers/Chengyu Qiu"
  - "community/kvcache-ai/KTransformers/Hongtao Chen"
  - "community/kvcache-ai/KTransformers/Jianwei Dong"
  - "community/kvcache-ai/KTransformers/Jingqi Tang"
  - "community/kvcache-ai/KTransformers/Peilin Li"
  - "community/kvcache-ai/KTransformers/Qingliang Ou"
  - "community/kvcache-ai/KTransformers/Yuening Zhu"
  - "community/kvcache-ai/KTransformers/Ziwei Yuan"
  - "company/趋境科技/武永卫 Yongwei Wu"
  - "university/清华大学/Jinlei Jiang"
  - "university/清华大学/Mingxing Zhang"
  - "university/清华大学/Ruoyu Qin"
  - "university/清华大学/Yingdi Shan"
areas: [machine-learning-systems, llm-inference, kv-cache, heterogeneous-inference, distributed-systems, rl-systems, memory-systems, data-movement]
projects: [Mooncake, KTransformers, TENT, Seer]
website: https://madsys.cs.tsinghua.edu.cn/
last_verified: "2026-09"
---
# MADSys

## 机构定位
MADSys（Machine Learning, AI, Big Data Systems）是清华大学计算机系系统研究团队。官方定位强调 parallel / distributed systems 与高效 data processing；在当前 AI Infra 图谱中，它最重要的演化是把长期积累的 memory、storage、network、disaggregation 与 heterogeneous systems 方法迁移到 LLM inference 热路径。

这条路线可以概括成：

`distributed / memory / storage systems → storage-for-compute → KVCache-centric serving → heterogeneous MoE inference → RL / RAG serving`

## Faculty 骨架
MADSys 2026 官方 faculty 列表包括 Yongwei Wu、Jinlei Jiang、Mingxing Zhang、Yingdi Shan、Jing Zheng；Kang Chen 标注为 2026 年转至 Peking University。

- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：长期 systems faculty，连接 Mooncake、KTransformers、TENT、Seer 与趋境科技产业化网络。
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：memory-centric systems / LLM serving 枢纽；官方个人页明确将其列为 KVCache.AI 项目 Mooncake 与 KTransformers 的 initiator。
- [[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]：storage / distributed systems → Seer / RL serving，以及 disaggregated memory / storage 研究。
- [[university/清华大学/Jinlei Jiang|蒋金磊（Jinlei Jiang）]]：distributed / cloud / big-data systems faculty，连接 DPU、NVMe-oF、stream processing 与 hardware offloading 底层系统支路。
- Jing Zheng：MADSys 官方 2026 faculty 列表成员；当前公开 AI Infra 证据较薄，因此暂不单独扩展人物节点。
- [[university/清华大学/Kang Chen|陈康（Kang Chen）]]：长期 MADSys systems faculty / 合作者，官方主页标注 2026 年转至北京大学；保留为历史 faculty 与跨校系统合作节点，不记作当前 MADSys affiliation。

## KVCache.AI：组织层桥梁
[[community/kvcache-ai/KVCache.AI/KVCache.AI|KVCache.AI]] 是 MADSys 当前进入 LLM inference optimization 的关键组织层。MADSys 官方主页将其描述为与 Approaching.AI、Moonshot AI 等产业伙伴合作的 KVCache-centric optimization 项目；KVCache.AI GitHub organization 则明确定位为 MADSys 与产业协作者之间、面向高效 Agent / LLM serving 的开源组织。

这一层很重要，因为它把“实验室论文作者网络”与“持续开源治理 / 产业部署”分开：MADSys 是研究组织，KVCache.AI 是面向 serving optimization 的开源协作层，Mooncake / KTransformers 是具体项目。

## AI Infra 主线
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：FAST 2025 Best Paper / ToS 2025，KVCache-centric disaggregated serving。它把 Moonshot AI 的 Kimi production workload 与 MADSys 的 storage / memory / networking 系统能力结合起来。
- [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025，CPU/GPU hybrid MoE inference；利用 CPU DRAM 容量与 GPU 算力，以异构执行降低超大 MoE 模型本地/低并发推理门槛。
- [[community/kvcache-ai/Mooncake/TENT|TENT]]：FAISys 2025，从 Mooncake Transfer Engine 延伸到 heterogeneous interconnect 的 declarative slice spraying、自适应数据移动与容错；作者网络同时连接清华、Moonshot AI、Alibaba、Ant Group 与 Approaching.AI。
- [[company/月之暗面/Seer|Seer]]：OSDI 2026 synchronous LLM RL rollout。[[university/清华大学/Ruoyu Qin|秦若愚]]、[[university/清华大学/Yingdi Shan|闪英迪]]、武永卫、章明星等把 MADSys 的 scheduling / systems 路线推进到 rollout load balance、tail latency 与 speculative decoding。
- `From Prefix Cache to Fusion RAG Cache`：SIGMOD 2026。作者包括章明星、武永卫、[[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]]、[[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]]、[[community/kvcache-ai/KTransformers/Yuening Zhu|Yuening Zhu]]、[[community/kvcache-ai/KTransformers/Chen Lin|Chen Lin]]、[[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]] 等，把 cache-centric inference 从普通 prefix/KV reuse 延伸到 RAG 场景。
- [[community/deepseek-ai/DualPath/DualPath|DualPath]]：SIGCOMM 2026 agentic LLM inference / KV-cache storage I/O；通过章明星与 2026 MADSys alumni [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] 接入 DeepSeek / 北大 systems 网络。

## 当前 inference-focused 学生
这里不把全部 MADSys 学生机械建节点，只保留直接落在 LLM inference / serving 论文或开源项目上的人物：

- [[university/清华大学/Ruoyu Qin|秦若愚（Ruoyu Qin）]]：Mooncake 第一作者、TENT / Seer 作者，连接 Kimi production serving 与 RL rollout。
- [[community/kvcache-ai/KTransformers/Hongtao Chen|Hongtao Chen]]、[[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]]：KTransformers 共同第一作者网络。
- [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]]、[[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]]、[[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]]：KTransformers 论文 / 维护网络。
- [[community/kvcache-ai/KTransformers/Chengyu Qiu|Chengyu Qiu]]：当前 Ph.D. student，KTransformers 作者。
- [[community/kvcache-ai/KTransformers/Yuening Zhu|Yuening Zhu]]：当前 Ph.D. student，同时跨 KTransformers 与 Fusion RAG Cache。
- [[community/kvcache-ai/KTransformers/Chen Lin|Chen Lin]]：当前 Master student，同时跨 KTransformers 与 Fusion RAG Cache。
- [[community/kvcache-ai/KTransformers/Ziwei Yuan|Ziwei Yuan]]：2026 加入 MADSys 的 Ph.D. student，既有 Approaching.AI / KTransformers 网络，又进入实验室当前学生层。
- [[community/kvcache-ai/KTransformers/Peilin Li|Peilin Li]]：2026 加入 MADSys 的 Ph.D. student、KTransformers maintainer；ChinaSys'26 公开分享 KTransformers-FineTune，连接异构 MoE inference 与 fine-tuning。

## 人才扩散
MADSys 官方 alumni 表给出了非常清晰的人才流向，这些边比单纯“同校”更有价值：

- 2026：[[company/趋境科技/Hongbo Kang|Hongbo Kang]]、[[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇（Weiyu Xie）]] → Approaching AI。
- 2026：[[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] → DeepSeek。
- 2023：[[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]] → Qiyuan Laboratory，之后进入 Approaching.AI / Mooncake data-movement 网络。
- 2022：[[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]] → Haizhi，之后进入 Approaching.AI / Mooncake Store 网络。
- 2021：[[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾（Teng Ma）]] → Alibaba，后来成为 Mooncake / TENT 重要跨公司合作者。
- 2020：[[community/kvcache-ai/KTransformers/Xianglin Chen|陈祥麟（Xianglin Chen）]] 为 MADSys Master alumnus，之后进入 Approaching.AI / KTransformers 产业网络。

这形成了一个很稳定的扩散模式：`MADSys → 大厂 systems / 启元实验室 → 新一代 LLM infra startup / open-source community`。

## 相邻但本轮不扩张的支路
MADSys 官方项目还包括 AgentENV 与 RDSM。AgentENV 面向大规模 agent environment runtime，RDSM 面向 RDMA/CXL distributed shared memory。它们对理解实验室完整 systems 谱系有价值，但与当前“推理优化人才”口径相比优先级低于 KVCache.AI / Mooncake / KTransformers，因此本轮只保留机构级记录，不扩成大量人物节点。

## 关系边界
`MADSys` affiliation 只表示人物与该研究团队存在公开可核验的 faculty / student / research affiliation。共享实验室不自动推断具体导师、同期同学或直属关系；正式 advisor/student 关系仍需学位论文、个人 CV 或官方导师资料等独立证据。

## Sources
- https://madsys.cs.tsinghua.edu.cn/
- https://madsys.cs.tsinghua.edu.cn/publication/
- https://madsys.cs.tsinghua.edu.cn/~zhangmx/
- https://kvcache.ai/
- https://github.com/kvcache-ai
- https://madsys.cs.tsinghua.edu.cn/publication/ktransformers-unleashing-the-full-potential-of-cpu/gpu-hybrid-inference-for-moe-models/
- https://madsys.cs.tsinghua.edu.cn/publication/mooncake-a-kvcache-centric-disaggregated-architecture-for-llm-serving/
- https://madsys.cs.tsinghua.edu.cn/publication/tent-a-declarative-slice-spraying-engine-for-performant-and-resilient-data-movement-in-disaggregated-llm-serving/
- https://madsys.cs.tsinghua.edu.cn/publication/seer-online-context-learning-for-fast-synchronous-llm-reinforcement-learning/
- https://madsys.cs.tsinghua.edu.cn/publication/from-prefix-cache-to-fusion-rag-cache-accelerating-llm-inference-in-retrieval-augmented/

<!-- BEGIN AUTO RESEARCH PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `current_affiliations:` 反向汇总，仅表示当前公开的研究机构 affiliation，不自动推断同组、导师、直属汇报或共同项目关系。

- [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Chen Lin|Chen Lin]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[community/kvcache-ai/KTransformers/Chengyu Qiu|Chengyu Qiu]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[community/kvcache-ai/KTransformers/Hongtao Chen|Hongtao Chen]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Peilin Li|Peilin Li]]：[[university/清华大学/MADSys|MADSys]]：官方主页 2026-08-31 新闻记录其加入 MADSys，并在当前 Ph.D. Students 列表中列出 Peilin Li。
- [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]]：[[清华大学]] / MADSys Lab
- [[community/kvcache-ai/KTransformers/Yuening Zhu|Yuening Zhu]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[community/kvcache-ai/KTransformers/Ziwei Yuan|Ziwei Yuan]]：[[university/清华大学/MADSys|MADSys]]：官方主页记录 Ziwei Yuan 于 2026-08-31 加入实验室，并列入当前 Ph.D. Students。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[university/清华大学/Jinlei Jiang|蒋金磊（Jinlei Jiang）]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[university/清华大学/Ruoyu Qin|秦若愚（Ruoyu Qin）]]：研究机构 affiliation；具体角色与时间以人物页公开来源为准。
- [[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]：2024–至今：清华大学计算机系高性能计算研究所助理研究员；MADSys 个人主页将其列为 Research Assistant Professor。

<!-- END AUTO RESEARCH PEOPLE -->
