# ai_infra_docs/software → ai_infra_relationship 迁移计划

> 目标：仅将 `ai_infra_docs/software/projects` 中的软件项目事实并入本仓库，使 `ai_infra_relationship` 形成更完整的 **Person ↔ Organization ↔ Project** AI Infra 生态图谱，同时保留项目自身的技术元数据。
>
> 原则：**只迁 Project，不迁 Concept；先统一 schema，再迁 canonical entity；先建立兼容层，再删除重复项目内容。**
>
> 非目标：本计划不迁移 `ai_infra_docs/software/concepts`、`chip`、`models` 或其他长篇技术资料。

## 0. 迁移边界与约束

- [ ] 将 `ai_infra_docs/software/projects/*` 的软件项目事实迁入本仓库对应 canonical project 页面。
- [ ] **不迁移 `ai_infra_docs/software/concepts/*`；Concept 继续以 `ai_infra_docs` 为 canonical source。**
- [ ] 不在本仓库新增 `concept` 一级节点类型。
- [ ] 不新增 Project ↔ Concept typed relation。
- [ ] 不原样迁移 `software/COMMUNITIES.md`；将其中与项目直接相关的 upstream organization / community 信息归一化到本仓库现有 company / community 节点。
- [ ] 不长期保留同一软件项目在两个仓库各自作为 canonical source。
- [ ] 迁移期间 `ai_infra_docs/software/projects` 保留兼容入口，避免 models / chip 页面中的旧项目链接立即失效。
- [ ] `ai_infra_docs/software/concepts` 保持原路径和原职责，不进入本次退役范围。
- [ ] Markdown 继续作为事实源；generated 数据继续只作为派生视图。
- [ ] 不因为软件项目迁入而降低现有“人物关系必须有直接证据”的证据标准。
- [ ] 项目集成、兼容、共同依赖不自动推断人物之间存在直接合作关系。
- [ ] 公司员工参与项目不自动推断公司是项目 founding/core-maintainer organization。
- [ ] 技术主题只作为 project 的 `areas` / `capabilities` 等属性存在，不升级为独立 concept graph entity。

## 1. Project Schema 收敛

### 1.1 Project Schema v3

- [ ] 将 `schema/project.yaml` 从 `project-v2` 升级到 `project-v3`。
- [ ] 保留现有 ecosystem 字段：
  - [ ] `companies`
  - [ ] `linked_companies`
  - [ ] `company_relation`
  - [ ] `people`
  - [ ] `linked_people`
  - [ ] `governance`
  - [ ] `repository`
  - [ ] `areas`
  - [ ] `hardware`
  - [ ] `last_verified`
- [ ] 从 Software Schema V0.1 吸收项目级技术字段：
  - [ ] `docs`
  - [ ] `status`
  - [ ] `upstream_org`
  - [ ] `capabilities`
  - [ ] `integrations`
  - [ ] `backends`
  - [ ] `snapshot.version`
  - [ ] `snapshot.commit`
  - [ ] `snapshot.as_of`
- [ ] 统一 `layer` 与 Software `category`，确定 canonical 枚举。
- [ ] 为现有 `layer` 值和 Software category 建 migration mapping。
- [ ] 明确 `areas` / `capabilities` 是项目属性，不要求对应独立 Concept 节点。
- [ ] 明确 `upstream_org` 只表示 canonical upstream namespace / governance organization，不等于 company ownership。
- [ ] 明确 `integrations` 只记录直接可核验的软件集成，不把“同类项目”写成 integration。
- [ ] 明确 `backends` 与 `hardware` 的边界，避免两个字段表达同一事实。
- [ ] 更新 `schema/catalog.yaml`、schema generator 和 validator 对 project-v3 的支持。
- [ ] 保证旧 project-v2 页面在迁移期只产生 warning，不立即成为 hard error。

### 1.2 项目间软件关系

- [ ] 继续以 project ↔ project 为本次迁移的主要技术关系。
- [ ] 明确支持 / 保留以下项目关系语义：
  - [ ] `integrates-with`
  - [ ] `depends-on`
  - [ ] `backend-for`
  - [ ] `alternative-to`
  - [ ] `extends`
  - [ ] `managed-by`
  - [ ] `related`
- [ ] 优先复用已有 relation model，避免再造平行关系系统。
- [ ] 不把正文中的普通 Wiki Link 自动升级为 typed relation。
- [ ] 不根据相同 `areas` / `capabilities` 自动生成 project ↔ project 强关系。

## 2. Canonical Entity 对齐与去重

- [ ] 为 59 个 Software 项目建立迁移映射表：
  `docs software slug → relationship canonical path → action(merge/create/alias)`。
- [ ] 优先识别本仓库已经存在的项目，禁止直接复制形成第二个 canonical 页面。
- [ ] 对重名或多层目录项目建立稳定 canonical ID。
- [ ] 对 vLLM、SGLang、LMCache、Mooncake、DeepEP、vLLM-Ascend 等已有丰富人物网络的项目，以 relationship 页面为主体吸收 Software 技术字段。
- [ ] 对当前 relationship 中尚不存在的 Software 项目新建 project 节点。
- [ ] 为旧 `software/projects/<slug>` 记录兼容 alias / redirect target。
- [ ] 完成一次 duplicate-name / duplicate-repository audit。
- [ ] 完成一次 repository URL canonicalization audit。

## 3. 59 个 Software 项目迁移

### 3.1 Inference Engine

- [ ] vLLM
- [ ] SGLang
- [ ] TensorRT-LLM
- [ ] llama.cpp
- [ ] LightLLM
- [ ] KTransformers
- [ ] vLLM-Ascend
- [ ] MindIE-LLM
- [ ] MindIE-SD

### 3.2 Distributed Serving / Gateway

- [ ] llm-d
- [ ] NVIDIA Dynamo
- [ ] AIBrix
- [ ] KServe
- [ ] Ray Serve
- [ ] Gateway API Inference Extension
- [ ] Triton Inference Server
- [ ] BentoML
- [ ] LiteLLM

### 3.3 KV / Storage

- [ ] LMCache
- [ ] Mooncake
- [ ] 3FS

### 3.4 Communication

- [ ] NIXL
- [ ] NCCL
- [ ] RCCL
- [ ] DeepEP
- [ ] UCX
- [ ] VCCL
- [ ] FlagCX

### 3.5 Runtime / Kernel

- [ ] FlashInfer
- [ ] FlashAttention
- [ ] CUTLASS
- [ ] DeepGEMM
- [ ] FlashMLA
- [ ] FlagGems
- [ ] FlagAttention
- [ ] ops-transformer
- [ ] MindIE-Motor
- [ ] TokenSpeed
- [ ] vllm-plugin-FL
- [ ] sglang-plugin-FL

### 3.6 Compiler

- [ ] Triton
- [ ] TileLang
- [ ] DeepJIT
- [ ] FlagTree

### 3.7 Training / Framework

- [ ] Colossal-AI
- [ ] OneFlow
- [ ] FlagScale

### 3.8 Scheduler

- [ ] KAI-Scheduler
- [ ] Volcano
- [ ] Kueue

### 3.9 Device Resource

- [ ] HAMi
- [ ] Kubernetes DRA
- [ ] NVIDIA GPU Operator
- [ ] NVIDIA k8s-device-plugin

### 3.10 Ecosystem / Optimization / Benchmark

- [ ] DeepSeek-Infra
- [ ] FlagOS
- [ ] msModelSlim
- [ ] FlagPerf
- [ ] FlagRelease

### 每个项目的迁移验收项

- [ ] canonical project 页面唯一。
- [ ] repository / docs URL 已核验。
- [ ] layer/category 已映射。
- [ ] status 已迁移。
- [ ] snapshot.as_of 已迁移或重新核验。
- [ ] areas / capabilities 已迁移，且不把推测写入 YAML。
- [ ] integrations 已迁移，并能解析到 canonical project。
- [ ] backends/hardware 已归一化。
- [ ] upstream_org 已解析到现有 company/community 或明确 namespace。
- [ ] 原 relationship 中的 people / companies / governance 信息无丢失。
- [ ] Sources 足以支撑新增的技术事实。
- [ ] 旧项目 Wiki Link 能通过 alias/redirect 或转换规则找到新节点。

## 4. Community / Organization 归一化

- [ ] 解析 Software 项目中的 `organization`。
- [ ] 若 relationship 已有 community/company 节点，改为 canonical reference。
- [ ] namespace 与真实公司不是同一实体时保留区别，例如 project namespace、foundation/community、company。
- [ ] 不将 GitHub organization 名称自动等价为公司。
- [ ] 为需要的新 community 节点补 schema 与来源。
- [ ] `software/COMMUNITIES.md` 继续留在 docs 时，不再承担已迁项目的第二份 canonical 项目事实。

## 5. Software Index 改为自动生成

- [ ] relationship 不再人工维护迁入项目的静态列表。
- [ ] 从 project `layer` / `status` 自动生成 Software Project Index。
- [ ] 支持按以下维度筛选：
  - [ ] inference-engine
  - [ ] distributed-serving
  - [ ] kv-cache / storage
  - [ ] communication
  - [ ] runtime / kernel
  - [ ] compiler
  - [ ] training
  - [ ] scheduler
  - [ ] device-resource
  - [ ] ecosystem / optimization / benchmark
- [ ] Index 中显示 project → people / company / community 的图谱入口。
- [ ] Graph Explorer 支持从 Software Index 一跳进入人物、公司、学校和社区。
- [ ] Concept 索引继续由 `ai_infra_docs/software/concepts` 自己维护，不合入 relationship Software Index。

## 6. Research Planner 接入

- [ ] 更新 EXPAND，使 project 节点可沿以下方向扩展：
  - [ ] maintainers / contributors
  - [ ] upstream organization
  - [ ] integrations / dependencies
  - [ ] technical areas / capabilities
- [ ] 更新 DISCOVER，使 project 技术元数据参与 coverage-gap，但仍以人物、组织、项目生态发现为目标。
- [ ] VERIFY 可检查：
  - [ ] project status freshness
  - [ ] repository / docs URL
  - [ ] integration 是否仍存在
  - [ ] governance / maintainer 漂移
  - [ ] snapshot 过期
- [ ] planner 明确禁止从“共同 areas / capabilities”自动产生 person-to-person 强边。
- [ ] 更新 `docs/research-action-planner.md` 与 `docs/research-operators.md`。

## 7. Validator / Graph Builder / CI

- [ ] Validator 支持 project-v3。
- [ ] 检查 `integrations` 指向存在的 canonical project。
- [ ] 检查 `snapshot.as_of` 格式与缺失。
- [ ] 检查 repository URL 冲突。
- [ ] 检查同一 repo 被多个 canonical project 重复声明。
- [ ] Graph builder 正确输出新增/合并后的 project 节点与 project relations。
- [ ] Graph Explorer 保持并增强 Project 筛选。
- [ ] Quartz route audit 覆盖新项目路径和兼容 alias。
- [ ] CI 在迁移期区分 hard error 与 migration warning。
- [ ] 不为 Concept 增加 relationship 侧 schema、validator 或 Graph Explorer 特殊逻辑。

## 8. ai_infra_docs 兼容迁移

- [ ] 第一阶段继续保留 `ai_infra_docs/software/projects`，但标注 relationship 为 project canonical source。
- [ ] 建立旧 software project path → relationship canonical URL 映射。
- [ ] 扫描 `ai_infra_docs/models/**` 对 software project 的引用。
- [ ] 扫描 `ai_infra_docs/chip/**` 对 software project 的引用。
- [ ] 将项目跨仓引用改为稳定 URL / external canonical reference，或在 build 时重写。
- [ ] **保留 models / chip 对 `software/concepts/*` 的本地引用，不做跨仓迁移。**
- [ ] 确认 docs Quartz 无 404。
- [ ] 确认 relationship Quartz 无 duplicate route。
- [ ] 兼容期结束后，将 docs 中重复 project 页面变成薄 redirect/stub 或删除。
- [ ] 保留 `software/concepts/*`、其索引与概念文档职责。
- [ ] Software Schema 若仍服务 docs Concept，可拆分或收缩为 Concept-only 规则；不要因 Project 迁移误删 Concept 所需约束。

## 9. 推荐执行批次

### Batch A：基础设施

- [ ] project-v3
- [ ] catalog
- [ ] validators
- [ ] graph builder
- [ ] migration mapping 表

### Batch B：高价值重复项目

优先处理两仓库重叠最深、人物关系最多的项目：

- [ ] vLLM
- [ ] SGLang
- [ ] LMCache
- [ ] Mooncake
- [ ] llm-d
- [ ] DeepEP
- [ ] DeepSeek-Infra
- [ ] vLLM-Ascend
- [ ] KTransformers
- [ ] FlashInfer
- [ ] DeepGEMM
- [ ] FlashMLA

### Batch C：其余 Software 项目

- [ ] 按 layer 分批迁移余下项目。
- [ ] 每批迁移后运行 duplicate / broken-link / schema audit。

### Batch D：Planner 与生成视图

- [ ] EXPAND / DISCOVER / VERIFY 接入 project-v3 新字段。
- [ ] 自动 Software Project Index。
- [ ] Graph Explorer Project 视图增强。
- [ ] coverage / freshness 报告。

### Batch E：docs 收尾

- [ ] models/chip 的 project 跨仓链接迁移完成。
- [ ] docs software project canonical 内容退役。
- [ ] 删除重复项目数据和不再需要的 project schema 规则。
- [ ] 保留 `software/concepts` 及其本地链接。
- [ ] 保留必要 redirects / compatibility notes。

## 10. 完成定义（Definition of Done）

当且仅当以下条件全部满足，才认为 Software Project 迁移完成：

- [ ] 59 个项目在 relationship 中均有且只有一个 canonical project 节点。
- [ ] `ai_infra_docs/software/concepts/*` 未迁移，仍由 docs 维护。
- [ ] relationship 未新增 concept canonical node type。
- [ ] 两仓库不存在同一软件项目的双 canonical source。
- [ ] 人物 / 公司 / 学校 / community 与项目关系无回归。
- [ ] Project ↔ Project integrations / dependencies 可查询。
- [ ] Person → Project 和 Project → Person 路径可查询。
- [ ] project 的 areas / capabilities / backends / snapshot 等技术元数据可查询。
- [ ] 所有 generated schema 可重新生成。
- [ ] audit / validator / Quartz build 全部通过。
- [ ] docs 中 models/chip 的原有 software project 链接无 404。
- [ ] docs 中 software concept 链接保持原状可用。
- [ ] EXPAND / DISCOVER / VERIFY 不因新增 project 元数据产生明显噪声。
- [ ] relationship 的 Software Project Index 已由数据自动生成，不再手工维护项目清单。

## 11. 暂不做

- [ ] 不迁移 `ai_infra_docs/software/concepts`。
- [ ] 不新增 Concept Schema。
- [ ] 不新增 Project ↔ Concept 图谱关系。
- [ ] 不迁移 `ai_infra_docs/chip`。
- [ ] 不迁移 `ai_infra_docs/models`。
- [ ] 不把所有 AI Infra 技术知识都塞进 relationship。
- [ ] 不把论文、博客、教程默认建成一级 graph entity。
- [ ] 不因技术邻接自动推断人际关系。
- [ ] 不在 project schema 稳定前批量删除 docs 原项目文件。
