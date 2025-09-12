# 项目概览

本项目使用 `diagrams` 与 Graphviz 生成四类系统设计图：

- 数据密集型系统设计（data_intensive_system）
- 操作系统设计（os_design）
- Kubernetes 子系统（k8s_design）
- IM 系统 SDK 设计（im_sdk_design）

## 依赖

- Python 3.8+
- Graphviz（提供 `dot` 命令）
- Python 包：`diagrams`

### macOS 安装

```bash
# 安装 Graphviz（含 dot）
brew install graphviz

# 安装 Python 依赖
python3 -m pip install --upgrade pip
python3 -m pip install diagrams
```

若 `brew` 不可用，请参考 Graphviz 官方安装说明，确保终端可执行 `dot -V`。

## 生成方式

在项目根目录执行：

### 1) 数据密集型系统设计图

```bash
python3 diagram.py
```

输出文件：

- `data_intensive_system.png`
- `data_intensive_system.pdf`

### 2) 操作系统设计图（独立脚本）

```bash
python3 os_diagram.py
```

输出文件：

- `os_design.png`
- `os_design.pdf`

### 3) Kubernetes 子系统图（独立脚本）

```bash
python3 k8s_diagram.py
```

输出文件：

- `k8s_design.png`
- `k8s_design.pdf`

### 4) IM 系统 SDK 设计图（独立脚本）

```bash
python3 im_sdk_diagram.py
```

输出文件：

- `im_sdk_design.png`
- `im_sdk_design.pdf`

### 使用 Makefile 一键生成

```bash
# 生成全部
make all
# 仅生成数据密集型
make data
# 仅生成 OS 图
make os
# 仅生成 K8s 图
make k8s
# 仅生成 IM SDK 图
make imsdk
# 清理输出
make clean
```

## 文件说明

- `diagram.py`：数据密集型系统设计图脚本（仅生成 PNG/PDF）。
- `os_diagram.py`：操作系统设计图脚本（独立，生成 PNG/PDF）。
- `k8s_diagram.py`：Kubernetes 子系统图脚本（独立，生成 PNG/PDF）。
- `im_sdk_diagram.py`：IM 系统 SDK 设计图脚本（独立，生成 PNG/PDF）。
- `Makefile`：一键生成与清理入口。
- `web_service.png`：示例 Web Service 图（示例用途）。

## Kubernetes 子系统要点

- 控制面：`kube-apiserver`、`kube-scheduler`、`kube-controller-manager`、`etcd`
- 工作负载：`Deployments`、`Jobs`、`Pods`
- 存储：`CSI`、`PV`、`PVC`
- 网络：`CNI`、`Service`、`Ingress`、`Ingress Controller`
- 节点组件：`kubelet`、`kube-proxy`、`CRI (containerd/CRI-O)`
- 多命名空间隔离：`namespace: prod`、`namespace: dev`
- 自动伸缩：`HPA`、`VPA`
- 扩展：`Operator`、`CRD`
- Service Mesh：`istiod`、`Envoy Sidecar`

## 常见问题

- 报错 `ImportError` 或某些 onprem 组件不可用：已使用通用 `Server` 节点以兼容不同版本 `diagrams`，若需特定图标，请升级 `diagrams` 并替换为对应组件。
- 报错找不到 `dot`：请确认已安装 Graphviz，且 `dot -V` 可正常执行；若仍失败，检查 PATH 配置。
