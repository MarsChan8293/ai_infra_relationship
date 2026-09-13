---
type: project
name: HAMi
layer: kubernetes-heterogeneous-device-virtualization
open_source: true
---
# HAMi

## 项目简介
HAMi 是 Kubernetes 上的异构加速器共享与虚拟化项目，重点解决 GPU/NPU 等设备的资源切分、调度、隔离和利用率问题。它位于模型 serving engine 之下、Kubernetes scheduler/device plugin 之上的资源层，因此与 LLM serving 的 autoscaling 和多租户部署天然相连。

## GitHub
https://github.com/Project-HAMi/HAMi

## 主要维护者 / 组织
由 Project-HAMi 社区维护。仓库中的 maintainer/长期贡献者节点包括 [[archlitchi]]、[[atttx123]]、[[chaunceyjiang]]、[[CoderTH]]、[[fyp711]]、[[gsakun]]、[[lengrongfu]]、[[ouyangluwei]]、[[peizhaoyou]]、[[wawa0210]]、[[whybeyoung]]、[[yangshiqi]]、[[yinyu]]、[[zhengbingxian]]。

## 生态关系
Kubernetes · CNCF ecosystem · [[AIBrix]] · [[llm-d]]。HAMi 解决的是设备资源供给与隔离，不等同于 vLLM/SGLang 的模型执行层。
