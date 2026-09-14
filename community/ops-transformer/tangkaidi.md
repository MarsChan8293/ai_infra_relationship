---
type: person
name: tangkaidi
communities: [ops-transformer]
areas: [block-sparse-attention, ascend, inference-kernel]
---
# tangkaidi

公开 GitCode 信息可确认 handle 为 `tangkaidi`；当前不依据邮箱或拼音猜测中文姓名。

## 推理优化贡献
- 2026 年在 CANN `ops-transformer` 推进 A5 推理 `BlockSparseAttention` 的 BSND input layout 支持，使推理算子 layout 能力继续向训练侧已有格式对齐。
- 该贡献位于 attention kernel / operator 层，直接属于昇腾推理执行路径，而不是普通模型接入。

## 人物关系
- [[Konstantin Berestizshevsky]]：**同一 CANN attention kernel 社区贡献者；2026**。二人分别覆盖 Quest sparse predictor 与 BlockSparseAttention 执行算子，处在可串联的稀疏 attention pipeline；尚未确认直接共同 MR。

## Sources
- https://gitcode.com/cann/ops-transformer
