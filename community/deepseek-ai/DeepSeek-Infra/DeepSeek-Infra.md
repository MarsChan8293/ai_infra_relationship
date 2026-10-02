---
type: project-collection
name: DeepSeek Infra
company: 深度求索
status: active
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Anyi Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Chengqi Deng"
  - "community/deepseek-ai/DeepSeek-Infra/Chenhao Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Chenqi Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Guanglin Li"
  - "community/deepseek-ai/DeepSeek-Infra/guyan364"
  - "community/deepseek-ai/DeepSeek-Infra/Huanqi Cao"
  - "community/deepseek-ai/DeepSeek-Infra/Jiashi Li"
  - "community/deepseek-ai/DeepSeek-Infra/Kaifeng Chen"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/kurisu6912"
  - "community/deepseek-ai/DeepSeek-Infra/Liang Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Liyue Zhang"
  - "community/deepseek-ai/DeepSeek-Infra/LyricZhao"
  - "community/deepseek-ai/DeepSeek-Infra/Rui Tian"
  - "community/deepseek-ai/DeepSeek-Infra/Ruifan Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Runji Wang"
  - "community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/Weilin Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Xiangwen Wang"
  - "community/deepseek-ai/DeepSeek-Infra/Yiliang Xiong"
  - "community/deepseek-ai/DeepSeek-Infra/Yizhi Wang"
  - "community/deepseek-ai/DeepSeek-Infra/Yuhao Meng"
  - "community/deepseek-ai/DeepSeek-Infra/Yunfan Xiao"
  - "community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu"
  - "community/deepseek-ai/DeepSeek-Infra/Yuxuan Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/Zhean Xu"
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
  - "community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
repository: https://github.com/deepseek-ai
last_verified: "2026-10"
companies: [深度求索]
company_relation: company-led
layer: ecosystem
linked_companies:
  - "company/深度求索/深度求索"
areas:
  - "ai-infrastructure"
  - "kernel-optimization"
  - "communication"
  - "storage"
integrations: []
---
# DeepSeek Infra

## 项目简介
DeepSeek Infra 是 [[深度求索]] 对外开源的系统基础设施项目集合，不是一个单独代码库。它把模型训练与推理中的关键系统能力拆成通信、GPU kernel、attention、Expert Parallel 负载均衡、分布式存储、数据处理、profiling、serving protocol 与 JIT 等独立组件，形成从 MoE communication / kernel 到 storage / serving glue 的纵向技术栈。

## GitHub
组织主页：https://github.com/deepseek-ai

官方 Open Infra 索引：https://github.com/deepseek-ai/open-infra-index

子项目：
- [[DeepEP]]：https://github.com/deepseek-ai/DeepEP
- [[DeepEP-Ascend]]：https://github.com/deepseek-ai/DeepEP-Ascend
- [[DeepGEMM]]：https://github.com/deepseek-ai/DeepGEMM
- [[DeepGEMM-Ascend]]：https://github.com/deepseek-ai/DeepGEMM-Ascend
- [[FlashMLA]]：https://github.com/deepseek-ai/FlashMLA
- [[3FS]]：https://github.com/deepseek-ai/3FS
- [[DeepJIT]]：https://github.com/deepseek-ai/DeepJIT
- [[clangd-ascend]]：https://github.com/deepseek-ai/clangd-ascend
- [[EPLB]]：https://github.com/deepseek-ai/EPLB
- [[LPLB]]：https://github.com/deepseek-ai/LPLB
- [[TileKernels]]：https://github.com/deepseek-ai/TileKernels
- [[smallpond]]：https://github.com/deepseek-ai/smallpond
- [[profile-data]]：https://github.com/deepseek-ai/profile-data
- [[DualPipe]]：https://github.com/deepseek-ai/DualPipe
- [[deepseek-recipe]]：https://github.com/deepseek-ai/deepseek-recipe

## 2026-09-30 Ascend 推理基础设施开源
DeepSeek 将一组关键推理组件扩展到 Huawei Ascend：[[DeepGEMM-Ascend]] 负责 GEMM / MegaMoE / MQA logits kernel，[[DeepEP-Ascend]] 负责 MoE Expert Parallel 通信，[[FlashMLA]] 增加 DeepSeek Sparse Attention 的 Ascend prefill/decode kernel，[[DeepJIT]] 提供 CUDA/Ascend 统一 JIT runtime，[[clangd-ascend]] 补齐 AscendC 的代码补全、诊断与导航工具。整体形成“开发工具 → JIT/compiler → compute kernel / attention kernel → EP communication”的 Ascend 软件链，并与 [[community/Ascend/Ascend/Ascend|Ascend]] / CANN / HCCL/HCOMM / UBMEM / URMA 连接。

## DeepSeek 2026 其他系统线
本次 DISCOVER 还发现了不应硬塞进 Open Infra 2025 子项目列表、但对 AI Infra 很重要的独立项目：
- [[community/deepseek-ai/DeepSeek-Harness/DeepSeek-Harness|DeepSeek Harness (dsh)]]：everything-is-a-plugin 的 agent harness / runtime，基于 [[community/cordiverse/Cordis/Cordis|Cordis]]，提供 Web/headless/SDK/ACP profiles、MCP、sandbox、session event log 与可替换 model/tool/agent-loop seams。
- [[community/deepseek-ai/Engram/Engram|Engram]]：Conditional Memory / scalable lookup 模块；官方实现强调 deterministic addressing 与 host-memory offload，和 [[DeepEP-Ascend]] 暴露的 EngramBuffer / remote-memory data plane 形成模型机制 ↔ 通信基础设施连接。
- [[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]]：speculative decoding 全栈。
- [[community/deepseek-ai/DualPath/DualPath|DualPath]]：agentic inference / disaggregated KV-cache storage I/O 研究线。

`awesome-deepseek-agent` 是 curated ecosystem index，本轮不把它当作独立 runtime；`dsh-libreoffice-kit` 与 `dsh-node-addon-require-builtin` 是 Harness 内部组件，也不提升为顶级 canonical 项目。

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
- [[community/deepseek-ai/DeepSeek-Infra/Chenqi Zhao|Chenqi Zhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Guanglin Li|Guanglin Li]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/guyan364|guyan364]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Huanqi Cao|Huanqi Cao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]]：[[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：**DeepEP + DeepGEMM 共同作者**。2025 两人同时出现在两个项目的原始作者名单，合作关系覆盖 Expert Parallel communication 与 GEMM / MoE kernels。公开资料不足以确认雇佣起止与直属关系。
- [[community/deepseek-ai/DeepSeek-Infra/Kaifeng Chen|Kaifeng Chen]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/kurisu6912|kurisu6912]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Liyue Zhang|Liyue Zhang]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/LyricZhao|LyricZhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Rui Tian|Rui Tian]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Ruifan Xu|Ruifan Xu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Runji Wang|Runji Wang]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou|Shangyan Zhou]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Weilin Zhao|Weilin Zhao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Xiangwen Wang|Xiangwen Wang]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yiliang Xiong|Yiliang Xiong]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yizhi Wang|Yizhi Wang]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yuhao Meng|Yuhao Meng]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yunfan Xiao|Yunfan Xiao]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu|Yuxuan Liu]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/Yuxuan Zhou|Yuxuan Zhou]]：社区贡献关联；人物页已明确记录该社区。
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
