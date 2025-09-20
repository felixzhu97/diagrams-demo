from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_risk_factor_model_algorithm(filename: str, outformat: str) -> None:
    with Diagram("风险因子模型（Barra/自建）架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据源层"):
            price_data = Server("价格数据")
            fundamental_data = Server("基本面数据")
            macro_data = Server("宏观经济数据")
            alternative_data = Server("替代数据")
            
        with Cluster("因子构建"):
            style_factors = Server("风格因子")
            industry_factors = Server("行业因子")
            country_factors = Server("国家因子")
            currency_factors = Server("货币因子")
            
        with Cluster("因子处理"):
            factor_cleaning = Server("因子清洗")
            factor_standardization = Server("因子标准化")
            factor_orthogonalization = Server("因子正交化")
            factor_selection = Server("因子选择")
            
        with Cluster("风险模型构建"):
            factor_exposures = Server("因子暴露度")
            factor_covariance = Server("因子协方差")
            specific_risk = Server("特异风险")
            total_risk = Server("总风险模型")
            
        with Cluster("模型验证"):
            backtesting = Server("回测验证")
            factor_stability = Server("因子稳定性")
            risk_attribution = Server("风险归因")
            model_diagnostics = Server("模型诊断")
            
        with Cluster("应用层"):
            portfolio_risk = Server("组合风险")
            risk_budgeting = Server("风险预算")
            risk_limits = Server("风险限额")
            stress_testing = Server("压力测试")
            
        with Cluster("监控与更新"):
            model_monitoring = Server("模型监控")
            factor_rotation = Server("因子轮换")
            model_rebalancing = Server("模型再平衡")
            performance_tracking = Server("绩效跟踪")
            
        # 连接关系
        price_data >> Edge(label="计算收益") >> style_factors
        fundamental_data >> Edge(label="财务指标") >> style_factors
        macro_data >> Edge(label="宏观指标") >> country_factors
        alternative_data >> Edge(label="另类数据") >> style_factors
        
        style_factors >> Edge(label="处理") >> factor_cleaning
        industry_factors >> Edge(label="处理") >> factor_cleaning
        country_factors >> Edge(label="处理") >> factor_cleaning
        currency_factors >> Edge(label="处理") >> factor_cleaning
        
        factor_cleaning >> Edge(label="标准化") >> factor_standardization
        factor_standardization >> Edge(label="正交化") >> factor_orthogonalization
        factor_orthogonalization >> Edge(label="选择") >> factor_selection
        
        factor_selection >> Edge(label="暴露度计算") >> factor_exposures
        factor_exposures >> Edge(label="协方差估计") >> factor_covariance
        factor_covariance >> Edge(label="特异风险") >> specific_risk
        specific_risk >> Edge(label="总风险") >> total_risk
        
        total_risk >> Edge(label="回测") >> backtesting
        backtesting >> Edge(label="稳定性检验") >> factor_stability
        factor_stability >> Edge(label="风险分解") >> risk_attribution
        risk_attribution >> Edge(label="诊断") >> model_diagnostics
        
        total_risk >> Edge(label="组合风险") >> portfolio_risk
        portfolio_risk >> Edge(label="风险分配") >> risk_budgeting
        risk_budgeting >> Edge(label="限额设置") >> risk_limits
        risk_limits >> Edge(label="压力场景") >> stress_testing
        
        model_diagnostics >> Edge(label="监控") >> model_monitoring
        model_monitoring >> Edge(label="因子调整") >> factor_rotation
        factor_rotation >> Edge(label="模型更新") >> model_rebalancing
        model_rebalancing >> Edge(label="绩效评估") >> performance_tracking
        
        # 反馈循环
        performance_tracking >> Edge(label="反馈") >> factor_selection
        model_diagnostics >> Edge(label="反馈") >> factor_cleaning


if __name__ == "__main__":
    create_risk_factor_model_algorithm(filename="risk_factor_model_algorithm", outformat="png")
    create_risk_factor_model_algorithm(filename="risk_factor_model_algorithm", outformat="pdf")
