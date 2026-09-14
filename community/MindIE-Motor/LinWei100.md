# LinWei100

社区：[[MindIE-Motor]]

## 推理优化贡献
2026 年在 MindIE-Motor 推进 Coordinator 调度热路径 Rust 重构，将每请求 IPC 记账改为共享内存原子记账；公开性能测试显示 `T_sched_proxy` P99 约提升 2.38×。同时参与 load balance、KV cache affinity、round robin 调度策略测试覆盖。

## Sources
- https://gitcode.com/Ascend/MindIE-Motor/tree/master/docs/zh
- https://gitcode.com/Ascend/MindIE-Motor/issues/131
