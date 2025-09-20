from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_fraud_detection_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能欺诈检测算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("交易数据"):
                transaction_data = Server("交易数据")
                payment_data = Server("支付数据")
                card_data = Server("卡片数据")
                account_data = Server("账户数据")
                
            with Cluster("行为数据"):
                user_behavior = Server("用户行为")
                device_data = Server("设备数据")
                location_data = Server("位置数据")
                session_data = Server("会话数据")
                
            with Cluster("外部数据"):
                blacklist_data = Server("黑名单数据")
                whitelist_data = Server("白名单数据")
                credit_bureau = Server("征信数据")
                social_network = Server("社交网络")
                
        # 欺诈检测引擎
        with Cluster("欺诈检测引擎"):
            with Cluster("实时检测引擎"):
                realtime_detection = Server("实时检测引擎")
                rule_engine = Server("规则引擎")
                pattern_matching = Server("模式匹配")
                
            with Cluster("机器学习引擎"):
                ml_detection = Server("机器学习检测")
                anomaly_detection = Server("异常检测")
                behavioral_analysis = Server("行为分析")
                
            with Cluster("深度学习引擎"):
                deep_learning = Server("深度学习检测")
                neural_network = Server("神经网络")
                ensemble_methods = Server("集成方法")
                
        # 算法层
        with Cluster("检测算法层"):
            with Cluster("监督学习算法"):
                logistic_regression = Server("逻辑回归")
                random_forest = Server("随机森林")
                gradient_boosting = Server("梯度提升")
                support_vector_machine = Server("支持向量机")
                
            with Cluster("无监督学习算法"):
                isolation_forest = Server("孤立森林")
                one_class_svm = Server("单类SVM")
                local_outlier_factor = Server("局部异常因子")
                autoencoder = Server("自编码器")
                
            with Cluster("深度学习算法"):
                lstm = Server("LSTM")
                cnn = Server("卷积神经网络")
                transformer = Server("Transformer")
                gnn = Server("图神经网络")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("基础特征"):
                transaction_features = Server("交易特征")
                temporal_features = Server("时间特征")
                geographic_features = Server("地理特征")
                device_features = Server("设备特征")
                
            with Cluster("衍生特征"):
                velocity_features = Server("速度特征")
                frequency_features = Server("频率特征")
                amount_features = Server("金额特征")
                pattern_features = Server("模式特征")
                
            with Cluster("高级特征"):
                graph_features = Server("图特征")
                sequence_features = Server("序列特征")
                embedding_features = Server("嵌入特征")
                interaction_features = Server("交互特征")
                
        # 规则引擎层
        with Cluster("规则引擎层"):
            with Cluster("业务规则"):
                amount_rules = Server("金额规则")
                frequency_rules = Server("频率规则")
                location_rules = Server("位置规则")
                time_rules = Server("时间规则")
                
            with Cluster("风险规则"):
                velocity_rules = Server("速度规则")
                pattern_rules = Server("模式规则")
                device_rules = Server("设备规则")
                behavior_rules = Server("行为规则")
                
            with Cluster("组合规则"):
                composite_rules = Server("组合规则")
                weighted_rules = Server("加权规则")
                dynamic_rules = Server("动态规则")
                adaptive_rules = Server("自适应规则")
                
        # 风险评估层
        with Cluster("风险评估层"):
            with Cluster("风险评分"):
                risk_scoring = Server("风险评分")
                probability_calculation = Server("概率计算")
                confidence_interval = Server("置信区间")
                uncertainty_quantification = Server("不确定性量化")
                
            with Cluster("风险等级"):
                high_risk = Server("高风险")
                medium_risk = Server("中等风险")
                low_risk = Server("低风险")
                suspicious = Server("可疑")
                
            with Cluster("决策引擎"):
                decision_engine = Server("决策引擎")
                threshold_management = Server("阈值管理")
                policy_engine = Server("策略引擎")
                approval_workflow = Server("审批流程")
                
        # 响应层
        with Cluster("响应层"):
            with Cluster("自动响应"):
                auto_block = Server("自动拦截")
                auto_approve = Server("自动通过")
                auto_hold = Server("自动暂停")
                auto_escalate = Server("自动升级")
                
            with Cluster("人工审核"):
                manual_review = Server("人工审核")
                case_management = Server("案例管理")
                investigation_tools = Server("调查工具")
                evidence_collection = Server("证据收集")
                
            with Cluster("通知系统"):
                alert_system = Server("告警系统")
                notification_service = Server("通知服务")
                dashboard = Server("监控面板")
                reporting = Server("报告系统")
                
        # 学习与优化层
        with Cluster("学习与优化层"):
            with Cluster("模型训练"):
                batch_training = Server("批量训练")
                online_learning = Server("在线学习")
                transfer_learning = Server("迁移学习")
                federated_learning = Server("联邦学习")
                
            with Cluster("模型评估"):
                performance_metrics = Server("性能指标")
                a_b_testing = Server("A/B测试")
                model_validation = Server("模型验证")
                bias_detection = Server("偏见检测")
                
            with Cluster("模型优化"):
                hyperparameter_tuning = Server("超参数调优")
                feature_selection = Server("特征选择")
                model_ensemble = Server("模型集成")
                model_compression = Server("模型压缩")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("交易数据"):
                transaction_db = Server("交易数据库")
                payment_db = Server("支付数据库")
                audit_log = Server("审计日志")
                
            with Cluster("模型数据"):
                model_store = Server("模型存储")
                feature_store = Server("特征存储")
                training_data = Server("训练数据")
                
            with Cluster("缓存层"):
                detection_cache = Server("检测缓存")
                rule_cache = Server("规则缓存")
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
        transaction_data >> Edge(label="交易数据") >> realtime_detection
        user_behavior >> Edge(label="行为数据") >> ml_detection
        blacklist_data >> Edge(label="外部数据") >> deep_learning
        
        # 检测引擎
        realtime_detection >> Edge(label="实时检测") >> rule_engine
        ml_detection >> Edge(label="机器学习") >> anomaly_detection
        deep_learning >> Edge(label="深度学习") >> neural_network
        
        # 算法调用
        rule_engine >> Edge(label="监督学习") >> logistic_regression
        anomaly_detection >> Edge(label="无监督学习") >> isolation_forest
        neural_network >> Edge(label="深度学习") >> lstm
        
        # 特征工程
        logistic_regression >> Edge(label="基础特征") >> transaction_features
        isolation_forest >> Edge(label="衍生特征") >> velocity_features
        lstm >> Edge(label="高级特征") >> graph_features
        
        # 规则引擎
        transaction_features >> Edge(label="业务规则") >> amount_rules
        velocity_features >> Edge(label="风险规则") >> velocity_rules
        graph_features >> Edge(label="组合规则") >> composite_rules
        
        # 风险评估
        amount_rules >> Edge(label="风险评分") >> risk_scoring
        velocity_rules >> Edge(label="风险等级") >> high_risk
        composite_rules >> Edge(label="决策引擎") >> decision_engine
        
        # 响应
        risk_scoring >> Edge(label="自动响应") >> auto_block
        high_risk >> Edge(label="人工审核") >> manual_review
        decision_engine >> Edge(label="通知系统") >> alert_system
        
        # 学习优化
        auto_block >> Edge(label="模型训练") >> batch_training
        manual_review >> Edge(label="模型评估") >> performance_metrics
        alert_system >> Edge(label="模型优化") >> hyperparameter_tuning
        
        # 数据存储
        batch_training >> Edge(label="交易数据") >> transaction_db
        performance_metrics >> Edge(label="模型数据") >> model_store
        hyperparameter_tuning >> Edge(label="缓存层") >> detection_cache
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        performance_metrics >> Edge(label="反馈数据") >> kafka_stream
        batch_training >> Edge(label="模型更新") >> logistic_regression
        
        # 监控
        realtime_detection >> Edge(label="指标上报") >> monitoring
        rule_engine >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_fraud_detection_algorithm(filename="fraud_detection_algorithm", outformat="png")
    create_fraud_detection_algorithm(filename="fraud_detection_algorithm", outformat="pdf")
