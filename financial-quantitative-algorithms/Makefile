PY=python3

.PHONY: all portfolio option quant riskparity statarb volmodel backtest execution marketmaking riskfactor attribution fixedincome crossasset alm hft mlpred clean

all: portfolio option quant riskparity statarb volmodel backtest execution marketmaking riskfactor attribution fixedincome crossasset alm hft mlpred

# 生成 投资组合优化图
portfolio:
	$(PY) portfolio_optimization_algorithm.py

# 生成 期权定价图
option:
	$(PY) option_pricing_algorithm.py

# 生成 量化交易流程图
quant:
	$(PY) quant_trading_algorithm.py

# 生成 风险平价图
riskparity:
	$(PY) risk_parity_algorithm.py

# 生成 统计套利图
statarb:
	$(PY) statistical_arbitrage_algorithm.py

# 生成 波动率建模图
volmodel:
	$(PY) volatility_modeling_algorithm.py

# 生成 回测框架图
backtest:
	$(PY) backtesting_framework_algorithm.py

# 生成 执行算法图
execution:
	$(PY) execution_algorithm.py

# 生成 做市算法图
marketmaking:
	$(PY) market_making_algorithm.py

# 生成 风险因子模型图
riskfactor:
	$(PY) risk_factor_model_algorithm.py

# 生成 收益归因分析图
attribution:
	$(PY) performance_attribution_algorithm.py

# 生成 固定收益曲线图
fixedincome:
	$(PY) fixed_income_curve_algorithm.py

# 生成 跨品种套利图
crossasset:
	$(PY) cross_asset_arbitrage_algorithm.py

# 生成 资产负债管理图
alm:
	$(PY) asset_liability_management_algorithm.py

# 生成 高频交易图
hft:
	$(PY) high_frequency_trading_algorithm.py

# 生成 机器学习预测图
mlpred:
	$(PY) ml_prediction_algorithm.py

# 清理输出文件
clean:
	rm -f \
	      portfolio_optimization_algorithm.png portfolio_optimization_algorithm.pdf \
	      option_pricing_algorithm.png option_pricing_algorithm.pdf \
	      quant_trading_algorithm.png quant_trading_algorithm.pdf \
	      risk_parity_algorithm.png risk_parity_algorithm.pdf \
	      statistical_arbitrage_algorithm.png statistical_arbitrage_algorithm.pdf \
	      volatility_modeling_algorithm.png volatility_modeling_algorithm.pdf \
	      backtesting_framework_algorithm.png backtesting_framework_algorithm.pdf \
	      execution_algorithm.png execution_algorithm.pdf \
	      market_making_algorithm.png market_making_algorithm.pdf \
	      risk_factor_model_algorithm.png risk_factor_model_algorithm.pdf \
	      performance_attribution_algorithm.png performance_attribution_algorithm.pdf \
	      fixed_income_curve_algorithm.png fixed_income_curve_algorithm.pdf \
	      cross_asset_arbitrage_algorithm.png cross_asset_arbitrage_algorithm.pdf \
	      asset_liability_management_algorithm.png asset_liability_management_algorithm.pdf \
	      high_frequency_trading_algorithm.png high_frequency_trading_algorithm.pdf \
	      ml_prediction_algorithm.png ml_prediction_algorithm.pdf
