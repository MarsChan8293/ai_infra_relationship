# university

高校、实验室与学术研究组织的一级分类入口。中国高校与中国研究机构统一使用中文 canonical 名称；这里不是简单校友录，而是用导师/学生、同实验室、论文、开源项目、访问经历与创业去向解释 AI Infra 人才如何流动。

## 国内 AI Systems / 智算研究机构第一梯队
- [[上海人工智能实验室]]：基础平台覆盖自研编译计算、高效能智算系统、网络与分布式系统、大模型训练系统；通过 [[LMDeploy]] 直接连接大模型推理、量化、TurboMind 与 serving。
- [[鹏城实验室]]：以先进计算研究部、鹏城云脑为核心，连接国产算力、分布式智能计算、高效能云计算、模型训练/部署与算网基础设施。
- [[北京智源人工智能研究院]]：通过 [[FlagOS]]、[[FlagScale]]、[[FlagGems]]、[[FlagTree]]、[[FlagCX]] 等连接异构芯片、训练推理、编译、算子与集合通信。
- [[启元实验室]]：通过 InfiniTensor / 九源统一智能计算平台连接 AI compiler、operator/runtime/communication 与国产异构芯片适配。

这一组不是按行政级别机械排名，而是按本图谱关心的 AI Infra 密度筛选：能否形成 compiler / runtime / communication / distributed training & inference / heterogeneous accelerator 的可遍历关系网络。

## 已实体化 AI Infra 学术网络
- [[清华大学]]：至少包含 MADSys/KVCache、KEG/GLM、PACMAN/vLLM 三条不同谱系，连接 KTransformers、Mooncake、智谱、月之暗面、vLLM、Inferact、Meta。
- [[UC Berkeley]]：Sky/RISE/AMPLab 系统网络，连接 Ray/Ray Serve、vLLM、SGLang、Inferact、Anyscale、Databricks 与 OpenAI/Meta 人才流动。
- [[上海交通大学]]：至少包含 IPADS Modern AI Infrastructure 与 NNE-Lab/LightLLM 两支，连接 serving resource management、KV cache、LightLLM 与产业推理系统。
- [[北京大学]]：已实体化杨智 AI compiler / kernel DSL 谱系，从 Rammer、Welder 延伸到 TileLang，并连接微软亚洲研究院、NVIDIA、字节跳动与现有深度求索/vLLM/UChicago 北大校友节点。
- [[浙江大学]]：已实体化寿丽丹 / 李环数据库与数据智能 → LLM inference systems 谱系，覆盖 HMI multi-tenant serving、FloE MoE inference、speculative decoding、KV-cache compression，并通过梁文锋、Jingfan Sun、Jue Wang 分别连接深度求索、NVIDIA/FlashInfer 与 Together AI。
- [[微软亚洲研究院]]：systems / AI research 网络，连接北大 compiler / TileLang、vLLM、SGLang、深度求索、一流科技 / 硅基流动等人才迁移路径。
- [[Carnegie Mellon University]]：高频人才教育节点，连接 Junchen Jiang、月之暗面、OpenAI 与 vLLM / TensorMesh 相关系统人才流动。
- [[Stanford University]]：当前主要通过谢志强、盛颖连接 SGLang / RadixArk serving systems 网络。
- [[香港科技大学]]：当前主要通过 Cyrus Leung 连接 vLLM / Inferact inference engineering 网络。
- [[University of Chicago]]：Junchen Jiang / LMCache / TensorMesh 的核心学术源头，形成 KV cache 与 inference memory/data plane 研究路线。

## 实体化策略
优先实体化在现有图谱中被多次引用、且能形成明确 inference optimization 关系闭环的学校/研究节点；低频红链暂保留，不为消除红链批量创建空壳页面。中国高校即使暂未实体化，也统一使用中文红链名。
