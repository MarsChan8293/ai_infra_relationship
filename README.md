# AI Infra Relationship

这是一个面向 Obsidian 的 AI Infrastructure 人才、社区、公司与学校关系图谱。

## 建模规则

- 社区 / 项目：一级目录，例如 `vLLM/`、`SGLang/`、`FlashInfer/`
- 公司 / 组织：一级目录，以 `README.md` 作为公司节点
- 人物简历：优先放在其核心社区目录，跨社区使用 `[[路径/人物|人物]]` 双链，避免重复维护
- 学校、公司、社区、技术项目均作为可点击节点
- 中文姓名只有在公开资料明确给出汉字时才使用；否则保留公开英文名 / 拼音 / GitHub handle
- 未公开的学历或工作信息明确写 `公开信息待补`，不做身份推断

## 按技术层浏览

### Serving Engine / Runtime
[[vLLM]] · [[SGLang]] · [[TensorRT-LLM]] · [[LightLLM]] · [[KTransformers]]

### GPU Kernel / MoE
[[FlashInfer]] · [[DeepGEMM]] · [[FlashMLA]] · [[DeepEP]]

### KV Cache / Data Movement / Storage
[[LMCache]] · [[Mooncake]] · [[NIXL]] · [[3FS]]

### Distributed Inference / Orchestration
[[Dynamo]] · [[llm-d]] · [[Ray-Serve]] · [[AIBrix]] · [[Triton-Inference-Server]]

### Hardware / Resource Management
[[vLLM-Ascend]] · [[HAMi]] · [[KTransformers]]

### Systems Stack
[[DeepSeek-Infra]] · [[DeepJIT]]

## 重点公司与组织

[[NVIDIA]] · [[Red Hat]] · [[Inferact]] · [[RadixArk]] · [[TensorMesh]] · [[DeepSeek]] · [[Together AI]] · [[Anyscale]] · [[Meta]] · [[ByteDance]] · [[Alibaba Cloud]] · [[xAI]] · [[Hugging Face]] · [[SenseTime]] · [[Approaching.AI]]

## 值得观察的桥梁人物

- [[vLLM/Simon Mo|Simon Mo]]：Ray Serve → vLLM → Inferact
- [[vLLM/Kaichao You|Kaichao You]]：清华 / Berkeley → vLLM → Inferact
- [[SGLang/Yineng Zhang|Yineng Zhang]]：FlashInfer ↔ SGLang ↔ Together AI
- [[RadixArk/盛颖|盛颖]]：SGLang ↔ xAI ↔ RadixArk
- [[vLLM/Yihua Cheng|Yihua Cheng]] / [[LMCache/Kuntai Du|Kuntai Du]]：vLLM ↔ LMCache ↔ TensorMesh
- [[Mooncake/Shangming Cai|Shangming Cai]]：Mooncake ↔ SGLang ↔ Alibaba Cloud ecosystem
- [[FlashInfer/Zihao Ye|Zihao Ye]]：TVM / UW systems ↔ FlashInfer ↔ NVIDIA
- [[NIXL/Adit Ranadive|Adit Ranadive]]：network virtualization ↔ NIXL ↔ Dynamo / NVIDIA
- [[vLLM/Robert Shaw|Robert Shaw]]：vLLM ↔ Red Hat ↔ llm-d

## Obsidian 使用建议

开启 Graph View 后，可按 `type`、`company`、`communities`、`roles`、`affiliation` 等 frontmatter 字段配合 Dataview 检索。重点观察同时连接多个社区或公司的高 betweenness 节点，它们通常对应技术路线迁移、公司人才流动或事实上的生态协调者。
