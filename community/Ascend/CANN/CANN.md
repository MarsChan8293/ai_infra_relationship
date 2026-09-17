---
type: project
name: CANN
organization: Ascend
linked_people: []
companies: ["华为"]
company_relation: company-led
layer: ai-compute-software-stack
open_source: true
linked_companies:
  - "company/华为/华为"
---
# CANN

CANN（Compute Architecture for Neural Networks）是华为昇腾 AI 计算软件栈的核心层，连接 Ascend NPU 与上层框架、算子、编译、通信和推理运行时。

## 开源位置
- 2025 年华为宣布 CANN 全面开源开放，并成立技术指导委员会。
- 开源范围逐步覆盖算子库、领域加速库、图计算、Ascend C 与相关工具链。
- 与 PyTorch、Triton、TileLang、vLLM、verl 等上游社区形成硬件后端与软件栈协作。

## 图谱关系
[[community/Ascend/CANN/ops-transformer|ops-transformer]] 是 CANN 面向 Transformer / LLM 的算子与 kernel 线；[[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]、MindIE、MemCache 等处于更上层的 serving / cache / runtime 生态。

## 治理发现
CANN 采用分层治理，而不是一个扁平的全项目 maintainer 名单：社区层有 TSC / PMC，具体代码职责继续下沉到 SIG、repository、branch / directory / file。官方治理仓库明确区分 TC、SIG Maintainers、Committers、Reviewers 等角色；例如 Ascend C SIG 单独公开自己的 Maintainer 列表。

因此这轮 DISCOVER **不把 TSC 成员自动写成 CANN umbrella maintainer**。TSC 能证明项目级技术治理，但不能替代具体仓库 / SIG 的维护 ownership。后续要补 `linked_people`，应从 CANN community 的 `org-info.yaml` / `sig-info.yaml` / repo ownership 配置按具体子项目逐层解析，再与本图谱的推理热点（ops-transformer、graph engine、runtime 等）对齐。

## Sources
- https://www.huawei.com/cn/news/2025/8/ascend-summit-CANN-open-source
- https://www.huawei.com/cn/news/2025/9/hc-shengten-opensource
- https://www.huawei.com/cn/news/2026/3/mwc-superpod-computing
- https://gitcode.com/cann
- https://gitcode.com/Ascend/community/tree/master
- https://gitcode.com/Ascend/community/tree/master/TSC
- https://gitcode.com/cann/community/tree/master/CANN/sigs/ascendc

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
