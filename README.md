# 项目概览

本项目使用 `diagrams` 与 Graphviz 生成多类系统设计图：

## 系统架构设计

- 数据密集型系统设计（data_intensive_system）
- 操作系统设计（os_design）
- Kubernetes 子系统（k8s_design）
- IM 系统 SDK 设计（im_sdk_design）及变体（mobile/desktop/web）与 RTC（im_sdk_rtc）
- 大数据系统（big_data_design）
- 数据挖掘系统（data_mining_design）
- 软件工程体系（software_engineering）
- 人工智能系统（ai_design）
- 云计算架构（cloud_computing）
- 自然语言处理系统（nlp_design）

## 知名公司技术栈

- WhatsApp 技术栈（whatsapp_tech_stack）
- Netflix 技术栈（netflix_tech_stack）
- Instagram 技术栈（instagram_tech_stack）
- Amazon 技术栈（amazon_tech_stack）
- Apple 技术栈（apple_tech_stack）

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

### 系统架构设计

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
# 自然语言处理
python3 nlp_diagram.py
# 工商管理
python3 business_admin_diagram.py
```

### 知名公司技术栈

```bash
# WhatsApp 技术栈
python3 whatsapp_tech_stack.py
# Netflix 技术栈
python3 netflix_tech_stack.py
# Instagram 技术栈
python3 instagram_tech_stack.py
# Amazon 技术栈
python3 amazon_tech_stack.py
# Apple 技术栈
python3 apple_tech_stack.py
```

## 使用 Makefile 一键生成

```bash
# 生成全部
make all
# 单独生成
make data | make os | make k8s | make imsdk | make imsdk-mobile | make imsdk-desktop | make imsdk-web | make imsdk-rtc | make bigdata | make datamining | make se | make ai | make cloud | make nlp | make ba
# 清理
make clean
```

## 输出文件

### 系统架构设计

- `data_intensive_system.(png|pdf)`
- `os_design.(png|pdf)`
- `k8s_design.(png|pdf)`
- `im_sdk_design.(png|pdf)`、`im_sdk_mobile.(png|pdf)`、`im_sdk_desktop.(png|pdf)`、`im_sdk_web.(png|pdf)`、`im_sdk_rtc.(png|pdf)`
- `big_data_design.(png|pdf)`、`data_mining_design.(png|pdf)`
- `software_engineering.(png|pdf)`
- `ai_design.(png|pdf)`
- `cloud_computing.(png|pdf)`
- `nlp_design.(png|pdf)`
- `business_admin.(png|pdf)`

### 知名公司技术栈

- `whatsapp_tech_stack.(png|pdf)`
- `netflix_tech_stack.(png|pdf)`
- `instagram_tech_stack.(png|pdf)`
- `amazon_tech_stack.(png|pdf)`
- `apple_tech_stack.(png|pdf)`

## 技术栈特色

### WhatsApp 技术栈

- **Erlang/OTP**: 高并发、容错性、热代码加载
- **FreeBSD**: 稳定的服务器操作系统
- **Ejabberd**: 基于 XMPP 的即时通讯服务器
- **端到端加密**: 消息安全传输
- **BEAM VM**: 支持百万级并发

### Netflix 技术栈

- **微服务架构**: 基于 Spring Boot 的微服务生态系统
- **Netflix OSS**: Zuul、Eureka、Hystrix、Ribbon 等开源组件
- **云原生**: 全面基于 AWS 云服务
- **大数据**: Spark、Hadoop、Kinesis 等大数据技术栈
- **机器学习**: 个性化推荐和 A/B 测试

### Instagram 技术栈

- **Python/Django**: 主要后端技术栈
- **多数据库策略**: PostgreSQL、Cassandra、MongoDB、Redis
- **媒体处理**: 专业的图像和视频处理服务
- **实时功能**: WebSocket、实时通知、直播
- **机器学习**: 内容推荐、用户行为分析

### Amazon 技术栈

- **微服务架构**: Java/Spring 微服务生态系统
- **AWS 生态**: 全面基于 AWS 云服务
- **多数据库**: Aurora、DynamoDB、RDS 等
- **大数据**: Spark、Hadoop、Kinesis、Redshift
- **机器学习**: 推荐系统、欺诈检测、需求预测

### Apple 技术栈

- **垂直整合**: 从硬件到软件的全栈控制
- **Swift 语言**: 现代化的类型安全编程语言
- **SwiftUI**: 声明式 UI 框架
- **Core ML**: 设备端机器学习框架
- **iCloud 生态**: 完整的云端服务套件

## 说明

- 所有图均使用通用 `Server` 图标以最大化兼容不同 `diagrams` 版本。
- 若需更细图标与主题，请升级 `diagrams` 或自定义节点。
- 技术栈图表展示了各公司的核心技术架构和特色功能。
