# 商业算法系统

本文件夹包含常用商业算法的体系架构图生成脚本，使用 `diagrams` 与 Graphviz 生成 PNG/PDF 格式的算法流程图。

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

## 包含的商业算法

### 核心商业算法

- 推荐系统算法（recommendation_system_algorithm）
- 动态定价算法（pricing_algorithm）
- 库存管理算法（inventory_management_algorithm）
- 风险评估算法（risk_assessment_algorithm）
- 客户细分算法（customer_segmentation_algorithm）
- 营销优化算法（marketing_optimization_algorithm）
- 供应链优化算法（supply_chain_optimization_algorithm）

### 常用商业算法

- 欺诈检测算法（fraud_detection_algorithm）
- 需求预测算法（demand_forecasting_algorithm）
- 客户流失预测算法（churn_prediction_algorithm）
- 信用评分算法（credit_scoring_algorithm）
- 情感分析算法（sentiment_analysis_algorithm）
- 异常检测算法（anomaly_detection_algorithm）
- A/B 测试算法（a_b_testing_algorithm）

## 生成方式

### 使用 Makefile 一键生成

```bash
# 生成全部商业算法图
make all

# 单独生成核心算法（示例）
make recommendation
make pricing
make inventory
make risk
make customer
make marketing
make supply

# 单独生成常用算法（示例）
make fraud
make demand
make churn
make credit
make sentiment
make anomaly
make abtest

# 清理输出（删除 PNG/PDF）
make clean
```

### 手动执行脚本

```bash
# 核心商业算法
echo "生成推荐系统算法图" && python3 recommendation_system_algorithm.py
python3 pricing_algorithm.py
python3 inventory_management_algorithm.py
python3 risk_assessment_algorithm.py
python3 customer_segmentation_algorithm.py
python3 marketing_optimization_algorithm.py
python3 supply_chain_optimization_algorithm.py

# 常用商业算法
python3 fraud_detection_algorithm.py
python3 demand_forecasting_algorithm.py
python3 churn_prediction_algorithm.py
python3 credit_scoring_algorithm.py
python3 sentiment_analysis_algorithm.py
python3 anomaly_detection_algorithm.py
python3 a_b_testing_algorithm.py
```

## 输出文件

### 核心商业算法输出

- `recommendation_system_algorithm.(png|pdf)`
- `pricing_algorithm.(png|pdf)`
- `inventory_management_algorithm.(png|pdf)`
- `risk_assessment_algorithm.(png|pdf)`
- `customer_segmentation_algorithm.(png|pdf)`
- `marketing_optimization_algorithm.(png|pdf)`
- `supply_chain_optimization_algorithm.(png|pdf)`

### 常用商业算法输出

- `fraud_detection_algorithm.(png|pdf)`
- `demand_forecasting_algorithm.(png|pdf)`
- `churn_prediction_algorithm.(png|pdf)`
- `credit_scoring_algorithm.(png|pdf)`
- `sentiment_analysis_algorithm.(png|pdf)`
- `anomaly_detection_algorithm.(png|pdf)`
- `a_b_testing_algorithm.(png|pdf)`

## 说明

- 为提升兼容性，当前图表统一使用通用 `Server` 图标构建。
- 若需更细图标与主题，可根据需要替换为 `diagrams` 里更具体的节点类别。
