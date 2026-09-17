---
type: project
name: lmcache-iluvatar
organization: Deep-Spark
companies: ["天数智芯"]
company_relation: company-originated
layer: kv-cache-hardware-plugin
open_source: true
linked_companies:
  - "company/天数智芯/天数智芯"
---
# lmcache-iluvatar

lmcache-iluvatar 是 2026-09 新公开的 Iluvatar / CoreX 硬件插件，用于让 [[LMCache]] 与 vLLM 在天数智芯 CoreX 环境上运行。

它直接把 `LMCache → vLLM → CoreX / 天数 GPU` 连成一条 KV Cache 硬件适配边，是 DeepSpark 推理生态里非常贴近本仓库主题的新节点。

## Sources
- https://github.com/Deep-Spark/lmcache-iluvatar
