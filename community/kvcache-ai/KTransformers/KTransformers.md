---
type: project
name: KTransformers
organization: KVCache.AI
status: active
repository: https://github.com/kvcache-ai/ktransformers
last_verified: "2026-09"
linked_people:
  - "community/kvcache-ai/KTransformers/Boxin Zhang"
  - "community/kvcache-ai/KTransformers/Chen Lin"
  - "community/kvcache-ai/KTransformers/Chengyu Qiu"
  - "community/kvcache-ai/KTransformers/Hongtao Chen"
  - "community/kvcache-ai/KTransformers/Jiahao Wang"
  - "community/kvcache-ai/KTransformers/Jianwei Dong"
  - "community/kvcache-ai/KTransformers/Jiaqi Liao"
  - "community/kvcache-ai/KTransformers/Jingqi Tang"
  - "community/kvcache-ai/KTransformers/Peilin Li"
  - "community/kvcache-ai/KTransformers/Qingliang Ou"
  - "community/kvcache-ai/KTransformers/Xianglin Chen"
  - "community/kvcache-ai/KTransformers/Xingxing Hao"
  - "community/kvcache-ai/KTransformers/Yuening Zhu"
  - "community/kvcache-ai/KTransformers/Ziwei Yuan"
  - "community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie"
  - "company/深度求索/Shaoyuan Chen"
  - "company/趋境科技/武永卫 Yongwei Wu"
  - "university/清华大学/Mingxing Zhang"
companies: ["趋境科技"]
company_relation: industry-academia-core-network
layer: inference-engine
linked_companies:
  - "company/趋境科技/趋境科技"
areas:
  - "heterogeneous-inference"
  - "cpu-gpu-offload"
  - "moe-inference"
hardware:
  - "cpu"
  - "nvidia"
integrations: []
---
# KTransformers

## 项目简介
KTransformers 是面向 heterogeneous LLM inference / fine-tune 优化的框架，尤其关注 CPU+GPU、多 NUMA 节点和多设备协同，让超大模型可以利用 CPU 内存与计算能力补足 GPU 显存/算力约束。它代表一条不同于“全 GPU 数据中心 serving”的本地与异构推理路线。

## GitHub
https://github.com/kvcache-ai/ktransformers

## 主要贡献公司
- [[company/趋境科技/趋境科技|趋境科技]]：当前公司人才网络与 KTransformers maintainer / 清华 MADSys 技术谱系直接重叠，是本图谱中最强的产业贡献节点。
- 9#AISoft 等组织也出现在项目历史维护/作者网络中；暂不为弱关系单独扩公司节点。

## 主要维护者 / 组织
项目现由 KVCache.AI 组织维护，核心研发网络与清华大学 MADSys Lab 高度重叠。SOSP 2025 KTransformers 作者网络包括 [[Hongtao Chen]]、[[谢威宇 Weiyu Xie]]、[[Boxin Zhang]]、[[Jingqi Tang]]、[[Jiahao Wang]]、[[Jianwei Dong]]、[[Qingliang Ou]]、[[Ziwei Yuan]] 等。

论文作者网络还包括 [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] 与 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]。两人随后又共同署名 SIGCOMM 2026 [[community/deepseek-ai/DualPath/DualPath|DualPath]]，因此 KTransformers 是从 MADSys 异构推理网络继续 BFS 到 DeepSeek inference systems 的重要桥，而不是把论文作者误写成当前 maintainer。

## 生态关系
[[DeepSeek-Infra]] · [[FlashInfer]] · [[Mooncake]] · KVCache.AI · [[清华大学]] · [[community/deepseek-ai/DualPath/DualPath|DualPath]]。它与 Mooncake 共同体现清华 MADSys 的“存储/内存层参与模型推理”路线；Shaoyuan Chen 的后续去向又把这条路线接入 DeepSeek 的 KV-cache I/O 与 speculative decoding 研究。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]]：[[KTransformers]]：官方 Maintainer、论文作者
- [[community/kvcache-ai/KTransformers/Chen Lin|Chen Lin]]：[[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025 论文作者，参与 CPU/GPU hybrid MoE inference。
- [[community/kvcache-ai/KTransformers/Chengyu Qiu|Chengyu Qiu]]：[[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025 正式论文作者，参与 CPU/GPU hybrid MoE inference 系统研究。
- [[community/kvcache-ai/KTransformers/Hongtao Chen|Hongtao Chen]]：[[KTransformers]]：官方 Maintainer、论文第一作者
- [[community/kvcache-ai/KTransformers/Jiahao Wang|Jiahao Wang]]：[[KTransformers]]：官方 Maintainer、论文作者
- [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]]：[[KTransformers]]：官方 Maintainer、论文作者
- [[community/kvcache-ai/KTransformers/Jiaqi Liao|Jiaqi Liao]]：[[KTransformers]]：官方 Maintainer、论文作者
- [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]]：[[KTransformers]]：官方 Maintainer、论文作者
- [[community/kvcache-ai/KTransformers/Peilin Li|Peilin Li]]：[[company/趋境科技/趋境科技|趋境科技（Approaching.AI）]]：KTransformers 官方 maintainer affiliation 记录其与公司有关联。
- [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]]：[[KTransformers]]：官方 Maintainer、论文作者
- [[community/kvcache-ai/KTransformers/Xianglin Chen|Xianglin Chen]]：[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：**师门网络 + 趋境科技同事 + KTransformers 共同作者**。公开材料支持“出身武永卫门下”，但本页谨慎保留为 `mentor-network`，不推断正式学位导师。
- [[community/kvcache-ai/KTransformers/Xingxing Hao|Xingxing Hao]]：[[KTransformers]]：官方 Maintainer
- [[community/kvcache-ai/KTransformers/Yuening Zhu|Yuening Zhu]]：[[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025 论文作者，参与 CPU/GPU hybrid MoE inference。
- [[community/kvcache-ai/KTransformers/Ziwei Yuan|Ziwei Yuan]]：[[company/趋境科技/趋境科技|趋境科技（Approaching.AI）]]：KTransformers 官方 maintainer affiliation。
- [[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇（Weiyu Xie）]]：[[KTransformers]]：官方 Maintainer、SOSP 2025 论文共同第一作者之一；截至 2026-09 KTransformers MAINTAINERS 仍列其为 maintainer。
- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：[[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025 论文作者，与 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]] 共同研究 CPU/GPU hybrid MoE inference。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：[[KTransformers]]：SOSP 2025 论文作者，连接清华 MADSys 与 Approaching.AI 的 MoE heterogeneous inference 网络。
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：**博士导师 + 长期 systems / AI Infra 合作者**。CCF 2018 优秀博士学位论文奖公示明确列出章明星博士论文《大规模图数据的高效计算》的培养单位为清华大学、导师为武永卫。毕业后两人仍持续共同署名 Mooncake、KTransformers 等工作，因此这条边同时具有正式 `student/advisor` 与长期 `research-collab...

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/趋境科技/趋境科技|趋境科技]]：公司页与社区/项目页均有显式记录；关系：`industry-academia-core-network`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

## Sources
- https://sigops.org/s/conferences/sosp/2025/accepted.html
- https://conferences.sigcomm.org/sigcomm/2026/accepted/
