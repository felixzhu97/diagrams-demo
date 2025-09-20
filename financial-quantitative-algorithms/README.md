# 金融与量化算法系统

本文件夹包含金融与量化交易相关的算法体系架构图生成脚本，使用 `diagrams` 与 Graphviz 生成 PNG/PDF 格式的算法流程图。

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

## 包含的金融与量化算法

### 投资组合与风险管理

- 投资组合优化（portfolio_optimization_algorithm）
- 期权定价与风险管理（option_pricing_algorithm）
- 风险平价与风险预算（risk_parity_algorithm）
- 风险因子模型（risk_factor_model_algorithm）
- 收益归因分析（performance_attribution_algorithm）
- 资产负债管理 ALM（asset_liability_management_algorithm）

### 量化交易系统

- 量化交易系统与流程（quant_trading_algorithm）
- 统计套利（statistical_arbitrage_algorithm）
- 跨品种套利（cross_asset_arbitrage_algorithm）
- 高频交易 HFT（high_frequency_trading_algorithm）
- 做市与流动性提供（market_making_algorithm）
- 执行算法（execution_algorithm）

### 建模与分析

- 波动率建模（volatility_modeling_algorithm）
- 回测与仿真框架（backtesting_framework_algorithm）
- 固定收益曲线与期限结构（fixed_income_curve_algorithm）
- 机器学习预测（ml_prediction_algorithm）

## 生成方式

### 使用 Makefile 一键生成

```bash
# 生成全部金融量化算法图
make all

# 单独生成算法（示例）
make portfolio
make option
make quant
make riskparity
make statarb
make volmodel
make backtest
make execution
make marketmaking
make riskfactor
make attribution
make fixedincome
make crossasset
make alm
make hft
make mlpred

# 清理输出（删除 PNG/PDF）
make clean
```

### 手动执行脚本

```bash
# 投资组合与风险管理
python3 portfolio_optimization_algorithm.py
python3 option_pricing_algorithm.py
python3 risk_parity_algorithm.py
python3 risk_factor_model_algorithm.py
python3 performance_attribution_algorithm.py
python3 asset_liability_management_algorithm.py

# 量化交易系统
python3 quant_trading_algorithm.py
python3 statistical_arbitrage_algorithm.py
python3 cross_asset_arbitrage_algorithm.py
python3 high_frequency_trading_algorithm.py
python3 market_making_algorithm.py
python3 execution_algorithm.py

# 建模与分析
python3 volatility_modeling_algorithm.py
python3 backtesting_framework_algorithm.py
python3 fixed_income_curve_algorithm.py
python3 ml_prediction_algorithm.py
```

## 输出文件

### 投资组合与风险管理输出

- `portfolio_optimization_algorithm.(png|pdf)`
- `option_pricing_algorithm.(png|pdf)`
- `risk_parity_algorithm.(png|pdf)`
- `risk_factor_model_algorithm.(png|pdf)`
- `performance_attribution_algorithm.(png|pdf)`
- `asset_liability_management_algorithm.(png|pdf)`

### 量化交易系统输出

- `quant_trading_algorithm.(png|pdf)`
- `statistical_arbitrage_algorithm.(png|pdf)`
- `cross_asset_arbitrage_algorithm.(png|pdf)`
- `high_frequency_trading_algorithm.(png|pdf)`
- `market_making_algorithm.(png|pdf)`
- `execution_algorithm.(png|pdf)`

### 建模与分析输出

- `volatility_modeling_algorithm.(png|pdf)`
- `backtesting_framework_algorithm.(png|pdf)`
- `fixed_income_curve_algorithm.(png|pdf)`
- `ml_prediction_algorithm.(png|pdf)`

## 说明

- 为提升兼容性，当前图表统一使用通用 `Server` 图标构建。
- 若需更细图标与主题，可根据需要替换为 `diagrams` 里更具体的节点类别。
