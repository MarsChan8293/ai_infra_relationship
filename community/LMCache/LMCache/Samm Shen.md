---
type: person
name: Samuel Shen
aliases: ["Samm Shen", "sammshen", "slshen"]
current_affiliations: ["TensorMesh"]
public_email: slshen@tensormesh.ai
schools:
  - "University of Chicago"
communities: [LMCache, vLLM]
roles: [Software Engineer, LMCache Committer, Component Owner]
linked_companies:
  - "company/TensorMesh/TensorMesh"
areas: [kv-cache, gpu-connector, storage-backend, vllm-integration, sglang-integration, tensorrt-llm-integration, ci]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/TensorMesh/程翊华 Yihua Cheng","type":["open-source-collaboration","community-maintainer"],"project":"LMCache","confidence":"high","evidence":["https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md","https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS"]}'
  - '{"target":"company/TensorMesh/杜昆泰 Kuntai Du","type":["open-source-collaboration","community-maintainer"],"project":"LMCache","confidence":"high","evidence":["https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md","https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS"]}'
  - '{"target":"company/腾讯/Baolong Mao","type":["open-source-collaboration","technical-collaboration","community-maintainer"],"project":"LMCache","start":"2025","confidence":"high","evidence":["https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS","https://blog.lmcache.ai/en/2026/01/21/p2p-1/"]}'
---
# Samuel Shen（Samm Shen）

当前：[[company/TensorMesh/TensorMesh|TensorMesh]] Software Engineer；LMCache Committer、核心组件 CODEOWNER。

## 教育 / 工作
- University of Chicago：Mathematics + Computer Science 双学位；TensorMesh 官方团队页公开确认。
- TensorMesh：Software Engineer。

## LMCache 角色
当前 `CODEOWNERS` 显示 Samuel Shen 覆盖范围非常广，包括 core engine、memory management、GPU connector、storage backends、native connector、C extensions、tests / docs / CI 等。

更重要的是，他直接位于多 serving-engine integration 的交叉点：
- `lmcache/integration/vllm/`：CODEOWNER；
- `lmcache/integration/sglang/`：CODEOWNER；
- `lmcache/integration/tensorrt_llm/`：CODEOWNER。

因此他是当前 LMCache 生态里很强的 `vLLM ↔ LMCache ↔ SGLang ↔ TensorRT-LLM ↔ TensorMesh` 桥节点。

公开 LMCache commit 使用 `slshen@tensormesh.ai`，因此 TensorMesh 组织关系也有职业邮箱这一层独立证据。

## vLLM 直接贡献
2026-06 Samuel Shen 直接向 vLLM 仓库提交 LMCache examples 更新，因此 vLLM 关系不仅来自 LMCache 内部 integration 目录，也有上游项目直接 commit 证据。

## 人物关系
- [[company/腾讯/Baolong Mao|Baolong Mao]]：LMCache P2P / storage / integration 技术协作者。2026-01 LMCache 官方 P2P 文章将 Samuel Shen（TensorMesh）与 Baolong Mao（Tencent）共同列为 production-grade multi-node CPU P2P KV sharing 的作者/工程网络。
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]、[[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：LMCache 维护协作者；这里记录开源协作，不因同属 TensorMesh 自动扩张人物关系类型。

## 学校关联
- [[university/University of Chicago/University of Chicago|University of Chicago]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://www.tensormesh.ai/team-members/samuel-shen
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/commit/1106823089b04a852f00dfa40b7c641d23a2e6fb
- https://blog.lmcache.ai/en/2026/01/21/p2p-1/
- https://github.com/vllm-project/vllm/commit/c9135db27cafb853af5e2cb86c1a0b3c6b5b8c91

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/TensorMesh/TensorMesh|TensorMesh]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
