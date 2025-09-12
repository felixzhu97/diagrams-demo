# 项目概览

本项目使用 `diagrams` 与 Graphviz 生成多类系统设计图：

- 数据密集型系统设计（data_intensive_system）
- 操作系统设计（os_design）
- Kubernetes 子系统（k8s_design）
- IM 系统 SDK 设计（im_sdk_design）及变体（mobile/desktop/web）与 RTC（im_sdk_rtc）
- 大数据系统（big_data_design）
- 数据挖掘系统（data_mining_design）
- 软件工程体系（software_engineering）
- 人工智能系统（ai_design）
- 云计算架构（cloud_computing）
- IM 系统 ER 图（im_er_design）

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
# IM SDK（通用/变体/Web/RTC）
python3 im_sdk_diagram.py
python3 im_sdk_mobile_diagram.py
python3 im_sdk_desktop_diagram.py
python3 im_sdk_web_diagram.py
python3 im_sdk_rtc_diagram.py
# 大数据
python3 big_data_diagram.py
# 数据挖掘
python3 data_mining_diagram.py
# 软件工程
python3 software_engineering_diagram.py
# 人工智能
python3 ai_diagram.py
# 云计算
python3 cloud_computing_diagram.py
# IM ER 图
python3 im_er_diagram.py
```

## 使用 Makefile 一键生成

```bash
# 生成全部
make all
# 单独生成
make data | make os | make k8s | make imsdk | make imsdk-mobile | make imsdk-desktop | make imsdk-web | make imsdk-rtc | make bigdata | make datamining | make se | make ai | make cloud | make im-er
# 清理
make clean
```

## 输出文件

- `data_intensive_system.(png|pdf)`
- `os_design.(png|pdf)`
- `k8s_design.(png|pdf)`
- `im_sdk_design.(png|pdf)`、`im_sdk_mobile.(png|pdf)`、`im_sdk_desktop.(png|pdf)`、`im_sdk_web.(png|pdf)`、`im_sdk_rtc.(png|pdf)`
- `big_data_design.(png|pdf)`、`data_mining_design.(png|pdf)`
- `software_engineering.(png|pdf)`
- `ai_design.(png|pdf)`
- `cloud_computing.(png|pdf)`
- `im_er_design.(png|pdf)`

## 说明

- 所有图均使用通用 `Server` 图标以最大化兼容不同 `diagrams` 版本。
- 若需更细图标与主题，请升级 `diagrams` 或自定义节点。
