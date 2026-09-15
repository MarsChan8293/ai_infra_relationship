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
linked_companies:
  - "company/月之暗面/月之暗面"
---
# Mooncake

## 项目简介
Mooncake 是面向 LLM serving 的 KVCache-centric 分布式系统，核心思想是把 prefill/decode 解耦后的 KV cache 作为一级系统资源管理，并利用 CPU DRAM、SSD、NIC 等资源构建分布式 KV 存储与传输路径。它来自清华 MADSys 与 Moonshot/Kimi 的产学协作，并获得 FAST 2025 Best Paper。

## GitHub
https://github.com/kvcache-ai/Mooncake

## 主要贡献公司
- [[company/月之暗面/月之暗面|月之暗面]]：真实 Kimi production serving workload 与工程共研的重要产业方；与清华 MADSys 共同构成 Mooncake 的产学协作起源。项目当前由 KVCache.AI 社区维护，因此不写成 Moonshot 单一公司治理。

## 主要维护者 / 组织
由 KVCache.AI 社区维护，研究/工程网络连接清华大学 MADSys 与 [[月之暗面]]。公开论文作者包括 [[university/清华大学/Ruoyu Qin|Ruoyu Qin]]、Zheming Li、Weiran He、Jialei Cui、Heyi Tang、[[任峰 Feng Ren]]、[[马腾 Teng Ma]]、[[Shangming Cai]]、[[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]、[[university/清华大学/Mingxing Zhang|Mingxing Zhang]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]、[[company/清程极智/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]]、Xinran Xu。

## 人才桥
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：Mooncake 论文作者，同时在 2024–2025 为 [[SGLang]] core maintainer、也是 [[FlashInfer]] 论文作者；2025-07 加入 [[Together AI]]，2026-03 co-create [[TokenSpeed]]。因此他把 Mooncake 的 KVCache-centric serving 网络直接连到 kernel、serving engine 与 production inference。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]、[[company/清程极智/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]]、[[university/清华大学/Mingxing Zhang|Mingxing Zhang]]：共同构成清华 systems / HPC 上游学术网络；只按论文/实验室证据建边，不从同实验室身份自动推断所有导师学生关系。

## 生态关系
[[SGLang]] · [[vLLM]] · [[LMCache]] · [[NIXL]] · [[KTransformers]] · [[TokenSpeed]] · [[清华大学]] · [[月之暗面]]。这是清华系 AI infra 中连接学术系统研究与真实 Kimi serving workload 的关键项目。

## Sources
- https://github.com/kvcache-ai/Mooncake
- https://zhyncs.com/

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
