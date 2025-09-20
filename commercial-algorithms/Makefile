PY=python3

.PHONY: all recommendation pricing inventory risk customer marketing supply fraud demand churn credit sentiment anomaly abtest clean

all: recommendation pricing inventory risk customer marketing supply fraud demand churn credit sentiment anomaly abtest

# 生成 推荐系统算法图
recommendation:
	$(PY) recommendation_system_algorithm.py

# 生成 定价算法图
pricing:
	$(PY) pricing_algorithm.py

# 生成 库存管理算法图
inventory:
	$(PY) inventory_management_algorithm.py

# 生成 风险评估算法图
risk:
	$(PY) risk_assessment_algorithm.py

# 生成 客户细分算法图
customer:
	$(PY) customer_segmentation_algorithm.py

# 生成 营销优化算法图
marketing:
	$(PY) marketing_optimization_algorithm.py

# 生成 供应链优化算法图
supply:
	$(PY) supply_chain_optimization_algorithm.py

# 生成 欺诈检测算法图
fraud:
	$(PY) fraud_detection_algorithm.py

# 生成 需求预测算法图
demand:
	$(PY) demand_forecasting_algorithm.py

# 生成 客户流失预测算法图
churn:
	$(PY) churn_prediction_algorithm.py

# 生成 信用评分算法图
credit:
	$(PY) credit_scoring_algorithm.py

# 生成 情感分析算法图
sentiment:
	$(PY) sentiment_analysis_algorithm.py

# 生成 异常检测算法图
anomaly:
	$(PY) anomaly_detection_algorithm.py

# 生成 A/B测试算法图
abtest:
	$(PY) a_b_testing_algorithm.py

# 清理输出文件
clean:
	rm -f \
	      recommendation_system_algorithm.png recommendation_system_algorithm.pdf \
	      pricing_algorithm.png pricing_algorithm.pdf \
	      inventory_management_algorithm.png inventory_management_algorithm.pdf \
	      risk_assessment_algorithm.png risk_assessment_algorithm.pdf \
	      customer_segmentation_algorithm.png customer_segmentation_algorithm.pdf \
	      marketing_optimization_algorithm.png marketing_optimization_algorithm.pdf \
	      supply_chain_optimization_algorithm.png supply_chain_optimization_algorithm.pdf \
	      fraud_detection_algorithm.png fraud_detection_algorithm.pdf \
	      demand_forecasting_algorithm.png demand_forecasting_algorithm.pdf \
	      churn_prediction_algorithm.png churn_prediction_algorithm.pdf \
	      credit_scoring_algorithm.png credit_scoring_algorithm.pdf \
	      sentiment_analysis_algorithm.png sentiment_analysis_algorithm.pdf \
	      anomaly_detection_algorithm.png anomaly_detection_algorithm.pdf \
	      a_b_testing_algorithm.png a_b_testing_algorithm.pdf
