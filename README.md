# AI Infra Relationship

这是一个面向 Obsidian 的 AI Infrastructure + Frontier Model Labs 人才、社区、公司、学校与项目关系图谱。

> 注意：除仓库根索引外，不再使用 `README.md` 作为实体节点文件名。所有社区、公司、模型团队与技术项目节点都使用实体同名文件，例如 `OpenAI/OpenAI.md`、`Qwen/Qwen.md`、`vLLM/vLLM.md`，避免 Obsidian Graph View 中出现大量无法区分的 `README` 节点。

## 建模规则

- 社区 / 项目：一级目录，例如 `vLLM/`、`SGLang/`、`FlashInfer/`
- 模型公司 / 团队：一级目录，例如 `OpenAI/`、`DeepSeek/`、`Zhipu-AI/`、`Qwen/`、`Moonshot-AI/`
- 实体首页：目录内使用与实体同名的 Markdown 文件，不使用 `README.md`
- 人物简历：优先放在其核心社区或模型团队目录，跨社区使用路径明确的 `[[目录/人物|人物]]` 双链
- 项目 credit、当前雇佣关系、论文合著、师生关系分开记录，不把“共同署名”自动等同于同一汇报线
- 中文姓名只有在公开资料明确给出汉字时才使用；否则保留公开英文名 / 拼音 / GitHub handle
- 未公开的学历或工作信息明确写 `公开信息待补`，不做身份推断

## Frontier Model Labs

[[OpenAI/OpenAI|OpenAI]] · [[DeepSeek/DeepSeek|DeepSeek]] · [[Zhipu-AI/Zhipu-AI|Zhipu AI / GLM]] · [[Qwen/Qwen|Qwen]] · [[Moonshot-AI/Moonshot-AI|Moonshot AI / Kimi]]

### 代表模型
[[OpenAI/GPT-4|GPT-4]] · [[OpenAI/GPT-4o|GPT-4o]] · [[OpenAI/o1|o1]] · [[DeepSeek/DeepSeek-V3|DeepSeek-V3]] · [[DeepSeek/DeepSeek-R1|DeepSeek-R1]] · [[Zhipu-AI/GLM-4.5|GLM-4.5]] · [[Qwen/Qwen3|Qwen3]] · [[Moonshot-AI/Kimi-K2|Kimi-K2]] · [[Moonshot-AI/Kimi-K3|Kimi-K3]]

## 按技术层浏览

### Serving Engine / Runtime
[[vLLM/vLLM|vLLM]] · [[SGLang/SGLang|SGLang]] · [[TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] · [[LightLLM/LightLLM|LightLLM]] · [[KTransformers/KTransformers|KTransformers]]

### GPU Kernel / MoE
[[FlashInfer/FlashInfer|FlashInfer]] · [[DeepSeek-Infra/DeepGEMM|DeepGEMM]] · [[DeepSeek-Infra/FlashMLA|FlashMLA]] · [[DeepSeek-Infra/DeepEP|DeepEP]] · [[Moonshot-AI/MoonEP|MoonEP]]

### KV Cache / Data Movement / Storage
[[LMCache/LMCache|LMCache]] · [[Mooncake/Mooncake|Mooncake]] · [[NIXL/NIXL|NIXL]] · [[DeepSeek-Infra/3FS|3FS]]

### Distributed Inference / Orchestration
[[Dynamo/Dynamo|Dynamo]] · [[llm-d/llm-d|llm-d]] · [[Ray-Serve/Ray-Serve|Ray Serve]] · [[AIBrix/AIBrix|AIBrix]] · [[Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]]

### Hardware / Resource Management
[[vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] · [[HAMi/HAMi|HAMi]] · [[KTransformers/KTransformers|KTransformers]]

### Systems Stack
[[DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]] · [[DeepSeek-Infra/DeepJIT|DeepJIT]]

## 值得观察的桥梁人物

- [[OpenAI/翁家翌|翁家翌]] ↔ [[vLLM/游凯超|游凯超]]：Tianshou 早期开源协作 → OpenAI RL infra / vLLM Inferact 两条路线
- [[OpenAI/翁家翌|翁家翌]] ↔ [[vLLM/李卓翰|李卓翰]]：OpenAI o1 contributor network ↔ vLLM
- [[Zhipu-AI/唐杰|唐杰]] → [[Moonshot-AI/杨植麟|杨植麟]]：清华师生关系；GLM 技术谱系 → Moonshot/Kimi
- [[Qwen/刘大一恒|刘大一恒]] ↔ [[DeepSeek/郭达雅|郭达雅]]：进入 Qwen / DeepSeek 前的论文合著网络
- [[Moonshot-AI/Guanduo Chen|Guanduo Chen]]：ByteDance runtime → Moonshot Training Infra → Kimi K2/K3
- [[DeepSeek/Jiashi Li|Jiashi Li]]：DeepSeek model author network → FlashMLA → vLLM/SGLang kernel ecosystem
- [[vLLM/Simon Mo|Simon Mo]]：Ray Serve → vLLM → Inferact
- [[SGLang/Yineng Zhang|Yineng Zhang]]：FlashInfer ↔ SGLang ↔ Together AI
- [[RadixArk/盛颖|盛颖]]：SGLang ↔ xAI ↔ RadixArk
- [[NIXL/Adit Ranadive|Adit Ranadive]]：network virtualization ↔ NIXL ↔ Dynamo / NVIDIA

## Obsidian 使用建议

开启 Graph View 后，可按 `type`、`company`、`communities`、`roles`、`areas`、`affiliation` 等 frontmatter 字段配合 Dataview 检索。重点观察同时连接模型项目、infra 项目与多家公司 / 学校的高 betweenness 节点，它们往往是技术迁移和人才流动的关键接口。