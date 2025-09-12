# 项目概览

本项目使用 `diagrams` 与 Graphviz 生成多类系统设计图：

- 数据密集型系统设计（data_intensive_system）
- 操作系统设计（os_design）
- Kubernetes 子系统（k8s_design）
- IM 系统 SDK 设计（im_sdk_design）
- IM SDK 变体：移动端（im_sdk_mobile）、桌面端（im_sdk_desktop）、Web（im_sdk_web）
- IM 实时音视频（im_sdk_rtc）

## 依赖

- Python 3.8+
- Graphviz（提供 `dot` 命令）
- Python 包：`diagrams`

### macOS 安装

```bash
brew install graphviz
python3 -m pip install --upgrade pip
python3 -m pip install diagrams
```

## 生成方式（脚本）

在项目根目录执行：

```bash
# 数据密集型
python3 diagram.py
# OS
python3 os_diagram.py
# K8s
python3 k8s_diagram.py
# IM SDK（通用）
python3 im_sdk_diagram.py
# IM SDK（移动端/桌面端/Web）
python3 im_sdk_mobile_diagram.py
python3 im_sdk_desktop_diagram.py
python3 im_sdk_web_diagram.py
# IM 实时音视频
python3 im_sdk_rtc_diagram.py
```

## 使用 Makefile 一键生成

```bash
# 生成全部
dmake all
# 单独生成
dmake data | dmake os | dmake k8s | dmake imsdk | dmake imsdk-mobile | dmake imsdk-desktop | dmake imsdk-web | dmake imsdk-rtc
# 清理
make clean
```

## 输出文件

- `data_intensive_system.(png|pdf)`
- `os_design.(png|pdf)`
- `k8s_design.(png|pdf)`
- `im_sdk_design.(png|pdf)`
- `im_sdk_mobile.(png|pdf)`、`im_sdk_desktop.(png|pdf)`、`im_sdk_web.(png|pdf)`
- `im_sdk_rtc.(png|pdf)`

## 说明

- 所有图均使用通用 `Server` 图标以最大化兼容不同 `diagrams` 版本。
- 若需更细图标与主题，请升级 `diagrams` 或自定义节点。
