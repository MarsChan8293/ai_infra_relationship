# DeepSeek Targeted DISCOVER — 2026-10-02

本轮从现有 `DeepSeek Infra / deepseek-ai` seed 出发，结合 deepseek-ai 组织仓库、官方 `open-infra-index`、新 Ascend 仓库 README 与 DeepSeek Harness architecture 文档，执行一次 systems-first targeted DISCOVER，并修复上一轮 Ascend 扩展暴露出的 project-migration CI 问题。

## 执行边界

- Seed：DeepSeek / deepseek-ai
- 重点：AI Infra、Ascend、agent runtime、parallelism、memory system
- 不把纯模型仓库、awesome list 或内部组件一律提升为顶级 project
- 不因为 deepseek-ai namespace 自动推断个人雇佣
- performance claim 必须保留硬件、CANN、HDK 与 workload 条件
- 本次由用户直接触发 targeted DISCOVER，不来自 checked-in planner action，因此不追加 planner action-history

## 新增 / 完善 canonical projects

1. **DeepGEMM-Ascend**：Ascend 950 上的 BF16/FP8/FP4 GEMM、MQA logits、MegaMoE、mHC。
2. **DeepEP-Ascend**：Ascend MoE EP all-to-all；扩展 PP / Bucket / Engram communication primitives。
3. **clangd-ascend**：AscendC language-server / developer tooling。
4. **DualPipe**：DeepSeek V3 的双向 Pipeline Parallelism schedule。
5. **DeepSeek Harness**：plugin-first agent harness/runtime。
6. **Cordis**：DeepSeek Harness 的上游 plugin meta-framework。
7. **Engram**：Conditional Memory / scalable lookup 官方实现。

FlashMLA 与 DeepJIT 不重复建 Ascend fork 节点：它们的 Ascend 实现直接存在于原仓库，因此在原 project node 上扩展 hardware / feature snapshot。

## 新增 canonical concepts

- **Agent Harness**：agent runtime / control-layer 机制。
- **Sparse Attention**：selector/indexer 之后的稀疏 attention kernel 机制。
- **Conditional Memory**：Engram 所代表的 conditional lookup / memory sparsity。

同时把 DeepGEMM-Ascend / DeepEP-Ascend / FlashMLA / DualPipe / Engram 映射回 GEMM、Grouped GEMM、JIT Kernel Compilation、FP8、FP4、All-to-All、Collective Communication、Expert Parallelism、Pipeline Parallelism、Attention Kernel、Host Memory 等现有 concept。

## Ascend 关键证据

### DeepGEMM-Ascend
- 2026-09-30 initial release。
- 官方首发验证 Ascend 950 series，CANN 9.20。
- API-compatible with DeepGEMM。
- README 公开 dense / grouped GEMM、MQA logits、MegaMoE、mHC benchmark。
- JIT = DeepJIT；HC prenorm = TileLang。
- Dense GEMM 表中部分 shape 报告接近 99.8% hardware limit；该数字不泛化到所有 shape / device。

### DeepEP-Ascend
- EPBuffer API 与 NVIDIA DeepEP 对齐。
- HCCL/HCOMM + UBMEM + URMA；DeepJIT runtime compilation。
- PP / Engram / Bucket 存在 experimental / ongoing 边界。
- 首发性能数据来自 Ascend 950DT + CANN 9.2.0 + DeepSeek PoC HDK / manual config；不能等价成普通公开商用软件 baseline。
- README 在 2026-09-30 时写明 Huawei 计划约 2026-10-15 发布包含相关配置的 Atlas 850E Q3 commercial HDK；该日期为厂商计划，后续需要 VERIFY 实际发布状态。

### FlashMLA
- 2026-09-30 release Ascend Sparse Attention prefill/decode。
- DeepSeek V4.1 typical workload：prefill 410 TFLOPS、decode 360 TFLOPS，官方分别标为理论峰值约 95% / 83%。
- 不是所有 FlashMLA kernel 都已支持 Ascend；其他路径仍可能 CUDA-only。

### DeepJIT
- 同一 header-only C++20 runtime 同时支持 CUDA 与 Ascend。
- Ascend backend：Bisheng + ld.lld compile/link，ACL load/launch，可使用 torch_npu current stream。
- DeepGEMM-Ascend / DeepEP-Ascend 均直接使用。

## DeepSeek 2026 frontier

### DeepSeek Harness
DSH 是 agent runtime 而非 inference engine：Cordis plugin tree、profiles/bundles、durable session log、agent loop、MCP、ACP、sandbox、LLM adapters 构成核心。官方仍标 developer preview。当前仓库未发现 MindIE 的官方直接 integration，因此不建立强 integration edge。

### Engram
Engram 把 conditional memory 作为 MoE 之外的新 sparsity 轴，并利用 deterministic addressing 支持 host-memory offload。DeepEP-Ascend 的 EngramBuffer / remote-memory access 形成模型机制到 communication/data-plane 的系统桥；当前接口仍有 experimental 边界。

### 不提升为顶级 project
- `awesome-deepseek-agent`：curated ecosystem index。
- `dsh-libreoffice-kit`、`dsh-node-addon-require-builtin`：DeepSeek Harness internal components。

## Contributor graph

DeepGEMM-Ascend 官方 README/citation 补充了 Kexing Zhou、Zhean Xu、Chenggang Zhao、Anyi Xu、Yuxuan Zhou、Yunfan Xiao、Guanglin Li、Kaifeng Chen、Yuhao Meng、Huanqi Cao、Ruifan Xu、Chenhao Xu、Kuai Yu 等项目贡献关系。

DeepEP-Ascend citation 补充 Chenggang Zhao、Shangyan Zhou、Kexing Zhou、Rui Tian、Chenqi Zhao、Chenhao Xu、Yizhi Wang、Kuai Yu。

这些边只代表公开项目/论文作者或 contributor 身份；除非人物页另有独立证据，不据此推断当前雇佣、职级、直属关系或 maintainer 权限。

## CI 修复

初次 Ascend 扩展曾把 `torch_npu` 写入 DeepJIT 的 `integrations`。Project v3 contract 要求 `integrations` 解析为 canonical project identity；`torch_npu` 当前不是本图谱 project node，因此触发 `audit-software-project-migration.py` 失败。已把它从 integrations 元数据移除，同时保留在正文中作为 runtime dependency。随后主干 `Sync Node Schemas` 与 `Validate and Deploy Quartz` 均恢复成功。

## Primary sources

- https://github.com/deepseek-ai/open-infra-index
- https://github.com/deepseek-ai/DeepGEMM-Ascend
- https://github.com/deepseek-ai/DeepEP-Ascend
- https://github.com/deepseek-ai/clangd-ascend
- https://github.com/deepseek-ai/FlashMLA
- https://github.com/deepseek-ai/DeepJIT
- https://github.com/deepseek-ai/DualPipe
- https://github.com/deepseek-ai/deepseek-harness
- https://github.com/cordiverse/cordis
- https://github.com/deepseek-ai/Engram
