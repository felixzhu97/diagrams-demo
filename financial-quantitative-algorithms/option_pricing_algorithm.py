from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_option_pricing_algorithm(filename: str, outformat: str) -> None:
    with Diagram("期权定价与风险管理算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据与输入"):
            with Cluster("市场数据"):
                spot = Server("标的价格 S")
                strike = Server("执行价 K")
                maturity = Server("到期 T")
                rate = Server("无风险利率 r")
                dividend = Server("分红/便利收益 q")
            
            with Cluster("波动率数据"):
                vol = Server("历史波动率 σ")
                surface = Server("隐含波动率曲面")
                term_structure = Server("期限结构")
                smile_skew = Server("微笑/偏斜")

        with Cluster("模型族"):
            with Cluster("基础模型"):
                bs = Server("Black-Scholes-Merton")
                binomial = Server("二叉树/三叉树")
                trinomial = Server("三叉树")
            
            with Cluster("随机波动率模型"):
                heston = Server("Heston 随机波动率")
                sabr = Server("SABR 模型")
                hull_white = Server("Hull-White")
                bergomi = Server("Bergomi 模型")
            
            with Cluster("跳跃模型"):
                jumps = Server("跳扩散 Merton")
                kou_model = Server("Kou 双指数跳跃")
                variance_gamma = Server("方差伽马")
            
            with Cluster("局部波动率"):
                local_vol = Server("本地波动率 Dupire")
                derman_kani = Server("Derman-Kani")
                implied_tree = Server("隐含树")

        with Cluster("数值方法"):
            with Cluster("偏微分方程"):
                pde_explicit = Server("显式有限差分")
                pde_implicit = Server("隐式有限差分")
                crank_nicolson = Server("Crank-Nicolson")
                alternating_direction = Server("交替方向隐式")
            
            with Cluster("积分变换"):
                fft = Server("快速傅里叶变换")
                characteristic_function = Server("特征函数")
                cosine_method = Server("余弦方法")
            
            with Cluster("蒙特卡洛"):
                standard_mc = Server("标准蒙特卡洛")
                quasi_mc = Server("准蒙特卡洛")
                ls_mc = Server("最小二乘蒙特卡洛")
                control_variates = Server("控制变量法")

        with Cluster("希腊字母与风险"):
            with Cluster("一阶希腊字母"):
                delta = Server("Delta")
                vega = Server("Vega")
                rho = Server("Rho")
                theta = Server("Theta")
            
            with Cluster("二阶希腊字母"):
                gamma = Server("Gamma")
                vanna = Server("Vanna")
                volga = Server("Volga")
                charm = Server("Charm")
            
            with Cluster("高阶风险"):
                speed = Server("Speed")
                color = Server("Color")
                ultima = Server("Ultima")

        with Cluster("校准与表面"):
            with Cluster("模型校准"):
                mle_calibration = Server("极大似然估计")
                least_squares = Server("最小二乘法")
                genetic_algorithm = Server("遗传算法")
                particle_swarm = Server("粒子群优化")
            
            with Cluster("曲面处理"):
                spline_interpolation = Server("样条插值")
                kernel_smoothing = Server("核平滑")
                arbitrage_check = Server("无套利检查")
                surface_repair = Server("曲面修复")

        with Cluster("定价与对冲"):
            with Cluster("定价引擎"):
                pricing_engine = Server("定价引擎")
                american_pricing = Server("美式期权定价")
                barrier_pricing = Server("障碍期权定价")
                exotic_pricing = Server("奇异期权定价")
            
            with Cluster("对冲策略"):
                delta_hedging = Server("Delta对冲")
                gamma_hedging = Server("Gamma对冲")
                vega_hedging = Server("Vega对冲")
                portfolio_hedging = Server("组合对冲")
            
            with Cluster("PnL分析"):
                pnl_decomposition = Server("PnL分解")
                attribution_analysis = Server("归因分析")
                hedge_effectiveness = Server("对冲有效性")

        with Cluster("风险与报告"):
            with Cluster("风险度量"):
                var_calculation = Server("VaR计算")
                expected_shortfall = Server("期望损失")
                greeks_risk = Server("希腊字母风险")
                model_risk = Server("模型风险")
            
            with Cluster("压力测试"):
                stress_scenarios = Server("压力情景")
                monte_carlo_stress = Server("蒙特卡洛压力测试")
                historical_simulation = Server("历史模拟")
            
            with Cluster("报告系统"):
                risk_dashboard = Server("风险仪表板")
                regulatory_report = Server("监管报告")
                management_report = Server("管理报告")

        # 数据输入连接
        spot >> Edge(label="标的价格") >> bs
        strike >> Edge(label="执行价格") >> bs
        maturity >> Edge(label="到期时间") >> bs
        rate >> Edge(label="无风险利率") >> bs
        dividend >> Edge(label="分红率") >> bs
        vol >> Edge(label="历史波动率") >> bs
        
        surface >> Edge(label="隐含波动率") >> heston
        term_structure >> Edge(label="期限结构") >> sabr
        smile_skew >> Edge(label="微笑偏斜") >> bergomi
        
        # 模型族连接
        bs >> Edge(label="封闭解") >> pricing_engine
        binomial >> Edge(label="离散化") >> pricing_engine
        trinomial >> Edge(label="三叉树") >> pricing_engine
        
        heston >> Edge(label="随机波动率") >> characteristic_function
        sabr >> Edge(label="SABR模型") >> characteristic_function
        hull_white >> Edge(label="利率模型") >> characteristic_function
        bergomi >> Edge(label="Bergomi模型") >> characteristic_function
        
        jumps >> Edge(label="跳跃扩散") >> standard_mc
        kou_model >> Edge(label="双指数跳跃") >> standard_mc
        variance_gamma >> Edge(label="方差伽马") >> standard_mc
        
        local_vol >> Edge(label="局部波动率") >> pde_implicit
        derman_kani >> Edge(label="Derman-Kani") >> implied_tree
        implied_tree >> Edge(label="隐含树") >> american_pricing
        
        # 数值方法连接
        characteristic_function >> Edge(label="特征函数") >> fft
        fft >> Edge(label="FFT变换") >> pricing_engine
        cosine_method >> Edge(label="余弦方法") >> pricing_engine
        
        pde_explicit >> Edge(label="显式差分") >> pricing_engine
        pde_implicit >> Edge(label="隐式差分") >> pricing_engine
        crank_nicolson >> Edge(label="Crank-Nicolson") >> pricing_engine
        alternating_direction >> Edge(label="ADI方法") >> pricing_engine
        
        standard_mc >> Edge(label="标准MC") >> pricing_engine
        quasi_mc >> Edge(label="准MC") >> pricing_engine
        ls_mc >> Edge(label="LSMC") >> american_pricing
        control_variates >> Edge(label="控制变量") >> standard_mc
        
        # 定价引擎连接
        pricing_engine >> Edge(label="欧式期权") >> delta
        american_pricing >> Edge(label="美式期权") >> delta
        barrier_pricing >> Edge(label="障碍期权") >> delta
        exotic_pricing >> Edge(label="奇异期权") >> delta
        
        # 希腊字母计算
        delta >> Edge(label="一阶导数") >> gamma
        vega >> Edge(label="波动率敏感度") >> vanna
        gamma >> Edge(label="二阶导数") >> speed
        vanna >> Edge(label="交叉导数") >> volga
        
        # 对冲策略连接
        delta >> Edge(label="Delta对冲") >> delta_hedging
        gamma >> Edge(label="Gamma对冲") >> gamma_hedging
        vega >> Edge(label="Vega对冲") >> vega_hedging
        delta_hedging >> Edge(label="组合对冲") >> portfolio_hedging
        
        # PnL分析连接
        portfolio_hedging >> Edge(label="对冲结果") >> pnl_decomposition
        pnl_decomposition >> Edge(label="归因分析") >> attribution_analysis
        attribution_analysis >> Edge(label="有效性评估") >> hedge_effectiveness
        
        # 校准与表面处理
        mle_calibration >> Edge(label="MLE校准") >> surface
        least_squares >> Edge(label="最小二乘") >> surface
        genetic_algorithm >> Edge(label="遗传算法") >> surface
        particle_swarm >> Edge(label="粒子群") >> surface
        
        spline_interpolation >> Edge(label="样条插值") >> surface
        kernel_smoothing >> Edge(label="核平滑") >> surface
        arbitrage_check >> Edge(label="无套利检查") >> surface_repair
        surface_repair >> Edge(label="曲面修复") >> surface
        
        # 风险度量连接
        pricing_engine >> Edge(label="价格分布") >> var_calculation
        var_calculation >> Edge(label="VaR计算") >> expected_shortfall
        delta >> Edge(label="希腊字母风险") >> greeks_risk
        greeks_risk >> Edge(label="模型风险") >> model_risk
        
        # 压力测试连接
        stress_scenarios >> Edge(label="压力情景") >> monte_carlo_stress
        monte_carlo_stress >> Edge(label="MC压力测试") >> historical_simulation
        historical_simulation >> Edge(label="历史模拟") >> risk_dashboard
        
        # 报告系统连接
        var_calculation >> Edge(label="风险数据") >> risk_dashboard
        hedge_effectiveness >> Edge(label="对冲数据") >> regulatory_report
        model_risk >> Edge(label="模型风险") >> management_report
        
        # 反馈循环
        hedge_effectiveness >> Edge(label="反馈") >> delta_hedging
        model_risk >> Edge(label="反馈") >> mle_calibration
        risk_dashboard >> Edge(label="反馈") >> pricing_engine


if __name__ == "__main__":
    create_option_pricing_algorithm(filename="option_pricing_algorithm", outformat="png")
    create_option_pricing_algorithm(filename="option_pricing_algorithm", outformat="pdf")


