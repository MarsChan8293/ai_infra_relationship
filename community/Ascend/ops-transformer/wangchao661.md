---
type: person
name: wangchao661
aliases: ["@wangchao661"]
current_affiliations: ["华为"]
communities: [ops-transformer]
areas: [block-sparse-attention, mxfp4, quantization, inference-kernel]
confidence: verified
last_verified: "2026-09"
---
# wangchao661

公开 GitCode 信息可确认 handle 为 `wangchao661`；当前不猜测中文姓名。

## 当前关联
CANN `ops-transformer` 的公开 merge/commit metadata 多次记录 `wangchao661@huawei.com`，包括 BlockSparseAttention 的 FP8 / MXFP4 路径。因此本图谱将其当前组织关联记录为 [[company/华为/华为|华为]]。这只证明可核验的公司 affiliation，不据邮箱继续推断职级或内部汇报关系。

## 推理优化贡献
- 2026 年在 CANN `ops-transformer` 的 experimental attention 路径为 `BlockSparseAttention` 增加 MXFP4 能力，并扩展相关 aclnn 接口参数。
- 后续继续推进 FP8 per-head KV quantization / block-effective-row 等稀疏 attention 路径。
- 这些工作把稀疏 attention 与低比特量化落到同一 NPU kernel 路径，属于本图谱重点关注的 inference kernel × quantization 交叉点。

## 人物关系
- [[tangkaidi]]：**同一 BlockSparseAttention 技术线贡献者；2026**。tangkaidi 负责 A5 推理 BSND layout，wangchao661 推进 MXFP4 / FP8 量化能力；公开证据可确认同项目技术线，不扩展为直属或强直接关系。

## Sources
- https://gitcode.com/cann/ops-transformer
- https://gitcode.com/cann/ops-transformer/tree/master/experimental/attention
