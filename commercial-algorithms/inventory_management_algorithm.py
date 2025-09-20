from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_inventory_management_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能库存管理算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据采集层
        with Cluster("数据采集层"):
            with Cluster("销售数据"):
                pos_system = Server("POS系统")
                ecommerce = Server("电商平台")
                mobile_sales = Server("移动销售")
                
            with Cluster("库存数据"):
                warehouse_system = Server("仓库系统")
                rfid_scanner = Server("RFID扫描")
                barcode_reader = Server("条码读取")
                
            with Cluster("供应链数据"):
                supplier_portal = Server("供应商门户")
                logistics_tracking = Server("物流跟踪")
                demand_forecast = Server("需求预测")
                
        # 库存优化引擎
        with Cluster("库存优化引擎"):
            with Cluster("实时库存引擎"):
                realtime_inventory = Server("实时库存引擎")
                stock_optimizer = Server("库存优化器")
                reorder_engine = Server("补货引擎")
                
            with Cluster("预测引擎"):
                demand_prediction = Server("需求预测")
                lead_time_forecast = Server("提前期预测")
                seasonality_analysis = Server("季节性分析")
                
            with Cluster("决策引擎"):
                abc_analysis = Server("ABC分析")
                eoq_calculator = Server("经济订货量")
                safety_stock = Server("安全库存")
                
        # 算法层
        with Cluster("库存算法层"):
            with Cluster("预测算法"):
                arima_model = Server("ARIMA模型")
                exponential_smoothing = Server("指数平滑")
                machine_learning = Server("机器学习")
                
            with Cluster("优化算法"):
                linear_programming = Server("线性规划")
                genetic_algorithm = Server("遗传算法")
                simulated_annealing = Server("模拟退火")
                
            with Cluster("分类算法"):
                abc_classification = Server("ABC分类")
                xyz_analysis = Server("XYZ分析")
                fsn_analysis = Server("FSN分析")
                
        # 库存策略层
        with Cluster("库存策略层"):
            with Cluster("补货策略"):
                continuous_review = Server("连续检查")
                periodic_review = Server("定期检查")
                hybrid_strategy = Server("混合策略")
                
            with Cluster("分配策略"):
                centralized = Server("集中分配")
                decentralized = Server("分散分配")
                dynamic_allocation = Server("动态分配")
                
            with Cluster("处置策略"):
                markdown_optimization = Server("降价优化")
                liquidation = Server("清仓处理")
                return_management = Server("退货管理")
                
        # 执行层
        with Cluster("执行层"):
            with Cluster("采购管理"):
                purchase_orders = Server("采购订单")
                vendor_management = Server("供应商管理")
                contract_management = Server("合同管理")
                
            with Cluster("仓储管理"):
                warehouse_operations = Server("仓库作业")
                picking_optimization = Server("拣货优化")
                putaway_strategy = Server("上架策略")
                
            with Cluster("配送管理"):
                route_optimization = Server("路径优化")
                delivery_scheduling = Server("配送调度")
                last_mile = Server("最后一公里")
                
        # 监控层
        with Cluster("监控层"):
            with Cluster("库存监控"):
                stock_level_monitor = Server("库存水平监控")
                turnover_analysis = Server("周转率分析")
                obsolescence_tracking = Server("滞销跟踪")
                
            with Cluster("成本监控"):
                holding_cost = Server("持有成本")
                ordering_cost = Server("订货成本")
                shortage_cost = Server("缺货成本")
                
            with Cluster("绩效监控"):
                service_level = Server("服务水平")
                fill_rate = Server("满足率")
                accuracy_metrics = Server("准确率指标")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("主数据"):
                product_master = Server("商品主数据")
                supplier_master = Server("供应商主数据")
                location_master = Server("位置主数据")
                
            with Cluster("交易数据"):
                sales_transactions = Server("销售交易")
                inventory_movements = Server("库存移动")
                purchase_orders = Server("采购订单")
                
            with Cluster("分析数据"):
                inventory_analytics = Server("库存分析")
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
        # 数据采集
        pos_system >> Edge(label="销售数据") >> realtime_inventory
        warehouse_system >> Edge(label="库存数据") >> stock_optimizer
        supplier_portal >> Edge(label="供应数据") >> reorder_engine
        
        # 库存优化
        realtime_inventory >> Edge(label="实时优化") >> stock_optimizer
        demand_prediction >> Edge(label="需求预测") >> reorder_engine
        abc_analysis >> Edge(label="分类分析") >> eoq_calculator
        
        # 算法调用
        demand_prediction >> Edge(label="时间序列") >> arima_model
        stock_optimizer >> Edge(label="优化算法") >> linear_programming
        abc_analysis >> Edge(label="分类算法") >> abc_classification
        
        # 策略应用
        arima_model >> Edge(label="补货策略") >> continuous_review
        linear_programming >> Edge(label="分配策略") >> dynamic_allocation
        abc_classification >> Edge(label="处置策略") >> markdown_optimization
        
        # 执行
        continuous_review >> Edge(label="采购执行") >> purchase_orders
        dynamic_allocation >> Edge(label="仓储执行") >> warehouse_operations
        markdown_optimization >> Edge(label="配送执行") >> route_optimization
        
        # 监控
        purchase_orders >> Edge(label="库存监控") >> stock_level_monitor
        warehouse_operations >> Edge(label="成本监控") >> holding_cost
        route_optimization >> Edge(label="绩效监控") >> service_level
        
        # 数据存储
        stock_level_monitor >> Edge(label="主数据") >> product_master
        holding_cost >> Edge(label="交易数据") >> sales_transactions
        service_level >> Edge(label="分析数据") >> inventory_analytics
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        stock_level_monitor >> Edge(label="反馈数据") >> kafka_stream
        service_level >> Edge(label="绩效反馈") >> demand_prediction
        
        # 监控
        realtime_inventory >> Edge(label="指标上报") >> monitoring
        stock_optimizer >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting


if __name__ == "__main__":
    create_inventory_management_algorithm(filename="inventory_management_algorithm", outformat="png")
    create_inventory_management_algorithm(filename="inventory_management_algorithm", outformat="pdf")