---
type: project
name: Volcano
linked_people:
  - "community/volcano-sh/Volcano/Jesse Stutler"
  - "community/volcano-sh/Volcano/Kevin Wang"
  - "community/volcano-sh/Volcano/Klaus Ma"
  - "community/volcano-sh/Volcano/Liang Tang"
  - "community/volcano-sh/Volcano/Thor-wl"
  - "community/volcano-sh/Volcano/William-wang"
  - "community/volcano-sh/Volcano/Xavier Chang"
  - "community/volcano-sh/Volcano/Zhonghu Xu"
layer: scheduler
status: active
repository: https://github.com/volcano-sh/volcano
docs: https://volcano.sh/en/docs/
areas:
  - "batch-scheduling"
  - "gang-scheduling"
  - "queue"
  - "preemption"
  - "backfill"
  - "kubernetes"
integrations:
last_verified: "2026-09"
linked_companies: []
---
# Volcano

> 面向 AI、HPC 和 Batch 工作负载的 Kubernetes 批调度系统。

## 核心能力

| 能力 | 说明 |
|---|---|
| Gang Scheduling | 保证一组 Pod 满足条件后再运行 |
| Queue | 提供批任务队列与资源管理 |
| Preempt / Reclaim | 支持抢占和资源回收 |
| 插件式 Scheduler | 通过 action/plugin 扩展调度行为 |

## 边界

Volcano 重点是 batch/Pod 调度，不负责模型 inference routing、KV Cache 或 GPU kernel。

## 集成与后端

V0.1 暂不把生态适配自动视作强集成。

## 关联项目

- AI 调度器：KAI-Scheduler。
- Job admission / queue：Kueue。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方文档为快照。

## 当前维护者

Volcano 社区仓库维护一份 canonical MAINTAINERS.md，并明确标注 Current active Maintainers。本轮 DISCOVER 将当前 8 人完整编码为项目维护关系：

- [[community/volcano-sh/Volcano/Klaus Ma|Klaus Ma (@k82cn)]]：Maintainer；官方 roster affiliation：NVIDIA。
- [[community/volcano-sh/Volcano/Kevin Wang|Kevin Wang (@kevin-wangzefeng)]]：Maintainer；官方 roster affiliation：Huawei。
- [[community/volcano-sh/Volcano/Zhonghu Xu|Zhonghu Xu (@hzxuzhonghu)]]：Maintainer；官方 roster affiliation：Alibaba。
- [[community/volcano-sh/Volcano/Thor-wl|Thor-wl (@Thor-wl)]]：Maintainer；官方 roster affiliation：Hjmicro。
- [[community/volcano-sh/Volcano/William-wang|William-wang (@william-wang)]]：Maintainer；官方 roster affiliation：NVIDIA。
- [[community/volcano-sh/Volcano/Liang Tang|Liang Tang (@shinytang6)]]：Maintainer；官方 roster affiliation：Baidu。
- [[community/volcano-sh/Volcano/Xavier Chang|Xavier Chang (@Monokaix)]]：Maintainer；官方 roster affiliation：NVIDIA。
- [[community/volcano-sh/Volcano/Jesse Stutler|Jesse Stutler (@JesseStutler)]]：Maintainer；官方 roster affiliation：Huawei。

这里使用项目官方治理文件中的角色与 affiliation，不据此额外推断公司职级或汇报关系。

## 直接来源

- https://volcano.sh/en/docs/
- https://github.com/volcano-sh/volcano

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/volcano-sh/Volcano/Jesse Stutler|Jesse Stutler]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/Kevin Wang|Kevin Wang]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/Klaus Ma|Klaus Ma]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/Liang Tang|Liang Tang]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/Thor-wl|Thor-wl]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/William-wang|William-wang]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/Xavier Chang|Xavier Chang]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。
- [[community/volcano-sh/Volcano/Zhonghu Xu|Zhonghu Xu]]：[[community/volcano-sh/Volcano/Volcano|Volcano]]：Current active Maintainer。

<!-- END AUTO PROJECT PEOPLE -->
