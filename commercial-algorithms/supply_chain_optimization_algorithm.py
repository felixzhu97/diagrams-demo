
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_supply_chain_optimization_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能供应链优化算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("需求数据"):
                sales_forecast = Server("销售预测")
                customer_orders = Server("客户订单")
                market_demand = Server("市场需求")
                seasonal_patterns = Server("季节性模式")
                
            with Cluster("供应数据"):
                supplier_capacity = Server("供应商产能")
                raw_materials = Server("原材料数据")
                production_capacity = Server("生产产能")
                quality_metrics = Server("质量指标")
                
            with Cluster("物流数据"):
                transportation_data = Server("运输数据")
                warehouse_capacity = Server("仓库容量")
                inventory_levels = Server("库存水平")
                delivery_performance = Server("配送绩效")
                
        # 供应链优化引擎
        with Cluster("供应链优化引擎"):
            with Cluster("需求规划引擎"):
                demand_planning = Server("需求规划")
                s_and_op_process = Server("S&OP流程")
                demand_sensing = Server("需求感知")
                
            with Cluster("供应规划引擎"):
                supply_planning = Server("供应规划")
                capacity_planning = Server("产能规划")
                supplier_optimization = Server("供应商优化")
                
            with Cluster("网络优化引擎"):
                network_design = Server("网络设计")
                location_optimization = Server("位置优化")
                flow_optimization = Server("流量优化")
                
        # 算法层
        with Cluster("优化算法层"):
            with Cluster("数学规划"):
                linear_programming = Server("线性规划")
                mixed_integer = Server("混合整数规划")
                quadratic_programming = Server("二次规划")
                stochastic_programming = Server("随机规划")
                
            with Cluster("启发式算法"):
                genetic_algorithm = Server("遗传算法")
                simulated_annealing = Server("模拟退火")
                tabu_search = Server("禁忌搜索")
                particle_swarm = Server("粒子群优化")
                
            with Cluster("机器学习算法"):
                time_series = Server("时间序列")
                neural_network = Server("神经网络")
                random_forest = Server("随机森林")
                reinforcement_learning = Server("强化学习")
                
        # 优化模块层
        with Cluster("优化模块层"):
            with Cluster("需求优化"):
                demand_forecasting = Server("需求预测")
                demand_aggregation = Server("需求聚合")
                demand_allocation = Server("需求分配")
                
            with Cluster("供应优化"):
                supplier_selection = Server("供应商选择")
                procurement_optimization = Server("采购优化")
                contract_optimization = Server("合同优化")
                
            with Cluster("生产优化"):
                production_scheduling = Server("生产调度")
                capacity_utilization = Server("产能利用")
                quality_optimization = Server("质量优化")
                
            with Cluster("物流优化"):
                route_optimization = Server("路径优化")
                warehouse_optimization = Server("仓库优化")
                transportation_optimization = Server("运输优化")
                
        # 决策支持层
        with Cluster("决策支持层"):
            with Cluster("场景分析"):
                scenario_planning = Server("场景规划")
                what_if_analysis = Server("假设分析")
                sensitivity_analysis = Server("敏感性分析")
                
            with Cluster("风险分析"):
                risk_assessment = Server("风险评估")
                disruption_analysis = Server("中断分析")
                resilience_planning = Server("弹性规划")
                
            with Cluster("绩效分析"):
                kpi_monitoring = Server("KPI监控")
                cost_analysis = Server("成本分析")
                service_level_analysis = Server("服务水平分析")
                
        # 执行层
        with Cluster("执行层"):
            with Cluster("采购执行"):
                purchase_orders = Server("采购订单")
                supplier_management = Server("供应商管理")
                contract_management = Server("合同管理")
                
            with Cluster("生产执行"):
                production_orders = Server("生产订单")
                shop_floor_control = Server("车间控制")
                quality_control = Server("质量控制")
                
            with Cluster("物流执行"):
                shipment_planning = Server("发货计划")
                warehouse_operations = Server("仓库作业")
                delivery_management = Server("配送管理")
                
        # 监控层
        with Cluster("监控层"):
            with Cluster("实时监控"):
                realtime_dashboard = Server("实时仪表板")
                alert_system = Server("告警系统")
                performance_monitoring = Server("性能监控")
                
            with Cluster("预测监控"):
                demand_monitoring = Server("需求监控")
                supply_monitoring = Server("供应监控")
                capacity_monitoring = Server("产能监控")
                
            with Cluster("异常监控"):
                anomaly_detection = Server("异常检测")
                disruption_detection = Server("中断检测")
                quality_monitoring = Server("质量监控")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("主数据"):
                product_master = Server("产品主数据")
                supplier_master = Server("供应商主数据")
                location_master = Server("位置主数据")
                
            with Cluster("交易数据"):
                order_data = Server("订单数据")
                shipment_data = Server("发货数据")
                inventory_data = Server("库存数据")
                
            with Cluster("分析数据"):
                optimization_results = Server("优化结果")
                performance_metrics = Server("绩效指标")
                forecast_data = Server("预测数据")
                
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
        sales_forecast >> Edge(label="需求数据") >> demand_planning
        supplier_capacity >> Edge(label="供应数据") >> supply_planning
        transportation_data >> Edge(label="物流数据") >> network_design
        
        # 供应链优化
        demand_planning >> Edge(label="需求规划") >> s_and_op_process
        supply_planning >> Edge(label="供应规划") >> capacity_planning
        network_design >> Edge(label="网络优化") >> location_optimization
        
        # 算法调用
        s_and_op_process >> Edge(label="数学规划") >> linear_programming
        capacity_planning >> Edge(label="启发式算法") >> genetic_algorithm
        location_optimization >> Edge(label="机器学习") >> time_series
        
        # 优化模块
        linear_programming >> Edge(label="需求优化") >> demand_forecasting
        genetic_algorithm >> Edge(label="供应优化") >> supplier_selection
        time_series >> Edge(label="生产优化") >> production_scheduling
        
        # 决策支持
        demand_forecasting >> Edge(label="场景分析") >> scenario_planning
        supplier_selection >> Edge(label="风险分析") >> risk_assessment
        production_scheduling >> Edge(label="绩效分析") >> kpi_monitoring
        
        # 执行
        scenario_planning >> Edge(label="采购执行") >> purchase_orders
        risk_assessment >> Edge(label="生产执行") >> production_orders
        kpi_monitoring >> Edge(label="物流执行") >> shipment_planning
        
        # 监控
        purchase_orders >> Edge(label="实时监控") >> realtime_dashboard
        production_orders >> Edge(label="预测监控") >> demand_monitoring
        shipment_planning >> Edge(label="异常监控") >> anomaly_detection
        
        # 数据存储
        realtime_dashboard >> Edge(label="主数据") >> product_master
        demand_monitoring >> Edge(label="交易数据") >> order_data
        anomaly_detection >> Edge(label="分析数据") >> optimization_results
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        realtime_dashboard >> Edge(label="反馈数据") >> kafka_stream
        demand_monitoring >> Edge(label="模型更新") >> time_series
        
        # 监控
        demand_planning >> Edge(label="指标上报") >> monitoring
        supply_planning >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_supply_chain_optimization_algorithm(filename="supply_chain_optimization_algorithm", outformat="png")
    create_supply_chain_optimization_algorithm(filename="supply_chain_optimization_algorithm", outformat="pdf")
