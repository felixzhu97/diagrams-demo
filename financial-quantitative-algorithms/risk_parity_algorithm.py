from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_risk_parity_algorithm(filename: str, outformat: str) -> None:
    with Diagram("风险平价与风险预算组合架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("输入与约束"):
            with Cluster("资产配置"):
                asset_universe = Server("资产池")
                asset_classification = Server("资产分类")
                liquidity_screening = Server("流动性筛选")
                rebalancing_frequency = Server("再平衡频率")
            
            with Cluster("约束条件"):
                constraints = Server("约束/杠杆/做空")
                concentration_limits = Server("集中度限制")
                sector_limits = Server("行业限制")
                country_limits = Server("国家限制")
            
            with Cluster("成本模型"):
                tc_model = Server("交易成本")
                market_impact = Server("市场冲击")
                borrowing_costs = Server("借贷成本")
                management_fees = Server("管理费")

        with Cluster("风险估计"):
            with Cluster("协方差估计"):
                sample_cov = Server("样本协方差")
                shrinkage_cov = Server("收缩协方差")
                factor_cov = Server("因子协方差")
                dcc_garch = Server("DCC-GARCH")
            
            with Cluster("波动率建模"):
                historical_vol = Server("历史波动率")
                garch_vol = Server("GARCH波动率")
                realized_vol = Server("实现波动率")
                implied_vol = Server("隐含波动率")
            
            with Cluster("相关性分析"):
                correlation = Server("相关性矩阵")
                rolling_correlation = Server("滚动相关性")
                regime_correlation = Server("状态相关性")
                tail_dependence = Server("尾部依赖")

        with Cluster("风险预算"):
            with Cluster("风险度量"):
                target_rb = Server("目标风险预算")
                marginal_risk = Server("边际风险贡献")
                total_risk = Server("总风险")
                component_risk = Server("成分风险")
            
            with Cluster("风险分解"):
                systematic_risk = Server("系统性风险")
                idiosyncratic_risk = Server("特异风险")
                factor_exposure = Server("因子暴露")
                concentration_risk = Server("集中度风险")

        with Cluster("优化与求解"):
            with Cluster("优化算法"):
                equal_risk = Server("等风险贡献 ERC")
                rb_optimizer = Server("风险预算优化")
                hierarchical_rp = Server("分层风险平价")
                most_diversified = Server("最大分散化")
            
            with Cluster("稳健化方法"):
                regularization = Server("正则化")
                robust_optimization = Server("鲁棒优化")
                scenario_optimization = Server("情景优化")
                bayesian_optimization = Server("贝叶斯优化")

        with Cluster("组合与执行"):
            with Cluster("权重计算"):
                weights = Server("目标权重")
                weight_optimization = Server("权重优化")
                turnover_control = Server("换手控制")
                tax_optimization = Server("税务优化")
            
            with Cluster("再平衡策略"):
                rebalancing = Server("再平衡规则")
                threshold_rebalancing = Server("阈值再平衡")
                calendar_rebalancing = Server("日历再平衡")
                volatility_targeting = Server("波动率目标")
            
            with Cluster("执行系统"):
                execution = Server("执行系统")
                smart_routing = Server("智能路由")
                algo_trading = Server("算法交易")
                venue_selection = Server("场所选择")
            
            with Cluster("监控系统"):
                monitoring = Server("监控")
                risk_monitoring = Server("风险监控")
                performance_tracking = Server("绩效跟踪")
                attribution_analysis = Server("归因分析")

        # 输入与约束连接
        asset_universe >> Edge(label="资产筛选") >> asset_classification
        asset_classification >> Edge(label="流动性检查") >> liquidity_screening
        liquidity_screening >> Edge(label="频率设置") >> rebalancing_frequency
        
        constraints >> Edge(label="集中度控制") >> concentration_limits
        concentration_limits >> Edge(label="行业限制") >> sector_limits
        sector_limits >> Edge(label="国家限制") >> country_limits
        
        tc_model >> Edge(label="交易成本") >> market_impact
        market_impact >> Edge(label="市场冲击") >> borrowing_costs
        borrowing_costs >> Edge(label="借贷成本") >> management_fees
        
        # 风险估计连接
        asset_universe >> Edge(label="历史数据") >> sample_cov
        sample_cov >> Edge(label="收缩估计") >> shrinkage_cov
        asset_universe >> Edge(label="因子模型") >> factor_cov
        asset_universe >> Edge(label="动态模型") >> dcc_garch
        
        asset_universe >> Edge(label="历史波动率") >> historical_vol
        historical_vol >> Edge(label="GARCH建模") >> garch_vol
        asset_universe >> Edge(label="高频数据") >> realized_vol
        asset_universe >> Edge(label="期权数据") >> implied_vol
        
        sample_cov >> Edge(label="相关性计算") >> correlation
        correlation >> Edge(label="滚动窗口") >> rolling_correlation
        rolling_correlation >> Edge(label="状态检测") >> regime_correlation
        regime_correlation >> Edge(label="尾部分析") >> tail_dependence
        
        # 风险预算连接
        shrinkage_cov >> Edge(label="协方差矩阵") >> total_risk
        factor_cov >> Edge(label="因子风险") >> systematic_risk
        systematic_risk >> Edge(label="特异风险") >> idiosyncratic_risk
        
        total_risk >> Edge(label="边际计算") >> marginal_risk
        marginal_risk >> Edge(label="成分分解") >> component_risk
        component_risk >> Edge(label="因子暴露") >> factor_exposure
        factor_exposure >> Edge(label="集中度风险") >> concentration_risk
        
        # 优化算法连接
        target_rb >> Edge(label="风险预算") >> rb_optimizer
        rb_optimizer >> Edge(label="ERC优化") >> equal_risk
        equal_risk >> Edge(label="分层优化") >> hierarchical_rp
        hierarchical_rp >> Edge(label="最大分散") >> most_diversified
        
        # 稳健化方法连接
        regularization >> Edge(label="正则化") >> robust_optimization
        robust_optimization >> Edge(label="鲁棒优化") >> scenario_optimization
        scenario_optimization >> Edge(label="情景优化") >> bayesian_optimization
        bayesian_optimization >> Edge(label="贝叶斯") >> rb_optimizer
        
        # 约束条件连接
        concentration_limits >> Edge(label="约束检查") >> rb_optimizer
        sector_limits >> Edge(label="约束检查") >> rb_optimizer
        country_limits >> Edge(label="约束检查") >> rb_optimizer
        management_fees >> Edge(label="成本约束") >> rb_optimizer
        
        # 权重计算连接
        most_diversified >> Edge(label="优化结果") >> weights
        weights >> Edge(label="权重优化") >> weight_optimization
        weight_optimization >> Edge(label="换手控制") >> turnover_control
        turnover_control >> Edge(label="税务优化") >> tax_optimization
        
        # 再平衡策略连接
        tax_optimization >> Edge(label="再平衡触发") >> rebalancing
        rebalancing >> Edge(label="阈值再平衡") >> threshold_rebalancing
        threshold_rebalancing >> Edge(label="日历再平衡") >> calendar_rebalancing
        calendar_rebalancing >> Edge(label="波动率目标") >> volatility_targeting
        
        # 执行系统连接
        volatility_targeting >> Edge(label="执行指令") >> execution
        execution >> Edge(label="智能路由") >> smart_routing
        smart_routing >> Edge(label="算法交易") >> algo_trading
        algo_trading >> Edge(label="场所选择") >> venue_selection
        
        # 监控系统连接
        venue_selection >> Edge(label="成交监控") >> monitoring
        monitoring >> Edge(label="风险监控") >> risk_monitoring
        risk_monitoring >> Edge(label="绩效跟踪") >> performance_tracking
        performance_tracking >> Edge(label="归因分析") >> attribution_analysis
        
        # 反馈循环
        attribution_analysis >> Edge(label="绩效反馈") >> rb_optimizer
        risk_monitoring >> Edge(label="风险反馈") >> target_rb
        performance_tracking >> Edge(label="跟踪反馈") >> rebalancing_frequency


if __name__ == "__main__":
    create_risk_parity_algorithm(filename="risk_parity_algorithm", outformat="png")
    create_risk_parity_algorithm(filename="risk_parity_algorithm", outformat="pdf")


