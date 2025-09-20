from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_pricing_algorithm(filename: str, outformat: str) -> None:
    with Diagram("动态定价算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据输入层
        with Cluster("数据输入层"):
            with Cluster("市场数据"):
                market_data = Server("市场行情")
                competitor_prices = Server("竞品价格")
                demand_supply = Server("供需数据")
                
            with Cluster("内部数据"):
                cost_data = Server("成本数据")
                inventory_data = Server("库存数据")
                sales_history = Server("销售历史")
                
            with Cluster("外部数据"):
                weather_data = Server("天气数据")
                economic_indicators = Server("经济指标")
                social_media = Server("社交媒体")
                
        # 定价引擎层
        with Cluster("定价引擎层"):
            with Cluster("实时定价引擎"):
                realtime_pricing = Server("实时定价引擎")
                price_optimizer = Server("价格优化器")
                dynamic_adjuster = Server("动态调整器")
                
            with Cluster("预测定价引擎"):
                demand_forecast = Server("需求预测")
                price_elasticity = Server("价格弹性")
                revenue_optimizer = Server("收益优化器")
                
            with Cluster("策略定价引擎"):
                rule_engine = Server("规则引擎")
                a_b_testing = Server("A/B测试")
                segmentation_pricing = Server("细分定价")
                
        # 算法层
        with Cluster("定价算法层"):
            with Cluster("机器学习算法"):
                regression_model = Server("回归模型")
                time_series = Server("时间序列")
                neural_network = Server("神经网络")
                
            with Cluster("优化算法"):
                linear_programming = Server("线性规划")
                genetic_algorithm = Server("遗传算法")
                simulated_annealing = Server("模拟退火")
                
            with Cluster("博弈论算法"):
                auction_mechanism = Server("拍卖机制")
                game_theory = Server("博弈论")
                nash_equilibrium = Server("纳什均衡")
                
        # 定价策略层
        with Cluster("定价策略层"):
            with Cluster("基础策略"):
                cost_plus = Server("成本加成")
                value_based = Server("价值定价")
                competitive = Server("竞争定价")
                
            with Cluster("动态策略"):
                surge_pricing = Server("高峰定价")
                personalized = Server("个性化定价")
                time_based = Server("时间定价")
                
            with Cluster("高级策略"):
                bundle_pricing = Server("捆绑定价")
                freemium = Server("免费增值")
                subscription = Server("订阅定价")
                
        # 决策支持层
        with Cluster("决策支持层"):
            with Cluster("价格分析"):
                price_analytics = Server("价格分析")
                sensitivity_analysis = Server("敏感性分析")
                scenario_modeling = Server("场景建模")
                
            with Cluster("风险评估"):
                risk_assessment = Server("风险评估")
                market_impact = Server("市场影响")
                competitor_response = Server("竞品响应")
                
            with Cluster("合规检查"):
                regulatory_check = Server("合规检查")
                price_limits = Server("价格限制")
                audit_trail = Server("审计跟踪")
                
        # 执行层
        with Cluster("执行层"):
            with Cluster("价格发布"):
                price_api = Server("价格API")
                price_database = Server("价格数据库")
                price_cache = Server("价格缓存")
                
            with Cluster("渠道分发"):
                web_channel = Server("Web渠道")
                mobile_channel = Server("移动渠道")
                pos_system = Server("POS系统")
                
            with Cluster("监控反馈"):
                price_monitor = Server("价格监控")
                sales_tracker = Server("销售跟踪")
                feedback_loop = Server("反馈循环")
                
        # 数据处理层
        with Cluster("数据处理层"):
            with Cluster("实时处理"):
                kafka_stream = Server("Kafka流")
                stream_processor = Server("流处理器")
                realtime_analytics = Server("实时分析")
                
            with Cluster("批处理"):
                spark_batch = Server("Spark批处理")
                data_warehouse = Server("数据仓库")
                etl_pipeline = Server("ETL管道")
                
        # 监控与日志
        with Cluster("监控与日志"):
            monitoring = Server("监控系统")
            logging = Server("日志收集")
            alerting = Server("告警系统")
            
        # 连接关系
        # 数据输入
        market_data >> Edge(label="市场数据") >> realtime_pricing
        cost_data >> Edge(label="成本数据") >> price_optimizer
        demand_supply >> Edge(label="供需数据") >> demand_forecast
        
        # 定价引擎
        realtime_pricing >> Edge(label="实时定价") >> price_optimizer
        demand_forecast >> Edge(label="需求预测") >> revenue_optimizer
        rule_engine >> Edge(label="规则执行") >> segmentation_pricing
        
        # 算法调用
        price_optimizer >> Edge(label="优化算法") >> linear_programming
        demand_forecast >> Edge(label="预测算法") >> time_series
        revenue_optimizer >> Edge(label="机器学习") >> neural_network
        
        # 策略应用
        linear_programming >> Edge(label="基础策略") >> cost_plus
        time_series >> Edge(label="动态策略") >> surge_pricing
        neural_network >> Edge(label="高级策略") >> personalized
        
        # 决策支持
        cost_plus >> Edge(label="价格分析") >> price_analytics
        surge_pricing >> Edge(label="风险评估") >> risk_assessment
        personalized >> Edge(label="合规检查") >> regulatory_check
        
        # 执行发布
        price_analytics >> Edge(label="价格发布") >> price_api
        price_api >> Edge(label="存储") >> price_database
        price_database >> Edge(label="缓存") >> price_cache
        
        # 渠道分发
        price_cache >> Edge(label="Web分发") >> web_channel
        price_cache >> Edge(label="移动分发") >> mobile_channel
        price_cache >> Edge(label="POS分发") >> pos_system
        
        # 监控反馈
        web_channel >> Edge(label="销售数据") >> sales_tracker
        mobile_channel >> Edge(label="用户行为") >> price_monitor
        pos_system >> Edge(label="交易数据") >> feedback_loop
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        feedback_loop >> Edge(label="反馈数据") >> kafka_stream
        sales_tracker >> Edge(label="销售反馈") >> demand_forecast
        
        # 监控
        realtime_pricing >> Edge(label="指标上报") >> monitoring
        price_optimizer >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting


if __name__ == "__main__":
    create_pricing_algorithm(filename="pricing_algorithm", outformat="png")
    create_pricing_algorithm(filename="pricing_algorithm", outformat="pdf")