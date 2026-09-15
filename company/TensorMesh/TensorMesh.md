---
type: company
name: TensorMesh
focus: ai-inference-infrastructure
projects: [LMCache, vLLM]
people:
  - "company/TensorMesh/Junchen Jiang"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/TensorMesh/程翊华 Yihua Cheng"
  - "company/TensorMesh/Jiayi Yao"
  - "community/LMCache/LMCache/Samm Shen"
last_verified: "2026-09"
---
# TensorMesh

## 公司简介
TensorMesh 是围绕 LLM KV cache、disaggregated serving 与 inference memory/data plane 商业化的 AI infrastructure 公司。它承接了 [[LMCache]] 等研究成果，试图把跨 GPU/CPU/远端存储的 KV 管理能力产品化，是“研究系统 → 开源项目 → startup”的典型路径。

## 主要贡献的社区项目
- [[community/LMCache/LMCache/LMCache|LMCache]]：**research → startup core network / commercialization**。TensorMesh 官方资料明确说明公司由 LMCache 创始/核心技术网络发展而来，并持续维护 LMCache。
- [[community/vllm-project/vLLM/vLLM|vLLM]]：通过 KV Connector、disaggregated serving 与 LMCache integration 形成直接贡献网络。

## 核心人物
- [[company/TensorMesh/Junchen Jiang|Junchen Jiang]]：联合创始人、CEO；University of Chicago Associate Professor；LMCache 共同创建者。
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：联合创始人、CTO。
- [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：联合创始人、Chief Scientist。
- [[company/TensorMesh/Jiayi Yao|Jiayi Yao]]：LMCache Committer、CacheBlend 第一作者；Google / LMCache 合作材料将其与 Kuntai Du、Yihua Cheng 一并列入 LMCache 后成立 TensorMesh 的核心网络。
- [[community/LMCache/LMCache/Samm Shen|Samuel Shen]]：TensorMesh Software Engineer；LMCache Committer，横跨 vLLM / SGLang / TensorRT-LLM integration ownership。

## 图谱中的连接
[[LMCache]] · [[vLLM]] · [[University of Chicago]] · KV Connector · disaggregated serving。TensorMesh 与 Berkeley 网络在 PrefillOnly/Jenga 等研究中存在跨校合作，但其创始学术谱系主要是 University of Chicago，不能误标为 Berkeley 系。

## Sources
- https://www.tensormesh.ai/
- https://www.tensormesh.ai/team-members/samuel-shen
- https://blog.lmcache.ai/zh/2025/10/23/gke-lmcache/
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
