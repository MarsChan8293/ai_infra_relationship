---
type: person
name: wangchao661
communities: [ops-transformer]
areas: [block-sparse-attention, mxfp4, quantization, inference-kernel]
---
# wangchao661

公开 GitCode 信息可确认 handle 为 `wangchao661`；当前不猜测中文姓名。

## 推理优化贡献
- 2026 年在 CANN `ops-transformer` 的 experimental attention 路径为 `BlockSparseAttention` 增加 MXFP4 能力，并扩展相关 aclnn 接口参数。
- 该工作把稀疏 attention 与低比特量化落到同一 NPU kernel 路径，属于本图谱重点关注的 inference kernel × quantization 交叉点。

## 人物关系
- [[tangkaidi]]：**同一 BlockSparseAttention 技术线贡献者；2026**。tangkaidi 负责 A5 推理 BSND layout，wangchao661 推进 MXFP4 量化能力；公开证据可确认同项目技术线，不扩展为直接共事结论。

## Sources
- https://gitcode.com/cann/ops-transformer/tree/master/experimental/attention
