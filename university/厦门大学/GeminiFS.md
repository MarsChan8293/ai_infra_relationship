---
type: project
name: GeminiFS
layer: gpu-storage
open_source: true
repository: https://github.com/nicexlab/GeminiFS
areas: [gpu-storage, filesystem, nvme, direct-storage, ml-systems, llm-storage]
people:
  - "university/厦门大学/Shi Qiu"
  - "university/上海交通大学/张一鸣 Yiming Zhang"
governance: NICE Lab research project; upstream repository is deprecated in favor of Tutti
last_verified: "2026-09"
---
# GeminiFS

GeminiFS 是面向 GPU 的 companion file system，发表于 USENIX FAST 2025。它让 GPU 程序以文件抽象直接访问 NVMe storage，同时由 host file system 负责存储管理，并通过 GPU-friendly page cache、并行 CPU/GPU control plane 与 `libGemini` 降低 GPU storage 编程复杂度。

## 与 Tutti 的技术血缘

官方 `nicexlab/GeminiFS` README 已明确标记仓库 deprecated，并指出新的 GPU-centric KV Storage [[community/xPU-IO/Tutti/Tutti|Tutti]] 基于 GeminiFS 的思想演进。因此这里记录 **GeminiFS → Tutti** 为直接 research / technical lineage，而不是仅仅“相似项目”。

作者网络也存在连续性：[[university/厦门大学/Shi Qiu|Shi Qiu]]、Yifan Hu、Jianqin Yan 与 [[university/上海交通大学/张一鸣 Yiming Zhang|张一鸣（Yiming Zhang）]] 同时出现在 GeminiFS 与 Tutti 作者列表中。

## 机构

FAST 2025 官方页面将 Shi Qiu、Weinan Liu、Yifan Hu、Jianqin Yan、Zhirong Shen 标为 NICE Lab, Xiamen University；Yiming Zhang 的 affiliation 同时包含 NICE Lab, Xiamen University 与 Shanghai Jiao Tong University。这里不因为共同论文 affiliation 自动推断所有作者当前任职状态。

## Sources
- https://www.usenix.org/conference/fast25/presentation/qiu
- https://github.com/nicexlab/GeminiFS
- https://arxiv.org/abs/2605.03375
