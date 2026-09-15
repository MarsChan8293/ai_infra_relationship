---
type: project
name: DeepSpec
companies: ["深度求索"]
company_relation: company-led
layer: speculative-decoding
open_source: true
repository: https://github.com/deepseek-ai/DeepSpec
areas: [llm-inference, speculative-decoding, draft-model, inference-acceleration]
last_verified: "2026-09"
---
# DeepSpec

## 项目简介
DeepSpec 是 [[company/深度求索/深度求索|深度求索]] / deepseek-ai 公开维护的 speculative decoding 全栈代码库，覆盖数据准备、draft model 训练、模型实现与评测。当前仓库支持 DSpark、DFlash 与 Eagle3 等 draft-model 路线。

## DSpark 作者网络
DeepSpec README 给出的 DSpark 论文作者网络包含：
- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：从 MADSys / KTransformers / DualPath 延伸到 speculative decoding。
- [[company/深度求索/梁文锋 Liang Wenfeng|梁文锋（Wenfeng Liang）]]：DeepSeek 创始人与 DSpark 作者网络成员。
- 其他作者还包括 Xin Cheng、Jiashi Li、Yixuan Tan、Wentao Zhang、Anyi Xu 等 DeepSeek 研究人员。

这里仅按公开论文作者 / 项目维护证据建边，不把全部作者自动视为同一直属团队。

## 技术定位
DeepSpec 关注通过 draft model 提高 token generation 效率。DSpark 使用 confidence-scheduled speculative decoding 与 semi-autoregressive generation，属于推理执行层的直接加速路径，与 [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]]、[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 等 kernel 层项目互补。

## 图谱意义
对章明星 BFS 而言，DeepSpec 是 `Shaoyuan Chen → DeepSeek speculative decoding → Wenfeng Liang / DeepSeek research network` 的第三跳，使 MADSys 人才迁移不只停留在“去了 DeepSeek”，而能继续落到具体 inference 技术项目。

## Sources
- https://github.com/deepseek-ai/DeepSpec
- https://github.com/deepseek-ai/DeepSpec/blob/main/README.md
- https://arxiv.org/abs/2607.05147
