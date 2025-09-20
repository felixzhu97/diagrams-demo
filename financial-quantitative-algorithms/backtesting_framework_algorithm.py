from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_backtesting_framework_algorithm(filename: str, outformat: str) -> None:
    with Diagram("回测与交易仿真框架架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据与预处理"):
            raw_data = Server("原始行情/交易")
            corporate_actions = Server("除权除息")
            data_cleaning = Server("清洗/对齐/复权")
            event_calendar = Server("事件/交易日历")

        with Cluster("策略模块"):
            signal = Server("信号生成")
            risk_model = Server("风险模型")
            portfolio = Server("组合优化")
            sizing = Server("仓位与杠杆")

        with Cluster("撮合与成本"):
            broker_sim = Server("撮合引擎")
            slippage = Server("滑点模型")
            tc_model = Server("交易成本模型")
            borrow_fee = Server("融券/融资费用")

        with Cluster("仿真与执行"):
            order_gen = Server("订单生成")
            execution = Server("执行/路由")
            fills = Server("成交回报")

        with Cluster("评估与分析"):
            metrics = Server("绩效指标")
            attribution = Server("归因分析")
            risk_report = Server("风险报告/VaR/ES")
            tear_sheet = Server("回测报告")

        raw_data >> Edge(label="预处理") >> data_cleaning
        corporate_actions >> Edge(label="复权") >> data_cleaning
        event_calendar >> Edge(label="交易日/停牌") >> data_cleaning

        data_cleaning >> Edge(label="特征") >> signal
        signal >> Edge(label="风险约束") >> risk_model
        risk_model >> Edge(label="优化") >> portfolio
        portfolio >> Edge(label=" sizing") >> sizing

        sizing >> Edge(label="生成订单") >> order_gen
        order_gen >> Edge(label="撮合") >> broker_sim
        broker_sim >> Edge(label="滑点/成本") >> slippage
        slippage >> Edge(label="成本") >> tc_model
        tc_model >> Edge(label="执行") >> execution
        execution >> Edge(label="成交") >> fills

        fills >> Edge(label="计算") >> metrics
        metrics >> Edge(label="归因") >> attribution
        metrics >> Edge(label="风险") >> risk_report
        attribution >> Edge(label="可视化") >> tear_sheet
        risk_report >> Edge(label="汇总") >> tear_sheet


if __name__ == "__main__":
    create_backtesting_framework_algorithm(filename="backtesting_framework_algorithm", outformat="png")
    create_backtesting_framework_algorithm(filename="backtesting_framework_algorithm", outformat="pdf")


