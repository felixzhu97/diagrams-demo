from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_volatility_modeling_algorithm(filename: str, outformat: str) -> None:
    with Diagram("波动率建模与预测架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据层"):
            returns = Server("收益率序列")
            realized_vol = Server("实现波动率")
            iv_surface = Server("隐含波动率曲面")

        with Cluster("条件异方差模型"):
            arch = Server("ARCH/GARCH")
            egarch = Server("EGARCH/GJR")
            hogarch = Server("高阶/多变量 GARCH")

        with Cluster("随机/本地波动"):
            heston = Server("Heston 随机波动")
            local_vol = Server("Dupire 本地波动")

        with Cluster("高频与实现波动"):
            rv = Server("实现波动率 RV")
            bipower = Server("双幂变差")
            jump_filter = Server("跳跃过滤")

        with Cluster("机器学习与深度"):
            rnn = Server("RNN/LSTM/Transformer")
            features = Server("宏观/因子/新闻")

        with Cluster("校准与评估"):
            calib = Server("参数估计/极大似然")
            forecast = Server("波动率预测")
            backtest = Server("回测/损失函数")

        with Cluster("应用"):
            var = Server("VaR/风控")
            pricing = Server("定价输入 σ")
            hedging = Server("对冲尺寸")

        returns >> Edge(label="拟合") >> arch
        returns >> Edge(label="拟合") >> egarch
        returns >> Edge(label="拟合") >> hogarch
        realized_vol >> Edge(label="校准") >> rv
        iv_surface >> Edge(label="约束/锚定") >> local_vol

        arch >> Edge(label="预测") >> forecast
        egarch >> Edge(label="预测") >> forecast
        hogarch >> Edge(label="预测") >> forecast
        heston >> Edge(label="路径") >> forecast
        local_vol >> Edge(label="曲面") >> forecast
        rnn >> Edge(label="序列预测") >> forecast
        features >> Edge(label="外生变量") >> rnn
        rv >> Edge(label="特征") >> rnn

        calib >> Edge(label="估计") >> arch
        calib >> Edge(label="估计") >> egarch
        calib >> Edge(label="估计") >> hogarch

        forecast >> Edge(label="风险输入") >> var
        forecast >> Edge(label="σ 输入") >> pricing
        forecast >> Edge(label="动态调整") >> hedging


if __name__ == "__main__":
    create_volatility_modeling_algorithm(filename="volatility_modeling_algorithm", outformat="png")
    create_volatility_modeling_algorithm(filename="volatility_modeling_algorithm", outformat="pdf")


