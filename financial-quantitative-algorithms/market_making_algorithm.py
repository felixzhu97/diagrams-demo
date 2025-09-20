from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_market_making_algorithm(filename: str, outformat: str) -> None:
    with Diagram("做市与流动性提供算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("市场数据与状态"):
            order_book = Server("订单簿深度")
            trade_flow = Server("成交流")
            volatility = Server("波动率估计")
            inventory = Server("库存状态")
            
        with Cluster("定价模型"):
            fair_value = Server("公允价值模型")
            spread_model = Server("点差模型")
            skew_model = Server("偏斜模型")
            inventory_adj = Server("库存调整")
            
        with Cluster("风险控制"):
            position_limits = Server("仓位限制")
            var_limits = Server("VaR限制")
            drawdown_limits = Server("回撤限制")
            exposure_limits = Server("敞口限制")
            
        with Cluster("订单管理"):
            quote_generator = Server("报价生成器")
            order_router = Server("订单路由")
            fill_monitor = Server("成交监控")
            hedge_engine = Server("对冲引擎")
            
        with Cluster("执行与对冲"):
            primary_venue = Server("主交易场所")
            alternative_venues = Server("备选场所")
            hedge_orders = Server("对冲订单")
            risk_reduction = Server("风险削减")
            
        with Cluster("监控与分析"):
            pnl_tracker = Server("PnL跟踪")
            performance_metrics = Server("绩效指标")
            risk_metrics = Server("风险指标")
            reporting = Server("报告系统")
            
        # 连接关系
        order_book >> Edge(label="深度分析") >> fair_value
        trade_flow >> Edge(label="成交分析") >> fair_value
        volatility >> Edge(label="波动率输入") >> spread_model
        inventory >> Edge(label="库存状态") >> inventory_adj
        
        fair_value >> Edge(label="基准价格") >> quote_generator
        spread_model >> Edge(label="点差计算") >> quote_generator
        skew_model >> Edge(label="偏斜调整") >> quote_generator
        inventory_adj >> Edge(label="库存调整") >> quote_generator
        
        position_limits >> Edge(label="仓位约束") >> quote_generator
        var_limits >> Edge(label="风险约束") >> quote_generator
        drawdown_limits >> Edge(label="回撤约束") >> quote_generator
        exposure_limits >> Edge(label="敞口约束") >> quote_generator
        
        quote_generator >> Edge(label="生成报价") >> order_router
        order_router >> Edge(label="路由订单") >> primary_venue
        order_router >> Edge(label="备选路由") >> alternative_venues
        
        primary_venue >> Edge(label="成交回报") >> fill_monitor
        alternative_venues >> Edge(label="成交回报") >> fill_monitor
        fill_monitor >> Edge(label="库存变化") >> inventory
        
        inventory >> Edge(label="风险暴露") >> hedge_engine
        hedge_engine >> Edge(label="生成对冲") >> hedge_orders
        hedge_orders >> Edge(label="执行对冲") >> risk_reduction
        
        fill_monitor >> Edge(label="成交数据") >> pnl_tracker
        pnl_tracker >> Edge(label="损益计算") >> performance_metrics
        inventory >> Edge(label="风险数据") >> risk_metrics
        
        performance_metrics >> Edge(label="绩效报告") >> reporting
        risk_metrics >> Edge(label="风险报告") >> reporting
        
        # 反馈循环
        pnl_tracker >> Edge(label="损益反馈") >> spread_model
        risk_metrics >> Edge(label="风险反馈") >> position_limits


if __name__ == "__main__":
    create_market_making_algorithm(filename="market_making_algorithm", outformat="png")
    create_market_making_algorithm(filename="market_making_algorithm", outformat="pdf")
