# ai_infra_docs/software → ai_infra_relationship 迁移计划

> 目标：仅将 `ai_infra_docs/software/projects` 中的软件项目事实并入本仓库，使 `ai_infra_relationship` 形成更完整的 **Person ↔ Organization ↔ Project** AI Infra 生态图谱，同时保留项目自身的技术元数据。
>
> 原则：**只迁 Project，不迁 Concept；先统一 schema，再迁 canonical entity；先建立兼容层，再删除重复项目内容。**
>
> 非目标：本计划不迁移 `ai_infra_docs/software/concepts`、`chip`、`models` 或其他长篇技术资料。

## 当前迁移进度

截至 2026-09-19，Software Project 源数据迁移已完成 **59 / 59**：

- [x] `schema/project.yaml` 已升级为精简的 `project-v3`。
- [x] `schema/catalog.yaml` 已停止把 `infra-project` 作为新的 canonical type。
- [x] MoonEP、Checkpoint Engine、ForgeTrain 三个 `infra-project` 源页面已迁为 `project`。
- [x] 相关 sync / audit / research 脚本已移除 `infra-project` 主路径，并在 node schema generator 中保留迁移兼容 alias。
- [x] 59 个 `ai_infra_docs/software/projects/*` 项目均已映射到 relationship canonical project：其中 **43 个 merge，16 个 create**。
- [x] 59 项目 canonical mapping 已固化到 `research/software-project-migration.json`。
- [x] 迁移项目已按 v3 规则收敛：`category → layer`、`capabilities → areas`、`backends → hardware`、`snapshot.as_of → last_verified`，并按需补充 `status/docs/integrations`。
- [x] Ray Serve / Ray、Kubernetes DRA / Kubernetes 已用可选 `parent` 字段表达合法 monorepo 子项目，避免 repository 去重误判。
- [x] 新增 `scripts/audit-software-project-migration.py`，严格验收 59 项目的唯一性、Project v3 字段、integration 解析、repository 冲突和 `infra-project` 归零。
- [x] Software migration audit 已接入 `.github/workflows/sync-node-schemas.yml`。
- [x] Software Project Index 生成器已接入 workflow，输出 `generated/software-project-index.md`。
- [x] Research Planner 已消费 Project v3 `integrations / last_verified`，新增 `verify_project_freshness` VERIFY objective。
- [ ] generated graph / schema mirrors 尚待 workflow 重建并通过新 migration audit；在结果落盘前不把最终 CI / generated DoD 标记为完成。
- [x] `ai_infra_docs` 侧 59 个 project 页面已全部转为 redirect；README / Project Index / COMMUNITIES / validator / graph kind 已同步到 Software Schema V0.2；Concept 保持原地不迁。

## 0. 迁移边界与约束

- [x] 将 `ai_infra_docs/software/projects/*` 的软件项目事实迁入本仓库对应 canonical project 页面。
- [x] **不迁移 `ai_infra_docs/software/concepts/*`；Concept 继续以 `ai_infra_docs` 为 canonical source。**
- [x] 不在本仓库新增 `concept` 一级节点类型。
- [x] 不新增 Project ↔ Concept typed relation。
- [ ] 不原样迁移 `software/COMMUNITIES.md`；将其中与项目直接相关的 upstream organization / community 信息归一化到本仓库现有 company / community 节点。
- [x] 不长期保留同一软件项目在两个仓库各自作为 canonical source。
- [x] `ai_infra_docs/software/projects` 已保留为 59 个兼容 redirect，避免 models / chip / concepts 的旧项目链接失效。
- [x] `ai_infra_docs/software/concepts` 保持原路径和原职责，不进入本次退役范围。
- [x] Markdown 继续作为事实源；generated 数据继续只作为派生视图。
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

- [x] 将 `schema/project.yaml` 从 `project-v2` 升级到 `project-v3`。
- [x] canonical Project Schema 优先只保留以下核心字段（另允许可选 `parent` 表达真实子项目）：
  - [x] `type`
  - [x] `name`
  - [x] `layer`
  - [x] `status`
  - [x] `repository`
  - [x] `docs`
  - [x] `areas`
  - [x] `hardware`
  - [x] `integrations`
  - [x] `companies`
  - [x] `last_verified`
- [x] 允许极少数兼容字段在迁移期继续存在，但不作为新页面推荐字段。
- [x] 更新 `schema/catalog.yaml`、schema generator 和 validator 对 project-v3 的支持。
- [x] 保证旧 project-v2 页面在迁移期只产生 warning，不立即成为 hard error。

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

- [x] `inference-engine`
- [x] `distributed-serving`
- [x] `gateway`
- [x] `kv-cache`
- [x] `storage`
- [x] `communication`
- [x] `runtime`
- [x] `kernel`
- [x] `compiler`
- [x] `training`
- [x] `scheduler`
- [x] `device-resource`
- [x] `benchmark`
- [x] `ecosystem`
- [x] `optimization`
- [x] `other`

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

- [x] 建立现有 relationship `layer` → canonical layer 的 migration mapping，固化于 `research/project-layer-migration.json`。
- [x] 建立 docs `category` → canonical layer 的 migration mapping。
- [x] Project v3 schema 对新/迁移页面使用 canonical layer 枚举；旧 project 页面继续按 migration warning 渐进处理。

### 1.4 `areas` 吸收 `capabilities`

- [x] Project v3 不再同时维护 `areas` 与 `capabilities` 两套标签。
- [ ] 只把稳定、适合检索的技术主题写入 `areas`。
- [ ] 细粒度 feature matrix、边界条件、版本差异继续放 Markdown 正文。
- [ ] 建立常见同义标签归一化，例如 `kv-offload` / `offloading`、`llm-serving-engine` / `inference-engine`。
- [ ] 不因为两个项目共享相同 `areas` 就自动产生项目关系或人物关系。

### 1.5 `hardware` 吸收 `backends`

- [x] docs 的 `backends` 在迁移时统一映射到 relationship 的 `hardware`。
- [ ] `hardware` 只记录明确支持的硬件/平台族，例如 `nvidia`、`amd`、`ascend`。
- [ ] 软件依赖、存储后端、通信 backend 不塞入 `hardware`，改放正文或 `integrations`。

### 1.6 时间字段只保留 `last_verified`

- [x] `snapshot.as_of` → `last_verified`。
- [x] docs 的 `updated` 不迁移。
- [x] `snapshot.version` / `snapshot.commit` 默认不进入 Project v3 frontmatter。
- [ ] 若页面明确绑定特定版本/commit，在正文增加 Version Snapshot 小节。
- [x] VERIFY 以 `last_verified` 为主要 freshness 输入。

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

- [x] 将现有 `type: infra-project` 节点逐个迁为 `type: project`。
- [x] `company` → `companies`。
- [x] 原 `infra-project.layer` 映射到 canonical layer。
- [ ] 原 `related_projects` 根据证据迁入正文或项目关系。
- [x] 从 `schema/catalog.yaml` 移除新的 `infra-project` 创建入口。
- [x] 迁移完成后删除或仅保留 `schema/infra-project.yaml` 兼容说明。
- [x] generator / planner / audit 不再把 `infra-project` 当独立 canonical entity type。

### 1.9 项目间软件关系

- [x] 本次迁移优先把 `integrations` 作为机器可查询的 project ↔ project 技术关系。
- [x] `integrations` 只记录直接、可核验的软件集成，不记录“同类项目”或纯技术邻接。
- [x] 更复杂的 `depends-on`、`backend-for`、`alternative-to`、`extends` 等关系继续使用现有 relation model 或正文，本次未新增第二套关系 schema。
- [x] 普通 Wiki Link 继续保持 generic wikilink；只有显式 `relations` 或 Project v3 `integrations` 生成 typed edge。
- [x] graph builder / planner 均不根据共同 `areas` 自动生成 project ↔ project 强关系。

## 2. Canonical Entity 对齐与去重

- [x] 为 59 个 Software 项目建立迁移映射表：
  `docs software slug → relationship canonical path → action(merge/create/alias)`。
- [x] 优先识别本仓库已经存在的项目，禁止直接复制形成第二个 canonical 页面。
- [x] 对重名或多层目录项目建立稳定 canonical ID。
- [x] 对 vLLM、SGLang、LMCache、Mooncake、DeepEP、vLLM-Ascend 等已有丰富人物网络的项目，以 relationship 页面为主体吸收 Software 技术字段。
- [x] 对当前 relationship 中尚不存在的 Software 项目新建 project 节点。
- [x] 为旧 `software/projects/<slug>` 建立兼容 redirect，并指向 relationship canonical project。
- [ ] 完成一次 duplicate-name / duplicate-repository audit。
- [ ] 完成一次 repository URL canonicalization audit。

## 3. 59 个 Software 项目迁移

### 3.1 Inference Engine

- [x] vLLM
- [x] SGLang
- [x] TensorRT-LLM
- [x] llama.cpp
- [x] LightLLM
- [x] KTransformers
- [x] vLLM-Ascend
- [x] MindIE-LLM
- [x] MindIE-SD

### 3.2 Distributed Serving / Gateway

- [x] llm-d
- [x] NVIDIA Dynamo
- [x] AIBrix
- [x] KServe
- [x] Ray Serve
- [x] Gateway API Inference Extension
- [x] Triton Inference Server
- [x] BentoML
- [x] LiteLLM

### 3.3 KV / Storage

- [x] LMCache
- [x] Mooncake
- [x] 3FS

### 3.4 Communication

- [x] NIXL
- [x] NCCL
- [x] RCCL
- [x] DeepEP
- [x] UCX
- [x] VCCL
- [x] FlagCX

### 3.5 Runtime / Kernel

- [x] FlashInfer
- [x] FlashAttention
- [x] CUTLASS
- [x] DeepGEMM
- [x] FlashMLA
- [x] FlagGems
- [x] FlagAttention
- [x] ops-transformer
- [x] MindIE-Motor
- [x] TokenSpeed
- [x] vllm-plugin-FL
- [x] sglang-plugin-FL

### 3.6 Compiler

- [x] Triton
- [x] TileLang
- [x] DeepJIT
- [x] FlagTree

### 3.7 Training / Framework

- [x] Colossal-AI
- [x] OneFlow
- [x] FlagScale

### 3.8 Scheduler

- [x] KAI-Scheduler
- [x] Volcano
- [x] Kueue

### 3.9 Device Resource

- [x] HAMi
- [x] Kubernetes DRA
- [x] NVIDIA GPU Operator
- [x] NVIDIA k8s-device-plugin

### 3.10 Ecosystem / Optimization / Benchmark

- [x] DeepSeek-Infra
- [x] FlagOS
- [x] msModelSlim
- [x] FlagPerf
- [x] FlagRelease

### 每个项目的迁移验收项

- [ ] canonical project 页面唯一。
- [ ] repository / docs URL 已核验并统一命名。
- [ ] docs category 与旧 relationship layer 已映射到 canonical layer。
- [ ] status 已迁移。
- [ ] snapshot.as_of 已折叠为 last_verified；updated 不迁移。
- [ ] capabilities 已归并到精简后的 areas 或正文，不保留第二套标签体系。
- [x] integrations 已迁移；59 个迁移项目已逐批核对 integration 名称，未发现断链。
- [ ] backends 已映射到 hardware；非硬件 backend 留正文或 integrations。
- [ ] organization 已归一化到现有 company/community 或保留在正文，不新增 upstream_org 字段。
- [ ] 原 relationship 中的重要 people / companies / governance 事实无丢失；people/governance 可转正文。
- [ ] linked_people / linked_companies 可由 generated graph 重建，不依赖手工 frontmatter。
- [ ] Sources 足以支撑新增的技术事实。
- [ ] 旧项目 Wiki Link 能通过 alias/redirect 或转换规则找到新节点。

## 4. Community / Organization 归一化

本次迁移不把 Software V0.1 的 `organization` 机械搬成 Project v3 字段。它原本混合了 GitHub namespace、治理社区和真实公司三种语义，继续保留只会制造新的歧义。

- [x] Software 项目的 `organization` 已停止作为 canonical project 字段迁移。
- [x] 若 relationship 已有明确 company/community 实体，只复用已有 canonical 实体；Project v3 用 `companies` 表达有强证据的公司关系，治理/namespace 细节留正文。
- [x] namespace 与真实公司保持区别：GitHub org、foundation/community、company 不互相自动等价。
- [x] 不将 GitHub organization 名称自动等价为公司。
- [x] 不要求为每个 upstream namespace 建 community 节点；只有当它本身是持续存在、具有独立治理/生态意义的技术社区时才建立 community。
- [x] 新建 community 仍沿用 `schema/community.yaml` 与直接来源要求，不从 repository owner 自动生成。
- [x] `ai_infra_docs/software/COMMUNITIES.md` 已降级为 upstream namespace 导航视图，不再复制 capability / integration / hardware / maintainer 等 canonical project 事实。

因此 Project v3 保持精简：不新增 `upstream_org`。需要回答“项目属于哪个 GitHub namespace”时可由 repository URL 或 docs 导航视图获得；需要回答“哪个公司/社区实际治理项目”时必须依赖 relationship 中的显式证据。

## 5. Software Index 改为自动生成

- [x] relationship 不再人工维护迁入项目的静态列表。
- [x] 从 project `layer` / `status` 自动生成 Software Project Index。
- [ ] 支持按以下维度筛选：
  - [x] inference-engine
  - [x] distributed-serving
  - [x] kv-cache / storage
  - [x] communication
  - [x] runtime / kernel
  - [x] compiler
  - [x] training
  - [x] scheduler
  - [x] device-resource
  - [x] ecosystem / optimization / benchmark
- [x] Index 增加 People / Companies 邻接计数与 Graph 深链，项目可直接聚焦到现有 1-hop Graph Explorer。
- [x] Software Index 通过 `graph-explorer/?focus=<project>` 复用现有 1-hop Explorer，可继续进入人物、公司、学校和社区邻居。
- [x] Concept 索引继续由 `ai_infra_docs/software/concepts` 自己维护，不合入 relationship Software Index。

## 6. Research Planner 接入

- [x] 更新 EXPAND，使 project 节点可沿以下方向扩展：
  - [x] maintainers / contributors
  - [x] upstream organization
  - [x] integrations / dependencies
  - [x] technical areas
- [x] 更新 DISCOVER，使 project 技术元数据参与 coverage-gap，但仍以人物、组织、项目生态发现为目标。
- [ ] VERIFY 可检查：
  - [x] project status freshness
  - [x] repository / docs URL
  - [x] integration 是否仍存在
  - [x] governance / maintainer 漂移
  - [x] last_verified 过期
- [x] planner 明确禁止从“共同 areas”自动产生 person-to-person 强边。
- [x] 更新 `docs/research-action-planner.md` 与 `docs/research-operators.md`。

## 7. Validator / Graph Builder / CI

- [x] Validator 支持 project-v3。
- [x] 检查 `integrations` 指向存在的 canonical project。
- [x] 检查 `last_verified` 格式与缺失。
- [x] 检查 repository URL 冲突。
- [x] 检查同一 repository 被多个 canonical project 重复声明。
- [x] 检查新页面不再新增 `capabilities` / `backends` / `snapshot` / `upstream_org` 等已收敛字段。
- [ ] 检查 `linked_people` / `linked_companies` 能从图结构重新生成。
- [x] Graph builder / typed relation export 已把 Project v3 `integrations` 输出为 `project-integration` typed edges；新增/合并后的 project 节点由 `audit-graph.py` 统一生成。
- [x] Graph Explorer 已有 Project 类型筛选，并新增 Software Index project focus 深链与 `project-integration` typed edge。
- [ ] Quartz route audit 覆盖新项目路径和兼容 alias。
- [x] CI 在迁移期区分 hard error 与 migration warning。
- [x] 不为 Concept 增加 relationship 侧 schema、validator 或 Graph Explorer 特殊逻辑。

## 8. ai_infra_docs 兼容迁移

- [x] `ai_infra_docs/software/projects` 已全部转为 `project-redirect`，relationship 为唯一 canonical project source。
- [x] 建立旧 software project path → relationship canonical URL 映射；relationship 侧同时保留 `research/software-project-migration.json`。
- [x] 已扫描 `ai_infra_docs/models/**`：当前 7 个页面引用 software project，均命中保留的 `software/projects/*` redirect。
- [x] 已扫描 `ai_infra_docs/chip/**`：当前没有 `software/projects/*` 引用。
- [x] 采用稳定的本地 redirect 兼容层：models/concepts 继续链接 `software/projects/*`，redirect 再指向 relationship canonical project；无需在每个引用页写跨仓硬链接。
- [x] **保留 models / chip 对 `software/concepts/*` 的本地引用，不做跨仓迁移。**
- [ ] 确认 docs Quartz 无 404。
- [ ] 确认 relationship Quartz 无 duplicate route。
- [x] docs 中 59 个重复 project 页面已全部变成薄 `project-redirect`，旧路径保持稳定。
- [x] 保留 `software/concepts/*`、其索引与概念文档职责。
- [x] `ai_infra_docs/software/SCHEMA.md` 已升级为 Software Schema V0.2：Concept + Project Redirect 双职责。

## 9. 推荐执行批次

### Batch A：基础设施

- [x] project-v3 精简 schema
- [x] layer/category migration mapping
- [x] infra-project → project 源节点迁移
- [x] catalog
- [x] validators（source-level migration audit 已接入 CI）
- [x] graph builder（`integrations` → derived `project-integration` typed edges）
- [x] 59 项目 migration mapping 表

### Batch B：高价值重复项目

优先处理两仓库重叠最深、人物关系最多的项目：

- [x] vLLM
- [x] SGLang
- [x] LMCache
- [x] Mooncake
- [x] llm-d
- [x] DeepEP
- [x] DeepSeek-Infra
- [x] vLLM-Ascend
- [x] KTransformers
- [x] FlashInfer
- [x] DeepGEMM
- [x] FlashMLA

### Batch C：其余 Software 项目

- [x] 按 layer 分批迁移余下项目。
- [ ] 每批迁移后运行 duplicate / broken-link / schema audit。

### Batch D：Planner 与生成视图

- [x] EXPAND / DISCOVER / VERIFY 接入 project-v3 新字段。
- [x] 自动 Software Project Index。
- [x] Software Index 增加 project focus 深链，复用 Graph Explorer 已有 Project 类型筛选与 1-hop 邻接。
- [x] project freshness 已进入 VERIFY；migration audit/index 由 CI 生成。

### Batch E：docs 收尾

- [x] models/chip 的 project 引用兼容迁移完成：models 通过本地 redirect 间接指向 relationship，chip 当前无 project 引用。
- [x] docs software project canonical 内容退役，59 个页面全部降级为 redirect。
- [x] docs project 页面不再复制 capability / integration / backend / snapshot 等 canonical 项目事实；validator 已要求全部 project 页面为 redirect。
- [x] 保留 `software/concepts` 及其本地链接。
- [x] 保留 59 个 project redirects / compatibility notes。

### 当前唯一阻塞：generated / Actions

当前通过 GitHub App API 直接提交到 `main` 的变更没有可靠触发 `Sync Node Schemas` GitHub Actions，因此 `generated/nodes.json`、`schema/nodes/**`、`generated/software-project-migration-audit.*` 和 `generated/software-project-index.md` 仍是旧快照或尚未生成。

- [ ] 通过普通 Git push 或 GitHub UI 的 `workflow_dispatch` 触发 `Sync Node Schemas`。
- [ ] 确认 `generated/software-project-migration-audit.json` 状态为 `pass`。
- [ ] 确认 `generated/nodes.json` 中 `infra-project` 数量归零。
- [ ] 确认 `generated/software-project-index.md` 已生成并包含 59 个项目。
- [ ] 确认 node schema mirrors 与 Project v3 源数据同步。

## 10. 完成定义（Definition of Done）

当且仅当以下条件全部满足，才认为 Software Project 迁移完成：

- [ ] 59 个项目在 relationship 中均有且只有一个 canonical project 节点。
- [x] `ai_infra_docs/software/concepts/*` 未迁移，仍由 docs 维护。
- [x] relationship 未新增 concept canonical node type。
- [x] 两仓库不存在同一软件项目的双 canonical source；docs 仅保留 redirect。
- [ ] 人物 / 公司 / 学校 / community 与项目关系无回归。
- [x] Project ↔ Project `integrations` 已进入 typed edges，可由 Graph Explorer / generated graph 查询；更复杂 dependencies 继续使用 relation model/正文。
- [ ] Person → Project 和 Project → Person 路径可查询。
- [x] project 的 layer / status / areas / hardware / integrations / last_verified 等精简技术元数据可查询。
- [x] infra-project 已收敛为 project，不再新增 infra-project canonical 节点。
- [ ] linked_people / linked_companies 不再依赖人工 frontmatter，generated 数据可重新生成。
- [ ] 所有 generated schema 可重新生成。
- [ ] audit / validator / Quartz build 全部通过。
- [x] models 中现有 software project 引用均命中 59 个保留 redirect；chip 当前无 project 引用。
- [x] docs 中 software concept 继续留在原仓库，未迁移。
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
