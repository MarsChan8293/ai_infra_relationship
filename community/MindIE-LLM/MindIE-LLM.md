---
type: project
name: MindIE-LLM
companies: [Huawei]
company_relation: company-led
layer: inference-runtime
hardware: [Ascend]
open_source: true
---
# MindIE-LLM

## 项目简介
MindIE-LLM 是昇腾侧大语言模型推理加速项目。本图谱重点记录 SplitFuse / chunked prefill、Prefix Cache、MTP、PD 混部、并行与调度等直接影响推理性能和稳定性的实现。

## GitCode
https://gitcode.com/Ascend/MindIE-LLM

## GitHub
未确认官方 GitHub canonical repository；本节点以官方 GitCode 仓库作为源码来源。

## 主要贡献公司
- [[company/Huawei/Huawei|Huawei]]：Ascend/MindIE 官方技术栈的主要开发与维护公司节点。

## 推理优化技术线
2026 年公开 MR 已出现 SplitFuse + Prefix Cache + MTP、Prefix Cache + SP、PD 混部等组合执行路径的修复与扩展。部分贡献者目前只能可靠确认 GitCode handle，暂不创建人物页，避免凭邮箱或拼音推断实名。

## 生态关系
[[vLLM-Ascend]] · [[ops-transformer]] · [[MindIE-Motor]] · [[msModelSlim]]

## Sources
- https://gitcode.com/Ascend/MindIE-LLM/tree/master/src
- https://gitcode.com/Ascend/MindIE-LLM/tree/master/mindie_llm
- https://gitcode.com/Ascend/MindIE-LLM/tree/master/examples/atb_models/atb_framework/models
