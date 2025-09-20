from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_portfolio_optimization_algorithm(filename: str, outformat: str) -> None:
    with Diagram("投资组合优化算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据源层"):
            with Cluster("市场数据"):
                price_history = Server("历史价格")
                returns_series = Server("收益序列")
                market_index = Server("市场指数")
                volume_data = Server("成交量数据")

            with Cluster("基本面与因子"):
                fundamentals = Server("基本面数据")
                factor_exposures = Server("因子暴露")
                risk_premia = Server("风险溢价")
                esg_scores = Server("ESG评分")

            with Cluster("约束与偏好"):
                mandate_rules = Server("投资约束")
                turnover_limit = Server("换手限制")
                tax_rules = Server("税务规则")
                liquidity_constraints = Server("流动性约束")

        with Cluster("风险建模"):
            with Cluster("协方差估计"):
                sample_cov = Server("样本协方差")
                shrinkage_cov = Server("收缩估计")
                factor_cov = Server("因子协方差")
                dcc_garch = Server("DCC-GARCH")
            
            with Cluster("波动率建模"):
                garch_vol = Server("GARCH波动率")
                realized_vol = Server("实现波动率")
                implied_vol = Server("隐含波动率")
            
            factor_model = Server("多因子风险模型")

        with Cluster("预期收益建模"):
            with Cluster("历史方法"):
                historical_mean = Server("历史均值")
                rolling_mean = Server("滚动均值")
                exponential_smoothing = Server("指数平滑")
            
            with Cluster("模型方法"):
                bl_model = Server("Black-Litterman")
                factor_alpha = Server("因子预期收益")
                ml_forecast = Server("机器学习预测")

        with Cluster("优化器与约束"):
            with Cluster("优化算法"):
                mean_variance = Server("均值-方差优化")
                robust_opt = Server("鲁棒优化")
                cvar_opt = Server("CVaR优化")
                max_sharpe = Server("最大夏普比率")
            
            with Cluster("约束处理"):
                linear_constraints = Server("线性约束")
                quadratic_constraints = Server("二次约束")
                integer_constraints = Server("整数约束")

        with Cluster("组合构建与调仓"):
            with Cluster("权重计算"):
                target_weights = Server("目标权重")
                weight_optimization = Server("权重优化")
                rebalancing_trigger = Server("再平衡触发")
            
            with Cluster("交易成本"):
                transaction_costs = Server("交易成本模型")
                market_impact = Server("市场冲击")
                timing_cost = Server("择时成本")
            
            rebalancing = Server("再平衡策略")

        with Cluster("执行与风控"):
            with Cluster("执行系统"):
                execution_engine = Server("执行引擎")
                smart_routing = Server("智能路由")
                algo_trading = Server("算法交易")
            
            with Cluster("风险控制"):
                risk_limits = Server("风险限额监控")
                var_monitoring = Server("VaR监控")
                stress_testing = Server("压力测试")
            
            performance_attribution = Server("业绩归因")

        with Cluster("回测与生产"):
            with Cluster("回测系统"):
                backtest = Server("回测框架")
                monte_carlo_sim = Server("蒙特卡洛模拟")
                scenario_analysis = Server("情景分析")
            
            with Cluster("生产环境"):
                live_portfolio = Server("实时组合")
                real_time_risk = Server("实时风险")
                monitoring = Server("监控告警")

        # 数据流连接
        price_history >> Edge(label="计算") >> returns_series
        volume_data >> Edge(label="流动性") >> liquidity_constraints
        
        # 风险建模连接
        returns_series >> Edge(label="估计") >> sample_cov
        sample_cov >> Edge(label="收缩") >> shrinkage_cov
        factor_exposures >> Edge(label="因子协方差") >> factor_cov
        returns_series >> Edge(label="动态相关") >> dcc_garch
        
        returns_series >> Edge(label="GARCH建模") >> garch_vol
        returns_series >> Edge(label="高频数据") >> realized_vol
        market_index >> Edge(label="期权数据") >> implied_vol
        
        # 预期收益建模连接
        returns_series >> Edge(label="历史统计") >> historical_mean
        returns_series >> Edge(label="滚动窗口") >> rolling_mean
        returns_series >> Edge(label="时间衰减") >> exponential_smoothing
        
        fundamentals >> Edge(label="投资观点") >> bl_model
        market_index >> Edge(label="市场先验") >> bl_model
        factor_exposures >> Edge(label="因子收益") >> factor_alpha
        returns_series >> Edge(label="ML预测") >> ml_forecast
        
        # 优化器连接
        bl_model >> Edge(label="预期收益") >> mean_variance
        historical_mean >> Edge(label="预期收益") >> mean_variance
        factor_alpha >> Edge(label="预期收益") >> mean_variance
        ml_forecast >> Edge(label="预期收益") >> mean_variance
        
        shrinkage_cov >> Edge(label="协方差矩阵") >> robust_opt
        factor_cov >> Edge(label="因子风险") >> cvar_opt
        garch_vol >> Edge(label="波动率") >> max_sharpe
        
        # 约束连接
        mandate_rules >> Edge(label="投资限制") >> linear_constraints
        turnover_limit >> Edge(label="换手约束") >> quadratic_constraints
        tax_rules >> Edge(label="税务优化") >> integer_constraints
        liquidity_constraints >> Edge(label="流动性要求") >> linear_constraints
        
        # 组合构建连接
        mean_variance >> Edge(label="优化结果") >> target_weights
        robust_opt >> Edge(label="鲁棒权重") >> target_weights
        cvar_opt >> Edge(label="CVaR权重") >> target_weights
        max_sharpe >> Edge(label="夏普权重") >> target_weights
        
        linear_constraints >> Edge(label="约束检查") >> weight_optimization
        quadratic_constraints >> Edge(label="约束检查") >> weight_optimization
        integer_constraints >> Edge(label="约束检查") >> weight_optimization
        
        target_weights >> Edge(label="权重优化") >> weight_optimization
        weight_optimization >> Edge(label="触发条件") >> rebalancing_trigger
        
        # 交易成本连接
        target_weights >> Edge(label="交易量") >> transaction_costs
        volume_data >> Edge(label="流动性影响") >> market_impact
        rebalancing_trigger >> Edge(label="择时决策") >> timing_cost
        
        transaction_costs >> Edge(label="成本优化") >> rebalancing
        market_impact >> Edge(label="冲击控制") >> rebalancing
        timing_cost >> Edge(label="择时优化") >> rebalancing
        
        # 执行系统连接
        rebalancing >> Edge(label="交易指令") >> execution_engine
        execution_engine >> Edge(label="智能路由") >> smart_routing
        smart_routing >> Edge(label="算法执行") >> algo_trading
        
        # 风险控制连接
        algo_trading >> Edge(label="成交监控") >> risk_limits
        risk_limits >> Edge(label="VaR计算") >> var_monitoring
        var_monitoring >> Edge(label="压力测试") >> stress_testing
        
        # 业绩归因连接
        algo_trading >> Edge(label="成交数据") >> performance_attribution
        performance_attribution >> Edge(label="归因分析") >> backtest
        
        # 回测系统连接
        backtest >> Edge(label="历史验证") >> monte_carlo_sim
        monte_carlo_sim >> Edge(label="情景生成") >> scenario_analysis
        
        # 生产环境连接
        scenario_analysis >> Edge(label="风险预测") >> live_portfolio
        live_portfolio >> Edge(label="实时监控") >> real_time_risk
        real_time_risk >> Edge(label="告警系统") >> monitoring
        
        # 反馈循环
        performance_attribution >> Edge(label="模型反馈") >> factor_model
        stress_testing >> Edge(label="风险反馈") >> risk_limits
        monitoring >> Edge(label="系统反馈") >> execution_engine


if __name__ == "__main__":
    create_portfolio_optimization_algorithm(filename="portfolio_optimization_algorithm", outformat="png")
    create_portfolio_optimization_algorithm(filename="portfolio_optimization_algorithm", outformat="pdf")


