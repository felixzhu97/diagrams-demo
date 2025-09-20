from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_asset_liability_management_algorithm(filename: str, outformat: str) -> None:
    with Diagram("资产负债管理（ALM）与流动性管理架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("资产负债数据层"):
            asset_data = Server("资产数据")
            liability_data = Server("负债数据")
            cash_flow_data = Server("现金流数据")
            regulatory_data = Server("监管数据")
            
        with Cluster("现金流建模"):
            cash_flow_projection = Server("现金流预测")
            duration_analysis = Server("久期分析")
            convexity_analysis = Server("凸性分析")
            prepayment_model = Server("提前还款模型")
            
        with Cluster("利率风险模型"):
            interest_rate_model = Server("利率模型")
            yield_curve_model = Server("收益率曲线模型")
            basis_risk_model = Server("基差风险模型")
            optionality_model = Server("期权性风险模型")
            
        with Cluster("流动性管理"):
            liquidity_forecast = Server("流动性预测")
            liquidity_buffer = Server("流动性缓冲")
            funding_plan = Server("融资计划")
            contingency_funding = Server("应急融资")
            
        with Cluster("ALM优化"):
            asset_allocation = Server("资产配置")
            liability_hedging = Server("负债对冲")
            duration_matching = Server("久期匹配")
            immunization = Server("免疫策略")
            
        with Cluster("风险度量"):
            var_calculation = Server("VaR计算")
            stress_testing = Server("压力测试")
            scenario_analysis = Server("情景分析")
            sensitivity_analysis = Server("敏感性分析")
            
        with Cluster("监管合规"):
            regulatory_reporting = Server("监管报告")
            capital_adequacy = Server("资本充足率")
            liquidity_ratio = Server("流动性比率")
            leverage_ratio = Server("杠杆比率")
            
        with Cluster("监控与报告"):
            performance_monitoring = Server("绩效监控")
            risk_dashboard = Server("风险仪表板")
            management_reporting = Server("管理报告")
            regulatory_submission = Server("监管报送")
            
        # 连接关系
        asset_data >> Edge(label="资产信息") >> cash_flow_projection
        liability_data >> Edge(label="负债信息") >> cash_flow_projection
        cash_flow_data >> Edge(label="历史现金流") >> cash_flow_projection
        regulatory_data >> Edge(label="监管要求") >> cash_flow_projection
        
        cash_flow_projection >> Edge(label="现金流预测") >> duration_analysis
        duration_analysis >> Edge(label="久期计算") >> convexity_analysis
        convexity_analysis >> Edge(label="凸性计算") >> prepayment_model
        
        interest_rate_model >> Edge(label="利率预测") >> yield_curve_model
        yield_curve_model >> Edge(label="曲线构建") >> basis_risk_model
        basis_risk_model >> Edge(label="基差风险") >> optionality_model
        
        cash_flow_projection >> Edge(label="现金流需求") >> liquidity_forecast
        liquidity_forecast >> Edge(label="流动性需求") >> liquidity_buffer
        liquidity_buffer >> Edge(label="缓冲管理") >> funding_plan
        funding_plan >> Edge(label="应急准备") >> contingency_funding
        
        asset_data >> Edge(label="资产配置") >> asset_allocation
        liability_data >> Edge(label="负债对冲") >> liability_hedging
        duration_analysis >> Edge(label="久期匹配") >> duration_matching
        duration_matching >> Edge(label="免疫策略") >> immunization
        
        asset_allocation >> Edge(label="风险度量") >> var_calculation
        liability_hedging >> Edge(label="压力测试") >> stress_testing
        immunization >> Edge(label="情景分析") >> scenario_analysis
        optionality_model >> Edge(label="敏感性分析") >> sensitivity_analysis
        
        var_calculation >> Edge(label="风险报告") >> regulatory_reporting
        stress_testing >> Edge(label="资本要求") >> capital_adequacy
        liquidity_forecast >> Edge(label="流动性要求") >> liquidity_ratio
        asset_allocation >> Edge(label="杠杆监控") >> leverage_ratio
        
        regulatory_reporting >> Edge(label="合规监控") >> performance_monitoring
        capital_adequacy >> Edge(label="风险监控") >> risk_dashboard
        liquidity_ratio >> Edge(label="管理报告") >> management_reporting
        leverage_ratio >> Edge(label="监管报送") >> regulatory_submission
        
        # 反馈循环
        performance_monitoring >> Edge(label="反馈") >> asset_allocation
        risk_dashboard >> Edge(label="反馈") >> liability_hedging


if __name__ == "__main__":
    create_asset_liability_management_algorithm(filename="asset_liability_management_algorithm", outformat="png")
    create_asset_liability_management_algorithm(filename="asset_liability_management_algorithm", outformat="pdf")
