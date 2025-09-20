from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server

def create_credit_scoring_algorithm(filename: str, outformat: str) -> None:
    with Diagram("智能信用评分算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 数据源层
        with Cluster("数据源层"):
            with Cluster("个人基础数据"):
                demographic_data = Server("人口统计数据")
                identity_data = Server("身份数据")
                contact_info = Server("联系信息")
                employment_data = Server("就业数据")
                
            with Cluster("财务数据"):
                income_data = Server("收入数据")
                asset_data = Server("资产数据")
                liability_data = Server("负债数据")
                expense_data = Server("支出数据")
                
            with Cluster("信用历史数据"):
                credit_bureau = Server("征信数据")
                payment_history = Server("还款历史")
                credit_utilization = Server("信用使用率")
                credit_inquiries = Server("信用查询")
                
            with Cluster("行为数据"):
                banking_behavior = Server("银行行为")
                transaction_patterns = Server("交易模式")
                digital_footprint = Server("数字足迹")
                social_media = Server("社交媒体")
                
        # 信用评分引擎
        with Cluster("信用评分引擎"):
            with Cluster("实时评分引擎"):
                realtime_scoring = Server("实时评分引擎")
                instant_decision = Server("即时决策")
                risk_assessment = Server("风险评估")
                
            with Cluster("批量评分引擎"):
                batch_scoring = Server("批量评分引擎")
                portfolio_analysis = Server("组合分析")
                trend_analysis = Server("趋势分析")
                
            with Cluster("多模型评分引擎"):
                ensemble_scoring = Server("集成评分")
                model_fusion = Server("模型融合")
                adaptive_scoring = Server("自适应评分")
                
        # 算法层
        with Cluster("评分算法层"):
            with Cluster("传统统计模型"):
                logistic_regression = Server("逻辑回归")
                linear_regression = Server("线性回归")
                decision_tree = Server("决策树")
                scorecard_model = Server("评分卡模型")
                
            with Cluster("机器学习算法"):
                random_forest = Server("随机森林")
                gradient_boosting = Server("梯度提升")
                support_vector_machine = Server("支持向量机")
                naive_bayes = Server("朴素贝叶斯")
                
            with Cluster("深度学习算法"):
                neural_network = Server("神经网络")
                deep_fm = Server("DeepFM")
                wide_deep = Server("Wide&Deep")
                transformer = Server("Transformer")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("基础特征"):
                demographic_features = Server("人口统计特征")
                financial_features = Server("财务特征")
                credit_features = Server("信用特征")
                behavioral_features = Server("行为特征")
                
            with Cluster("衍生特征"):
                debt_to_income = Server("债务收入比")
                credit_utilization_ratio = Server("信用使用率")
                payment_consistency = Server("还款一致性")
                income_stability = Server("收入稳定性")
                
            with Cluster("高级特征"):
                interaction_features = Server("交互特征")
                temporal_features = Server("时间特征")
                network_features = Server("网络特征")
                embedding_features = Server("嵌入特征")
                
        # 评分分层层
        with Cluster("评分分层层"):
            with Cluster("信用等级"):
                excellent_credit = Server("优秀信用")
                good_credit = Server("良好信用")
                fair_credit = Server("一般信用")
                poor_credit = Server("较差信用")
                
            with Cluster("风险等级"):
                low_risk = Server("低风险")
                medium_risk = Server("中等风险")
                high_risk = Server("高风险")
                very_high_risk = Server("极高风险")
                
            with Cluster("决策建议"):
                approve = Server("批准")
                conditional_approve = Server("有条件批准")
                decline = Server("拒绝")
                manual_review = Server("人工审核")
                
        # 产品匹配层
        with Cluster("产品匹配层"):
            with Cluster("产品推荐"):
                credit_card = Server("信用卡")
                personal_loan = Server("个人贷款")
                mortgage = Server("抵押贷款")
                auto_loan = Server("汽车贷款")
                
            with Cluster("额度建议"):
                credit_limit = Server("信用额度")
                loan_amount = Server("贷款金额")
                interest_rate = Server("利率")
                term_length = Server("期限")
                
            with Cluster("条件设置"):
                down_payment = Server("首付要求")
                collateral = Server("担保要求")
                co_signor = Server("共同签署人")
                insurance = Server("保险要求")
                
        # 决策引擎层
        with Cluster("决策引擎层"):
            with Cluster("规则引擎"):
                business_rules = Server("业务规则")
                policy_rules = Server("政策规则")
                regulatory_rules = Server("监管规则")
                risk_rules = Server("风险规则")
                
            with Cluster("决策树"):
                decision_tree = Server("决策树")
                rule_engine = Server("规则引擎")
                workflow_engine = Server("工作流引擎")
                approval_matrix = Server("审批矩阵")
                
            with Cluster("优化引擎"):
                profit_optimization = Server("利润优化")
                risk_optimization = Server("风险优化")
                portfolio_optimization = Server("组合优化")
                pricing_optimization = Server("定价优化")
                
        # 监控与合规层
        with Cluster("监控与合规层"):
            with Cluster("模型监控"):
                model_performance = Server("模型性能")
                model_drift = Server("模型漂移")
                feature_importance = Server("特征重要性")
                bias_detection = Server("偏见检测")
                
            with Cluster("合规监控"):
                regulatory_compliance = Server("监管合规")
                fair_lending = Server("公平借贷")
                data_privacy = Server("数据隐私")
                audit_trail = Server("审计跟踪")
                
            with Cluster("业务监控"):
                approval_rate = Server("批准率")
                default_rate = Server("违约率")
                portfolio_quality = Server("组合质量")
                profitability = Server("盈利能力")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("客户数据"):
                customer_database = Server("客户数据库")
                application_store = Server("申请存储")
                credit_history = Server("信用历史")
                
            with Cluster("模型数据"):
                model_store = Server("模型存储")
                feature_store = Server("特征存储")
                score_store = Server("评分存储")
                
            with Cluster("缓存层"):
                scoring_cache = Server("评分缓存")
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
        demographic_data >> Edge(label="个人数据") >> realtime_scoring
        income_data >> Edge(label="财务数据") >> batch_scoring
        credit_bureau >> Edge(label="信用数据") >> ensemble_scoring
        banking_behavior >> Edge(label="行为数据") >> realtime_scoring
        
        # 评分引擎
        realtime_scoring >> Edge(label="实时评分") >> instant_decision
        batch_scoring >> Edge(label="批量评分") >> portfolio_analysis
        ensemble_scoring >> Edge(label="集成评分") >> model_fusion
        
        # 算法调用
        instant_decision >> Edge(label="传统统计") >> logistic_regression
        portfolio_analysis >> Edge(label="机器学习") >> random_forest
        model_fusion >> Edge(label="深度学习") >> neural_network
        
        # 特征工程
        logistic_regression >> Edge(label="基础特征") >> demographic_features
        random_forest >> Edge(label="衍生特征") >> debt_to_income
        neural_network >> Edge(label="高级特征") >> interaction_features
        
        # 评分分层
        demographic_features >> Edge(label="信用等级") >> excellent_credit
        debt_to_income >> Edge(label="风险等级") >> low_risk
        interaction_features >> Edge(label="决策建议") >> approve
        
        # 产品匹配
        excellent_credit >> Edge(label="产品推荐") >> credit_card
        low_risk >> Edge(label="额度建议") >> credit_limit
        approve >> Edge(label="条件设置") >> down_payment
        
        # 决策引擎
        credit_card >> Edge(label="规则引擎") >> business_rules
        credit_limit >> Edge(label="决策树") >> decision_tree
        down_payment >> Edge(label="优化引擎") >> profit_optimization
        
        # 监控合规
        business_rules >> Edge(label="模型监控") >> model_performance
        decision_tree >> Edge(label="合规监控") >> regulatory_compliance
        profit_optimization >> Edge(label="业务监控") >> approval_rate
        
        # 数据存储
        model_performance >> Edge(label="客户数据") >> customer_database
        regulatory_compliance >> Edge(label="模型数据") >> model_store
        approval_rate >> Edge(label="缓存层") >> scoring_cache
        
        # 数据处理
        kafka_stream >> Edge(label="实时流") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> realtime_analytics
        
        spark_batch >> Edge(label="批处理") >> data_warehouse
        data_warehouse >> Edge(label="ETL") >> etl_pipeline
        
        # 反馈循环
        model_performance >> Edge(label="反馈数据") >> kafka_stream
        approval_rate >> Edge(label="模型更新") >> logistic_regression
        
        # 监控
        realtime_scoring >> Edge(label="指标上报") >> monitoring
        instant_decision >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="告警") >> alerting

if __name__ == "__main__":
    create_credit_scoring_algorithm(filename="credit_scoring_algorithm", outformat="png")
    create_credit_scoring_algorithm(filename="credit_scoring_algorithm", outformat="pdf")
