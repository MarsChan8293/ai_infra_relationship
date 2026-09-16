---
type: project
name: openYuanRong
aliases: [YuanRong, 元戎]
linked_people:
  - "community/openEuler/openYuanRong/梁义 Yi Liang"
  - "community/openEuler/openYuanRong/罗站城 Zhancheng Luo"
companies: ["华为"]
company_relation: company-originated-open-source
layer: distributed-compute-runtime
open_source: true
repository: https://github.com/openyuanrong/runtime
areas: [serverless, distributed-runtime, scheduling, distributed-data, ai-infrastructure, reinforcement-learning, inference]
people:
  - "community/openEuler/openYuanRong/梁义 Yi Liang"
  - "community/openEuler/openYuanRong/罗站城 Zhancheng Luo"
related_projects: ["YuanRong DataSystem", "YuanRong TransferEngine", "TransferQueue", "vLLM-Ascend", "vLLM-Omni"]
last_verified: "2026-09"
linked_companies:
  - "company/华为/华为"
---
# openYuanRong

## 项目定位
openYuanRong 是 OpenAtom openEuler 社区中的 Serverless 分布式计算引擎。它以统一的函数抽象、分布式动态调度和数据共享能力承载 AI、大数据、微服务等工作负载，核心由多语言 runtime、function system 与 data system 组成。

项目的前身 YuanRong 来自华为生产系统。SIGCOMM 2024 论文披露其已在华为多个数据中心区域长期运行；openEuler 社区在 2025 年底将 openYuanRong 正式开源，因此本图谱把它记录为“华为起源、openEuler 社区治理”的开源基础设施，而不是当前华为私有项目。

## AI Infra 价值
- [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]]：HBM / DRAM / SSD 近计算多级缓存与异构数据传输，已进入 Ascend 推理和 RL 数据面。
- [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]]：用于 Ascend NPU 的点对点数据 / 权重 / KV 传输；当前已被 vLLM-Ascend RFork 与 vLLM-Omni connector 使用。
- [[community/Ascend/TransferQueue/TransferQueue|TransferQueue]]：其首个 KV storage backend 即 openYuanRong DataSystem，连接 post-training / veRL 数据流。
- [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]：KV Pool 可以选择 YuanRong DataSystem backend，RFork 则直接安装 YuanRong TransferEngine。
- [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]]：当前实现同时提供 YuanrongConnector 与 Ascend NPU 专用 YuanrongTransferEngineConnector。

## 治理
openEuler `sig-YuanRong` 负责项目演进与维护。截至 2026-09，SIG 页面列出 [[community/openEuler/openYuanRong/梁义 Yi Liang|梁义（Yi Liang）]] 与 [[community/openEuler/openYuanRong/罗站城 Zhancheng Luo|罗站城（Zhancheng Luo）]] 两位 Maintainer；各子仓还有更多 repository-level maintainer / committer，本轮不把所有仓库权限成员机械升级为核心人物。

## Sources
- https://www.openeuler.org/zh/projects/yuanrong/
- https://www.openeuler.org/zh/sig/sig-YuanRong
- https://github.com/openyuanrong/runtime
- https://doi.org/10.1145/3651890.3672216
- https://www.openeuler.org/zh/news/20260509-April%20Monthly%20Report/20260509-April%20Monthly%20Report.html
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/rfork.html
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_pool.html
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/omni_connectors/yuanrong_transfer_engine_connector/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/openEuler/openYuanRong/梁义 Yi Liang|梁义（Yi Liang）]]：openEuler `sig-YuanRong` 当前两位 Maintainer 之一，AtomGit ID `liangyi1234`。
- [[community/openEuler/openYuanRong/罗站城 Zhancheng Luo|罗站城（Zhancheng Luo）]]：openEuler `sig-YuanRong` 当前两位 Maintainer 之一，AtomGit ID `luozhancheng`。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-originated-open-source`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
