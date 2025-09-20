# 系统架构、技术栈与算法图表集合

本项目使用 `diagrams` 与 Graphviz 生成多类系统设计图，包含系统架构设计、知名公司技术栈、商业算法和金融量化算法四大类图表。

## 项目结构

### 📁 [system-designs](./system-designs/)

系统架构设计相关图表，包含 **13 个** 不同的系统架构设计：

- 数据密集型系统设计
- 操作系统设计
- Kubernetes 容器编排系统
- IM 系统 SDK 设计（通用/移动端/桌面端/Web 端/RTC）
- 大数据与数据挖掘系统
- 软件工程体系
- 人工智能系统（AI/计算机视觉/自然语言处理）
- 新兴技术系统（物联网/区块链/云计算）

### 📁 [company-tech-stacks](./company-tech-stacks/)

知名公司技术栈相关图表，包含 **40 个** 不同的公司技术栈：

- 社交媒体与通讯（WhatsApp、Instagram、LinkedIn、YouTube、X 等）
- 流媒体与娱乐（Netflix、Spotify）
- 电商与支付（Amazon、PayPal、Stripe、阿里巴巴、支付宝等）
- 科技巨头（Apple、Microsoft、Google、Meta、Tesla）
- 企业级软件（Salesforce、Oracle、SAP、ServiceNow、Workday）
- 金融科技（Goldman Sachs、Morgan Stanley、Coinbase）
- AI 与云计算（OpenAI、Nvidia、AWS）
- 中国科技公司（微信、抖音、飞书、小红书）
- 其他知名公司（Adobe、Airbnb）

### 📁 [commercial-algorithms](./commercial-algorithms/)

商业算法相关图表，包含 **13 个** 不同的商业算法：

- 推荐系统算法
- 客户细分算法
- 流失预测算法
- 需求预测算法
- 价格优化算法
- 营销优化算法
- 库存管理算法
- 供应链优化算法
- 情感分析算法
- 异常检测算法
- 欺诈检测算法
- 信用评分算法
- 风险评估算法
- A/B 测试算法

### 📁 [financial-quantitative-algorithms](./financial-quantitative-algorithms/)

金融量化算法相关图表，包含 **16 个** 不同的金融量化算法：

- 投资组合优化算法
- 风险平价算法
- 动量策略算法
- 均值回归算法
- 套利策略算法
- 高频交易算法
- 期权定价算法
- 风险度量算法
- 回测框架算法
- 因子模型算法
- 多因子模型算法
- 事件驱动策略算法
- 算法交易算法
- 风险管理算法
- 压力测试算法
- 流动性管理算法

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

## 使用方式

### 生成所有图表

```bash
# 在项目根目录执行
make all
```

### 分别生成

```bash
# 生成所有系统架构设计图
make system-designs

# 生成所有公司技术栈图
make company-tech-stacks

# 生成所有商业算法图
make commercial-algorithms

# 生成所有金融量化算法图
make financial-quantitative-algorithms
```

### 单独生成特定类别

```bash
# 进入对应文件夹
cd system-designs
make data          # 数据密集型系统
make ai            # 人工智能系统
make iot           # 物联网系统
# ... 更多选项请查看对应文件夹的 README

cd company-tech-stacks
make social        # 社交媒体与通讯
make streaming     # 流媒体与娱乐
make ecommerce     # 电商与支付
# ... 更多选项请查看对应文件夹的 README

cd commercial-algorithms
make recommendation         # 推荐系统算法
make customer-segmentation  # 客户细分算法
make churn-prediction      # 流失预测算法
# ... 更多选项请查看对应文件夹的 README

cd financial-quantitative-algorithms
make portfolio-optimization  # 投资组合优化
make risk-parity           # 风险平价
make momentum-strategy     # 动量策略
# ... 更多选项请查看对应文件夹的 README
```

### 清理输出文件

```bash
# 清理所有输出文件
make clean

# 或分别清理
make clean-system-designs
make clean-company-tech-stacks
make clean-commercial-algorithms
make clean-financial-quantitative-algorithms
```

## 输出文件

每个图表都会生成以下格式的输出文件：

- `*.png`: PNG 格式的图表文件
- `*.pdf`: PDF 格式的图表文件

## 技术特色

### 系统架构设计

- **全面覆盖**: 涵盖从基础系统到前沿技术的完整架构设计
- **分层设计**: 从应用层到基础设施层的完整技术栈
- **实践导向**: 基于真实场景的系统架构设计

### 公司技术栈

- **全球视角**: 展示全球知名公司的核心技术架构和特色功能
- **行业分类**: 按社交媒体、流媒体、电商、金融等行业分类
- **技术深度**: 深入分析各公司的技术选型和架构决策

### 商业算法

- **业务导向**: 面向实际商业场景的算法设计
- **数据驱动**: 基于大数据和机器学习的智能算法
- **效果优化**: 专注于业务指标和用户体验的优化

### 金融量化算法

- **量化投资**: 专业的金融量化投资算法
- **风险控制**: 全面的风险管理和控制机制
- **回测验证**: 完整的历史数据回测和验证框架

## 说明

- 所有图均使用通用 `Server` 图标以最大化兼容不同 `diagrams` 版本
- 若需更细图标与主题，请升级 `diagrams` 或自定义节点
- 项目总计包含 **82 个** 不同的技术架构和算法图表
- 每个子文件夹都有详细的文档说明和独立的使用方式
- 为提升兼容性，当前图表统一使用通用 `Server` 图标构建
- 若需更细图标与主题，可根据需要替换为 `diagrams` 里更具体的节点类别
- 每个文件夹都有独立的 README.md 和 Makefile，便于独立使用和维护
