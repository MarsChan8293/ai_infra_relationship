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
- [ ] 技术主题只作为 project 的 `areas` 等属性或正文内容存在，不升级为独立 concept graph entity。

## 1. Project Schema 收敛与精简

本次迁移不采用“Software Schema + relationship Project Schema 字段并集”的方式，而是重新收敛为一个更小的 canonical Project Schema。原则是：**只把需要稳定查询、需要机器校验、且无法可靠从正文或图结构派生的信息放进 frontmatter。**

### 1.1 Project Schema v3：建议只保留核心字段

目标 canonical frontmatter：

```yaml
type: project
name: vLLM
layer: inference-engine
status: active
repository: https://github.com/vllm-project/vllm
docs: https://docs.vllm.ai/
areas:
  - llm-serving
  - kv-cache
  - speculative-decoding
hardware:
  - nvidia
  - amd
  - ascend
integrations:
  - LMCache
  - llm-d
  - Mooncake
companies:
  - Inferact
  - Meta
last_verified: "2026-09"
```

- [ ] 将 `schema/project.yaml` 从 `project-v2` 升级到 `project-v3`。
- [ ] canonical Project Schema 优先只保留：
  - [ ] `type`
  - [ ] `name`
  - [ ] `layer`
  - [ ] `status`
  - [ ] `repository`
  - [ ] `docs`
  - [ ] `areas`
  - [ ] `hardware`
  - [ ] `integrations`
  - [ ] `companies`
  - [ ] `last_verified`
- [ ] 允许极少数兼容字段在迁移期继续存在，但不作为新页面推荐字段。
- [ ] 更新 `schema/catalog.yaml`、schema generator 和 validator 对 project-v3 的支持。
- [ ] 保证旧 project-v2 页面在迁移期只产生 warning，不立即成为 hard error。

### 1.2 两边字段映射与删减

| ai_infra_docs / relationship 现有字段 | Project v3 处理 | 原因 |
| --- | --- | --- |
| `object_type` | → `type` | 与 relationship 命名统一 |
| `schema_version` | 删除 | schema catalog 已负责 schema 版本 |
| `category` | → `layer` | 保留 relationship 字段名，但采用有限枚举 |
| `organization` | 不直接迁字段 | 归一化到已有 company/community 实体或正文治理信息 |
| `repo` | → `repository` | 纯命名统一 |
| `docs` | 保留 | 稳定且有查询价值 |
| `status` | 保留 | 可用于 VERIFY / freshness |
| `snapshot.as_of` | → `last_verified` | 避免两套事实时间 |
| `snapshot.version` | 移到正文 | 多数项目为空，只有版本绑定页面才需要 |
| `snapshot.commit` | 移到正文 | 同上 |
| `updated` | 删除 | Git 历史已经提供文件更新时间 |
| `capabilities` | 合并进 `areas`，细节留正文 | 避免 capability / area 标签体系重复漂移 |
| `integrations` | 保留 | 是最有价值的机器可查询项目关系之一 |
| `relations` | 本次不迁入 Project v3 核心字段 | 避免同时维护两套项目关系系统 |
| `backends` | → `hardware` | 当前主要表达硬件/平台支持 |
| `open_source` | 逐步废弃 | 对绝大多数项目信息量低；repository 与正文可表达 |
| `company_relation` | 逐步废弃 | 单一 scalar 无法准确描述多个公司的不同关系 |
| `people` | 逐步退出 canonical frontmatter | curated maintainer/contributor 事实放正文，反向关系由图生成 |
| `linked_people` | 仅派生 | 不应手工维护 |
| `linked_companies` | 仅派生 | 不应手工维护 |
| `governance` | 移到正文 | 治理结构通常不是一个 string 能准确表达 |

### 1.3 `layer` 收敛：有限枚举，技术细节放 `areas`

relationship 当前 `layer` 已混入大量细粒度描述。本次迁移统一为有限枚举，优先复用 Software Schema 的分类思想。

建议 canonical `layer`：

- [ ] `inference-engine`
- [ ] `distributed-serving`
- [ ] `gateway`
- [ ] `kv-cache`
- [ ] `storage`
- [ ] `communication`
- [ ] `runtime`
- [ ] `kernel`
- [ ] `compiler`
- [ ] `training`
- [ ] `scheduler`
- [ ] `device-resource`
- [ ] `benchmark`
- [ ] `ecosystem`
- [ ] `optimization`
- [ ] `other`

例如 HAMi 不再使用：

```yaml
layer: kubernetes-heterogeneous-device-virtualization
```

而是：

```yaml
layer: device-resource
areas:
  - kubernetes
  - heterogeneous-accelerator
  - gpu-sharing
  - device-virtualization
```

- [ ] 建立现有 relationship `layer` → canonical layer 的 migration mapping。
- [ ] 建立 docs `category` → canonical layer 的 migration mapping。
- [ ] validator 对新页面强制 canonical layer；旧页面迁移期先 warning。

### 1.4 `areas` 吸收 `capabilities`

- [ ] Project v3 不再同时维护 `areas` 与 `capabilities` 两套标签。
- [ ] 只把稳定、适合检索的技术主题写入 `areas`。
- [ ] 细粒度 feature matrix、边界条件、版本差异继续放 Markdown 正文。
- [ ] 建立常见同义标签归一化，例如 `kv-offload` / `offloading`、`llm-serving-engine` / `inference-engine`。
- [ ] 不因为两个项目共享相同 `areas` 就自动产生项目关系或人物关系。

### 1.5 `hardware` 吸收 `backends`

- [ ] docs 的 `backends` 在迁移时统一映射到 relationship 的 `hardware`。
- [ ] `hardware` 只记录明确支持的硬件/平台族，例如 `nvidia`、`amd`、`ascend`。
- [ ] 软件依赖、存储后端、通信 backend 不塞入 `hardware`，改放正文或 `integrations`。

### 1.6 时间字段只保留 `last_verified`

- [ ] `snapshot.as_of` → `last_verified`。
- [ ] docs 的 `updated` 不迁移。
- [ ] `snapshot.version` / `snapshot.commit` 默认不进入 Project v3 frontmatter。
- [ ] 若页面明确绑定特定版本/commit，在正文增加 Version Snapshot 小节。
- [ ] VERIFY 以 `last_verified` 为主要 freshness 输入。

### 1.7 派生字段不再污染 canonical Markdown

长期目标：

```text
人工维护 Project Frontmatter
        ↓
约 10 个稳定字段

Markdown 正文
        ↓
治理、维护者、核心能力、边界、证据、版本细节

Generated Graph / schema mirrors
        ↓
linked_people
linked_companies
reverse integrations
metrics / coverage
```

- [ ] `linked_people` 只存在于 generated 数据 / schema mirror，不作为人工事实源。
- [ ] `linked_companies` 只存在于 generated 数据 / schema mirror，不作为人工事实源。
- [ ] 评估 `people` 是否完全由正文维护者段落 + person 侧显式 project membership 派生；迁移期允许兼容，Project v3 不推荐新增。
- [ ] 自动生成字段必须可从 Markdown / 关系边重新构建，禁止成为唯一事实源。

### 1.8 合并 `infra-project` → `project`

当前 `infra-project` 与 `project` 的字段高度重复，且现有实例很少。本次迁移顺手统一。

- [ ] 将现有 `type: infra-project` 节点逐个迁为 `type: project`。
- [ ] `company` → `companies`。
- [ ] 原 `infra-project.layer` 映射到 canonical layer。
- [ ] 原 `related_projects` 根据证据迁入正文或项目关系。
- [ ] 从 `schema/catalog.yaml` 移除新的 `infra-project` 创建入口。
- [ ] 迁移完成后删除或仅保留 `schema/infra-project.yaml` 兼容说明。
- [ ] generator / planner / audit 不再把 `infra-project` 当独立 canonical entity type。

### 1.9 项目间软件关系

- [ ] 本次迁移优先把 `integrations` 作为机器可查询的 project ↔ project 技术关系。
- [ ] `integrations` 只记录直接、可核验的软件集成，不记录“同类项目”或纯技术邻接。
- [ ] 更复杂的 `depends-on`、`backend-for`、`alternative-to`、`extends` 等关系继续使用现有 relation model 或正文，不在本次迁移中再造一套平行 schema。
- [ ] 不把正文中的普通 Wiki Link 自动升级为 typed relation。
- [ ] 不根据相同 `areas` 自动生成 project ↔ project 强关系。

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
- [ ] repository / docs URL 已核验并统一命名。
- [ ] docs category 与旧 relationship layer 已映射到 canonical layer。
- [ ] status 已迁移。
- [ ] snapshot.as_of 已折叠为 last_verified；updated 不迁移。
- [ ] capabilities 已归并到精简后的 areas 或正文，不保留第二套标签体系。
- [ ] integrations 已迁移，并能解析到 canonical project。
- [ ] backends 已映射到 hardware；非硬件 backend 留正文或 integrations。
- [ ] organization 已归一化到现有 company/community 或保留在正文，不新增 upstream_org 字段。
- [ ] 原 relationship 中的重要 people / companies / governance 事实无丢失；people/governance 可转正文。
- [ ] linked_people / linked_companies 可由 generated graph 重建，不依赖手工 frontmatter。
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
  - [ ] technical areas
- [ ] 更新 DISCOVER，使 project 技术元数据参与 coverage-gap，但仍以人物、组织、项目生态发现为目标。
- [ ] VERIFY 可检查：
  - [ ] project status freshness
  - [ ] repository / docs URL
  - [ ] integration 是否仍存在
  - [ ] governance / maintainer 漂移
  - [ ] last_verified 过期
- [ ] planner 明确禁止从“共同 areas”自动产生 person-to-person 强边。
- [ ] 更新 `docs/research-action-planner.md` 与 `docs/research-operators.md`。

## 7. Validator / Graph Builder / CI

- [ ] Validator 支持 project-v3。
- [ ] 检查 `integrations` 指向存在的 canonical project。
- [ ] 检查 `last_verified` 格式与缺失。
- [ ] 检查 repository URL 冲突。
- [ ] 检查同一 repository 被多个 canonical project 重复声明。
- [ ] 检查新页面不再新增 `capabilities` / `backends` / `snapshot` / `upstream_org` 等已收敛字段。
- [ ] 检查 `linked_people` / `linked_companies` 能从图结构重新生成。
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

- [ ] project-v3 精简 schema
- [ ] layer/category migration mapping
- [ ] infra-project → project 迁移
- [ ] catalog
- [ ] validators
- [ ] graph builder
- [ ] 59 项目 migration mapping 表

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
- [ ] project 的 layer / status / areas / hardware / integrations / last_verified 等精简技术元数据可查询。
- [ ] infra-project 已收敛为 project，不再新增 infra-project canonical 节点。
- [ ] linked_people / linked_companies 不再依赖人工 frontmatter，generated 数据可重新生成。
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
- [ ] 不把 docs 的所有 Software 字段机械搬入 relationship。
- [ ] 不在 Project v3 新增 `upstream_org` / `capabilities` / `backends` / `snapshot`。
- [ ] 不把 `linked_people` / `linked_companies` 当成人工维护的 canonical facts。
