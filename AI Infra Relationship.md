# AI Infra Relationship

这是一个面向 Obsidian 的 AI Infrastructure + Frontier Model Labs 人才、社区、公司、学校与项目关系图谱。

## 一级目录结构
- `company/`：模型公司、云厂商、AI Infra 创业公司与平台公司。
- `community/`：开源推理引擎、GPU/NPU kernel、KV Cache、数据传输、Kubernetes serving、异构计算等社区与技术项目。
- `university/`：高校、实验室和研究机构，用于表达导师学生、同学、同门、访问研究和人才培养关系。
- 根目录保留本总索引；三个英文目录作为唯一一级分类结构，不再维护重复的中文镜像目录。

对应分类入口：[[company]] · [[community]] · [[university]]

## 命名规则
- 不使用 `README.md` 作为图谱实体节点。
- 社区、公司、模型团队与技术项目均使用实体同名文件，例如 `company/OpenAI/OpenAI.md`、`community/vllm-project/vLLM/vLLM.md`。
- 中国公司与中国高校统一使用**中文 canonical 名称**：目录名、实体文件 basename、frontmatter `name` / `title` 与双链目标均使用中文；英文名称只允许出现在来源 URL、必要的历史说明或非 canonical 搜索信息中。
- 集团内部业务线与模型团队不重复建公司实体；例如阿里巴巴是唯一公司主节点，阿里云作为业务关系、Qwen/通义千问作为团队/模型节点挂在阿里巴巴下。
- 对有可靠公开中文汉字姓名可确认的人物，文件名统一为 `中文名 English Name.md`，例如 `叶子豪 Zihao Ye.md`。
- 人物页 frontmatter 同时保留 `name`、`english_name` 与 `aliases`，便于 Obsidian / Dataview 中英文检索。
- 仅凭拼音、邮箱或 GitHub / GitCode handle 不猜中文汉字姓名。
- 跨社区人物尽量只保留一个 canonical 人物页，其他社区通过双链引用。
- `community/` 目录按 canonical upstream namespace / 治理组织分层，统一使用 `community/<organization>/<project>/...`；例如 `vLLM`、`vLLM-Ascend`、`AIBrix` 均归入 `community/vllm-project/`。项目短双链仍以项目 basename 为 canonical 引用。
- 新建显式路径链接时使用完整分类路径；能以唯一 basename 稳定解析时，优先使用不依赖目录的 `人物名` / `实体名`，降低未来迁移断链风险。

## 人物关系硬规则
人物之间禁止只写裸双链，例如 `A · B`。每条人物关系必须尽量包含以下信息：

`人物：关系类型；时间；共事/合作场景；可核验依据或置信度。`

### 关系类型
- **同事**：必须能确认在同一公司 / 实验室 / 正式团队同期共事；尽量写起止年份或“YYYY–至今”。
- **大学同学 / 实验室同门**：写学校、院系 / 实验室与重叠年份；只同校但无法确认同期时不得写“同学”。
- **导师 / 学生**：写指导阶段与学校，例如“2019–2024 UC Berkeley 博士导师 / 学生”。
- **共同创业**：写公司和公开成立 / 加入时间，例如“2025–至今 Inferact 联合创始人”。
- **论文合著**：写论文 / 技术报告与年份，例如“DeepSeek-V3 technical report，2024”。
- **开源项目协作**：写项目、模块与大致时间，例如“2024–至今 vLLM KV Connector / disaggregated serving 协作”；不能因此自动称为同事。
- **技术上下游协作**：写具体接口 / 项目，例如“MoonEP 受 DeepEP 启发，属于项目级技术关系”，不要虚构人物直接共事。

### 时间精度
- 有公开起止月份时写 `YYYY-MM–YYYY-MM`。
- 只有年份时写 `YYYY–YYYY`。
- 只能确认某一论文 / release 时，用该事件年份，不扩展成长期共事。
- 无法确认开始时间时写“截至 2026-09 可确认……”，不要猜日期。

### 证据与措辞
- 公司 / 学校 / 个人主页 / 官方项目治理文档优先。
- 只能确认同一开源社区时，用“社区协作 / 共同维护”，不要写“同事”。
- 关系时间、职位或直接合作证据不足时，在关系后注明“具体起始时间公开未确认”。

### 低信息贡献者节点
- 对只有 GitHub / GitCode handle、AUTHORS / CODEOWNERS / commit 记录可确认的人物，允许保留**证据受限的薄节点**，但必须明确“可确认的是项目贡献/责任域，个人履历未确认”。
- 不为了让图谱看起来“完整”而猜真实姓名、公司、学历、同事关系或长期维护者身份。
- 一旦获得官方 governance、作者页、个人主页、论文 affiliation 或公司资料，再把薄节点升级为完整人物页并补人物关系。
- 因此，“关系健全”优先指**所有已声明的边都可解释、可追踪且不过度推断**，而不是强迫每个贡献者节点都拥有相同密度的私人/职业信息。

## 公司节点硬规则
每个公司 / 组织节点必须有可独立阅读的简介，不能只放人物或项目双链。至少包含：
- **公司简介**：公司定位、主要业务 / 技术方向，以及与 AI Infra / foundation model 的关系。
- **图谱中的连接**：该公司与哪些开源项目、模型团队或社区有直接关系。
- 若公开资料足够，可补成立时间、总部 / 主要研发地点、关键产品，但不为了完整度猜测未确认信息。

## 开源项目节点硬规则
每个开源项目节点必须有可独立阅读的项目介绍，不能只写“连接”。至少包含：
- **项目简介**：解决什么问题、位于 AI Infra 哪一层、核心技术特征。
- **源码仓库**：必须给出官方 canonical repository 地址；优先 GitHub。若项目官方主仓位于 GitCode（例如部分 Ascend / CANN 项目），允许 GitCode 作为 canonical source，并明确说明未确认官方 GitHub 镜像。
- **主要维护者 / 组织**：优先使用官方 governance、CODEOWNERS、MAINTAINERS 或公开 author credits。
- **生态关系**：说明与 vLLM / SGLang / Kubernetes / CUDA / ROCm / Ascend / KV cache 等上下游的具体连接，不把“兼容”自动推断成人物直接合作。

推荐格式：

`## 项目简介`  
`...`  
`## GitHub / GitCode`  
`https://...`  
`## 主要维护者 / 组织`  
`...`

## 图谱完整性检查
每次 BFS 扩张或批量补节点后，至少检查以下四项：
- **canonical 可达**：所有 `type: person-link` / `canonical:` 指向的主人物页必须真实存在，禁止出现“跳到不存在页面”的软断链。
- **一人一主档**：同一人物跨公司、学校、社区出现时，保留一个 canonical 人物页；其他目录改为轻量关系页，不复制整份履历。
- **关键边双向可追踪**：高价值的人才迁移、共同创业、论文合著、核心维护关系，应至少能从人物页追到公司/项目，必要时公司/项目页也反向列出该人物。普通兼容性/生态列表不要求机械双向复制。
- **孤立节点复核**：人物页至少说明其与一个公司、学校、项目或社区的可核验关系；公司/项目页至少说明一个图谱连接。只有名字、裸双链或无法解释“为什么在图里”的节点应继续补证据或降级为待核验线索。

## Frontier Model Labs
[[OpenAI]] · [[深度求索]] · [[阿里巴巴]]（[[Qwen|通义千问]]） · [[月之暗面]] · [[智谱]]

## AI Infra
[[GPUStack]] · [[vLLM]] · [[vLLM Production Stack]] · [[SGLang]] · [[xLLM]] · [[xLLM-service]] · [[TokenSpeed]] · [[FlashInfer]] · [[LMCache]] · [[Mooncake]] · [[Dynamo]] · [[NIXL]] · [[llm-d]] · [[AIBrix]] · [[KServe]] · [[Gateway API Inference Extension]] · [[Ray Serve]] · [[BentoML]] · [[TensorRT-LLM]] · [[KTransformers]] · [[HAMi]] · [[vLLM-Ascend]] · [[ops-transformer]] · [[MindIE-LLM]] · [[MindIE-Motor]] · [[MindIE-SD]] · [[msModelSlim]] · [[openYuanRong]] · [[YuanRong DataSystem]]
