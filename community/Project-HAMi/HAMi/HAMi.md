---
type: project
name: HAMi
status: active
repository: https://github.com/Project-HAMi/HAMi
docs: https://project-hami.io/
last_verified: "2026-09"
linked_people:
  - "community/Project-HAMi/HAMi/archlitchi"
  - "community/Project-HAMi/HAMi/chaunceyjiang"
  - "community/Project-HAMi/HAMi/DSFans2014"
  - "community/Project-HAMi/HAMi/wawa0210"
companies: ["第四范式","密瓜智能","道客","NVIDIA","华为"]
company_relation: cross-company-maintainer-network
layer: device-resource
areas:
  - "gpu-sharing"
  - "memory-isolation"
  - "device-plugin"
  - "heterogeneous-accelerators"
  - "topology-aware-allocation"
hardware:
  - "nvidia"
  - "ascend"
  - "cambricon"
  - "hygon"
  - "iluvatar"
  - "metax"
  - "moore-threads"
integrations:
  - "KAI-Scheduler"
  - "Kubernetes DRA"
linked_companies:
  - "company/NVIDIA/NVIDIA"
  - "company/华为/华为"
  - "company/密瓜智能/密瓜智能"
  - "company/第四范式/第四范式"
  - "company/道客/道客"
---
# HAMi

## 项目简介
HAMi 是 Kubernetes 上的异构加速器共享与虚拟化项目，重点解决 GPU/NPU 等设备的资源切分、调度、隔离和利用率问题。它位于模型 serving engine 之下、Kubernetes scheduler/device plugin 之上的资源层，因此与 LLM serving 的 autoscaling 和多租户部署天然相连。

## GitHub
https://github.com/Project-HAMi/HAMi

## 主要贡献公司
- [[company/第四范式/第四范式|第四范式]]：HAMi 的原始创建/早期项目来源（前身 k8s-vGPU-scheduler）。
- [[company/密瓜智能/密瓜智能|密瓜智能]]：当前 maintainer 网络中的重要公司节点。
- [[company/道客/道客|道客]]：云原生与 HAMi 社区的长期产业贡献方。
- [[company/NVIDIA/NVIDIA|NVIDIA]]：当前 maintainer / 异构加速器生态的重要产业贡献节点。
- [[company/华为/华为|华为]]：Huawei Cloud / Ascend 侧参与社区与异构设备生态贡献。

HAMi 当前是跨公司社区项目，上述边分别表示 originator、maintainer 或主要产业贡献，不表示任何一家拥有项目。

## 主要维护者 / 组织
由 Project-HAMi 社区维护。仓库中的 maintainer/长期贡献者节点包括 [[archlitchi]]、[[atttx123]]、[[chaunceyjiang]]、[[CoderTH]]、[[fyp711]]、[[gsakun]]、[[lengrongfu]]、[[ouyangluwei]]、[[peizhaoyou]]、[[wawa0210]]、[[whybeyoung]]、[[yangshiqi]]、[[yinyu]]、[[zhengbingxian]]。

## 设备插件 / 子项目
- [[community/Project-HAMi/ascend-device-plugin/ascend-device-plugin|HAMi Ascend Device Plugin]]：Ascend/vNPU 设备插件与调度扩展。其 OWNERS 明确记录 [[community/Project-HAMi/HAMi/archlitchi|Mengxuan Li]] 为 approver、[[community/Project-HAMi/HAMi/DSFans2014|DSFans2014]] 为 reviewer，因此单独实体化以承接治理关系。

## 生态关系
Kubernetes · CNCF ecosystem · [[AIBrix]] · [[llm-d]]。HAMi 解决的是设备资源供给与隔离，不等同于 vLLM/SGLang 的模型执行层。

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录；关系：`cross-company-maintainer-network`。
- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`cross-company-maintainer-network`。
- [[company/密瓜智能/密瓜智能|密瓜智能]]：公司页与社区/项目页均有显式记录；关系：`cross-company-maintainer-network`。
- [[company/第四范式/第四范式|第四范式]]：公司页与社区/项目页均有显式记录；关系：`cross-company-maintainer-network`。
- [[company/道客/道客|道客]]：公司页与社区/项目页均有显式记录；关系：`cross-company-maintainer-network`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/Project-HAMi/HAMi/archlitchi|Mengxuan Li]]：HAMi 官方 Maintainer。
- [[community/Project-HAMi/HAMi/chaunceyjiang|chaunceyjiang]]：[[HAMi]]：官方 AUTHORS 收录的贡献者；HAMi 仓库历史中可见持续贡献。AUTHORS 身份本身不自动等同于 maintainer 职级。
- [[community/Project-HAMi/HAMi/DSFans2014|DSFans2014]]：当前公开资料足以确认 GitHub handle 与 HAMi / Ascend 贡献关系，但未可靠确认实名和当前雇主，因此保留 handle 作为 canonical name。
- [[community/Project-HAMi/HAMi/wawa0210|Xiao Zhang]]：HAMi 官方 Maintainer。

<!-- END AUTO PROJECT PEOPLE -->
