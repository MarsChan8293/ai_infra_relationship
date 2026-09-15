---
type: person
name: Shaoting Feng
aliases: ["Shaoting-Feng"]
current_affiliations: ["University of Chicago"]
schools:
  - "University of Chicago"
communities: [LMCache]
roles: [LMCache Committer, Component Owner]
areas: [kv-cache, multimodal-inference, gpu-connector, gds, sglang-integration]
confidence: verified
last_verified: "2026-09"
---
# Shaoting Feng

当前：University of Chicago；LMCache Committer、组件 CODEOWNER。

## LMCache 角色
官方 `MAINTAINERS.md` 将 Shaoting Feng 列为 UChicago Committer。当前 `CODEOWNERS` 显示其参与 GPU connector / GDS memory manager 路径，并直接出现在 `lmcache/integration/sglang/` 的 ownership 列表。

LMCache 官方 2025 年 multimodal KV caching 文章明确记录其参与 vLLM V1 multimodal KV cache 支持，包括 multimodal hash、request tracking、cache store/retrieve 路径。这条关系记录为 LMCache 侧面向 vLLM 的直接集成工作，不把它夸大为 vLLM 项目治理身份。

## 图谱意义
Shaoting Feng 是 LMCache 在两个方向上的高价值桥节点：一端连接 GPU/GDS 数据路径，另一端连接 vLLM multimodal 与 SGLang integration。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://blog.lmcache.ai/en/2025/07/03/lmcache-extends-its-turbo-boost-to-multimodal-models-in-vllm-v1/
