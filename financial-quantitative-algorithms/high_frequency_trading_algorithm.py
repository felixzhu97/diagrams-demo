from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_high_frequency_trading_algorithm(filename: str, outformat: str) -> None:
    with Diagram("高频交易与超低延迟系统架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("市场数据层"):
            market_data_feed = Server("市场数据源")
            order_book_data = Server("订单簿数据")
            trade_data = Server("成交数据")
            news_feed = Server("新闻数据流")
            
        with Cluster("数据处理层"):
            data_normalization = Server("数据标准化")
            tick_processing = Server("Tick处理")
            order_book_reconstruction = Server("订单簿重构")
            latency_optimization = Server("延迟优化")
            
        with Cluster("信号生成"):
            momentum_signals = Server("动量信号")
            mean_reversion = Server("均值回归")
            order_flow_imbalance = Server("订单流不平衡")
            microstructure_alpha = Server("微结构Alpha")
            
        with Cluster("策略引擎"):
            strategy_framework = Server("策略框架")
            signal_combination = Server("信号组合")
            position_management = Server("仓位管理")
            risk_controls = Server("风险控制")
            
        with Cluster("执行系统"):
            order_generation = Server("订单生成")
            smart_routing = Server("智能路由")
            execution_optimization = Server("执行优化")
            fill_detection = Server("成交检测")
            
        with Cluster("基础设施"):
            co_location = Server("托管服务")
            low_latency_network = Server("低延迟网络")
            fpga_acceleration = Server("FPGA加速")
            memory_optimization = Server("内存优化")
            
        with Cluster("监控与风控"):
            real_time_monitoring = Server("实时监控")
            position_limits = Server("仓位限制")
            pnl_tracking = Server("PnL跟踪")
            risk_metrics = Server("风险指标")
            
        with Cluster("合规与报告"):
            trade_reporting = Server("交易报告")
            regulatory_compliance = Server("监管合规")
            audit_trail = Server("审计轨迹")
            performance_analysis = Server("绩效分析")
            
        # 连接关系
        market_data_feed >> Edge(label="原始数据") >> data_normalization
        order_book_data >> Edge(label="深度数据") >> data_normalization
        trade_data >> Edge(label="成交数据") >> data_normalization
        news_feed >> Edge(label="新闻流") >> data_normalization
        
        data_normalization >> Edge(label="标准化") >> tick_processing
        tick_processing >> Edge(label="Tick处理") >> order_book_reconstruction
        order_book_reconstruction >> Edge(label="订单簿") >> latency_optimization
        
        latency_optimization >> Edge(label="低延迟数据") >> momentum_signals
        latency_optimization >> Edge(label="低延迟数据") >> mean_reversion
        order_book_reconstruction >> Edge(label="订单流") >> order_flow_imbalance
        order_book_reconstruction >> Edge(label="微结构") >> microstructure_alpha
        
        momentum_signals >> Edge(label="信号输入") >> strategy_framework
        mean_reversion >> Edge(label="信号输入") >> strategy_framework
        order_flow_imbalance >> Edge(label="信号输入") >> strategy_framework
        microstructure_alpha >> Edge(label="信号输入") >> strategy_framework
        
        strategy_framework >> Edge(label="策略逻辑") >> signal_combination
        signal_combination >> Edge(label="信号组合") >> position_management
        position_management >> Edge(label="仓位控制") >> risk_controls
        
        risk_controls >> Edge(label="风险检查") >> order_generation
        order_generation >> Edge(label="订单生成") >> smart_routing
        smart_routing >> Edge(label="路由优化") >> execution_optimization
        execution_optimization >> Edge(label="执行") >> fill_detection
        
        co_location >> Edge(label="托管环境") >> low_latency_network
        low_latency_network >> Edge(label="网络优化") >> fpga_acceleration
        fpga_acceleration >> Edge(label="硬件加速") >> memory_optimization
        memory_optimization >> Edge(label="内存优化") >> latency_optimization
        
        fill_detection >> Edge(label="成交回报") >> real_time_monitoring
        real_time_monitoring >> Edge(label="实时监控") >> position_limits
        position_limits >> Edge(label="仓位监控") >> pnl_tracking
        pnl_tracking >> Edge(label="损益跟踪") >> risk_metrics
        
        risk_metrics >> Edge(label="风险报告") >> trade_reporting
        trade_reporting >> Edge(label="交易报告") >> regulatory_compliance
        regulatory_compliance >> Edge(label="合规检查") >> audit_trail
        audit_trail >> Edge(label="审计数据") >> performance_analysis
        
        # 反馈循环
        performance_analysis >> Edge(label="反馈") >> strategy_framework
        risk_metrics >> Edge(label="反馈") >> risk_controls


if __name__ == "__main__":
    create_high_frequency_trading_algorithm(filename="high_frequency_trading_algorithm", outformat="png")
    create_high_frequency_trading_algorithm(filename="high_frequency_trading_algorithm", outformat="pdf")
