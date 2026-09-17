---
type: project
name: DeepSelect
organization: DeepSeek-AI
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
  - "community/deepseek-ai/DeepSeek-Infra/Yi Qian"
companies: ["深度求索"]
company_relation: company-led
layer: sparse-attention-topk-kernels
open_source: true
repository: https://github.com/deepseek-ai/DeepSelect
areas: [topk, sparse-attention, sampling, cuda, gpu-kernels, deepseek-v4]
last_verified: "2026-09"
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepSelect

DeepSelect 是 DeepSeek 于 2026-09 开源的高性能 TopK kernel 库，直接服务于 DeepSeek Sparse Attention（DSA）的 Lightning Indexer 与 token sampling。官方 README 给出的目标场景覆盖 DeepSeek V3.2、V4、V4.1，并报告相对 `torch.topk` 的 2–20× 加速。

## 与刘胜与的关系
- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：官方 citation 三位作者之一；仓库提交还直接显示其以 `shengyuliu@deepseek.com` 提交 NaN checking 优化。
- [[community/deepseek-ai/DeepSeek-Infra/Yi Qian|Yi Qian]]：官方 citation 作者；GitHub commit 将实名 **Yi Qian** 映射到 `@skip2004`，并与刘胜与共同完成 DeepSelect algorithm / implementation analysis。
- Yichen Li：官方 citation 第三位作者；当前缺少足以稳定消歧的公开身份信息，本轮不强行建立人物节点。

## 技术位置
DeepSelect 把刘胜与的 kernel 路线从 MLA/GEMM 进一步延伸到 sparse-attention indexing 与 sampling。它不是通用排序库，而是针对 LLM 热路径中的小 TopK、特定 dtype / batch / vocabulary shape 做专门 kernel 设计。

## Sources
- https://github.com/deepseek-ai/DeepSelect
- https://github.com/deepseek-ai/DeepSelect/blob/main/README.md
- https://github.com/deepseek-ai/DeepSelect/commit/0f03b68748b304863fdf0181a11458d04ae533a9
- https://github.com/deepseek-ai/DeepSelect/commit/671e260b3ae8c5b12352dec063569b54d34e12b1
