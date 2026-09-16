---
type: person
name: Konstantin Berestizshevsky
aliases: [kostyab]
current_affiliations: ["华为"]
schools: ["Tel Aviv University"]
communities: [ops-transformer]
roles: [Senior Researcher]
areas: [ascendc, sparse-attention, kv-cache, llm-decoding]
confidence: verified
last_verified: "2026-09"
---
# Konstantin Berestizshevsky

GitCode handle：`kostyab`。

## 当前关联
个人学术主页明确写明其当前为 **Senior Researcher at Huawei in Zurich**，并列出 2021 年至今从 intern、postdoc 到 Senior Researcher 的 Huawei Zurich Research Center / Computing Systems Lab 经历。因此本图谱将其当前 affiliation 记录为 [[company/华为/华为|华为]]。

其主页也明确列出 Tel Aviv University 的博士、硕士和本科学习经历；这里仅记录学校关联，不据同校自动推断人物关系。

## 推理优化贡献
- 2026 年在 CANN `ops-transformer` 贡献 Quest-based block-sparse attention predictor 的 AscendC kernel。
- `quest_block_select_paged` 在 decode 阶段按 KV head 选择 top-k KV-cache blocks，并复用与 vLLM-Ascend KV cache 相同的 page / metadata 格式。
- 公开 MR 给出的 benchmark 显示 predictor 相比普通 Python / torch_npu 路径约快 20×–300×；后续计划是把预测结果接到 sparse `npu_paged_attention`，减少 attention 实际计算量。

## 人物关系
- [[vLLM-Ascend]]：**技术上下游关系；2026**。该 kernel 明确兼容 vLLM-Ascend 的 KV-cache page 格式，但不能仅据此推断与 vLLM-Ascend 维护者存在直接共事关系。
- [[tangkaidi]]：**同一 CANN attention kernel 社区贡献者；2026**。二人均在 `ops-transformer` 的稀疏 attention / BlockSparseAttention 技术层贡献；尚未确认直接共同 MR。

## Sources
- https://sites.google.com/view/kostya-phd/home
- https://gitcode.com/cann/ops-transformer/tree/master/experimental/select_attention_operators
