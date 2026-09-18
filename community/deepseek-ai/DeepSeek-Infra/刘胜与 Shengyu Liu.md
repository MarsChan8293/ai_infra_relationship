---
type: person
name: 刘胜与
english_name: Shengyu Liu
aliases: [刘胜与, Shengyu Liu, interestingLSY, "@interestingLSY"]
current_affiliations: ["深度求索"]
public_email: shengyuliu@deepseek.com
schools:
  - "北京大学"
communities: [DeepGEMM, FlashMLA, DeepSelect, DeepSeek-Infra]
linked_companies:
  - "company/深度求索/深度求索"
email_affiliations:
  - "深度求索"
projects: [DeepGEMM, FlashMLA, DeepSelect, DistServe, LoongServe, SwiftLLM]
education: [北京大学]
areas: [mlsys, gpu-kernels, mla, sparse-attention, topk, llm-serving, distributed-systems]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"university/北京大学/Xin Jin","type":["advisor","paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://interestinglsy.github.io/","https://xinjin.github.io/","https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin","https://arxiv.org/abs/2404.09526"]}'
  - '{"target":"company/深度求索/Yinmin Zhong","type":["coworker","paper-coauthor","research-collaboration"],"start":"2025-04","confidence":"high","evidence":["https://interestinglsy.github.io/","https://www.yinminzhong.com/","https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin","https://arxiv.org/abs/2404.09526"]}'
  - '{"target":"university/北京大学/Bingyang Wu","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://interestinglsy.github.io/","https://bingyangwu.github.io/","https://arxiv.org/abs/2404.09526"]}'
  - '{"target":"community/deepseek-ai/DeepSeek-Infra/Yi Qian","type":["open-source-collaboration","technical-collaboration"],"project":"DeepSelect","confidence":"high","evidence":["https://github.com/deepseek-ai/DeepSelect/blob/main/README.md","https://github.com/deepseek-ai/DeepSelect/commit/671e260b3ae8c5b12352dec063569b54d34e12b1"]}'
  - '{"target":"community/deepseek-ai/DeepSeek-Infra/Jiashi Li","type":["open-source-collaboration","technical-collaboration"],"confidence":"high","evidence":["https://github.com/deepseek-ai/FlashMLA","https://github.com/deepseek-ai/DeepGEMM"]}'
  - '{"target":"community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao","type":["open-source-collaboration","technical-collaboration"],"confidence":"high","evidence":["https://github.com/deepseek-ai/DeepGEMM"]}'
  - '{"target":"community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou","type":["open-source-collaboration"],"confidence":"high","evidence":["https://github.com/deepseek-ai/DeepGEMM"]}'
---
# 刘胜与（Shengyu Liu）

[[company/深度求索/深度求索|深度求索]] AI Infra / kernel 方向工程与研究人员，GitHub 身份 `@interestingLSY`。个人主页明确写明其自 2025-04 起在 DeepSeek-AI 从事 Machine Learning Systems 与 kernel design / optimization；2026-09 的 FlashMLA / DeepSelect 提交继续显示其直接处于 DeepSeek V4.1 推理 kernel 热路径。

## 教育经历
- [[university/北京大学/北京大学|北京大学]]：2021-09–2025-07，EECS 图灵班；[[university/北京大学/Xin Jin|Xin Jin]] 指导。
- 曾任北京大学超算队队长，带队获得第 10 届 ASC 第一名，并在 SC23 Student Cluster Competition 获第二名。

## 工作经历
- [[company/深度求索/深度求索|深度求索]]：2025-04–至今，MLSys 与 kernel design / optimization。
- 公开职业邮箱 `shengyuliu@deepseek.com` 同时出现在个人主页与 2026 FlashMLA / DeepSelect Git commit metadata 中。

## 项目与研究
### DeepSeek kernel 热路径
- [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]]：从 2025 MLA decode kernel 持续推进到 2026 DeepSeek V4.1；2026-09-10 直接提交 V4.1 attention kernels，覆盖 SM100 sparse prefill/decode、FP8 / FP4 KV cache，以及 fused norm + RoPE + attention + RoPE + cast operator。
- [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]]：公开作者，GEMM / MoE kernel 技术线。
- [[community/deepseek-ai/DeepSeek-Infra/DeepSelect|DeepSelect]]：2026-09 新开源 TopK kernel，服务 DeepSeek Sparse Attention Lightning Indexer 与 sampler；与 [[community/deepseek-ai/DeepSeek-Infra/Yi Qian|Yi Qian]]、Yichen Li 共同署名。

### 北大 LLM serving 谱系
- [[community/LLMServe/DistServe/DistServe|DistServe]]：OSDI 2024，prefill / decode disaggregation 与 goodput/SLO 联合优化。
- [[community/LoongServe/LoongServe/LoongServe|LoongServe]]：SOSP 2024，Elastic Sequence Parallelism，面向 long-context serving 的动态并行与 KV-cache 管理。
- [[community/interestingLSY/swiftLLM/swiftLLM|SwiftLLM]]：个人主导的轻量研究型 inference engine，用约 2k 行核心代码连接 scheduler、PagedAttention 与 Triton kernels。
- 还参与 FastServe 与 RLHFuse，说明其在进入 DeepSeek 之前已经覆盖 serving scheduler、distributed inference 与 RLHF training systems。

## 人物关系
- [[university/北京大学/Xin Jin|Xin Jin]]：**本科研究导师 + 长期系统论文合作者**。个人主页/CV 明确写明 advisor 关系；共同工作覆盖 DistServe、LoongServe 等。
- [[company/深度求索/Yinmin Zhong|Yinmin Zhong]]：**北大长期系统合作者 + DeepSeek 同期同事**。两人共同参与 DistServe、LoongServe、FastServe、RLHFuse；双方主页均显示 2025-04 起在 DeepSeek，形成从学术合作到产业系统研发的连续边。
- [[university/北京大学/Bingyang Wu|Bingyang Wu]]：**北大 serving 合作者**。共同参与 LoongServe、FastServe、RLHFuse，技术主题覆盖 long-context、distributed serving 与 training/serving fusion。
- [[community/deepseek-ai/DeepSeek-Infra/Yi Qian|Yi Qian]]：**DeepSelect kernel 技术协作者**。DeepSelect 官方 citation 共同署名；Yi Qian 的 `@skip2004` commit 还由刘胜与 co-author，共同维护算法/实现分析。
- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：**FlashMLA + DeepGEMM 技术协作**，合作覆盖 MLA/attention kernels 与 GEMM/MoE kernels。
- [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]、[[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行（Kexing Zhou）]]：DeepGEMM 作者网络中的直接开源协作者。

## 图谱意义
刘胜与是一个很干净的“系统层逐级下沉”节点：`北大 serving architecture / scheduling → 自研 inference engine / Triton → DeepSeek MLA / GEMM → V4.1 sparse-attention / TopK kernels`。他同时把 [[university/北京大学/Xin Jin|Xin Jin]] 的 LLM systems 学术网络与 DeepSeek 当前 production inference kernel 网络连接起来。

## Sources
- https://interestinglsy.github.io/
- https://github.com/interestingLSY/swiftLLM
- https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin
- https://arxiv.org/abs/2404.09526
- https://github.com/deepseek-ai/FlashMLA/commit/07a1089857b63e74e3133630c02b083b75e8d4b2
- https://github.com/deepseek-ai/FlashMLA/commit/063a9f05aaf86d25c3da213a6e79cd5c879f99fe
- https://github.com/deepseek-ai/DeepGEMM
- https://github.com/deepseek-ai/DeepSelect
- https://github.com/deepseek-ai/DeepSelect/commit/0f03b68748b304863fdf0181a11458d04ae533a9

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/深度求索/深度求索|深度求索]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO PERSON COMPANIES -->
