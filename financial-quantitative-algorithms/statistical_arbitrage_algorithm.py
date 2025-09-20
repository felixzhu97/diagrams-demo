from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_statistical_arbitrage_algorithm(filename: str, outformat: str) -> None:
    with Diagram("统计套利（配对/协整/多资产）算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据层"):
            prices = Server("价格时间序列")
            fundamentals = Server("基本面")
            sector_map = Server("行业/板块映射")
            feature_store = Server("特征库")

        with Cluster("配对与协整检测"):
            distance_metric = Server("距离/相关/皮尔逊")
            cointegration = Server("协整检验 Engle-Granger/Johansen")
            half_life = Server("半衰期估计")

        with Cluster("信号构建"):
            zscore = Server("Z-Score")
            spread = Server("价差构建")
            regime = Server("状态切换/HMM")
            risk_model = Server("风险模型")

        with Cluster("组合与执行"):
            position = Server("头寸与杠杆")
            tc_model = Server("交易成本")
            execution_algo = Server("执行算法")
            monitoring = Server("监控与风控")

        with Cluster("评估与回测"):
            backtest = Server("回测引擎")
            performance = Server("绩效指标")
            attribution = Server("归因分析")

        prices >> Edge(label="对齐/去极值") >> feature_store
        fundamentals >> Edge(label="行业中性/分层") >> sector_map
        feature_store >> Edge(label="相似度") >> distance_metric
        distance_metric >> Edge(label="候选对") >> cointegration
        cointegration >> Edge(label="筛选") >> spread
        spread >> Edge(label="标准化") >> zscore
        zscore >> Edge(label="入场/出场/止损") >> position
        regime >> Edge(label="过滤/加权") >> position
        risk_model >> Edge(label="约束") >> position
        position >> Edge(label="下单") >> execution_algo
        execution_algo >> Edge(label="成本") >> tc_model
        execution_algo >> Edge(label="监控") >> monitoring
        backtest >> Edge(label="评估") >> performance
        performance >> Edge(label="归因") >> attribution
        attribution >> Edge(label="优化") >> position


if __name__ == "__main__":
    create_statistical_arbitrage_algorithm(filename="statistical_arbitrage_algorithm", outformat="png")
    create_statistical_arbitrage_algorithm(filename="statistical_arbitrage_algorithm", outformat="pdf")


