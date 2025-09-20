# 知名公司技术栈

本文件夹包含全球知名公司的技术栈架构图表，使用 `diagrams` 与 Graphviz 生成。

## 包含的公司技术栈

### 社交媒体与通讯

- **WhatsApp**: Erlang/OTP、FreeBSD、Ejabberd、端到端加密
- **Instagram**: Python/Django、多数据库策略、媒体处理、机器学习
- **LinkedIn**: 自研技术栈、流处理架构、大数据分析、AI 推荐
- **YouTube**: Google Cloud、视频处理、AI 技术、大数据
- **X (Twitter)**: 实时处理、大数据、机器学习、云原生
- **Tinder**: 匹配算法、跨平台支持、实时功能、地理位置
- **Bumble**: 女性优先设计、多产品生态、安全功能、实时通信

### 流媒体与娱乐

- **Netflix**: 微服务架构、Netflix OSS、云原生、大数据、机器学习
- **Spotify**: 微服务架构、推荐系统、跨平台支持、音频技术
- **YouTube**: Google Cloud、视频处理、AI 技术、大数据

### 电商与支付

- **Amazon**: 微服务架构、AWS 生态、多数据库、大数据、机器学习
- **PayPal**: 支付处理、风险控制、数据安全、云原生架构
- **Stripe**: API 优先设计、支付基础设施、机器学习、开发者工具
- **阿里巴巴**: 电商平台、阿里云、大数据、金融科技、AI 技术
- **支付宝**: 移动支付、金融产品、区块链、AI 风控、开放平台
- **DoorDash**: 外卖平台、实时配送、多端应用、支付系统

### 科技巨头

- **Apple**: 垂直整合、Swift、SwiftUI、Core ML、iCloud 生态
- **Microsoft**: .NET 生态、Azure 云服务、Office 365、Visual Studio
- **Google**: Go 语言、Kubernetes、TensorFlow、BigQuery、Firebase
- **Meta**: React 生态、Hack 语言、HHVM、GraphQL、PyTorch
- **Tesla**: 自动驾驶技术、OTA 更新、电池管理、数据驱动

### 企业级软件

- **Salesforce**: 多租户架构、Lightning 平台、Apex 语言、Einstein AI
- **Oracle**: Oracle 数据库、WebLogic 中间件、Oracle 云服务、企业应用
- **SAP**: ERP 系统、SAP HANA、SAP BTP、Fiori 应用、集成平台
- **ServiceNow**: ITSM 平台、多实例架构、工作流自动化、低代码开发
- **Workday**: 企业级 SaaS、多租户架构、内存数据库、低代码平台

### 金融科技

- **Goldman Sachs**: 投资银行、自研系统、风险控制、大数据、云服务
- **Morgan Stanley**: 金融服务、交易系统、风险管理、数据分析、云架构
- **Coinbase**: 加密货币交易、区块链技术、安全系统、实时交易、DeFi

### AI 与云计算

- **OpenAI**: 大型语言模型、多模态 AI、API 服务、云基础设施、安全 AI
- **Nvidia**: GPU 计算、CUDA 平台、深度学习框架、AI 和数据科学
- **AWS**: 全球领先云平台、完整服务生态、无服务器架构、大数据和 AI

### 中国科技公司

- **微信**: 即时通讯、小程序生态、企业服务、AI 技术、开放平台
- **抖音**: 短视频平台、推荐算法、视频处理、AI 技术、全球化
- **飞书**: 企业协作、实时通信、文档协作、工作流、集成能力
- **小红书**: 生活方式平台、内容推荐、电商系统、多媒体处理

### 其他知名公司

- **Adobe**: 创意软件、多产品生态、AI 驱动、多云架构、全球 CDN
- **Airbnb**: 共享经济平台、架构演进、开源贡献、跨平台开发、大数据驱动

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

## 生成方式

### 使用脚本

```bash
# 社交媒体与通讯
python3 whatsapp_tech_stack.py
python3 instagram_tech_stack.py
python3 linkedin_tech_stack.py
python3 youtube_tech_stack.py
python3 x_tech_stack.py
python3 tinder_tech_stack.py
python3 bumble_tech_stack.py

# 流媒体与娱乐
python3 netflix_tech_stack.py
python3 spotify_tech_stack.py

# 电商与支付
python3 amazon_tech_stack.py
python3 paypal_tech_stack.py
python3 stripe_tech_stack.py
python3 alibaba_tech_stack.py
python3 alipay_tech_stack.py
python3 doordash_tech_stack.py

# 科技巨头
python3 apple_tech_stack.py
python3 microsoft_tech_stack.py
python3 google_tech_stack.py
python3 meta_tech_stack.py
python3 tesla_tech_stack.py

# 企业级软件
python3 salesforce_tech_stack.py
python3 oracle_tech_stack.py
python3 sap_tech_stack.py
python3 servicenow_tech_stack.py
python3 workday_tech_stack.py

# 金融科技
python3 goldman_sachs_tech_stack.py
python3 morgan_stanley_tech_stack.py
python3 coinbase_tech_stack.py

# AI 与云计算
python3 openai_tech_stack.py
python3 nvidia_tech_stack.py
python3 aws_tech_stack.py

# 中国科技公司
python3 wechat_tech_stack.py
python3 douyin_tech_stack.py
python3 feishu_tech_stack.py
python3 xiaohongshu_tech_stack.py

# 其他知名公司
python3 adobe_tech_stack.py
python3 airbnb_tech_stack.py
```

### 使用 Makefile

```bash
# 生成全部技术栈图
make all

# 按类别生成
make social      # 社交媒体与通讯
make streaming   # 流媒体与娱乐
make ecommerce   # 电商与支付
make tech-giants # 科技巨头
make enterprise  # 企业级软件
make fintech     # 金融科技
make ai-cloud    # AI 与云计算
make china-tech  # 中国科技公司
make others      # 其他知名公司

# 清理输出文件
make clean
```

## 输出文件

每个公司技术栈都会生成以下格式的输出文件：

- `*_tech_stack.png`: PNG 格式的图表文件
- `*_tech_stack.pdf`: PDF 格式的图表文件

## 技术栈特色

### 社交媒体平台

- **高并发处理**: 支持百万级用户同时在线
- **实时通信**: WebSocket、消息队列、实时通知
- **内容推荐**: 机器学习驱动的个性化推荐系统
- **多媒体处理**: 图像、视频、音频的专业处理
- **全球化部署**: 多地区数据中心和 CDN 网络

### 流媒体平台

- **视频处理**: 大规模视频编码、转码和流媒体技术
- **推荐系统**: 先进的机器学习推荐算法
- **内容分发**: 全球 CDN 网络和边缘计算
- **用户体验**: 自适应码率、低延迟播放
- **数据分析**: 用户行为分析和内容优化

### 电商平台

- **交易处理**: 高并发、高可用的交易系统
- **支付安全**: PCI DSS 合规和端到端加密
- **推荐引擎**: 商品推荐和个性化营销
- **库存管理**: 实时库存同步和订单处理
- **数据分析**: 用户行为分析和商业智能

### 企业级软件

- **多租户架构**: 安全的数据隔离和资源共享
- **工作流引擎**: 强大的业务流程自动化
- **集成能力**: 丰富的第三方应用集成
- **数据分析**: 强大的 BI 和分析能力
- **安全合规**: 企业级安全防护和合规管理

### 金融科技

- **风险控制**: 实时风险监控和欺诈检测
- **交易处理**: 高并发、低延迟的交易系统
- **合规管理**: 严格的监管合规和审计
- **数据安全**: 企业级数据加密和安全防护
- **区块链技术**: 加密货币和智能合约应用

## 说明

- 所有图均使用通用 `Server` 图标以最大化兼容不同 `diagrams` 版本
- 若需更细图标与主题，请升级 `diagrams` 或自定义节点
- 技术栈图表展示了各公司的核心技术架构和特色功能
- 本文件夹包含 **40 个** 不同的知名公司技术栈图表
