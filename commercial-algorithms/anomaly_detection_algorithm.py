from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_anomaly_detection_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能异常检测算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("系统监控数据"):
                cpu_usage = Server("CPU使用率")
                memory_usage = Server("内存使用率")
                disk_io = Server("磁盘I/O")
                network_traffic = Server("网络流量")
                
            with Cluster("业务数据"):
                transaction_volume = Server("交易量")
                user_activity = Server("用户活动")
                revenue_data = Server("收入数据")
                conversion_rates = Server("转化率")
                
            with Cluster("日志数据"):
                application_logs = Server("应用日志")
                system_logs = Server("系统日志")
                security_logs = Server("安全日志")
                audit_logs = Server("审计日志")
                
            with Cluster("传感器数据"):
                iot_sensors = Server("IoT传感器")
                temperature_data = Server("温度数据")
                pressure_data = Server("压力数据")
                vibration_data = Server("振动数据")
                
        # 异常检测引擎
        with Cluster("异常检测引擎"):
            with Cluster("实时检测引擎"):
                realtime_detection = Server("实时检测引擎")
                streaming_anomaly = Server("流式异常检测")
                online_learning = Server("在线学习")
                
            with Cluster("批量检测引擎"):
                batch_detection = Server("批量检测引擎")
                historical_analysis = Server("历史分析")
                pattern_discovery = Server("模式发现")
                
            with Cluster("多模态检测引擎"):
                multimodal_detection = Server("多模态检测")
                cross_domain_analysis = Server("跨域分析")
                ensemble_detection = Server("集成检测")
                
        # 算法层
        with Cluster("检测算法层"):
            with Cluster("统计方法"):
                z_score = Server("Z-Score")
                modified_z_score = Server("修正Z-Score")
                interquartile_range = Server("四分位距")
                grubbs_test = Server("Grubbs检验")
                
            with Cluster("机器学习算法"):
                isolation_forest = Server("孤立森林")
                one_class_svm = Server("单类SVM")
                local_outlier_factor = Server("局部异常因子")
                elliptic_envelope = Server("椭圆包络")
                
            with Cluster("深度学习算法"):
                autoencoder = Server("自编码器")
                variational_autoencoder = Server("变分自编码器")
                lstm_autoencoder = Server("LSTM自编码器")
                generative_adversarial_network = Server("生成对抗网络")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("时间特征"):
                time_series_features = Server("时间序列特征")
                lag_features = Server("滞后特征")
                rolling_statistics = Server("滚动统计")
                seasonal_decomposition = Server("季节分解")
                
            with Cluster("统计特征"):
                mean_features = Server("均值特征")
                variance_features = Server("方差特征")
                skewness_features = Server("偏度特征")
                kurtosis_features = Server("峰度特征")
                
            with Cluster("变换特征"):
                fourier_transform = Server("傅里叶变换")
                wavelet_transform = Server("小波变换")
                principal_component = Server("主成分分析")
                independent_component = Server("独立成分分析")
                
        # 异常类型层
        with Cluster("异常类型层"):
            with Cluster("点异常"):
                point_anomaly = Server("点异常")
                global_anomaly = Server("全局异常")
                contextual_anomaly = Server("上下文异常")
                collective_anomaly = Server("集体异常")
                
            with Cluster("时间异常"):
                trend_anomaly = Server("趋势异常")
                seasonal_anomaly = Server("季节异常")
                change_point = Server("变点检测")
                burst_anomaly = Server("突发异常")
                
            with Cluster("模式异常"):
                pattern_deviation = Server("模式偏差")
                sequence_anomaly = Server("序列异常")
                graph_anomaly = Server("图异常")
                network_anomaly = Server("网络异常")
                
        # 检测策略层
        with Cluster("检测策略层"):
            with Cluster("阈值策略"):
                static_threshold = Server("静态阈值")
                dynamic_threshold = Server("动态阈值")
                adaptive_threshold = Server("自适应阈值")
                multi_threshold = Server("多阈值")
                
            with Cluster("模型策略"):
                single_model = Server("单模型")
                ensemble_model = Server("集成模型")
                hierarchical_model = Server("层次模型")
                cascading_model = Server("级联模型")
                
            with Cluster("检测策略"):
                supervised_detection = Server("监督检测")
                unsupervised_detection = Server("无监督检测")
                semi_supervised = Server("半监督检测")
                active_learning = Server("主动学习")
                
        # 响应层
        with Cluster("响应层"):
            with Cluster("自动响应"):
                auto_alert = Server("自动告警")
                auto_mitigation = Server("自动缓解")
                auto_isolation = Server("自动隔离")
                auto_recovery = Server("自动恢复")
                
            with Cluster("人工响应"):
                manual_investigation = Server("人工调查")
                incident_management = Server("事件管理")
                root_cause_analysis = Server("根因分析")
                remediation_planning = Server("修复规划")
                
            with Cluster("通知系统"):
                alert_notification = Server("告警通知")
                escalation_procedure = Server("升级程序")
                dashboard_update = Server("仪表板更新")
                report_generation = Server("报告生成")
                
        # 学习优化层
        with Cluster("学习优化层"):
            with Cluster("模型训练"):
                batch_training = Server("批量训练")
                incremental_learning = Server("增量学习")
                transfer_learning = Server("迁移学习")
                federated_learning = Server("联邦学习")
                
            with Cluster("模型评估"):
                precision_recall = Server("精确率召回率")
                f1_score = Server("F1分数")
                roc_auc = Server("ROC-AUC")
                false_positive_rate = Server("误报率")
                
            with Cluster("模型优化"):
                hyperparameter_tuning = Server("超参数调优")
                feature_selection = Server("特征选择")
                model_ensemble = Server("模型集成")
                online_adaptation = Server("在线适应")
                
        # 可视化层
        with Cluster("可视化层"):
            with Cluster("监控面板"):
                anomaly_dashboard = Server("异常仪表板")
                realtime_monitoring = Server("实时监控")
                trend_visualization = Server("趋势可视化")
                heatmap_display = Server("热力图显示")
                
            with Cluster("分析报告"):
                anomaly_report = Server("异常报告")
                pattern_analysis = Server("模式分析")
                impact_assessment = Server("影响评估")
                recommendation_report = Server("建议报告")
                
            with Cluster("交互工具"):
                drill_down_analysis = Server("钻取分析")
                filter_controls = Server("过滤控制")
                time_range_selector = Server("时间范围选择")
                export_functionality = Server("导出功能")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("原始数据"):
                raw_data_store = Server("原始数据存储")
                time_series_db = Server("时间序列数据库")
                log_storage = Server("日志存储")
                
            with Cluster("检测数据"):
                anomaly_store = Server("异常存储")
                model_store = Server("模型存储")
                feature_store = Server("特征存储")
                
            with Cluster("缓存层"):
                detection_cache = Server("检测缓存")
                model_cache = Server("模型缓存")
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
        cpu_usage >> Edge(label="系统数据") >> realtime_detection
        transaction_volume >> Edge(label="业务数据") >> batch_detection
        application_logs >> Edge(label="日志数据") >> multimodal_detection
        iot_sensors >> Edge(label="传感器数据") >> realtime_detection
        
        # 检测引擎
        realtime_detection >> Edge(label="实时检测") >> streaming_anomaly
        batch_detection >> Edge(label="批量检测") >> historical_analysis
        multimodal_detection >> Edge(label="多模态检测") >> cross_domain_analysis
        
        # 算法调用
        streaming_anomaly >> Edge(label="统计方法") >> z_score
        historical_analysis >> Edge(label="机器学习") >> isolation_forest
        cross_domain_analysis >> Edge(label="深度学习") >> autoencoder
        
        # 特征工程
        z_score >> Edge(label="时间特征") >> time_series_features
        isolation_forest >> Edge(label="统计特征") >> mean_features
        autoencoder >> Edge(label="变换特征") >> fourier_transform
        
        # 异常类型
        time_series_features >> Edge(label="点异常") >> point_anomaly
        mean_features >> Edge(label="时间异常") >> trend_anomaly
        fourier_transform >> Edge(label="模式异常") >> pattern_deviation
        
        # 检测策略
        point_anomaly >> Edge(label="阈值策略") >> dynamic_threshold
        trend_anomaly >> Edge(label="模型策略") >> ensemble_model
        pattern_deviation >> Edge(label="检测策略") >> unsupervised_detection
        
        # 响应
        dynamic_threshold >> Edge(label="自动响应") >> auto_alert
        ensemble_model >> Edge(label="人工响应") >> manual_investigation
        unsupervised_detection >> Edge(label="通知系统") >> alert_notification
        
        # 学习优化
        auto_alert >> Edge(label="模型训练") >> batch_training
        manual_investigation >> Edge(label="模型评估") >> precision_recall
        alert_notification >> Edge(label="模型优化") >> hyperparameter_tuning
        
        # 可视化
        batch_training >> Edge(label="监控面板") >> anomaly_dashboard
        precision_recall >> Edge(label="分析报告") >> anomaly_report
        hyperparameter_tuning >> Edge(label="交互工具") >> drill_down_analysis
        
        # 数据存储
        anomaly_dashboard >> Edge(label="原始数据") >> raw_data_store
        anomaly_report >> Edge(label="检测数据") >> anomaly_store
        drill_down_analysis >> Edge(label="缓存层") >> detection_cache
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        precision_recall >> Edge(label="反馈数据") >> kafka_stream
        batch_training >> Edge(label="模型更新") >> z_score
        
        # 监控
        realtime_detection >> Edge(label="指标上报") >> monitoring
        streaming_anomaly >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_anomaly_detection_algorithm(filename="anomaly_detection_algorithm", outformat="png")
    create_anomaly_detection_algorithm(filename="anomaly_detection_algorithm", outformat="pdf")
