from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_demand_forecasting_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能需求预测算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("历史销售数据"):
                sales_history = Server("销售历史")
                order_history = Server("订单历史")
                revenue_data = Server("收入数据")
                quantity_data = Server("数量数据")
                
            with Cluster("市场数据"):
                market_trends = Server("市场趋势")
                competitor_data = Server("竞品数据")
                economic_indicators = Server("经济指标")
                seasonal_patterns = Server("季节性模式")
                
            with Cluster("产品数据"):
                product_attributes = Server("产品属性")
                lifecycle_stage = Server("生命周期阶段")
                price_history = Server("价格历史")
                promotion_data = Server("促销数据")
                
            with Cluster("外部数据"):
                weather_data = Server("天气数据")
                holiday_calendar = Server("节假日日历")
                social_media = Server("社交媒体")
                news_sentiment = Server("新闻情感")
                
        # 需求预测引擎
        with Cluster("需求预测引擎"):
            with Cluster("短期预测引擎"):
                short_term_forecast = Server("短期预测引擎")
                daily_forecast = Server("日预测")
                weekly_forecast = Server("周预测")
                monthly_forecast = Server("月预测")
                
            with Cluster("中期预测引擎"):
                medium_term_forecast = Server("中期预测引擎")
                quarterly_forecast = Server("季度预测")
                seasonal_forecast = Server("季节性预测")
                trend_forecast = Server("趋势预测")
                
            with Cluster("长期预测引擎"):
                long_term_forecast = Server("长期预测引擎")
                annual_forecast = Server("年度预测")
                strategic_forecast = Server("战略预测")
                scenario_forecast = Server("场景预测")
                
        # 算法层
        with Cluster("预测算法层"):
            with Cluster("时间序列算法"):
                arima = Server("ARIMA")
                exponential_smoothing = Server("指数平滑")
                seasonal_decomposition = Server("季节分解")
                prophet = Server("Prophet")
                
            with Cluster("机器学习算法"):
                linear_regression = Server("线性回归")
                random_forest = Server("随机森林")
                gradient_boosting = Server("梯度提升")
                support_vector_regression = Server("支持向量回归")
                
            with Cluster("深度学习算法"):
                lstm = Server("LSTM")
                gru = Server("GRU")
                transformer = Server("Transformer")
                cnn_lstm = Server("CNN-LSTM")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("时间特征"):
                time_features = Server("时间特征")
                lag_features = Server("滞后特征")
                rolling_features = Server("滚动特征")
                seasonal_features = Server("季节特征")
                
            with Cluster("产品特征"):
                product_features = Server("产品特征")
                category_features = Server("类别特征")
                brand_features = Server("品牌特征")
                price_features = Server("价格特征")
                
            with Cluster("市场特征"):
                market_features = Server("市场特征")
                competitor_features = Server("竞品特征")
                economic_features = Server("经济特征")
                external_features = Server("外部特征")
                
        # 模型集成层
        with Cluster("模型集成层"):
            with Cluster("集成方法"):
                ensemble_learning = Server("集成学习")
                stacking = Server("堆叠")
                blending = Server("混合")
                voting = Server("投票")
                
            with Cluster("模型选择"):
                model_selection = Server("模型选择")
                cross_validation = Server("交叉验证")
                performance_evaluation = Server("性能评估")
                hyperparameter_tuning = Server("超参数调优")
                
            with Cluster("动态权重"):
                dynamic_weighting = Server("动态权重")
                adaptive_ensemble = Server("自适应集成")
                online_learning = Server("在线学习")
                concept_drift = Server("概念漂移")
                
        # 预测优化层
        with Cluster("预测优化层"):
            with Cluster("准确性优化"):
                accuracy_optimization = Server("准确性优化")
                bias_correction = Server("偏差校正")
                uncertainty_quantification = Server("不确定性量化")
                confidence_intervals = Server("置信区间")
                
            with Cluster("业务约束"):
                business_constraints = Server("业务约束")
                capacity_constraints = Server("产能约束")
                budget_constraints = Server("预算约束")
                policy_constraints = Server("政策约束")
                
            with Cluster("多目标优化"):
                multi_objective = Server("多目标优化")
                pareto_optimization = Server("帕累托优化")
                trade_off_analysis = Server("权衡分析")
                scenario_planning = Server("场景规划")
                
        # 应用层
        with Cluster("应用层"):
            with Cluster("库存管理"):
                inventory_planning = Server("库存规划")
                safety_stock = Server("安全库存")
                reorder_points = Server("再订货点")
                capacity_planning = Server("产能规划")
                
            with Cluster("供应链管理"):
                procurement_planning = Server("采购规划")
                production_planning = Server("生产规划")
                distribution_planning = Server("分销规划")
                logistics_optimization = Server("物流优化")
                
            with Cluster("销售管理"):
                sales_targeting = Server("销售目标")
                territory_planning = Server("区域规划")
                channel_optimization = Server("渠道优化")
                pricing_strategy = Server("定价策略")
                
        # 监控与评估层
        with Cluster("监控与评估层"):
            with Cluster("预测监控"):
                forecast_monitoring = Server("预测监控")
                accuracy_tracking = Server("准确性跟踪")
                bias_monitoring = Server("偏差监控")
                drift_detection = Server("漂移检测")
                
            with Cluster("性能评估"):
                mape_evaluation = Server("MAPE评估")
                mae_evaluation = Server("MAE评估")
                rmse_evaluation = Server("RMSE评估")
                directional_accuracy = Server("方向准确性")
                
            with Cluster("业务影响"):
                business_impact = Server("业务影响")
                roi_analysis = Server("ROI分析")
                cost_benefit = Server("成本效益")
                kpi_tracking = Server("KPI跟踪")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("历史数据"):
                historical_database = Server("历史数据库")
                time_series_store = Server("时间序列存储")
                feature_store = Server("特征存储")
                
            with Cluster("预测数据"):
                forecast_store = Server("预测存储")
                model_store = Server("模型存储")
                metadata_store = Server("元数据存储")
                
            with Cluster("缓存层"):
                forecast_cache = Server("预测缓存")
                feature_cache = Server("特征缓存")
                model_cache = Server("模型缓存")
                
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
        sales_history >> Edge(label="历史数据") >> short_term_forecast
        market_trends >> Edge(label="市场数据") >> medium_term_forecast
        product_attributes >> Edge(label="产品数据") >> long_term_forecast
        weather_data >> Edge(label="外部数据") >> short_term_forecast
        
        # 预测引擎
        short_term_forecast >> Edge(label="短期预测") >> daily_forecast
        medium_term_forecast >> Edge(label="中期预测") >> seasonal_forecast
        long_term_forecast >> Edge(label="长期预测") >> strategic_forecast
        
        # 算法调用
        daily_forecast >> Edge(label="时间序列") >> arima
        seasonal_forecast >> Edge(label="机器学习") >> random_forest
        strategic_forecast >> Edge(label="深度学习") >> lstm
        
        # 特征工程
        arima >> Edge(label="时间特征") >> time_features
        random_forest >> Edge(label="产品特征") >> product_features
        lstm >> Edge(label="市场特征") >> market_features
        
        # 模型集成
        time_features >> Edge(label="集成方法") >> ensemble_learning
        product_features >> Edge(label="模型选择") >> model_selection
        market_features >> Edge(label="动态权重") >> dynamic_weighting
        
        # 预测优化
        ensemble_learning >> Edge(label="准确性优化") >> accuracy_optimization
        model_selection >> Edge(label="业务约束") >> business_constraints
        dynamic_weighting >> Edge(label="多目标优化") >> multi_objective
        
        # 应用
        accuracy_optimization >> Edge(label="库存管理") >> inventory_planning
        business_constraints >> Edge(label="供应链管理") >> procurement_planning
        multi_objective >> Edge(label="销售管理") >> sales_targeting
        
        # 监控评估
        inventory_planning >> Edge(label="预测监控") >> forecast_monitoring
        procurement_planning >> Edge(label="性能评估") >> mape_evaluation
        sales_targeting >> Edge(label="业务影响") >> business_impact
        
        # 数据存储
        forecast_monitoring >> Edge(label="历史数据") >> historical_database
        mape_evaluation >> Edge(label="预测数据") >> forecast_store
        business_impact >> Edge(label="缓存层") >> forecast_cache
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        forecast_monitoring >> Edge(label="反馈数据") >> kafka_stream
        mape_evaluation >> Edge(label="模型更新") >> arima
        
        # 监控
        short_term_forecast >> Edge(label="指标上报") >> monitoring
        daily_forecast >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_demand_forecasting_algorithm(filename="demand_forecasting_algorithm", outformat="png")
    create_demand_forecasting_algorithm(filename="demand_forecasting_algorithm", outformat="pdf")
