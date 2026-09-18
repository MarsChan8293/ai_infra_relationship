---
type: project
name: DeepGEMM
parent: DeepSeek-Infra
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Anyi Xu"
  - "community/deepseek-ai/DeepSeek-Infra/guyan364"
  - "community/deepseek-ai/DeepSeek-Infra/Jiashi Li"
  - "community/deepseek-ai/DeepSeek-Infra/Liang Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/LyricZhao"
  - "community/deepseek-ai/DeepSeek-Infra/Zhean Xu"
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
  - "community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou"
companies: ["深度求索"]
company_relation: company-led
layer: gpu-kernels
open_source: true
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepGEMM

## 项目简介
DeepGEMM 是 DeepSeek 开源的高性能 GEMM/MoE kernel 项目，覆盖 FP8/FP4、grouped GEMM 与大规模 MoE 执行等路径。它展示了模型低精度与专家混合设计如何被落实到可复用 GPU kernel。

## GitHub
https://github.com/deepseek-ai/DeepGEMM

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。公开作者网络包括 [[赵成钢 Chenggang Zhao]]、[[Zhean Xu]]、[[Liang Zhao]]、[[Jiashi Li]]、[[Chenhao Xu]]、[[Anyi Xu]]、[[刘胜与 Shengyu Liu]]、[[周可行 Kexing Zhou]]、[[Kuai Yu]]。

## 生态关系
[[FlashInfer]] · [[vLLM]] · [[SGLang]] · [[DeepEP]] · [[DeepJIT]]。DeepGEMM 位于 GPU kernel 层，与 serving engine 是上下游而非同层竞争。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Anyi Xu|Anyi Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/guyan364|guyan364]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：[[DeepGEMM]]：2025 原始公开作者
- [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/LyricZhao|LyricZhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]]：公开作者，GEMM / MoE kernel 技术线。
- [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行（Kexing Zhou）]]：[[DeepGEMM]]：2025 原始公开作者

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
