---
type: person
name: 刘胜与
english_name: Shengyu Liu
aliases: [刘胜与, Shengyu Liu]
company: 深度求索
communities: [DeepGEMM, FlashMLA, DeepSeek-Infra]
education: [北京大学]
areas: [mlsys, gpu-kernels, mla, llm-serving, distributed-systems]
---
# 刘胜与（Shengyu Liu）

[[深度求索]] AI Infra / kernel 方向工程与研究人员，个人主页明确以 `Shengyu Liu | 刘胜与` 署名，当前聚焦 Machine Learning Systems 与 kernel design / optimization。

## 教育经历
- [[北京大学]]：2021–2025，EECS 图灵班；导师 Xin Jin
- 曾任北京大学超算队队长，参与 ASC / SC Student Cluster Competition

## 工作经历
- [[深度求索]]：2025-04–至今，MLSys 与 kernel design / optimization

## 项目与研究
- [[FlashMLA]]：高性能 MLA decoding kernels；公开作者 / 核心技术贡献
- [[DeepGEMM]]：公开作者，GEMM / MoE kernel 技术线
- DistServe：prefill / decode disaggregation serving
- LoongServe：长上下文 LLM serving
- SwiftLLM：轻量级高性能 LLM inference system

## 人物关系
- [[DeepSeek-Infra/Jiashi Li|Jiashi Li]]：**FlashMLA + DeepGEMM 共同作者**。两人共同出现在 2025 FlashMLA 与 DeepGEMM 公开作者网络，合作覆盖 MLA/attention kernels 与 GEMM/MoE kernels；刘胜与 2025-04 起在 DeepSeek，Jiashi Li 的公开雇佣时间不足，因此不写精确同事起点。
- [[DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：**DeepGEMM 共同作者 / kernel 技术协作者**。2025 DeepGEMM 作者网络明确重叠；赵成钢同时参与 DeepEP，刘胜与同时参与 FlashMLA，因此二人分别从通信与 attention/kernel 两侧连接 DeepSeek MoE inference stack。
- [[DeepSeek-Infra/周可行 Kexing Zhou|周可行（Kexing Zhou）]]：**DeepGEMM 共同作者**。2025 共同位于 DeepGEMM 原始作者网络；周可行偏 compiler/MLIR/GEMM，刘胜与偏 serving/attention/GEMM kernel。公开资料未确认首次直接协作月份。

## 图谱意义
刘胜与是“学术型 LLM serving → 模型公司 kernel → 开源推理生态”之间很清晰的桥梁节点：北大 DistServe / LoongServe 的 serving 研究经验，进入 DeepSeek 后继续下沉到 FlashMLA / DeepGEMM 等 GPU kernel 项目。

## Sources
- Personal homepage: Shengyu Liu | 刘胜与
- Peking University supercomputing / public academic profile
- DeepSeek FlashMLA / DeepGEMM public project credits
