
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_customer_segmentation_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能客户细分算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("客户基础数据"):
                demographic_data = Server("人口统计数据")
                contact_info = Server("联系信息")
                account_info = Server("账户信息")
                identity_data = Server("身份数据")
                
            with Cluster("行为数据"):
                transaction_data = Server("交易数据")
                browsing_behavior = Server("浏览行为")
                purchase_history = Server("购买历史")
                interaction_data = Server("互动数据")
                
            with Cluster("偏好数据"):
                product_preferences = Server("产品偏好")
                channel_preferences = Server("渠道偏好")
                communication_preferences = Server("沟通偏好")
                service_preferences = Server("服务偏好")
                
        # 客户细分引擎
        with Cluster("客户细分引擎"):
            with Cluster("实时细分引擎"):
                realtime_segmentation = Server("实时细分引擎")
                dynamic_profiling = Server("动态画像")
                behavior_tracking = Server("行为跟踪")
                
            with Cluster("预测细分引擎"):
                predictive_segmentation = Server("预测细分")
                lifetime_value = Server("生命周期价值")
                churn_prediction = Server("流失预测")
                
            with Cluster("多维细分引擎"):
                multi_dimensional = Server("多维细分")
                hierarchical_clustering = Server("层次聚类")
                fuzzy_segmentation = Server("模糊细分")
                
        # 算法层
        with Cluster("细分算法层"):
            with Cluster("聚类算法"):
                k_means = Server("K-Means")
                dbscan = Server("DBSCAN")
                hierarchical = Server("层次聚类")
                gaussian_mixture = Server("高斯混合")
                
            with Cluster("分类算法"):
                decision_tree = Server("决策树")
                random_forest = Server("随机森林")
                svm = Server("支持向量机")
                naive_bayes = Server("朴素贝叶斯")
                
            with Cluster("深度学习算法"):
                autoencoder = Server("自编码器")
                deep_clustering = Server("深度聚类")
                neural_network = Server("神经网络")
                lstm = Server("LSTM")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("基础特征"):
                demographic_features = Server("人口统计特征")
                geographic_features = Server("地理特征")
                temporal_features = Server("时间特征")
                behavioral_features = Server("行为特征")
                
            with Cluster("衍生特征"):
                rfm_features = Server("RFM特征")
                engagement_score = Server("参与度评分")
                loyalty_score = Server("忠诚度评分")
                value_score = Server("价值评分")
                
            with Cluster("高级特征"):
                sequence_features = Server("序列特征")
                network_features = Server("网络特征")
                sentiment_features = Server("情感特征")
                predictive_features = Server("预测特征")
                
        # 细分策略层
        with Cluster("细分策略层"):
            with Cluster("价值细分"):
                high_value = Server("高价值客户")
                medium_value = Server("中等价值客户")
                low_value = Server("低价值客户")
                potential_value = Server("潜在价值客户")
                
            with Cluster("行为细分"):
                loyal_customers = Server("忠诚客户")
                price_sensitive = Server("价格敏感客户")
                brand_loyal = Server("品牌忠诚客户")
                deal_seekers = Server("优惠寻求者")
                
            with Cluster("生命周期细分"):
                new_customers = Server("新客户")
                growing_customers = Server("成长客户")
                mature_customers = Server("成熟客户")
                at_risk_customers = Server("风险客户")
                
        # 应用层
        with Cluster("应用层"):
            with Cluster("营销应用"):
                targeted_campaigns = Server("定向营销")
                personalized_offers = Server("个性化优惠")
                cross_sell = Server("交叉销售")
                up_sell = Server("向上销售")
                
            with Cluster("服务应用"):
                customer_service = Server("客户服务")
                priority_support = Server("优先支持")
                proactive_outreach = Server("主动外呼")
                retention_programs = Server("保留计划")
                
            with Cluster("产品应用"):
                product_recommendation = Server("产品推荐")
                feature_development = Server("功能开发")
                pricing_strategy = Server("定价策略")
                channel_optimization = Server("渠道优化")
                
        # 监控层
        with Cluster("监控层"):
            with Cluster("细分监控"):
                segment_performance = Server("细分绩效")
                segment_stability = Server("细分稳定性")
                segment_evolution = Server("细分演化")
                
            with Cluster("模型监控"):
                model_accuracy = Server("模型准确性")
                feature_importance = Server("特征重要性")
                model_drift = Server("模型漂移")
                
            with Cluster("业务监控"):
                business_impact = Server("业务影响")
                roi_analysis = Server("ROI分析")
                kpi_tracking = Server("KPI跟踪")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("客户数据"):
                customer_database = Server("客户数据库")
                profile_store = Server("画像存储")
                segment_store = Server("细分存储")
                
            with Cluster("分析数据"):
                analytics_warehouse = Server("分析仓库")
                feature_store = Server("特征存储")
                model_store = Server("模型存储")
                
            with Cluster("缓存层"):
                customer_cache = Server("客户缓存")
                segment_cache = Server("细分缓存")
                feature_cache = Server("特征缓存")
                
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
        demographic_data >> Edge(label="基础数据") >> realtime_segmentation
        transaction_data >> Edge(label="行为数据") >> dynamic_profiling
        product_preferences >> Edge(label="偏好数据") >> predictive_segmentation
        
        # 细分引擎
        realtime_segmentation >> Edge(label="实时细分") >> dynamic_profiling
        predictive_segmentation >> Edge(label="预测细分") >> lifetime_value
        multi_dimensional >> Edge(label="多维细分") >> hierarchical_clustering
        
        # 算法调用
        dynamic_profiling >> Edge(label="聚类算法") >> k_means
        lifetime_value >> Edge(label="分类算法") >> random_forest
        hierarchical_clustering >> Edge(label="深度学习") >> autoencoder
        
        # 特征工程
        k_means >> Edge(label="基础特征") >> demographic_features
        random_forest >> Edge(label="衍生特征") >> rfm_features
        autoencoder >> Edge(label="高级特征") >> sequence_features
        
        # 细分策略
        demographic_features >> Edge(label="价值细分") >> high_value
        rfm_features >> Edge(label="行为细分") >> loyal_customers
        sequence_features >> Edge(label="生命周期细分") >> new_customers
        
        # 应用
        high_value >> Edge(label="营销应用") >> targeted_campaigns
        loyal_customers >> Edge(label="服务应用") >> customer_service
        new_customers >> Edge(label="产品应用") >> product_recommendation
        
        # 监控
        targeted_campaigns >> Edge(label="细分监控") >> segment_performance
        customer_service >> Edge(label="模型监控") >> model_accuracy
        product_recommendation >> Edge(label="业务监控") >> business_impact
        
        # 数据存储
        segment_performance >> Edge(label="客户数据") >> customer_database
        model_accuracy >> Edge(label="分析数据") >> analytics_warehouse
        business_impact >> Edge(label="缓存层") >> customer_cache
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        segment_performance >> Edge(label="反馈数据") >> kafka_stream
        model_accuracy >> Edge(label="模型更新") >> k_means
        
        # 监控
        realtime_segmentation >> Edge(label="指标上报") >> monitoring
        dynamic_profiling >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_customer_segmentation_algorithm(filename="customer_segmentation_algorithm", outformat="png")
    create_customer_segmentation_algorithm(filename="customer_segmentation_algorithm", outformat="pdf")
