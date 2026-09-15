---
type: project
name: HAMi
linked_people: []
companies: ["第四范式","密瓜智能","道客","NVIDIA","华为"]
company_relation: cross-company-maintainer-network
layer: kubernetes-heterogeneous-device-virtualization
open_source: true
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

## 生态关系
Kubernetes · CNCF ecosystem · [[AIBrix]] · [[llm-d]]。HAMi 解决的是设备资源供给与隔离，不等同于 vLLM/SGLang 的模型执行层。
