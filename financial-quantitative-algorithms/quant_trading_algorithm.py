from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_quant_trading_algorithm(filename: str, outformat: str) -> None:
    with Diagram("量化交易系统与策略流程架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据层"):
            with Cluster("市场数据"):
                market_data = Server("行情源")
                order_book = Server("订单簿/深度")
                trade_data = Server("成交数据")
                news_feed = Server("新闻流")
            
            with Cluster("替代数据"):
                alt_data = Server("另类数据")
                satellite_data = Server("卫星数据")
                social_sentiment = Server("社交情感")
                economic_indicators = Server("经济指标")
            
            with Cluster("数据存储"):
                feature_store = Server("特征库")
                time_series_db = Server("时序数据库")
                real_time_cache = Server("实时缓存")

        with Cluster("研究与信号"):
            with Cluster("研究环境"):
                research_env = Server("研究环境")
                jupyter_notebooks = Server("Jupyter环境")
                data_exploration = Server("数据探索")
                hypothesis_testing = Server("假设检验")
            
            with Cluster("特征工程"):
                feature_engineering = Server("特征工程")
                technical_indicators = Server("技术指标")
                fundamental_factors = Server("基本面因子")
                macro_factors = Server("宏观因子")
            
            with Cluster("模型训练"):
                model_training = Server("模型训练")
                ml_models = Server("机器学习模型")
                deep_learning = Server("深度学习")
                ensemble_methods = Server("集成方法")
            
            with Cluster("信号生成"):
                alpha_signals = Server("Alpha 信号")
                momentum_signals = Server("动量信号")
                mean_reversion = Server("均值回归")
                arbitrage_signals = Server("套利信号")

        with Cluster("风险与合规"):
            with Cluster("风险模型"):
                risk_model = Server("风险模型")
                var_model = Server("VaR模型")
                stress_testing = Server("压力测试")
                scenario_analysis = Server("情景分析")
            
            with Cluster("合规系统"):
                regulatory_compliance = Server("监管合规")
                position_limits = Server("仓位限制")
                exposure_limits = Server("敞口限制")
                pre_trade_checks = Server("交易前检查")

        with Cluster("组合与执行"):
            with Cluster("组合构建"):
                portfolio_construction = Server("组合构建")
                optimization_engine = Server("优化引擎")
                rebalancing_logic = Server("再平衡逻辑")
                tax_optimization = Server("税务优化")
            
            with Cluster("仓位管理"):
                position_sizing = Server("仓位与杠杆")
                kelly_criterion = Server("凯利准则")
                risk_parity = Server("风险平价")
                volatility_targeting = Server("波动率目标")
            
            with Cluster("执行系统"):
                execution_algo = Server("执行算法")
                smart_router = Server("智能路由")
                venue_selection = Server("场所选择")
                order_management = Server("订单管理")

        with Cluster("交易后与运维"):
            with Cluster("交易分析"):
                slippage = Server("滑点分析")
                transaction_cost = Server("交易成本分析")
                market_impact = Server("市场冲击")
                timing_analysis = Server("择时分析")
            
            with Cluster("监控系统"):
                monitoring = Server("监控与告警")
                real_time_risk = Server("实时风险")
                performance_tracking = Server("绩效跟踪")
                anomaly_detection = Server("异常检测")
            
            with Cluster("风控系统"):
                risk_limits = Server("限额/风控")
                drawdown_control = Server("回撤控制")
                correlation_monitoring = Server("相关性监控")
                liquidity_monitoring = Server("流动性监控")
            
            with Cluster("报告系统"):
                reporting = Server("报表与审计")
                regulatory_reporting = Server("监管报告")
                management_dashboard = Server("管理仪表板")
                client_reporting = Server("客户报告")

        with Cluster("回测与评估"):
            with Cluster("回测系统"):
                backtest_engine = Server("回测引擎")
                walk_forward = Server("滚动回测")
                monte_carlo = Server("蒙特卡洛")
                scenario_backtest = Server("情景回测")
            
            with Cluster("绩效分析"):
                performance = Server("绩效指标")
                risk_adjusted_returns = Server("风险调整收益")
                attribution = Server("归因分析")
                benchmark_comparison = Server("基准比较")
            
            with Cluster("模型验证"):
                out_of_sample = Server("样本外验证")
                cross_validation = Server("交叉验证")
                model_stability = Server("模型稳定性")
                overfitting_detection = Server("过拟合检测")

        # 数据流连接
        market_data >> Edge(label="实时数据") >> real_time_cache
        order_book >> Edge(label="深度数据") >> real_time_cache
        trade_data >> Edge(label="成交数据") >> real_time_cache
        news_feed >> Edge(label="新闻数据") >> real_time_cache
        
        alt_data >> Edge(label="另类数据") >> feature_store
        satellite_data >> Edge(label="卫星数据") >> feature_store
        social_sentiment >> Edge(label="情感数据") >> feature_store
        economic_indicators >> Edge(label="宏观数据") >> feature_store
        
        real_time_cache >> Edge(label="缓存数据") >> time_series_db
        time_series_db >> Edge(label="历史数据") >> feature_store
        
        # 研究环境连接
        research_env >> Edge(label="研究工具") >> jupyter_notebooks
        jupyter_notebooks >> Edge(label="数据探索") >> data_exploration
        data_exploration >> Edge(label="假设检验") >> hypothesis_testing
        
        # 特征工程连接
        feature_store >> Edge(label="原始特征") >> feature_engineering
        feature_engineering >> Edge(label="技术指标") >> technical_indicators
        feature_engineering >> Edge(label="基本面因子") >> fundamental_factors
        feature_engineering >> Edge(label="宏观因子") >> macro_factors
        
        # 模型训练连接
        technical_indicators >> Edge(label="特征输入") >> model_training
        fundamental_factors >> Edge(label="特征输入") >> model_training
        macro_factors >> Edge(label="特征输入") >> model_training
        
        model_training >> Edge(label="ML模型") >> ml_models
        model_training >> Edge(label="深度学习") >> deep_learning
        model_training >> Edge(label="集成方法") >> ensemble_methods
        
        # 信号生成连接
        ml_models >> Edge(label="预测信号") >> alpha_signals
        deep_learning >> Edge(label="深度信号") >> alpha_signals
        ensemble_methods >> Edge(label="集成信号") >> alpha_signals
        
        alpha_signals >> Edge(label="动量信号") >> momentum_signals
        alpha_signals >> Edge(label="均值回归") >> mean_reversion
        alpha_signals >> Edge(label="套利机会") >> arbitrage_signals
        
        # 风险与合规连接
        risk_model >> Edge(label="风险度量") >> var_model
        var_model >> Edge(label="压力测试") >> stress_testing
        stress_testing >> Edge(label="情景分析") >> scenario_analysis
        
        regulatory_compliance >> Edge(label="合规检查") >> position_limits
        position_limits >> Edge(label="仓位限制") >> exposure_limits
        exposure_limits >> Edge(label="敞口检查") >> pre_trade_checks
        
        # 组合构建连接
        alpha_signals >> Edge(label="信号输入") >> portfolio_construction
        momentum_signals >> Edge(label="信号输入") >> portfolio_construction
        mean_reversion >> Edge(label="信号输入") >> portfolio_construction
        arbitrage_signals >> Edge(label="信号输入") >> portfolio_construction
        
        portfolio_construction >> Edge(label="优化") >> optimization_engine
        optimization_engine >> Edge(label="再平衡") >> rebalancing_logic
        rebalancing_logic >> Edge(label="税务优化") >> tax_optimization
        
        # 仓位管理连接
        tax_optimization >> Edge(label="目标权重") >> position_sizing
        position_sizing >> Edge(label="凯利准则") >> kelly_criterion
        position_sizing >> Edge(label="风险平价") >> risk_parity
        position_sizing >> Edge(label="波动率目标") >> volatility_targeting
        
        # 执行系统连接
        kelly_criterion >> Edge(label="仓位指令") >> execution_algo
        risk_parity >> Edge(label="仓位指令") >> execution_algo
        volatility_targeting >> Edge(label="仓位指令") >> execution_algo
        
        execution_algo >> Edge(label="智能路由") >> smart_router
        smart_router >> Edge(label="场所选择") >> venue_selection
        venue_selection >> Edge(label="订单管理") >> order_management
        
        # 交易后分析连接
        order_management >> Edge(label="成交数据") >> slippage
        slippage >> Edge(label="滑点分析") >> transaction_cost
        transaction_cost >> Edge(label="成本分析") >> market_impact
        market_impact >> Edge(label="冲击分析") >> timing_analysis
        
        # 监控系统连接
        timing_analysis >> Edge(label="交易数据") >> monitoring
        monitoring >> Edge(label="实时监控") >> real_time_risk
        real_time_risk >> Edge(label="风险监控") >> performance_tracking
        performance_tracking >> Edge(label="异常检测") >> anomaly_detection
        
        # 风控系统连接
        anomaly_detection >> Edge(label="异常告警") >> risk_limits
        risk_limits >> Edge(label="风险控制") >> drawdown_control
        drawdown_control >> Edge(label="回撤控制") >> correlation_monitoring
        correlation_monitoring >> Edge(label="相关性监控") >> liquidity_monitoring
        
        # 报告系统连接
        liquidity_monitoring >> Edge(label="流动性数据") >> reporting
        reporting >> Edge(label="监管报告") >> regulatory_reporting
        regulatory_reporting >> Edge(label="管理报告") >> management_dashboard
        management_dashboard >> Edge(label="客户报告") >> client_reporting
        
        # 回测系统连接
        backtest_engine >> Edge(label="历史回测") >> walk_forward
        walk_forward >> Edge(label="滚动验证") >> monte_carlo
        monte_carlo >> Edge(label="随机模拟") >> scenario_backtest
        
        # 绩效分析连接
        scenario_backtest >> Edge(label="回测结果") >> performance
        performance >> Edge(label="绩效指标") >> risk_adjusted_returns
        risk_adjusted_returns >> Edge(label="风险调整") >> attribution
        attribution >> Edge(label="归因分析") >> benchmark_comparison
        
        # 模型验证连接
        benchmark_comparison >> Edge(label="基准比较") >> out_of_sample
        out_of_sample >> Edge(label="样本外") >> cross_validation
        cross_validation >> Edge(label="交叉验证") >> model_stability
        model_stability >> Edge(label="稳定性") >> overfitting_detection
        
        # 反馈循环
        overfitting_detection >> Edge(label="模型反馈") >> model_training
        attribution >> Edge(label="策略反馈") >> portfolio_construction
        risk_limits >> Edge(label="风控反馈") >> execution_algo
        client_reporting >> Edge(label="客户反馈") >> research_env


if __name__ == "__main__":
    create_quant_trading_algorithm(filename="quant_trading_algorithm", outformat="png")
    create_quant_trading_algorithm(filename="quant_trading_algorithm", outformat="pdf")


