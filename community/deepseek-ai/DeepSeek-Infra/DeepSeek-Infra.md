---
type: project-collection
name: DeepSeek Infra
company: 深度求索
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Anyi Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Chengqi Deng"
  - "community/deepseek-ai/DeepSeek-Infra/Chenhao Xu"
  - "community/deepseek-ai/DeepSeek-Infra/guyan364"
  - "community/deepseek-ai/DeepSeek-Infra/Jiashi Li"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/kurisu6912"
  - "community/deepseek-ai/DeepSeek-Infra/Liang Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Liyue Zhang"
  - "community/deepseek-ai/DeepSeek-Infra/LyricZhao"
  - "community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu"
  - "community/deepseek-ai/DeepSeek-Infra/Zhean Xu"
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
  - "community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
companies: [深度求索]
company_relation: company-led
layer: systems-stack
open_source: true
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepSeek Infra

## 项目简介
DeepSeek Infra 是 [[深度求索]] 对外开源的系统基础设施项目集合，不是一个单独代码库。它把模型训练与推理中的关键系统能力拆成通信、GPU kernel、attention、Expert Parallel 负载均衡、分布式存储、数据处理、profiling、serving protocol 与 JIT 等独立组件，形成从 MoE communication / kernel 到 storage / serving glue 的纵向技术栈。

## GitHub
组织主页：https://github.com/deepseek-ai

子项目：
- [[DeepEP]]：https://github.com/deepseek-ai/DeepEP
- [[DeepGEMM]]：https://github.com/deepseek-ai/DeepGEMM
- [[FlashMLA]]：https://github.com/deepseek-ai/FlashMLA
- [[3FS]]：https://github.com/deepseek-ai/3FS
- [[DeepJIT]]：https://github.com/deepseek-ai/DeepJIT\n- [[EPLB]]：https://github.com/deepseek-ai/EPLB\n- [[LPLB]]：https://github.com/deepseek-ai/LPLB\n- [[TileKernels]]：https://github.com/deepseek-ai/TileKernels\n- [[smallpond]]：https://github.com/deepseek-ai/smallpond\n- [[profile-data]]：https://github.com/deepseek-ai/profile-data\n- [[deepseek-recipe]]：https://github.com/deepseek-ai/deepseek-recipe

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：项目集合的发起、开源与主要维护组织；各子项目均单独保留公司归属与人物维护证据。

## 主要维护者 / 组织
由 DeepSeek / deepseek-ai 组织公开维护。各子项目的作者与维护网络独立记录，不把同属 DeepSeek Infra 自动等价为同一小组长期共事。

## 生态关系
[[vLLM]] · [[SGLang]] · [[FlashInfer]] · [[Mooncake]] · [[NIXL]]

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Anyi Xu|Anyi Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Chengqi Deng|Chengqi Deng]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Chenhao Xu|Chenhao Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/guyan364|guyan364]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：[[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：**DeepEP + DeepGEMM 共同作者**。2025 两人同时出现在两个项目的原始作者名单，合作关系覆盖 Expert Parallel communication 与 GEMM / MoE kernels。公开资料不足以确认雇佣起止与直属关系。
- [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/kurisu6912|kurisu6912]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Liyue Zhang|Liyue Zhang]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/LyricZhao|LyricZhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou|Shangyan Zhou]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu|Yuxuan Liu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：[[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]]：从 2025 MLA decode kernel 持续推进到 2026 DeepSeek V4.1；2026-09-10 直接提交 V4.1 attention kernels，覆盖 SM100 sparse prefill/decode、FP8 / FP4 KV cache，以及 fused norm + RoPE + attention + RoPE...
- [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行（Kexing Zhou）]]：[[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：**DeepGEMM 共同作者**。两人共同出现在 2025 DeepGEMM 原始公开作者名单；周可行偏 MLIR/compiler 与 GEMM，赵成钢同时横跨 DeepEP 与 MoE communication。关系仅按共同开源项目作者记录，雇佣关系公开未确认。
- [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：[[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：**DeepEP + DeepGEMM 共同作者**。两人同时出现在 2025 DeepEP 与 DeepGEMM 的原始公开作者名单，关系横跨 EP communication 与 GEMM/kernel 两层；公开资料不足以据此断言公司汇报关系。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
