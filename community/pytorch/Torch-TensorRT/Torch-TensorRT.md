---
type: project
name: Torch-TensorRT
layer: compiler
status: active
code_availability: public
repository: https://github.com/pytorch/TensorRT
docs: https://pytorch.org/TensorRT/
areas:
  - pytorch-compiler
  - torch-compile
  - tensorrt-backend
  - aot-export
  - gpu-inference
hardware:
  - nvidia
integrations:
  - "TensorRT"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# Torch-TensorRT

## 项目简介
Torch-TensorRT 将 PyTorch 的 Module / `torch.compile`、`torch.export` 路径接入 NVIDIA [[TensorRT]] 进行优化执行；既可以在 Python 环境按需编译，也提供导出供 C++/LibTorch 加载的工作流。

## 项目归属
- GitHub 官方仓库位于 **`pytorch/TensorRT`**，而不是 `NVIDIA/Torch-TensorRT`。
- 官方文档指向 NVIDIA 维护的 Torch-TensorRT 页面，并随 NVIDIA 计算平台发布构建；记录公司 NVIDIA 的核心工程参与，并不因此声称 PyTorch 社区归 NVIDIA 独占。

## 层级与价值
- 在图谱中属于 **Compiler/模型编译入口**，而非 vLLM 类 Token Serving Engine。
- 关注 PyTorch 模型子图到 TensorRT 执行的图捕获/图断裂、序列化产物、算子覆盖率和精度回退。
- 对比 [[community/NVIDIA/Flare/Flare|Flare]] 时，Flare 复用 PyTorch/Transformers 做模型准备并产生专用 Runtime Package；Torch-TensorRT 核心是 PyTorch → TensorRT 编译与部署通道。

## Sources
- https://github.com/pytorch/TensorRT
- https://pytorch.org/TensorRT/
- https://github.com/pytorch/TensorRT/blob/main/README.md
