---
type: project
name: vLLM-Omni
linked_people:
  - "community/vllm-project/vLLM-Omni/Canlin Guo"
  - "community/vllm-project/vLLM-Omni/Gao Han"
  - "community/vllm-project/vLLM-Omni/Hongsheng Liu"
  - "community/vllm-project/vLLM-Omni/Yongxiang Huang"
  - "community/vllm-project/vLLM/Roger Wang"
  - "university/香港中文大学/James Cheng"
  - "university/香港中文大学/Peiqi Yin"
layer: multimodal-serving
open_source: true
repository: https://github.com/vllm-project/vllm-omni
areas: [multimodal-inference, disaggregated-inference, diffusion-serving, realtime-serving, data-transfer, reinforcement-learning, npu, serving]
people:
  - "community/vllm-project/vLLM/Roger Wang"
  - "community/vllm-project/vLLM-Omni/Gao Han"
  - "community/vllm-project/vLLM-Omni/Hongsheng Liu"
  - "community/vllm-project/vLLM-Omni/Canlin Guo"
  - "community/vllm-project/vLLM-Omni/Yongxiang Huang"
  - "university/香港中文大学/Peiqi Yin"
  - "university/香港中文大学/James Cheng"
related_projects: ["vLLM", "vLLM-Ascend", "MindIE-SD", "YuanRong DataSystem", "YuanRong TransferEngine", "Mooncake", "VeRL-Omni", "LiveServe"]
last_verified: "2026-09"
linked_companies: []
---
# vLLM-Omni

## 项目定位
vLLM-Omni 是 vLLM 生态面向 **any-to-any omni-modality models** 的推理与 serving 系统。它不只是“多模态版 vLLM”：2026 论文的核心是把由 autoregressive LLM、Diffusion Transformer 等不同计算范式组成的复杂模型拆成 stage graph，每个 stage 独立 serving，并通过统一 inter-stage connector 和动态资源分配实现 fully-disaggregated execution。

官方 README 当前强调三类性能机制：
- vLLM 的高效 KV cache / autoregressive runtime；
- 多 stage pipelined execution overlap；
- 基于 OmniConnector 的 fully disaggregation 与动态 stage resource allocation。

论文报告相对 baseline 的 job completion time 最高降低 91.4%。

## 官方治理
2026-09 官方 governance 的三位 Lead Maintainer：
- [[community/vllm-project/vLLM-Omni/Gao Han|Gao Han / @Gaohan123]]：overall direction、AR runtime / modality contracts 等核心路径。
- [[community/vllm-project/vLLM-Omni/Hongsheng Liu|Hongsheng Liu / @hsliuustc0106]]：overall direction、roadmap、production / hardware portability。
- [[community/vllm-project/vLLM/Roger Wang|Roger Wang / @ywang96]]：vLLM / vLLM-Omni 跨项目治理与 multimodality bridge。

高价值 Active Committer：
- [[community/vllm-project/vLLM-Omni/Canlin Guo|Canlin Guo / @gcanlin]]：Hardware plugin、NPU integration、TTS；是 Ascend 方向主要 bridge。
- [[community/vllm-project/vLLM-Omni/Yongxiang Huang|Yongxiang Huang / @SamitHuang]]：RL、Diffusion、cache；同时是 VeRL-Omni Lead Maintainer。

官方 governance 明确声明 committer status 属于个人而不是公司，因此即使 Gao Han / Hongsheng Liu 当前均有华为 affiliation，也不把 vLLM-Omni 建模为华为公司项目。

## Ascend / NPU 线
- [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]：AR / NPU 基础依赖；vLLM-Omni NPU roadmap 明确与其版本和 ModelRunner 路线协同。
- [[MindIE-SD]]：作为 Ascend-optimized diffusion operator library，通过 FlashAttentionBackend / CustomOp 等路径为 diffusion models 提供 NPU-native operator。
- [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]]：`YuanrongConnector` 分布式 store backend。
- [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]]：`YuanrongTransferEngineConnector` 在 Ascend NPU 上做跨 stage P2P data transfer。

## RL / post-training 线
[[community/verl-project/VeRL-Omni/VeRL-Omni|VeRL-Omni]] 把 vLLM-Omni 直接作为 multimodal / diffusion RL rollout backend，并围绕 request-level / step-wise batching、rollout routing、embed caching 等优化 post-training throughput。这个连接把 vLLM-Omni 从纯 inference serving 延伸到 `rollout → reward → training` 闭环。

## Realtime serving 线
[[university/香港中文大学/Peiqi Yin|尹沛骐（Peiqi Yin）]] 是 vLLM-Omni 论文第一作者。其后续 [[university/香港中文大学/LiveServe|LiveServe]] 工作直接建立在 vLLM-Omni 上，把 playback progress、speech activity 与 barge-in 纳入 scheduling / KV management，形成 realtime omni-modal serving 的下一层系统优化。

## YuanRong 连接
当前代码和文档已经同时提供两条 YuanRong 路径：
- `YuanrongConnector`：使用 [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 作为分布式 KV store。
- `YuanrongTransferEngineConnector`：使用 [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]] 做 Ascend NPU P2P transfer，直接管理 NPU memory pool。

这不是早期 RFC 的占位关系；connector factory 与 API 文档已注册并公开对应实现。

## Sources
- https://github.com/vllm-project/vllm-omni
- https://github.com/vllm-project/vllm-omni/blob/main/docs/community/governance.md
- https://github.com/vllm-project/vllm-omni/blob/main/.github/CODEOWNERS
- https://arxiv.org/abs/2602.02204
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/disaggregated_inference/
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/omni_connectors/yuanrong_transfer_engine_connector/
- https://github.com/vllm-project/vllm-omni/issues/886
- https://github.com/vllm-project/vllm-omni/issues/2223
- https://github.com/verl-project/verl-omni
- https://arxiv.org/abs/2606.22983

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/vllm-project/vLLM-Omni/Canlin Guo|Canlin Guo]]：2026 Q1 / Q2 NPU roadmap 的主要推动者，公开路线明确写出 vLLM-Omni NPU 支持依赖 [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]，并把 [[MindIE-SD]] 作为 Ascend-optimized diffusion operator library 接入 FlashAttentionBackend / CustomOp 路径。
- [[community/vllm-project/vLLM-Omni/Gao Han|Gao Han]]：vLLM-Omni 2026 论文作者（论文署名 `Han Gao`）。
- [[community/vllm-project/vLLM-Omni/Hongsheng Liu|Hongsheng Liu]]：vLLM-Omni 2026 fully-disaggregated serving 论文作者。
- [[community/vllm-project/vLLM-Omni/Yongxiang Huang|Yongxiang Huang]]：https://github.com/vllm-project/vllm-omni/blob/main/docs/community/governance.md
- [[community/vllm-project/vLLM/Roger Wang|Roger Wang]]：https://github.com/vllm-project/vllm-omni
- [[university/香港中文大学/James Cheng|James Cheng]]：[[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]]：2026 fully-disaggregated any-to-any multimodal serving 论文作者。
- [[university/香港中文大学/Peiqi Yin|尹沛骐（Peiqi Yin）]]：[[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]]：2026 论文第一作者。该系统把复杂 any-to-any multimodal model 拆成 stage graph，并通过独立 stage serving、动态资源分配与统一 connector 做 fully-disaggregated serving。

<!-- END AUTO PROJECT PEOPLE -->
