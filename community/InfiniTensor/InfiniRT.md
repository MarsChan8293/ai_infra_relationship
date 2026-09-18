---
type: project
name: InfiniRT
linked_people:
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
layer: hardware-runtime
open_source: true
repository: https://github.com/InfiniTensor/InfiniRT
areas: [runtime, device-abstraction, memory-management, heterogeneous-compute, cuda, hardware-backend]
people:
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
last_verified: "2026-09"
linked_companies: []
---
# InfiniRT

InfiniRT 是 [[InfiniCore]] 的 runtime / device abstraction 层，负责 device management、memory management、runtime operations 与多后端统一接口。

2026 的独立化使 InfiniCore 从“大仓库内嵌 runtime”转向可单独演进的组件化架构。公开提交覆盖 NVIDIA driver API、device attributes、Moore graph runtime、Cambricon 与其他硬件 backend。

[[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（Jiacheng Huang / voltjia）]]在现代九源栈的 runtime 重构与跨组件集成中持续活跃，但本页不据此声明 formal maintainer 身份。

## Sources
- https://github.com/InfiniTensor/InfiniRT
- https://github.com/InfiniTensor/InfiniRT/pull/44
- https://github.com/InfiniTensor/InfiniRT/pull/45

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（Jiacheng Huang）]]：GitHub `voltjia` 的直接工程轨迹横跨 [[community/InfiniTensor/NineToothed|NineToothed]]、[[community/InfiniTensor/InfiniCore|InfiniCore]]、[[community/InfiniTensor/InfiniOps|InfiniOps]]、[[community/InfiniTensor/InfiniRT|InfiniRT]]、[[community/Infini...

<!-- END AUTO PROJECT PEOPLE -->
