---
type: project
name: Tutti
layer: kv-cache
open_source: true
repository: https://github.com/xPU-IO/Tutti
areas: [kv-cache, gpu-storage, nvme, ssd-offload, llm-serving, vllm-integration, storage-runtime, multi-vendor-gpu]
hardware: [NVIDIA GPU, MetaX GPU]
people:
  - "university/厦门大学/Shi Qiu"
  - "university/上海交通大学/张一鸣 Yiming Zhang"
governance: xPU-IO hosted project; public formal maintainer roster not yet specified
last_verified: "2026-09"
---
# Tutti

Tutti 是面向长上下文 LLM serving 的 GPU-centric、SSD-backed KV cache object store。它把 NVMe I/O 的关键控制与数据路径下沉到 GPU，让 CPU 主要负责按 layer 异步发起 I/O kernel，从而避免碎片化 KV cache 产生的大量小 I/O 把 CPU 变成瓶颈。

## 技术定位

论文《Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving》于 2026 年 5 月公开。论文报告相对 GDS-enabled、SSD-backed [[community/LMCache/LMCache/LMCache|LMCache]]，Tutti 在严格 SLO 下将 TTFT 降低 78.3%，可实现请求率提高 2 倍，serving cost 降低 27%。这些数字记录为论文实验结果，不外推到所有部署。

仓库当前实现包括 GPU io_uring、GPU-resident / host-pinned metadata cache、multi-device striping、`snvme` kernel module、vendor-neutral `cuda_like` abstraction，以及 [[community/vllm-project/vLLM/vLLM|vLLM]] KV connector。

## 技术血缘

- [[university/厦门大学/GeminiFS|GeminiFS]]：官方 GeminiFS 仓库已标记 deprecated，并明确指向 Tutti，说明 Tutti 基于 GeminiFS 的 GPU-centric storage 思路继续演进。
- [[community/LMCache/LMCache/LMCache|LMCache]]：论文主要 benchmark / alternative-system 对象，不写成 collaboration。
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：Tutti README 明确说明 `cuda_like` GPU-vendor framework 借鉴 Mooncake 的设计模式；这里记录 design-inspiration，不升级为共同治理。
- [[community/MetaX-MACA/vLLM-metax/vLLM-metax|vLLM-metax]]：并非 Tutti 的直接依赖；但 Tutti 已有明确 MetaX/MACA 适配，二者处于同一 MetaX LLM serving / accelerator 软件生态。

## 人物

- [[university/厦门大学/Shi Qiu|Shi Qiu]]：Tutti 第一作者；GitHub 账号 `qq502233945` 直接提交 vLLM KV connector baseline，README 也将其列为社区联系入口。
- [[university/上海交通大学/张一鸣 Yiming Zhang|张一鸣（Yiming Zhang）]]：Tutti 论文作者，NICE Lab 存储与系统研究网络核心教师。

## MetaX / MACA

Tutti PR #11 / 对应 merge commit 由 `ljye2023` 提交，公开提交邮箱为 `Lijing.Ye@metax-tech.com`，内容包括 MACA profile、libnvm compatibility 与 SNVMe P2P backend 适配。这只能证明明确的 MetaX/MACA 工程贡献，不自动推出 MetaX 对 Tutti 的项目所有权或治理权。

## Sources
- https://arxiv.org/abs/2605.03375
- https://github.com/xPU-IO/Tutti
- https://github.com/xPU-IO/Tutti/commit/8ffd81f294b85dadc80e40aa04a58b56d010bec7
- https://github.com/xPU-IO/Tutti/pull/11
- https://github.com/xPU-IO/Tutti/commit/2f1c7f91513f17cf157da5c159c635a71096d32c
- https://github.com/nicexlab/GeminiFS
