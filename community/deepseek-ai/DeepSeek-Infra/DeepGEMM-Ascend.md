---
type: project
name: DeepGEMM-Ascend
parent: DeepSeek-Infra
linked_concepts:
  - "concept/quantization/FP4 Quantization"
  - "concept/quantization/FP8 Quantization"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/gemm/Grouped GEMM"
  - "concept/kernel/programming/JIT Kernel Compilation"
status: active
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Anyi Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Chenhao Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Guanglin Li"
  - "community/deepseek-ai/DeepSeek-Infra/Huanqi Cao"
  - "community/deepseek-ai/DeepSeek-Infra/Kaifeng Chen"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/Ruifan Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Yuhao Meng"
  - "community/deepseek-ai/DeepSeek-Infra/Yunfan Xiao"
  - "community/deepseek-ai/DeepSeek-Infra/Yuxuan Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/Zhean Xu"
  - "community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
repository: https://github.com/deepseek-ai/DeepGEMM-Ascend
docs: https://github.com/deepseek-ai/DeepGEMM-Ascend
last_verified: "2026-10"
companies: ["深度求索"]
layer: runtime
areas:
  - "gemm"
  - "grouped-gemm"
  - "fp8"
  - "fp4"
  - "moe-kernels"
  - "mqa-logits"
  - "megamaoe"
  - "jit"
hardware:
  - "ascend"
integrations:
  - "DeepGEMM"
  - "DeepJIT"
  - "TileLang"
  - "CANN"
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepGEMM-Ascend

## 项目简介
DeepGEMM-Ascend 是 DeepSeek 于 2026-09-30 开源的 [[DeepGEMM]] Huawei Ascend 实现。它保持 DeepGEMM API / package / development workflow 兼容，覆盖 BF16、FP8、FP4 GEMM、MQA logits 与 MegaMoE，并针对 Ascend MAD、fractal layout、对齐约束、地址计算、稀疏数据加载和 coroutine pipeline 做专门优化。

## 首发平台与依赖
- 首发开发/验证平台：Ascend 950 series。
- 官方要求：CANN 9.20，提供 Bisheng 与 ld.lld；同时依赖 torch_npu。
- JIT runtime：[[DeepJIT]]。
- HC prenorm kernel：[[community/tile-ai/TileLang/TileLang|TileLang]]。
- 与上游 [[DeepGEMM]] 形成“同 API、不同硬件 backend”的关系，而不是新的 serving engine。

## 公开性能
官方 README 在 Ascend 950DT / CANN 9.20 上给出：dense GEMM 多种 dtype/shape 可接近硬件极限，示例最高报告到约 99.8% hardware limit；同时公开 FP8 inference、M-grouped GEMM、DeepSeek Lightning Indexer MQA logits、MegaMoE 与 mHC prenorm 的复现实验表。性能数字应与具体 shape、dtype、CANN 与设备型号绑定理解，不能泛化为所有 Ascend 设备。

## 与 DeepSeek 模型热路径
- **GEMM / Grouped GEMM**：覆盖 dense 与 MoE expert 计算。
- **MQA logits**：直接服务 DeepSeek Lightning Indexer，README 同时给出 FP8 / FP4 prefill 与 decode 工况。
- **MegaMoE**：融合 EP dispatch、两次 grouped GEMM、SwiGLU 与 combine。
- **mHC prenorm**：对应 Manifold-Constrained Hyper-Connections 路径。

## 公开贡献者
官方 README / citation 明确列出：
- Project Leads：[[周可行 Kexing Zhou|Kexing Zhou]]、[[Zhean Xu]]、[[赵成钢 Chenggang Zhao|Chenggang Zhao]]。
- GEMM：Kexing Zhou、Zhean Xu、[[Yunfan Xiao]]、[[Yuhao Meng]]。
- MQA logits：[[Anyi Xu]]、Zhean Xu、[[Kaifeng Chen]]。
- mHC：[[Yuxuan Zhou]]、Chenggang Zhao、[[Ruifan Xu]]、[[Huanqi Cao]]、[[Chenhao Xu]]。
- SF layout：[[Guanglin Li]]；Infrastructure：Kexing Zhou、[[Kuai Yu]]。

这些是项目/代码作者关系；不因出现在 deepseek-ai 仓库中就自动推断个人雇佣状态。

## 生态关系
[[DeepGEMM]] · [[DeepJIT]] · [[DeepEP-Ascend]] · [[FlashMLA]] · [[community/Ascend/Ascend/Ascend|Ascend]] · [[community/Ascend/CANN/CANN|CANN]] · [[community/tile-ai/TileLang/TileLang|TileLang]]

## Sources
- https://github.com/deepseek-ai/DeepGEMM-Ascend
- https://github.com/deepseek-ai/DeepJIT
- https://github.com/deepseek-ai/DeepGEMM

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Anyi Xu|Anyi Xu]]：[[DeepGEMM-Ascend]]：2026 official citation author；负责 MQA logits 路径。
- [[community/deepseek-ai/DeepSeek-Infra/Chenhao Xu|Chenhao Xu]]：[[DeepGEMM-Ascend]]：2026 official citation author；参与 mHC kernel。
- [[community/deepseek-ai/DeepSeek-Infra/Guanglin Li|Guanglin Li]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Huanqi Cao|Huanqi Cao]]：[[DeepGEMM-Ascend]]：2026 official citation author；参与 mHC kernel。
- [[community/deepseek-ai/DeepSeek-Infra/Kaifeng Chen|Kaifeng Chen]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]]：[[DeepGEMM-Ascend]]：2026 official citation author；Infrastructure contributor。
- [[community/deepseek-ai/DeepSeek-Infra/Ruifan Xu|Ruifan Xu]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Yuhao Meng|Yuhao Meng]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Yunfan Xiao|Yunfan Xiao]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Yuxuan Zhou|Yuxuan Zhou]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]]：[[DeepGEMM-Ascend]]：Project Lead；GEMM / MegaMoE contributor。
- [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行（Kexing Zhou）]]：[[DeepGEMM-Ascend]]：Project Lead；GEMM / infrastructure contributor。
- [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：[[DeepGEMM-Ascend]]：Project Lead；参与 mHC kernel。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/quantization/FP4 Quantization|FP4 Quantization]]
- [[concept/quantization/FP8 Quantization|FP8 Quantization]]
- [[concept/kernel/gemm/GEMM|GEMM]]
- [[concept/kernel/gemm/Grouped GEMM|Grouped GEMM]]
- [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
