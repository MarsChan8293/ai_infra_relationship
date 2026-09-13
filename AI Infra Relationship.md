# AI Infra Relationship

这是一个面向 Obsidian 的 AI Infrastructure + Frontier Model Labs 人才、社区、公司、学校与项目关系图谱。

## 命名规则
- 不使用 `README.md` 作为图谱实体节点。
- 社区、公司、模型团队与技术项目均使用实体同名文件，例如 `OpenAI/OpenAI.md`、`vLLM/vLLM.md`。
- 对有可靠公开中文汉字姓名可确认的人物，文件名统一为 `中文名 English Name.md`，例如 `叶子豪 Zihao Ye.md`。
- 人物页 frontmatter 同时保留 `name`、`english_name` 与 `aliases`，便于 Obsidian / Dataview 中英文检索。
- 仅凭拼音、邮箱或 GitHub handle 不猜中文汉字姓名。
- 跨社区人物尽量只保留一个 canonical 人物页，其他社区通过路径双链引用。

## 人物关系硬规则
人物之间禁止只写裸双链，例如 `[[A]] · [[B]]`。每条人物关系必须尽量包含以下信息：

`[[人物]]：关系类型；时间；共事/合作场景；可核验依据或置信度。`

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

## 公司节点硬规则
每个公司 / 组织节点必须有可独立阅读的简介，不能只放人物或项目双链。至少包含：
- **公司简介**：公司定位、主要业务 / 技术方向，以及与 AI Infra / foundation model 的关系。
- **图谱中的连接**：该公司与哪些开源项目、模型团队或社区有直接关系。
- 若公开资料足够，可补成立时间、总部 / 主要研发地点、关键产品，但不为了完整度猜测未确认信息。

## 开源项目节点硬规则
每个开源项目节点必须有可独立阅读的项目介绍，不能只写“连接”。至少包含：
- **项目简介**：解决什么问题、位于 AI Infra 哪一层、核心技术特征。
- **GitHub 仓库**：必须给出官方 GitHub repository 地址；如果项目没有独立仓库而是 monorepo 子目录，要写清楚 monorepo 地址和子路径。
- **主要维护者 / 组织**：优先使用官方 governance、CODEOWNERS、MAINTAINERS 或公开 author credits。
- **生态关系**：说明与 vLLM / SGLang / Kubernetes / CUDA / ROCm / Ascend / KV cache 等上下游的具体连接，不把“兼容”自动推断成人物直接合作。

推荐格式：

`## 项目简介`  
`...`  
`## GitHub`  
`https://github.com/owner/repo`  
`## 主要维护者 / 组织`  
`...`

## Frontier Model Labs
[[OpenAI]] · [[DeepSeek]] · [[Zhipu-AI]] · [[Qwen]] · [[Moonshot-AI]]

## AI Infra
[[vLLM]] · [[SGLang]] · [[FlashInfer]] · [[LMCache]] · [[Mooncake]] · [[Dynamo]] · [[NIXL]] · [[llm-d]] · [[TensorRT-LLM]] · [[KTransformers]] · [[AIBrix]] · [[HAMi]] · [[vLLM-Ascend]]
