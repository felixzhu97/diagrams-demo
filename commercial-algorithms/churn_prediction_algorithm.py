from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_churn_prediction_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能客户流失预测算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("客户基础数据"):
                customer_profile = Server("客户画像")
                demographic_data = Server("人口统计数据")
                account_info = Server("账户信息")
                subscription_data = Server("订阅数据")
                
            with Cluster("行为数据"):
                usage_data = Server("使用数据")
                interaction_data = Server("互动数据")
                support_tickets = Server("支持工单")
                feedback_data = Server("反馈数据")
                
            with Cluster("交易数据"):
                payment_history = Server("支付历史")
                billing_data = Server("账单数据")
                refund_data = Server("退款数据")
                upgrade_downgrade = Server("升级降级")
                
            with Cluster("外部数据"):
                market_data = Server("市场数据")
                competitor_data = Server("竞品数据")
                economic_indicators = Server("经济指标")
                social_media = Server("社交媒体")
                
        # 流失预测引擎
        with Cluster("流失预测引擎"):
            with Cluster("实时预测引擎"):
                realtime_prediction = Server("实时预测引擎")
                early_warning = Server("早期预警")
                risk_scoring = Server("风险评分")
                
            with Cluster("批量预测引擎"):
                batch_prediction = Server("批量预测引擎")
                cohort_analysis = Server("队列分析")
                survival_analysis = Server("生存分析")
                
            with Cluster("多模型预测引擎"):
                ensemble_prediction = Server("集成预测")
                multi_model_fusion = Server("多模型融合")
                adaptive_prediction = Server("自适应预测")
                
        # 算法层
        with Cluster("预测算法层"):
            with Cluster("传统机器学习"):
                logistic_regression = Server("逻辑回归")
                random_forest = Server("随机森林")
                gradient_boosting = Server("梯度提升")
                support_vector_machine = Server("支持向量机")
                
            with Cluster("深度学习算法"):
                neural_network = Server("神经网络")
                deep_fm = Server("DeepFM")
                wide_deep = Server("Wide&Deep")
                transformer = Server("Transformer")
                
            with Cluster("时间序列算法"):
                lstm = Server("LSTM")
                gru = Server("GRU")
                arima = Server("ARIMA")
                prophet = Server("Prophet")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("基础特征"):
                demographic_features = Server("人口统计特征")
                behavioral_features = Server("行为特征")
                transactional_features = Server("交易特征")
                temporal_features = Server("时间特征")
                
            with Cluster("衍生特征"):
                rfm_features = Server("RFM特征")
                engagement_score = Server("参与度评分")
                satisfaction_score = Server("满意度评分")
                loyalty_score = Server("忠诚度评分")
                
            with Cluster("高级特征"):
                sequence_features = Server("序列特征")
                interaction_features = Server("交互特征")
                network_features = Server("网络特征")
                sentiment_features = Server("情感特征")
                
        # 风险分层层
        with Cluster("风险分层层"):
            with Cluster("风险等级"):
                high_risk = Server("高风险客户")
                medium_risk = Server("中等风险客户")
                low_risk = Server("低风险客户")
                stable_customers = Server("稳定客户")
                
            with Cluster("流失类型"):
                voluntary_churn = Server("主动流失")
                involuntary_churn = Server("被动流失")
                seasonal_churn = Server("季节性流失")
                competitive_churn = Server("竞争性流失")
                
            with Cluster("时间窗口"):
                immediate_risk = Server("即时风险")
                short_term_risk = Server("短期风险")
                medium_term_risk = Server("中期风险")
                long_term_risk = Server("长期风险")
                
        # 干预策略层
        with Cluster("干预策略层"):
            with Cluster("预防策略"):
                proactive_outreach = Server("主动外呼")
                personalized_offers = Server("个性化优惠")
                loyalty_programs = Server("忠诚度计划")
                value_communication = Server("价值沟通")
                
            with Cluster("挽留策略"):
                retention_campaigns = Server("挽留活动")
                win_back_programs = Server("赢回计划")
                special_discounts = Server("特殊折扣")
                premium_support = Server("优先支持")
                
            with Cluster("升级策略"):
                up_sell_opportunities = Server("向上销售机会")
                cross_sell_opportunities = Server("交叉销售机会")
                feature_upgrades = Server("功能升级")
                service_enhancements = Server("服务增强")
                
        # 执行层
        with Cluster("执行层"):
            with Cluster("营销自动化"):
                campaign_automation = Server("活动自动化")
                email_campaigns = Server("邮件营销")
                sms_campaigns = Server("短信营销")
                push_notifications = Server("推送通知")
                
            with Cluster("客户服务"):
                customer_service = Server("客户服务")
                priority_support = Server("优先支持")
                account_management = Server("账户管理")
                relationship_management = Server("关系管理")
                
            with Cluster("产品优化"):
                product_improvements = Server("产品改进")
                feature_development = Server("功能开发")
                user_experience = Server("用户体验")
                onboarding_optimization = Server("入门优化")
                
        # 效果评估层
        with Cluster("效果评估层"):
            with Cluster("预测评估"):
                accuracy_metrics = Server("准确性指标")
                precision_recall = Server("精确率召回率")
                roc_auc = Server("ROC-AUC")
                lift_analysis = Server("提升分析")
                
            with Cluster("业务评估"):
                churn_rate_reduction = Server("流失率降低")
                revenue_impact = Server("收入影响")
                cost_effectiveness = Server("成本效益")
                roi_analysis = Server("ROI分析")
                
            with Cluster("干预评估"):
                intervention_effectiveness = Server("干预效果")
                campaign_performance = Server("活动绩效")
                customer_satisfaction = Server("客户满意度")
                retention_success = Server("挽留成功率")
                
        # 学习优化层
        with Cluster("学习优化层"):
            with Cluster("模型优化"):
                hyperparameter_tuning = Server("超参数调优")
                feature_selection = Server("特征选择")
                model_ensemble = Server("模型集成")
                online_learning = Server("在线学习")
                
            with Cluster("策略优化"):
                strategy_optimization = Server("策略优化")
                a_b_testing = Server("A/B测试")
                multi_armed_bandit = Server("多臂老虎机")
                reinforcement_learning = Server("强化学习")
                
            with Cluster("持续改进"):
                feedback_loop = Server("反馈循环")
                model_drift_detection = Server("模型漂移检测")
                concept_drift_adaptation = Server("概念漂移适应")
                performance_monitoring = Server("性能监控")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("客户数据"):
                customer_database = Server("客户数据库")
                profile_store = Server("画像存储")
                interaction_store = Server("交互存储")
                
            with Cluster("预测数据"):
                prediction_store = Server("预测存储")
                model_store = Server("模型存储")
                feature_store = Server("特征存储")
                
            with Cluster("缓存层"):
                prediction_cache = Server("预测缓存")
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
        customer_profile >> Edge(label="客户数据") >> realtime_prediction
        usage_data >> Edge(label="行为数据") >> batch_prediction
        payment_history >> Edge(label="交易数据") >> ensemble_prediction
        market_data >> Edge(label="外部数据") >> realtime_prediction
        
        # 预测引擎
        realtime_prediction >> Edge(label="实时预测") >> early_warning
        batch_prediction >> Edge(label="批量预测") >> cohort_analysis
        ensemble_prediction >> Edge(label="集成预测") >> multi_model_fusion
        
        # 算法调用
        early_warning >> Edge(label="传统机器学习") >> logistic_regression
        cohort_analysis >> Edge(label="深度学习") >> neural_network
        multi_model_fusion >> Edge(label="时间序列") >> lstm
        
        # 特征工程
        logistic_regression >> Edge(label="基础特征") >> demographic_features
        neural_network >> Edge(label="衍生特征") >> rfm_features
        lstm >> Edge(label="高级特征") >> sequence_features
        
        # 风险分层
        demographic_features >> Edge(label="风险等级") >> high_risk
        rfm_features >> Edge(label="流失类型") >> voluntary_churn
        sequence_features >> Edge(label="时间窗口") >> immediate_risk
        
        # 干预策略
        high_risk >> Edge(label="预防策略") >> proactive_outreach
        voluntary_churn >> Edge(label="挽留策略") >> retention_campaigns
        immediate_risk >> Edge(label="升级策略") >> up_sell_opportunities
        
        # 执行
        proactive_outreach >> Edge(label="营销自动化") >> campaign_automation
        retention_campaigns >> Edge(label="客户服务") >> customer_service
        up_sell_opportunities >> Edge(label="产品优化") >> product_improvements
        
        # 效果评估
        campaign_automation >> Edge(label="预测评估") >> accuracy_metrics
        customer_service >> Edge(label="业务评估") >> churn_rate_reduction
        product_improvements >> Edge(label="干预评估") >> intervention_effectiveness
        
        # 学习优化
        accuracy_metrics >> Edge(label="模型优化") >> hyperparameter_tuning
        churn_rate_reduction >> Edge(label="策略优化") >> strategy_optimization
        intervention_effectiveness >> Edge(label="持续改进") >> feedback_loop
        
        # 数据存储
        hyperparameter_tuning >> Edge(label="客户数据") >> customer_database
        strategy_optimization >> Edge(label="预测数据") >> prediction_store
        feedback_loop >> Edge(label="缓存层") >> prediction_cache
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        accuracy_metrics >> Edge(label="反馈数据") >> kafka_stream
        churn_rate_reduction >> Edge(label="模型更新") >> logistic_regression
        
        # 监控
        realtime_prediction >> Edge(label="指标上报") >> monitoring
        early_warning >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_churn_prediction_algorithm(filename="churn_prediction_algorithm", outformat="png")
    create_churn_prediction_algorithm(filename="churn_prediction_algorithm", outformat="pdf")
