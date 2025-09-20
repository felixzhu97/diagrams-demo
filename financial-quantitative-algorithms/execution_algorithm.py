from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_execution_algorithm(filename: str, outformat: str) -> None:
    with Diagram("执行算法（交易成本最小化）架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("输入与约束"):
            parent_order = Server("母单/目标数量")
            urgency = Server("紧急度/时间约束")
            participation = Server("参与率上限")
            risk_limits = Server("风险与限制")

        with Cluster("市场微结构"):
            order_book = Server("订单簿深度")
            volume_profile = Server("成交量曲线 VWAP")
            short_term_alpha = Server("短期信号")

        with Cluster("算法族"):
            vwap = Server("VWAP/POV")
            twap = Server("TWAP")
            is_algo = Server("Implementation Shortfall")
            smart_router = Server("智能路由")

        with Cluster("交易成本模型"):
            impact = Server("冲击成本")
            spread = Server("点差成本")
            timing = Server("时间择时")

        with Cluster("执行与反馈"):
            child_orders = Server("子单生成")
            venues = Server("多场所路由")
            fills = Server("成交回报")
            analytics = Server("执行分析/TCA")

        parent_order >> Edge(label="紧急度/参与率") >> vwap
        parent_order >> Edge(label="时间约束") >> twap
        parent_order >> Edge(label="成本-风险权衡") >> is_algo
        urgency >> Edge(label="参数化") >> is_algo
        participation >> Edge(label="阈值") >> vwap
        risk_limits >> Edge(label="约束") >> smart_router

        order_book >> Edge(label="微结构") >> smart_router
        volume_profile >> Edge(label="基准/曲线") >> vwap
        short_term_alpha >> Edge(label="择时") >> is_algo

        vwap >> Edge(label="子单") >> child_orders
        twap >> Edge(label="子单") >> child_orders
        is_algo >> Edge(label="子单") >> child_orders
        child_orders >> Edge(label="路由") >> smart_router

        smart_router >> Edge(label="分配") >> venues
        venues >> Edge(label="成交") >> fills

        fills >> Edge(label="估计") >> impact
        fills >> Edge(label="估计") >> spread
        fills >> Edge(label="估计") >> timing
        impact >> Edge(label="反馈") >> is_algo
        spread >> Edge(label="反馈") >> vwap
        timing >> Edge(label="反馈") >> twap
        fills >> Edge(label="评估") >> analytics


if __name__ == "__main__":
    create_execution_algorithm(filename="execution_algorithm", outformat="png")
    create_execution_algorithm(filename="execution_algorithm", outformat="pdf")


