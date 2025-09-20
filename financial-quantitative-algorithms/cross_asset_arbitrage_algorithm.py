from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_cross_asset_arbitrage_algorithm(filename: str, outformat: str) -> None:
    with Diagram("跨品种套利与相对价值交易架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("多资产数据层"):
            equity_data = Server("股票数据")
            bond_data = Server("债券数据")
            fx_data = Server("外汇数据")
            commodity_data = Server("商品数据")
            crypto_data = Server("加密货币数据")
            
        with Cluster("相关性分析"):
            correlation_matrix = Server("相关性矩阵")
            cointegration_test = Server("协整检验")
            lead_lag_analysis = Server("领先滞后分析")
            regime_detection = Server("状态检测")
            
        with Cluster("价差构建"):
            spread_calculation = Server("价差计算")
            ratio_analysis = Server("比率分析")
            basis_trading = Server("基差交易")
            calendar_spread = Server("日历价差")
            
        with Cluster("套利信号"):
            mean_reversion = Server("均值回归信号")
            momentum_signal = Server("动量信号")
            volatility_signal = Server("波动率信号")
            liquidity_signal = Server("流动性信号")
            
        with Cluster("风险管理"):
            position_sizing = Server("仓位管理")
            correlation_risk = Server("相关性风险")
            liquidity_risk = Server("流动性风险")
            basis_risk = Server("基差风险")
            
        with Cluster("执行系统"):
            multi_venue_routing = Server("多场所路由")
            smart_order_routing = Server("智能路由")
            execution_optimization = Server("执行优化")
            fill_monitoring = Server("成交监控")
            
        with Cluster("监控与分析"):
            pnl_attribution = Server("损益归因")
            risk_metrics = Server("风险指标")
            performance_analysis = Server("绩效分析")
            stress_testing = Server("压力测试")
            
        # 连接关系
        equity_data >> Edge(label="价格数据") >> correlation_matrix
        bond_data >> Edge(label="收益率") >> correlation_matrix
        fx_data >> Edge(label="汇率") >> correlation_matrix
        commodity_data >> Edge(label="价格") >> correlation_matrix
        crypto_data >> Edge(label="价格") >> correlation_matrix
        
        correlation_matrix >> Edge(label="相关性") >> cointegration_test
        cointegration_test >> Edge(label="长期关系") >> lead_lag_analysis
        lead_lag_analysis >> Edge(label="时序关系") >> regime_detection
        
        equity_data >> Edge(label="价差构建") >> spread_calculation
        bond_data >> Edge(label="价差构建") >> spread_calculation
        fx_data >> Edge(label="价差构建") >> spread_calculation
        commodity_data >> Edge(label="价差构建") >> spread_calculation
        
        spread_calculation >> Edge(label="价差分析") >> ratio_analysis
        ratio_analysis >> Edge(label="基差交易") >> basis_trading
        basis_trading >> Edge(label="时间价差") >> calendar_spread
        
        spread_calculation >> Edge(label="均值回归") >> mean_reversion
        lead_lag_analysis >> Edge(label="动量信号") >> momentum_signal
        regime_detection >> Edge(label="波动率") >> volatility_signal
        correlation_matrix >> Edge(label="流动性") >> liquidity_signal
        
        mean_reversion >> Edge(label="信号综合") >> position_sizing
        momentum_signal >> Edge(label="信号综合") >> position_sizing
        volatility_signal >> Edge(label="信号综合") >> position_sizing
        liquidity_signal >> Edge(label="信号综合") >> position_sizing
        
        position_sizing >> Edge(label="风险控制") >> correlation_risk
        correlation_risk >> Edge(label="流动性约束") >> liquidity_risk
        liquidity_risk >> Edge(label="基差风险") >> basis_risk
        
        position_sizing >> Edge(label="订单生成") >> multi_venue_routing
        multi_venue_routing >> Edge(label="智能路由") >> smart_order_routing
        smart_order_routing >> Edge(label="执行优化") >> execution_optimization
        execution_optimization >> Edge(label="成交监控") >> fill_monitoring
        
        fill_monitoring >> Edge(label="成交数据") >> pnl_attribution
        pnl_attribution >> Edge(label="风险分解") >> risk_metrics
        risk_metrics >> Edge(label="绩效评估") >> performance_analysis
        performance_analysis >> Edge(label="压力场景") >> stress_testing
        
        # 反馈循环
        stress_testing >> Edge(label="反馈") >> position_sizing
        performance_analysis >> Edge(label="反馈") >> mean_reversion


if __name__ == "__main__":
    create_cross_asset_arbitrage_algorithm(filename="cross_asset_arbitrage_algorithm", outformat="png")
    create_cross_asset_arbitrage_algorithm(filename="cross_asset_arbitrage_algorithm", outformat="pdf")
