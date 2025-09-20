from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_fixed_income_curve_algorithm(filename: str, outformat: str) -> None:
    with Diagram("固定收益曲线与期限结构建模架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("市场数据层"):
            bond_prices = Server("债券价格")
            swap_rates = Server("互换利率")
            treasury_rates = Server("国债利率")
            credit_spreads = Server("信用利差")
            
        with Cluster("曲线构建方法"):
            bootstrapping = Server("自举法")
            spline_interpolation = Server("样条插值")
            nelson_siegel = Server("Nelson-Siegel")
            svensson_model = Server("Svensson模型")
            
        with Cluster("期限结构模型"):
            vasicek_model = Server("Vasicek模型")
            hull_white = Server("Hull-White模型")
            heath_jarrow_morton = Server("HJM模型")
            libor_market_model = Server("LMM模型")
            
        with Cluster("信用曲线建模"):
            hazard_rate = Server("违约强度")
            recovery_rate = Server("回收率")
            credit_curve = Server("信用曲线")
            cds_pricing = Server("CDS定价")
            
        with Cluster("风险度量"):
            duration = Server("久期")
            convexity = Server("凸性")
            key_rate_duration = Server("关键利率久期")
            dv01 = Server("DV01")
            
        with Cluster("套利检测"):
            arbitrage_check = Server("套利检测")
            curve_smoothing = Server("曲线平滑")
            consistency_check = Server("一致性检查")
            outlier_detection = Server("异常值检测")
            
        with Cluster("应用层"):
            bond_pricing = Server("债券定价")
            portfolio_risk = Server("组合风险")
            hedging_strategy = Server("对冲策略")
            yield_curve_trading = Server("收益率曲线交易")
            
        with Cluster("监控与更新"):
            curve_monitoring = Server("曲线监控")
            model_calibration = Server("模型校准")
            performance_tracking = Server("绩效跟踪")
            stress_testing = Server("压力测试")
            
        # 连接关系
        bond_prices >> Edge(label="价格数据") >> bootstrapping
        swap_rates >> Edge(label="利率数据") >> bootstrapping
        treasury_rates >> Edge(label="基准利率") >> bootstrapping
        credit_spreads >> Edge(label="信用数据") >> credit_curve
        
        bootstrapping >> Edge(label="基础曲线") >> spline_interpolation
        spline_interpolation >> Edge(label="平滑曲线") >> nelson_siegel
        nelson_siegel >> Edge(label="参数化") >> svensson_model
        
        svensson_model >> Edge(label="无风险曲线") >> vasicek_model
        vasicek_model >> Edge(label="单因子") >> hull_white
        hull_white >> Edge(label="多因子") >> heath_jarrow_morton
        heath_jarrow_morton >> Edge(label="远期利率") >> libor_market_model
        
        hazard_rate >> Edge(label="违约建模") >> credit_curve
        recovery_rate >> Edge(label="回收建模") >> credit_curve
        credit_curve >> Edge(label="信用定价") >> cds_pricing
        
        svensson_model >> Edge(label="利率敏感性") >> duration
        duration >> Edge(label="二阶导数") >> convexity
        convexity >> Edge(label="关键点") >> key_rate_duration
        key_rate_duration >> Edge(label="基点价值") >> dv01
        
        svensson_model >> Edge(label="套利检查") >> arbitrage_check
        arbitrage_check >> Edge(label="平滑处理") >> curve_smoothing
        curve_smoothing >> Edge(label="一致性") >> consistency_check
        consistency_check >> Edge(label="异常检测") >> outlier_detection
        
        svensson_model >> Edge(label="定价输入") >> bond_pricing
        credit_curve >> Edge(label="信用调整") >> bond_pricing
        duration >> Edge(label="风险度量") >> portfolio_risk
        convexity >> Edge(label="风险度量") >> portfolio_risk
        
        portfolio_risk >> Edge(label="对冲计算") >> hedging_strategy
        hedging_strategy >> Edge(label="交易策略") >> yield_curve_trading
        
        svensson_model >> Edge(label="实时监控") >> curve_monitoring
        curve_monitoring >> Edge(label="参数更新") >> model_calibration
        model_calibration >> Edge(label="绩效评估") >> performance_tracking
        performance_tracking >> Edge(label="压力场景") >> stress_testing
        
        # 反馈循环
        stress_testing >> Edge(label="反馈") >> model_calibration
        performance_tracking >> Edge(label="反馈") >> svensson_model


if __name__ == "__main__":
    create_fixed_income_curve_algorithm(filename="fixed_income_curve_algorithm", outformat="png")
    create_fixed_income_curve_algorithm(filename="fixed_income_curve_algorithm", outformat="pdf")
