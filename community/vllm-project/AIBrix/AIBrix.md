---
type: project
name: AIBrix
parent: vLLM Project
linked_people:
  - "community/vllm-project/AIBrix/Chenyu Jiang"
  - "community/vllm-project/AIBrix/CYJiang"
  - "community/vllm-project/AIBrix/Guangjian"
  - "community/vllm-project/AIBrix/Jiang Xiaobin"
  - "community/vllm-project/AIBrix/Jianliang Qi"
  - "community/vllm-project/AIBrix/Jingyuan Zhang"
  - "community/vllm-project/AIBrix/Xin Li"
companies: ["字节跳动"]
company_relation: company-originated
layer: cloud-native-inference-infrastructure
open_source: true
linked_companies:
  - "company/字节跳动/字节跳动"
---
# AIBrix

## 项目简介
AIBrix 是 vLLM Project 旗下的云原生 GenAI inference infrastructure 项目，重点不在单机 engine，而在把模型 serving 变成 Kubernetes 上可调度、可扩缩、可路由、可观测的服务系统。核心方向包括 gateway/routing、autoscaling、distributed inference、runtime 管理、模型缓存与成本效率。

## GitHub
https://github.com/vllm-project/aibrix

## 主要维护者 / 组织
由 vLLM Project 社区维护；仓库以 Go 为主，采用 Apache-2.0 许可证。人物图谱优先按长期 maintainer、codeowner 与项目领导角色建模，不把普通 contributor 自动视为核心维护者。

## 主要贡献公司
- [[company/字节跳动/字节跳动|字节跳动]]：AIBrix 的原始开发/开源贡献方，并有 ByteDance 内部生产部署背景；项目后续进入 vLLM Project 社区治理。因此这里标记为 **originator / primary company contributor**，不把当前社区治理误写成 ByteDance 私有项目。
- Google、DaoCloud 等也有公开社区贡献，但当前不与“原始发起/主要公司贡献”混写；后续按持续 maintainer / codeowner 证据升级关系强度。

## 生态关系
- [[vLLM]]：最直接的 inference engine 上游之一。
- [[llm-d]]：同处 Kubernetes distributed inference 层，但治理与架构路线不同。
- [[HAMi]]：在 Kubernetes GPU/异构资源调度与共享层存在上下游关系。
- Kubernetes：AIBrix 的主要编排与部署底座。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/vllm-project/AIBrix/Chenyu Jiang|Chenyu Jiang]]：[[AIBrix]]：Batch / scheduling 方向活跃贡献者
- [[community/vllm-project/AIBrix/CYJiang|CYJiang]]：Project source / contributor context: https://github.com/vllm-project/aibrix
- [[community/vllm-project/AIBrix/Guangjian|Guangjian]]：Project source / contributor context: https://github.com/vllm-project/aibrix
- [[community/vllm-project/AIBrix/Jiang Xiaobin|Jiang Xiaobin]]：Project source / contributor context: https://github.com/vllm-project/aibrix
- [[community/vllm-project/AIBrix/Jianliang Qi|Jianliang Qi]]：Project source / contributor context: https://github.com/vllm-project/aibrix
- [[community/vllm-project/AIBrix/Jingyuan Zhang|Jingyuan Zhang]]：[[AIBrix]]：Batch runtime 方向活跃贡献者
- [[community/vllm-project/AIBrix/Xin Li|Xin Li]]：[[AIBrix]]：GPU optimizer / Kubernetes deployment 贡献者

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/字节跳动/字节跳动|字节跳动]]：公司页与社区/项目页均有显式记录；关系：`company-originated`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
