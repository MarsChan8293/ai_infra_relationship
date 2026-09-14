# betta18

社区：[[MindIE-SD]]

## 推理优化贡献
2026 年在 MindIE-SD 修复 MoE dispatcher 路由与 W8A8 dynamic quant 精度对齐问题，并根据 `top_k` 与 EP size 的关系选择 static / dynamic dispatcher，目标是降低 all-to-all 通信量并保持量化路径一致性。

## Sources
- https://gitcode.com/Ascend/MindIE-SD/tree/master/tests/layers
