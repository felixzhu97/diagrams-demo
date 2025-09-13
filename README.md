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
- Microsoft 技术栈（microsoft_tech_stack）
- Google 技术栈（google_tech_stack）
- Meta 技术栈（meta_tech_stack）
- Tesla 技术栈（tesla_tech_stack）
- Salesforce 技术栈（salesforce_tech_stack）
- Oracle 技术栈（oracle_tech_stack）
- Nvidia 技术栈（nvidia_tech_stack）
- SAP 技术栈（sap_tech_stack）
- PayPal 技术栈（paypal_tech_stack）
- Stripe 技术栈（stripe_tech_stack）
- OpenAI 技术栈（openai_tech_stack）
- 阿里巴巴技术栈（alibaba_tech_stack）
- 支付宝技术栈（alipay_tech_stack）
- 微信技术栈（wechat_tech_stack）
- LinkedIn 技术栈（linkedin_tech_stack）
- YouTube 技术栈（youtube_tech_stack）
- X 技术栈（x_tech_stack）
- 小红书技术栈（xiaohongshu_tech_stack）
- Coinbase 技术栈（coinbase_tech_stack）
- Goldman Sachs 技术栈（goldman_sachs_tech_stack）
- Morgan Stanley 技术栈（morgan_stanley_tech_stack）
- 抖音技术栈（douyin_tech_stack）
- 飞书技术栈（feishu_tech_stack）
- DoorDash 技术栈（doordash_tech_stack）
- Workday 技术栈（workday_tech_stack）
- ServiceNow 技术栈（servicenow_tech_stack）
- Adobe 技术栈（adobe_tech_stack）
- AWS 技术栈（aws_tech_stack）
- Airbnb 技术栈（airbnb_tech_stack）
- Spotify 技术栈（spotify_tech_stack）
- Tinder 技术栈（tinder_tech_stack）
- Bumble 技术栈（bumble_tech_stack）

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
# Microsoft 技术栈
python3 microsoft_tech_stack.py
# Google 技术栈
python3 google_tech_stack.py
# Meta 技术栈
python3 meta_tech_stack.py
# Tesla 技术栈
python3 tesla_tech_stack.py
# Salesforce 技术栈
python3 salesforce_tech_stack.py
# Oracle 技术栈
python3 oracle_tech_stack.py
# Nvidia 技术栈
python3 nvidia_tech_stack.py
# SAP 技术栈
python3 sap_tech_stack.py
# PayPal 技术栈
python3 paypal_tech_stack.py
# Stripe 技术栈
python3 stripe_tech_stack.py
# OpenAI 技术栈
python3 openai_tech_stack.py
# 阿里巴巴技术栈
python3 alibaba_tech_stack.py
# 支付宝技术栈
python3 alipay_tech_stack.py
# 微信技术栈
python3 wechat_tech_stack.py
# LinkedIn 技术栈
python3 linkedin_tech_stack.py
# YouTube 技术栈
python3 youtube_tech_stack.py
# X 技术栈
python3 x_tech_stack.py
# 小红书技术栈
python3 xiaohongshu_tech_stack.py
# Coinbase 技术栈
python3 coinbase_tech_stack.py
# Goldman Sachs 技术栈
python3 goldman_sachs_tech_stack.py
# Morgan Stanley 技术栈
python3 morgan_stanley_tech_stack.py
# 抖音技术栈
python3 douyin_tech_stack.py
# 飞书技术栈
python3 feishu_tech_stack.py
# DoorDash 技术栈
python3 doordash_tech_stack.py
# Workday 技术栈
python3 workday_tech_stack.py
# ServiceNow 技术栈
python3 servicenow_tech_stack.py
# Adobe 技术栈
python3 adobe_tech_stack.py
# AWS 技术栈
python3 aws_tech_stack.py
# Airbnb 技术栈
python3 airbnb_tech_stack.py
# Spotify 技术栈
python3 spotify_tech_stack.py
# Tinder 技术栈
python3 tinder_tech_stack.py
# Bumble 技术栈
python3 bumble_tech_stack.py
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
- `microsoft_tech_stack.(png|pdf)`
- `google_tech_stack.(png|pdf)`
- `meta_tech_stack.(png|pdf)`
- `tesla_tech_stack.(png|pdf)`
- `salesforce_tech_stack.(png|pdf)`
- `oracle_tech_stack.(png|pdf)`
- `nvidia_tech_stack.(png|pdf)`
- `sap_tech_stack.(png|pdf)`
- `paypal_tech_stack.(png|pdf)`
- `stripe_tech_stack.(png|pdf)`
- `openai_tech_stack.(png|pdf)`
- `alibaba_tech_stack.(png|pdf)`
- `alipay_tech_stack.(png|pdf)`
- `wechat_tech_stack.(png|pdf)`
- `linkedin_tech_stack.(png|pdf)`
- `youtube_tech_stack.(png|pdf)`
- `x_tech_stack.(png|pdf)`
- `xiaohongshu_tech_stack.(png|pdf)`
- `coinbase_tech_stack.(png|pdf)`
- `goldman_sachs_tech_stack.(png|pdf)`
- `morgan_stanley_tech_stack.(png|pdf)`
- `douyin_tech_stack.(png|pdf)`
- `feishu_tech_stack.(png|pdf)`
- `doordash_tech_stack.(png|pdf)`
- `workday_tech_stack.(png|pdf)`
- `servicenow_tech_stack.(png|pdf)`
- `adobe_tech_stack.(png|pdf)`
- `aws_tech_stack.(png|pdf)`
- `airbnb_tech_stack.(png|pdf)`
- `spotify_tech_stack.(png|pdf)`
- `tinder_tech_stack.(png|pdf)`
- `bumble_tech_stack.(png|pdf)`

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

### Microsoft 技术栈

- **.NET 生态**: 统一的跨平台开发框架
- **Azure 云服务**: 完整的云计算平台
- **Office 365**: 生产力工具套件
- **Visual Studio**: 强大的 IDE 工具链
- **TypeScript**: JavaScript 的超集语言

### Google 技术栈

- **Go 语言**: 谷歌开发的并发编程语言
- **Kubernetes**: 容器编排的业界标准
- **TensorFlow**: 开源的机器学习框架
- **BigQuery**: 强大的数据仓库和分析平台
- **Firebase**: 移动和 Web 应用开发平台

### Meta 技术栈

- **React 生态**: 前端 UI 框架的领导者
- **Hack 语言**: 基于 PHP 的现代编程语言
- **HHVM**: 高性能 PHP/Hack 虚拟机
- **GraphQL**: 灵活的 API 查询语言
- **PyTorch**: 开源的深度学习框架

### Tesla 技术栈

- **自动驾驶技术**: Autopilot、神经网络、计算机视觉
- **OTA 更新**: 车辆软件远程更新系统
- **电池管理**: 先进的电池管理系统和充电技术
- **数据驱动**: 大规模车辆遥测数据收集和分析
- **云端服务**: 车辆管理、能源管理、用户服务

### Salesforce 技术栈

- **多租户架构**: 企业级 SaaS 平台的核心架构
- **Lightning 平台**: 现代化的 Web 和移动应用开发框架
- **Apex 语言**: Salesforce 专有的面向对象编程语言
- **Einstein AI**: 内置的 AI 和机器学习能力
- **MuleSoft 集成**: 强大的企业集成和数据连接平台

### Oracle 技术栈

- **Oracle 数据库**: 企业级关系型数据库的领导者
- **WebLogic 中间件**: Java 企业级应用服务器
- **Oracle 云服务**: 完整的云计算解决方案
- **企业应用套件**: EBS、PeopleSoft、JD Edwards 等
- **数据仓库和 BI**: Oracle 数据仓库、Analytics Cloud

### Nvidia 技术栈

- **GPU 计算**: GeForce、Tesla、Quadro 等 GPU 产品线
- **CUDA 平台**: 并行计算编程模型和平台
- **深度学习框架**: TensorRT、cuDNN、cuBLAS 等加速库
- **AI 和数据科学**: RAPIDS、NGC 容器、预训练模型
- **自动驾驶**: DRIVE 平台、Isaac、Omniverse 仿真

### SAP 技术栈

- **ERP 系统**: SAP ECC、S/4HANA、Business One 等核心业务系统
- **SAP HANA**: 内存数据库和实时分析平台
- **SAP BTP**: 业务技术平台和云原生开发环境
- **Fiori 应用**: 现代化的用户界面和移动应用
- **集成平台**: Cloud Integration、API 管理、Event Mesh

### PayPal 技术栈

- **支付处理**: 全球支付引擎和交易处理系统
- **风险控制**: 机器学习驱动的欺诈检测和风险评分
- **数据安全**: PCI DSS 合规和端到端加密
- **云原生架构**: 微服务、容器化和无服务器计算
- **实时分析**: 大数据处理和实时决策系统

### Stripe 技术栈

- **API 优先设计**: 开发者友好的 RESTful API 和 SDK
- **支付基础设施**: 全球支付网络和多种支付方式支持
- **机器学习**: Radar 欺诈检测和风险评分系统
- **开发者工具**: CLI 工具、Webhook、文档和测试工具
- **云原生架构**: 微服务、容器化和实时数据处理

### OpenAI 技术栈

- **大型语言模型**: GPT-4、GPT-3.5、Codex 等先进 AI 模型
- **多模态 AI**: DALL-E 图像生成、Whisper 语音识别
- **API 服务**: RESTful API 和开发者友好的 SDK
- **云基础设施**: 大规模 GPU 集群和分布式训练
- **安全 AI**: 内容审核、安全分类器和偏见检测

### 阿里巴巴技术栈

- **电商平台**: 淘宝、天猫、阿里巴巴国际站等完整电商生态
- **阿里云服务**: ECS、RDS、OSS 等完整的云计算解决方案
- **大数据平台**: MaxCompute、DataWorks、EMR 等大数据处理
- **金融科技**: 支付宝、蚂蚁链、余额宝等金融创新
- **AI 技术**: PAI 机器学习、智能推荐、自然语言处理

### 支付宝技术栈

- **移动支付**: 全球领先的移动支付平台和数字钱包
- **金融产品**: 余额宝、花呗、借呗等创新金融产品
- **区块链技术**: 蚂蚁链和智能合约应用
- **AI 风控**: 机器学习驱动的实时风险控制系统
- **开放平台**: 丰富的 API 服务和开发者生态

### 微信技术栈

- **即时通讯**: 全球最大的即时通讯平台和社交网络
- **小程序生态**: 完整的小程序开发平台和生态系统
- **企业服务**: 企业微信和完整的办公协作解决方案
- **AI 技术**: 自然语言处理、计算机视觉和智能推荐
- **开放平台**: 微信开放平台和丰富的第三方集成

### LinkedIn 技术栈

- **职场社交平台**: 全球领先的专业社交网络和职业发展平台
- **自研技术**: Voldemort 分布式存储、Espresso 文档存储、Galene 搜索引擎
- **流处理架构**: Apache Kafka、Samza 流处理框架
- **大数据分析**: Hadoop、Spark、实时数据仓库和分析系统
- **AI 推荐系统**: 机器学习驱动的职业推荐、内容推荐和人才匹配

### YouTube 技术栈

- **视频平台**: 全球最大的视频分享和流媒体平台
- **Google Cloud**: 全面基于 Google Cloud Platform 的云原生架构
- **视频处理**: 大规模视频编码、转码和流媒体技术
- **AI 技术**: 视频智能分析、内容推荐、自动字幕生成
- **大数据**: BigQuery、Dataflow、Pub/Sub 等大数据处理技术

### X 技术栈

- **社交媒体**: 全球领先的实时信息分享和社交网络平台
- **实时处理**: 高并发实时消息处理和流媒体技术
- **大数据**: Hadoop、Spark、Kafka 等大数据技术栈
- **机器学习**: 内容推荐、趋势分析、垃圾信息检测
- **云原生**: 微服务架构和容器化部署

### 小红书技术栈

- **生活方式平台**: 中国领先的生活方式分享和电商平台
- **内容推荐**: 基于机器学习的个性化内容推荐系统
- **电商系统**: 完整的电商交易和支付系统
- **多媒体处理**: 图像、视频处理和内容审核
- **社交功能**: 用户互动、关注、分享等社交功能

### Coinbase 技术栈

- **加密货币交易**: 全球领先的加密货币交易和托管平台
- **区块链技术**: 多链支持和智能合约集成
- **安全系统**: 企业级安全防护和合规管理
- **实时交易**: 高并发交易处理和风险控制
- **DeFi 集成**: 去中心化金融协议和流动性管理

### Goldman Sachs 技术栈

- **投资银行**: 全球领先的投资银行和金融服务
- **自研系统**: SecDB、Slang、Marquee 等专有交易系统
- **风险控制**: 实时风险管理和合规监控系统
- **大数据**: 大规模数据处理和量化分析
- **云服务**: 混合云架构和云原生应用

### Morgan Stanley 技术栈

- **金融服务**: 全球领先的投资银行和财富管理
- **交易系统**: Matrix、Athena 等专有交易平台
- **风险管理**: 实时风险监控和合规管理
- **数据分析**: 大数据分析和机器学习应用
- **云架构**: 混合云部署和微服务架构

### 抖音技术栈

- **短视频平台**: 全球领先的短视频分享和创作平台
- **推荐算法**: 基于深度学习的个性化推荐系统
- **视频处理**: 实时视频编码、特效和流媒体技术
- **AI 技术**: 计算机视觉、自然语言处理和内容理解
- **全球化**: 多地区部署和本地化服务

### 飞书技术栈

- **企业协作**: 字节跳动推出的企业级协作办公平台
- **实时通信**: 即时消息、音视频通话和会议系统
- **文档协作**: 在线文档编辑和团队协作功能
- **工作流**: 自动化工作流和审批系统
- **集成能力**: 丰富的第三方应用集成

### DoorDash 技术栈

- **外卖平台**: 美国领先的本地配送和外卖平台
- **实时配送**: 智能配送路线规划和实时跟踪
- **多端应用**: 消费者、商家、配送员三端应用
- **支付系统**: 安全的支付处理和风险控制
- **数据分析**: 用户行为分析和业务智能

### Workday 技术栈

- **企业级 SaaS**: 全球领先的 HCM 和财务管理云平台
- **多租户架构**: 安全的数据隔离和租户管理
- **内存数据库**: OMS 提供高性能数据访问
- **低代码平台**: Workday Extend 支持自定义应用开发
- **数据分析**: Prism Analytics 提供强大的分析能力

### ServiceNow 技术栈

- **ITSM 平台**: 全球领先的 IT 服务管理平台
- **多实例架构**: 安全的数据隔离和资源池管理
- **工作流自动化**: 强大的业务流程自动化引擎
- **低代码开发**: App Engine 支持快速应用开发
- **全栈解决方案**: 涵盖 IT、HR、CSM、EAM 等多个领域

### Adobe 技术栈

- **创意软件**: 全球领先的创意软件和数字体验平台
- **多产品生态**: Creative Cloud、Experience Cloud、Document Cloud
- **AI 驱动**: Adobe Sensei 人工智能平台
- **多云架构**: AWS、Azure、GCP 混合云部署
- **全球 CDN**: Fastly 提供全球内容分发

### AWS 技术栈

- **全球领先的云平台**: 世界最大的云计算服务提供商
- **完整的服务生态**: 涵盖计算、存储、数据库、网络、安全等全栈服务
- **无服务器架构**: Lambda、Fargate 等无服务器计算服务
- **容器化支持**: ECS、EKS 等容器编排服务
- **大数据和 AI**: EMR、SageMaker、Rekognition 等 AI/ML 服务

### Airbnb 技术栈

- **共享经济平台**: 全球领先的住宿共享平台
- **架构演进**: 从单体架构到微服务再到宏服务混合架构
- **开源贡献**: Apache Airflow、Superset 等知名开源项目
- **跨平台开发**: React Native 实现 iOS 和 Android 统一开发
- **大数据驱动**: 强大的数据分析和机器学习能力

### Spotify 技术栈

- **音乐流媒体领导者**: 全球领先的音乐流媒体服务提供商
- **微服务架构**: 基于 Squad 模型的微服务架构
- **推荐系统**: 先进的机器学习推荐算法
- **跨平台支持**: Web、移动、桌面、智能设备全覆盖
- **音频技术**: 专业的音频编码、流媒体和质量控制

### Tinder 技术栈

- **约会应用领导者**: 全球领先的约会和社交应用
- **匹配算法**: 先进的 ELO 和 Gale-Shapley 匹配算法
- **跨平台支持**: iOS、Android、Web 全覆盖
- **实时功能**: 即时消息、视频聊天、实时匹配
- **地理位置**: 基于位置的匹配和推荐

### Bumble 技术栈

- **女性优先约会应用**: 全球领先的女性优先约会平台
- **多产品生态**: Date、Bizz、BFF 多产品线
- **女性安全**: 专门的安全功能和保护机制
- **跨平台支持**: iOS、Android、Web 全覆盖
- **实时通信**: 即时消息、视频聊天、语音笔记

## 说明

- 所有图均使用通用 `Server` 图标以最大化兼容不同 `diagrams` 版本。
- 若需更细图标与主题，请升级 `diagrams` 或自定义节点。
- 技术栈图表展示了各公司的核心技术架构和特色功能。
- 项目包含 **11 个系统架构设计** 和 **40 个知名公司技术栈**，总计 **51 个** 不同的技术架构图表。
