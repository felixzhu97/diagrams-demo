from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Users, User
from diagrams.onprem.network import Internet
from diagrams.onprem.database import PostgreSQL, MongoDB, Cassandra
from diagrams.onprem.storage import Ceph
from diagrams.onprem.queue import Kafka
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.security import Vault
from diagrams.onprem.analytics import Spark, Hadoop, Superset
from diagrams.onprem.workflow import Airflow
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python, Java, JavaScript, Cpp, Rust, Go
from diagrams.programming.framework import React, Django, Spring
from diagrams.aws.compute import EC2, Lambda, ECS, EKS
from diagrams.aws.database import RDS, Dynamodb, Aurora
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB, VPC
from diagrams.aws.analytics import Kinesis, Glue, EMR, Redshift
from diagrams.aws.management import Cloudwatch, Organizations
from diagrams.aws.security import IAM, WAF, Shield
from diagrams.aws.devtools import Codebuild, Codedeploy
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.storage import EBS, EFS
from diagrams.gcp.compute import ComputeEngine, GKE, Run, Functions
from diagrams.gcp.database import Bigtable, Firestore, Spanner, SQL
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Dataproc
from diagrams.saas.cdn import Cloudflare
from diagrams.saas.identity import Auth0
from diagrams.saas.logging import Datadog
from diagrams.saas.chat import Slack

def create_alipay_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建支付宝技术栈图表
    with Diagram("支付宝技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("支付宝用户")
            merchants = Users("商户")
            developers = Users("开发者")
            financial_institutions = Users("金融机构")
            
            with Cluster("客户端应用"):
                alipay_app = Server("支付宝App")
                merchant_portal = Server("商户门户")
                open_platform = Server("开放平台")
                financial_services = Server("金融服务")
                
        # 接入层
        with Cluster("接入层"):
            with Cluster("负载均衡和CDN"):
                load_balancer = ELB("负载均衡器")
                cdn = CloudFront("CDN")
                edge_locations = Server("边缘节点")
                
            with Cluster("API网关"):
                api_gateway = Server("API网关")
                rate_limiting = Server("速率限制")
                authentication = Server("身份认证")
                request_routing = Server("请求路由")
                
        # 支付核心层
        with Cluster("支付核心层"):
            with Cluster("支付引擎"):
                payment_engine = Server("支付引擎")
                transaction_processor = Server("交易处理器")
                payment_methods = Server("支付方式管理")
                currency_support = Server("多币种支持")
                
            with Cluster("支付方式"):
                bank_cards = Server("银行卡")
                balance_payment = Server("余额支付")
                credit_products = Server("信用产品")
                international_cards = Server("国际卡")
                
            with Cluster("交易管理"):
                order_management = Server("订单管理")
                payment_flows = Server("支付流程")
                refund_processing = Server("退款处理")
                settlement_system = Server("结算系统")
                
        # 金融产品层
        with Cluster("金融产品层"):
            with Cluster("理财产品"):
                yuebao = Server("余额宝")
                wealth_management = Server("理财通")
                insurance_products = Server("保险产品")
                fund_services = Server("基金服务")
                
            with Cluster("信贷产品"):
                huabei = Server("花呗")
                jiebei = Server("借呗")
                credit_assessment = Server("信用评估")
                loan_management = Server("贷款管理")
                
            with Cluster("保险服务"):
                ant_insurance = Server("蚂蚁保险")
                health_insurance = Server("健康险")
                travel_insurance = Server("旅游险")
                property_insurance = Server("财产险")
                
        # 风险控制层
        with Cluster("风险控制层"):
            with Cluster("实时风控"):
                risk_engine = Server("风险引擎")
                fraud_detection = Server("欺诈检测")
                real_time_monitoring = Server("实时监控")
                risk_scoring = Server("风险评分")
                
            with Cluster("机器学习"):
                ml_models = Server("机器学习模型")
                behavioral_analysis = Server("行为分析")
                device_fingerprinting = Server("设备指纹")
                anomaly_detection = Server("异常检测")
                
            with Cluster("合规管理"):
                aml_compliance = Server("反洗钱合规")
                kyc_verification = Server("KYC验证")
                regulatory_reporting = Server("监管报告")
                audit_trail = Server("审计跟踪")
                
        # 区块链技术层
        with Cluster("区块链技术层"):
            with Cluster("蚂蚁链"):
                ant_chain = Server("蚂蚁链")
                blockchain_consensus = Server("共识机制")
                smart_contracts = Server("智能合约")
                cross_chain = Server("跨链技术")
                
            with Cluster("应用场景"):
                supply_chain = Server("供应链金融")
                copyright_protection = Server("版权保护")
                charity_tracking = Server("公益追踪")
                digital_assets = Server("数字资产")
                
        # 大数据处理层
        with Cluster("大数据处理层"):
            with Cluster("数据存储"):
                data_warehouse = Redshift("数据仓库")
                data_lake = S3("数据湖")
                real_time_db = Server("实时数据库")
                graph_database = Server("图数据库")
                
            with Cluster("数据处理"):
                stream_processing = Server("流处理")
                batch_processing = Server("批处理")
                etl_pipeline = Server("ETL管道")
                data_quality = Server("数据质量")
                
            with Cluster("分析服务"):
                user_behavior_analysis = Server("用户行为分析")
                transaction_analytics = Server("交易分析")
                risk_analytics = Server("风险分析")
                business_intelligence = Server("商业智能")
                
        # AI技术层
        with Cluster("AI技术层"):
            with Cluster("机器学习平台"):
                ml_platform = Server("机器学习平台")
                model_training = Server("模型训练")
                model_deployment = Server("模型部署")
                feature_engineering = Server("特征工程")
                
            with Cluster("AI应用"):
                intelligent_customer_service = Server("智能客服")
                credit_scoring = Server("信用评分")
                fraud_prevention = Server("反欺诈")
                personalized_recommendation = Server("个性化推荐")
                
            with Cluster("自然语言处理"):
                nlp_service = Server("NLP服务")
                text_analysis = Server("文本分析")
                sentiment_analysis = Server("情感分析")
                chatbot = Server("聊天机器人")
                
        # 安全层
        with Cluster("安全层"):
            with Cluster("数据安全"):
                data_encryption = Server("数据加密")
                tokenization = Server("令牌化")
                secure_storage = Server("安全存储")
                key_management = Server("密钥管理")
                
            with Cluster("网络安全"):
                ddos_protection = Server("DDoS防护")
                waf = WAF("Web应用防火墙")
                network_security = Server("网络安全")
                ssl_tls = Server("SSL/TLS")
                
            with Cluster("身份安全"):
                multi_factor_auth = Server("多因子认证")
                biometric_auth = Server("生物识别")
                device_trust = Server("设备信任")
                session_management = Server("会话管理")
                
        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("计算资源"):
                container_orchestration = EKS("容器编排")
                serverless_compute = Lambda("无服务器计算")
                gpu_compute = Server("GPU计算")
                edge_computing = Server("边缘计算")
                
            with Cluster("存储服务"):
                object_storage = S3("对象存储")
                block_storage = EBS("块存储")
                file_storage = EFS("文件存储")
                database_services = RDS("数据库服务")
                
            with Cluster("网络服务"):
                vpc = VPC("虚拟私有云")
                load_balancers = ELB("负载均衡器")
                dns_service = Route53("DNS服务")
                cdn_service = CloudFront("CDN服务")
                
        # 开放平台层
        with Cluster("开放平台层"):
            with Cluster("API服务"):
                payment_api = Server("支付API")
                user_api = Server("用户API")
                merchant_api = Server("商户API")
                data_api = Server("数据API")
                
            with Cluster("开发者工具"):
                sdk_libraries = Server("SDK库")
                developer_documentation = Server("开发者文档")
                sandbox_environment = Server("沙盒环境")
                api_explorer = Server("API浏览器")
                
            with Cluster("合作伙伴"):
                third_party_integration = Server("第三方集成")
                isv_platform = Server("ISV平台")
                partner_portal = Server("合作伙伴门户")
                certification_program = Server("认证计划")
                
        # 监控运维层
        with Cluster("监控运维层"):
            with Cluster("应用监控"):
                performance_monitoring = Server("性能监控")
                error_tracking = Server("错误跟踪")
                user_experience = Server("用户体验监控")
                business_metrics = Server("业务指标")
                
            with Cluster("基础设施监控"):
                system_health = Server("系统健康")
                resource_utilization = Server("资源利用率")
                capacity_planning = Server("容量规划")
                disaster_recovery = Server("灾难恢复")
                
            with Cluster("日志管理"):
                log_aggregation = Server("日志聚合")
                log_analysis = Server("日志分析")
                audit_logs = Server("审计日志")
                security_logs = Server("安全日志")
                
        # 国际化服务层
        with Cluster("国际化服务层"):
            with Cluster("跨境支付"):
                cross_border_payment = Server("跨境支付")
                currency_exchange = Server("货币兑换")
                international_remittance = Server("国际汇款")
                global_wallet = Server("全球钱包")
                
            with Cluster("本地化服务"):
                local_payment_methods = Server("本地支付方式")
                regional_compliance = Server("区域合规")
                multi_language_support = Server("多语言支持")
                local_operations = Server("本地运营")
                
        # 企业服务层
        with Cluster("企业服务层"):
            with Cluster("企业解决方案"):
                enterprise_payment = Server("企业支付")
                financial_management = Server("财务管理")
                treasury_services = Server("资金管理")
                corporate_accounts = Server("企业账户")
                
            with Cluster("行业解决方案"):
                retail_solutions = Server("零售解决方案")
                travel_solutions = Server("旅游解决方案")
                education_solutions = Server("教育解决方案")
                healthcare_solutions = Server("医疗解决方案")
                
        # 连接关系
        users >> alipay_app
        merchants >> merchant_portal
        developers >> open_platform
        financial_institutions >> financial_services
        
        alipay_app >> load_balancer
        merchant_portal >> cdn
        open_platform >> edge_locations
        financial_services >> api_gateway
        
        load_balancer >> cdn
        cdn >> api_gateway
        
        api_gateway >> rate_limiting
        rate_limiting >> authentication
        authentication >> request_routing
        
        request_routing >> payment_engine
        payment_engine >> transaction_processor
        transaction_processor >> payment_methods
        payment_methods >> currency_support
        
        bank_cards >> payment_methods
        balance_payment >> payment_methods
        credit_products >> payment_methods
        international_cards >> payment_methods
        
        order_management >> payment_flows
        payment_flows >> refund_processing
        refund_processing >> settlement_system
        
        yuebao >> wealth_management
        wealth_management >> insurance_products
        insurance_products >> fund_services
        
        huabei >> jiebei
        jiebei >> credit_assessment
        credit_assessment >> loan_management
        
        ant_insurance >> health_insurance
        health_insurance >> travel_insurance
        travel_insurance >> property_insurance
        
        risk_engine >> fraud_detection
        fraud_detection >> real_time_monitoring
        real_time_monitoring >> risk_scoring
        
        ml_models >> behavioral_analysis
        behavioral_analysis >> device_fingerprinting
        device_fingerprinting >> anomaly_detection
        
        aml_compliance >> kyc_verification
        kyc_verification >> regulatory_reporting
        regulatory_reporting >> audit_trail
        
        ant_chain >> blockchain_consensus
        blockchain_consensus >> smart_contracts
        smart_contracts >> cross_chain
        
        supply_chain >> copyright_protection
        copyright_protection >> charity_tracking
        charity_tracking >> digital_assets
        
        data_warehouse >> data_lake
        data_lake >> real_time_db
        real_time_db >> graph_database
        
        stream_processing >> batch_processing
        batch_processing >> etl_pipeline
        etl_pipeline >> data_quality
        
        user_behavior_analysis >> transaction_analytics
        transaction_analytics >> risk_analytics
        risk_analytics >> business_intelligence
        
        ml_platform >> model_training
        model_training >> model_deployment
        model_deployment >> feature_engineering
        
        intelligent_customer_service >> credit_scoring
        credit_scoring >> fraud_prevention
        fraud_prevention >> personalized_recommendation
        
        nlp_service >> text_analysis
        text_analysis >> sentiment_analysis
        sentiment_analysis >> chatbot
        
        data_encryption >> tokenization
        tokenization >> secure_storage
        secure_storage >> key_management
        
        ddos_protection >> waf
        waf >> network_security
        network_security >> ssl_tls
        
        multi_factor_auth >> biometric_auth
        biometric_auth >> device_trust
        device_trust >> session_management
        
        container_orchestration >> serverless_compute
        serverless_compute >> gpu_compute
        gpu_compute >> edge_computing
        
        object_storage >> block_storage
        block_storage >> file_storage
        file_storage >> database_services
        
        vpc >> load_balancers
        load_balancers >> dns_service
        dns_service >> cdn_service
        
        payment_api >> user_api
        user_api >> merchant_api
        merchant_api >> data_api
        
        sdk_libraries >> developer_documentation
        developer_documentation >> sandbox_environment
        sandbox_environment >> api_explorer
        
        third_party_integration >> isv_platform
        isv_platform >> partner_portal
        partner_portal >> certification_program
        
        performance_monitoring >> error_tracking
        error_tracking >> user_experience
        user_experience >> business_metrics
        
        system_health >> resource_utilization
        resource_utilization >> capacity_planning
        capacity_planning >> disaster_recovery
        
        log_aggregation >> log_analysis
        log_analysis >> audit_logs
        audit_logs >> security_logs
        
        cross_border_payment >> currency_exchange
        currency_exchange >> international_remittance
        international_remittance >> global_wallet
        
        local_payment_methods >> regional_compliance
        regional_compliance >> multi_language_support
        multi_language_support >> local_operations
        
        enterprise_payment >> financial_management
        financial_management >> treasury_services
        treasury_services >> corporate_accounts
        
        retail_solutions >> travel_solutions
        travel_solutions >> education_solutions
        education_solutions >> healthcare_solutions

if __name__ == "__main__":
    create_alipay_tech_stack_diagram(filename="alipay_tech_stack", outformat="png")
    create_alipay_tech_stack_diagram(filename="alipay_tech_stack", outformat="pdf")
