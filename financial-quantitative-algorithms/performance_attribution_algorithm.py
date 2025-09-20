from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_performance_attribution_algorithm(filename: str, outformat: str) -> None:
    with Diagram("收益归因分析（Brinson/Fama-French）架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据输入层"):
            portfolio_returns = Server("组合收益")
            benchmark_returns = Server("基准收益")
            asset_returns = Server("资产收益")
            weights_data = Server("权重数据")
            
        with Cluster("Brinson归因模型"):
            asset_allocation = Server("资产配置效应")
            security_selection = Server("证券选择效应")
            interaction_effect = Server("交互效应")
            total_attribution = Server("总归因")
            
        with Cluster("Fama-French因子模型"):
            market_factor = Server("市场因子")
            size_factor = Server("规模因子")
            value_factor = Server("价值因子")
            momentum_factor = Server("动量因子")
            quality_factor = Server("质量因子")
            
        with Cluster("多因子归因"):
            factor_exposures = Server("因子暴露度")
            factor_returns = Server("因子收益")
            factor_attribution = Server("因子归因")
            alpha_attribution = Server("Alpha归因")
            
        with Cluster("风险调整归因"):
            risk_adjusted_returns = Server("风险调整收益")
            information_ratio = Server("信息比率")
            sharpe_ratio = Server("夏普比率")
            treynor_ratio = Server("特雷诺比率")
            
        with Cluster("时间序列归因"):
            rolling_attribution = Server("滚动归因")
            cumulative_attribution = Server("累积归因")
            attribution_volatility = Server("归因波动率")
            attribution_consistency = Server("归因一致性")
            
        with Cluster("报告与可视化"):
            attribution_report = Server("归因报告")
            performance_dashboard = Server("绩效仪表板")
            risk_metrics = Server("风险指标")
            benchmark_analysis = Server("基准分析")
            
        # 连接关系
        portfolio_returns >> Edge(label="输入") >> asset_allocation
        benchmark_returns >> Edge(label="基准") >> asset_allocation
        weights_data >> Edge(label="权重") >> asset_allocation
        asset_returns >> Edge(label="资产收益") >> security_selection
        
        asset_allocation >> Edge(label="配置效应") >> total_attribution
        security_selection >> Edge(label="选择效应") >> total_attribution
        interaction_effect >> Edge(label="交互效应") >> total_attribution
        
        portfolio_returns >> Edge(label="回归分析") >> market_factor
        portfolio_returns >> Edge(label="回归分析") >> size_factor
        portfolio_returns >> Edge(label="回归分析") >> value_factor
        portfolio_returns >> Edge(label="回归分析") >> momentum_factor
        portfolio_returns >> Edge(label="回归分析") >> quality_factor
        
        market_factor >> Edge(label="因子暴露") >> factor_exposures
        size_factor >> Edge(label="因子暴露") >> factor_exposures
        value_factor >> Edge(label="因子暴露") >> factor_exposures
        momentum_factor >> Edge(label="因子暴露") >> factor_exposures
        quality_factor >> Edge(label="因子暴露") >> factor_exposures
        
        factor_exposures >> Edge(label="因子收益") >> factor_returns
        factor_returns >> Edge(label="归因计算") >> factor_attribution
        factor_attribution >> Edge(label="Alpha分解") >> alpha_attribution
        
        total_attribution >> Edge(label="风险调整") >> risk_adjusted_returns
        risk_adjusted_returns >> Edge(label="信息比率") >> information_ratio
        risk_adjusted_returns >> Edge(label="夏普比率") >> sharpe_ratio
        risk_adjusted_returns >> Edge(label="特雷诺比率") >> treynor_ratio
        
        factor_attribution >> Edge(label="时间序列") >> rolling_attribution
        rolling_attribution >> Edge(label="累积计算") >> cumulative_attribution
        cumulative_attribution >> Edge(label="波动率计算") >> attribution_volatility
        attribution_volatility >> Edge(label="一致性分析") >> attribution_consistency
        
        total_attribution >> Edge(label="生成报告") >> attribution_report
        factor_attribution >> Edge(label="仪表板") >> performance_dashboard
        risk_adjusted_returns >> Edge(label="风险指标") >> risk_metrics
        benchmark_returns >> Edge(label="基准分析") >> benchmark_analysis
        
        # 反馈循环
        attribution_consistency >> Edge(label="反馈") >> factor_exposures
        risk_metrics >> Edge(label="反馈") >> risk_adjusted_returns


if __name__ == "__main__":
    create_performance_attribution_algorithm(filename="performance_attribution_algorithm", outformat="png")
    create_performance_attribution_algorithm(filename="performance_attribution_algorithm", outformat="pdf")
