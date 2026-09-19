---
type: project
name: LightLLM
status: active
repository: https://github.com/ModelTC/lightllm
last_verified: "2026-09"
linked_people:
  - "community/ModelTC/LightLLM/Hailong Yang"
  - "community/ModelTC/LightLLM/Junyi Chen"
  - "community/ModelTC/LightLLM/Niu Shengxiao"
  - "community/ModelTC/LightLLM/Ruihao Gong"
  - "community/ModelTC/LightLLM/Sang Chengmeng"
  - "community/ModelTC/LightLLM/Shihao Bai"
  - "community/ModelTC/LightLLM/Siyu Wu"
  - "community/ModelTC/LightLLM/Su Fubao"
  - "community/ModelTC/LightLLM/Zaijun Wang"
companies: ["商汤科技"]
company_relation: community-led
layer: inference-engine
areas:
  - "llm-serving"
  - "distributed-inference"
  - "token-generation"
hardware:
  - "nvidia"
integrations: []
linked_companies:
  - "company/商汤科技/商汤科技"
---
# LightLLM

## 项目简介
LightLLM 是 Python-based 的高性能 LLM inference / serving framework，强调轻量、可扩展与模型/硬件适配。它与 vLLM、SGLang 同属 serving engine 层，但形成了独立的调度、kernel 与模型支持技术路线。

## GitHub
https://github.com/ModelTC/lightllm

## 主要贡献公司
当前没有足够公开证据把 LightLLM 归为某一家公司的主要贡献项目；本图谱继续按 **ModelTC 社区主导** 建模。公司使用、论文引用或模型适配不会自动升级为“主要贡献公司”。

## 主要维护者 / 组织
由 ModelTC 社区维护。仓库与论文作者网络包含 serving scheduler、prefill/decode、KV cache 等方向贡献者；其中 [[Junyi Chen]] 可确认属于上海交通大学 NNE-Lab，并曾作为 LightLLM core contributor。

## 生态关系
[[FlashInfer]] · [[DeepSeek-Infra]] · [[vLLM]] · [[SGLang]] · [[上海交通大学]]。对 LightLLM 贡献者是否属于同一学校/公司必须逐人核验，不能仅凭共同仓库推断。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/ModelTC/LightLLM/Hailong Yang|Hailong Yang]]：Project source / contributor context: https://github.com/ModelTC/lightllm
- [[community/ModelTC/LightLLM/Junyi Chen|Junyi Chen]]：SenseTime Research：曾从事大模型系统与工具链工作，并成为 [[LightLLM]] core contributor。
- [[community/ModelTC/LightLLM/Niu Shengxiao|Niu Shengxiao]]：[[LightLLM]]：高活跃工程贡献者
- [[community/ModelTC/LightLLM/Ruihao Gong|Ruihao Gong]]：Project source / contributor context: https://github.com/ModelTC/lightllm
- [[community/ModelTC/LightLLM/Sang Chengmeng|Sang Chengmeng]]：[[LightLLM]]：模型与多模态方向活跃贡献者
- [[community/ModelTC/LightLLM/Shihao Bai|Shihao Bai]]：Project source / contributor context: https://github.com/ModelTC/lightllm
- [[community/ModelTC/LightLLM/Siyu Wu|Siyu Wu]]：Project source / contributor context: https://github.com/ModelTC/lightllm
- [[community/ModelTC/LightLLM/Su Fubao|Su Fubao]]：[[LightLLM]]：量化与 kernel 方向贡献者
- [[community/ModelTC/LightLLM/Zaijun Wang|Zaijun Wang]]：[[LightLLM]]：论文作者、持续核心工程贡献者

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/商汤科技/商汤科技|商汤科技]]：公司页与社区/项目页均有显式记录；关系：`community-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
