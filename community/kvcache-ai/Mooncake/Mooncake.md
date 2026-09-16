---
type: project
name: Mooncake
linked_people:
  - "community/kvcache-ai/Mooncake/任峰 Feng Ren"
  - "community/kvcache-ai/Mooncake/马腾 Teng Ma"
  - "community/sgl-project/SGLang/Yineng Zhang"
  - "company/清程极智/郑纬民 Weimin Zheng"
  - "company/趋境科技/卢佳豪 Jiahao Lu"
  - "company/趋境科技/武永卫 Yongwei Wu"
  - "university/清华大学/Mingxing Zhang"
  - "university/清华大学/Ruoyu Qin"
companies: ["月之暗面"]
company_relation: industry-academia-co-development
layer: kv-cache-centric-serving
open_source: true
repository: https://github.com/kvcache-ai/Mooncake
areas: [kv-cache, disaggregated-serving, rdma, data-movement, distributed-storage, reinforcement-learning, heterogeneous-interconnect]
governance: KVCache.AI community; four official codeowners in MAINTAINERS.md
people:
  - "community/kvcache-ai/Mooncake/马腾 Teng Ma"
  - "community/kvcache-ai/Mooncake/Shangming Cai"
  - "community/kvcache-ai/Mooncake/任峰 Feng Ren"
  - "community/kvcache-ai/Mooncake/Ke Yang"
linked_companies:
  - "company/月之暗面/月之暗面"
last_verified: "2026-09"
---
# Mooncake

## 项目简介
Mooncake 起点是面向 LLM serving 的 KVCache-centric 分布式系统：把 prefill/decode 解耦后的 KV cache 作为一级系统资源管理，并利用 CPU DRAM、SSD、NIC 等资源构建分布式 KV 存储与传输路径。它来自清华 MADSys 与 Moonshot/Kimi 的产学协作，并获得 FAST 2025 Best Paper。

到 2026 年，Mooncake 已经不只是一套 KV cache backend。官方项目把 Transfer Engine、Mooncake Store、P2P/Checkpoint 数据分发、弹性 MoE，以及 inference ↔ training / RL 数据移动组织成更广的数据平面，开始覆盖 hidden states、模型权重、rollout data 与多种异构互联。

## GitHub
https://github.com/kvcache-ai/Mooncake

## 主要贡献公司
- [[company/月之暗面/月之暗面|月之暗面]]：真实 Kimi production serving workload 与工程共研的重要产业方；与清华 MADSys 共同构成 Mooncake 的产学协作起源。项目当前由 KVCache.AI 社区维护，因此不写成 Moonshot 单一公司治理。

## 官方 Codeowners
Mooncake 当前 `MAINTAINERS.md` 明确列出四位 Codeowner：
- [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾（Teng Ma）]]：Alibaba Cloud，LLM Eco-System Cooperation
- [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]：Alibaba Cloud，SGLang Integration
- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]]：维护文档标注 9#AISoft，负责 Mooncake Transfer Engine；其个人主页显示 2026 年 affiliation 已转向 Approaching AI，因此公司标签按各来源时间分别保留
- [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]]：Approaching AI，Mooncake Store

## 研究作者网络
公开论文作者包括 [[university/清华大学/Ruoyu Qin|Ruoyu Qin]]、Zheming Li、Weiran He、Jialei Cui、Heyi Tang、[[community/kvcache-ai/Mooncake/任峰 Feng Ren|Feng Ren]]、[[community/kvcache-ai/Mooncake/马腾 Teng Ma|Teng Ma]]、[[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]、[[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]、[[university/清华大学/Mingxing Zhang|Mingxing Zhang]]、[[company/趋境科技/武永卫 Yongwei Wu|Yongwei Wu]]、[[company/清程极智/郑纬民 Weimin Zheng|Weimin Zheng]]、Xinran Xu。FAST'25 版本与后续 ACM TOS 版本作者集合不同，正文按具体论文分别核验，不把作者列表机械合并为同一贡献角色。

## 2026 数据平面扩张
- [[community/kvcache-ai/Mooncake/TENT|TENT]]：Mooncake Transfer Engine NEXT，把静态路径选择升级为异构互联上的 declarative slice spraying / 动态调度 / 自愈数据移动层。
- [[company/月之暗面/checkpoint-engine|Checkpoint Engine]]：Moonshot AI 的 RL / serving 权重更新中间件，P2P 路径直接依赖 Mooncake Transfer Engine；TENT 论文也以其参数更新作为生产场景。
- [[community/radixark/Miles/Miles|Miles]]：2026-08 集成 Mooncake 作为 rollout ↔ training 的数据传输 backend，进入 disaggregated RL 数据流。
- [[community/vllm-project/Speculators/Speculators|Speculators]]：使用 Mooncake backend 在 vLLM inference workers 与 trainer 之间多节点传输 hidden states，进入在线 speculative decoding training。
- [[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]]：使用 Mooncake Store 直接流式传输 hidden states，解耦 inference 与 speculative-draft training。
- [[SGLang]]：2026 年进一步用 Mooncake Transfer Engine 做大规模分布式 RL 的 P2P 权重更新，并在 Kimi-K2 1T 模型场景中公开 7× 权重更新时间优化结果。

## 人才桥
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：Mooncake 论文作者，同时连接 [[SGLang]]、[[FlashInfer]]、[[TokenSpeed]] 与 TENT 作者网络。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]、[[company/清程极智/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]]、[[university/清华大学/Mingxing Zhang|Mingxing Zhang]]：共同构成清华 systems / HPC 上游学术网络；只按论文/实验室证据建边，不从同实验室身份自动推断所有导师学生关系。

## 生态关系
[[SGLang]] · [[vLLM]] · [[LMCache]] · [[NIXL]] · [[KTransformers]] · [[TokenSpeed]] · [[community/kvcache-ai/Mooncake/TENT|TENT]] · [[company/月之暗面/checkpoint-engine|Checkpoint Engine]] · [[community/radixark/Miles/Miles|Miles]] · [[community/vllm-project/Speculators/Speculators|Speculators]] · [[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]] · [[清华大学]] · [[月之暗面]]。

## Sources
- https://github.com/kvcache-ai/Mooncake
- https://github.com/kvcache-ai/Mooncake/blob/main/MAINTAINERS.md
- https://www.usenix.org/conference/fast25/presentation/qin
- https://doi.org/10.1145/3773772
- https://arxiv.org/abs/2604.00368

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]]：Mooncake 联合创建者之一
- [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾（Teng Ma）]]：参与 Mooncake 社区维护与跨生态协作
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：[[Mooncake]]：KVCache-centric disaggregated serving 论文作者，连接 SGLang / kernel 与清华 MADSys、Moonshot/Kimi serving 网络。
- [[company/清程极智/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]]：[[Mooncake]]：2025 Mooncake 论文作者，与 [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]、[[university/清华大学/Mingxing Zhang|Mingxing Zhang]] 等共同构成清华 systems / HPC 上游作者网络。
- [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪（Jiahao Lu）]]：[[趋境科技]]：公开个人主页写明正在公司实习并参与 Mooncake 开发。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：[[Mooncake]]：2025 Mooncake 论文作者，连接 MADSys 与 Moonshot/Kimi production workload。
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：FAST 2025 论文作者与研究导师网络核心；清华官方报道明确将 [[university/清华大学/Ruoyu Qin|Ruoyu Qin]] 列为其指导学生。
- [[university/清华大学/Ruoyu Qin|秦若愚（Ruoyu Qin）]]：[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：FAST 2025 第一作者，连接清华 MADSys 与真实 Kimi production serving workload。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/月之暗面/月之暗面|月之暗面]]：公司页与社区/项目页均有显式记录；关系：`industry-academia-co-development`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
