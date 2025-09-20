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

def create_paypal_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建PayPal技术栈图表
    with Diagram("PayPal技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("PayPal用户")
            merchants = Users("商户")
            developers = Users("开发者")
            partners = Users("合作伙伴")
            
            with Cluster("客户端应用"):
                mobile_app = Server("PayPal移动应用")
                web_app = Server("PayPal Web端")
                merchant_portal = Server("商户门户")
                api_clients = Server("API客户端")
                
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
                authorization = Server("授权服务")
                
        # 支付处理层
        with Cluster("支付处理层"):
            with Cluster("支付引擎"):
                payment_engine = Server("支付引擎")
                transaction_processor = Server("交易处理器")
                payment_methods = Server("支付方式管理")
                currency_converter = Server("货币转换器")
                
            with Cluster("支付方式"):
                credit_cards = Server("信用卡")
                debit_cards = Server("借记卡")
                bank_transfers = Server("银行转账")
                digital_wallets = Server("数字钱包")
                cryptocurrency = Server("加密货币")
                
            with Cluster("交易管理"):
                transaction_storage = Server("交易存储")
                payment_flows = Server("支付流程")
                refund_processing = Server("退款处理")
                dispute_management = Server("争议管理")
                
        # 风险控制层
        with Cluster("风险控制层"):
            with Cluster("欺诈检测"):
                fraud_detection = Server("欺诈检测")
                machine_learning_models = Server("机器学习模型")
                behavioral_analysis = Server("行为分析")
                device_fingerprinting = Server("设备指纹识别")
                
            with Cluster("合规监控"):
                aml_compliance = Server("反洗钱合规")
                kyc_verification = Server("KYC验证")
                sanctions_screening = Server("制裁筛查")
                regulatory_reporting = Server("监管报告")
                
            with Cluster("风险评分"):
                risk_scoring = Server("风险评分")
                transaction_monitoring = Server("交易监控")
                anomaly_detection = Server("异常检测")
                threat_intelligence = Server("威胁情报")
                
        # 数据处理层
        with Cluster("数据处理层"):
            with Cluster("实时数据流"):
                event_streaming = Kafka("事件流")
                real_time_analytics = Server("实时分析")
                stream_processing = Server("流处理")
                event_store = Server("事件存储")
                
            with Cluster("数据仓库"):
                data_warehouse = Redshift("数据仓库")
                data_lake = S3("数据湖")
                etl_pipeline = Server("ETL管道")
                data_pipeline = Server("数据管道")
                
            with Cluster("大数据处理"):
                spark_cluster = Spark("Spark集群")
                hadoop_cluster = Hadoop("Hadoop集群")
                emr_cluster = EMR("EMR集群")
                data_processing = Server("数据处理")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系型数据库"):
                primary_db = PostgreSQL("主数据库")
                replica_db = PostgreSQL("只读副本")
                backup_db = PostgreSQL("备份数据库")
                
            with Cluster("NoSQL数据库"):
                document_db = MongoDB("文档数据库")
                key_value_store = Dynamodb("键值存储")
                column_db = Cassandra("列式数据库")
                
            with Cluster("缓存层"):
                redis_cache = Server("Redis缓存")
                memcached = Server("Memcached")
                cdn_cache = Server("CDN缓存")
                
        # 分析层
        with Cluster("分析层"):
            with Cluster("业务智能"):
                business_intelligence = Server("商业智能")
                reporting_dashboard = Server("报表仪表板")
                data_visualization = Server("数据可视化")
                kpi_monitoring = Server("KPI监控")
                
            with Cluster("机器学习"):
                ml_platform = Server("机器学习平台")
                model_training = Server("模型训练")
                model_deployment = Server("模型部署")
                feature_store = Server("特征存储")
                
            with Cluster("A/B测试"):
                experiment_platform = Server("实验平台")
                traffic_splitting = Server("流量分割")
                statistical_analysis = Server("统计分析")
                result_analysis = Server("结果分析")
                
        # 安全层
        with Cluster("安全层"):
            with Cluster("数据安全"):
                data_encryption = Server("数据加密")
                pci_compliance = Server("PCI合规")
                tokenization = Server("令牌化")
                key_management = Server("密钥管理")
                
            with Cluster("网络安全"):
                ddos_protection = Server("DDoS防护")
                waf = WAF("Web应用防火墙")
                network_security = Server("网络安全")
                ssl_tls = Server("SSL/TLS")
                
            with Cluster("身份安全"):
                multi_factor_auth = Server("多因子认证")
                biometric_auth = Server("生物识别认证")
                session_management = Server("会话管理")
                access_control = Server("访问控制")
                
        # 集成层
        with Cluster("集成层"):
            with Cluster("第三方集成"):
                bank_apis = Server("银行API")
                card_networks = Server("卡网络")
                payment_processors = Server("支付处理商")
                fintech_partners = Server("金融科技合作伙伴")
                
            with Cluster("内部集成"):
                microservices = Server("微服务")
                service_mesh = Server("服务网格")
                api_management = Server("API管理")
                event_driven = Server("事件驱动架构")
                
        # 云服务层
        with Cluster("云服务层"):
            with Cluster("基础设施"):
                container_orchestration = EKS("容器编排")
                serverless_compute = Lambda("无服务器计算")
                managed_databases = RDS("托管数据库")
                object_storage = S3("对象存储")
                
            with Cluster("监控和日志"):
                application_monitoring = Server("应用监控")
                infrastructure_monitoring = Server("基础设施监控")
                log_aggregation = Server("日志聚合")
                alerting_system = Server("告警系统")
                
            with Cluster("DevOps"):
                ci_cd_pipeline = Server("CI/CD管道")
                infrastructure_as_code = Server("基础设施即代码")
                configuration_management = Server("配置管理")
                deployment_automation = Server("部署自动化")
                
        # 移动和前端层
        with Cluster("移动和前端层"):
            with Cluster("前端技术"):
                react_apps = React("React应用")
                mobile_sdk = Server("移动SDK")
                web_sdk = Server("Web SDK")
                widget_library = Server("组件库")
                
            with Cluster("用户体验"):
                personalization = Server("个性化")
                recommendation_engine = Server("推荐引擎")
                user_onboarding = Server("用户引导")
                customer_support = Server("客户支持")
                
        # 合规和审计层
        with Cluster("合规和审计层"):
            with Cluster("审计跟踪"):
                audit_logging = Server("审计日志")
                compliance_monitoring = Server("合规监控")
                regulatory_reporting = Server("监管报告")
                data_governance = Server("数据治理")
                
            with Cluster("隐私保护"):
                gdpr_compliance = Server("GDPR合规")
                data_privacy = Server("数据隐私")
                consent_management = Server("同意管理")
                data_retention = Server("数据保留")
                
        # 连接关系
        users >> mobile_app
        merchants >> web_app
        developers >> merchant_portal
        partners >> api_clients
        
        mobile_app >> load_balancer
        web_app >> cdn
        merchant_portal >> edge_locations
        api_clients >> api_gateway
        
        load_balancer >> cdn
        cdn >> api_gateway
        
        api_gateway >> rate_limiting
        rate_limiting >> authentication
        authentication >> authorization
        
        authorization >> payment_engine
        payment_engine >> transaction_processor
        transaction_processor >> payment_methods
        payment_methods >> currency_converter
        
        credit_cards >> payment_methods
        debit_cards >> payment_methods
        bank_transfers >> payment_methods
        digital_wallets >> payment_methods
        cryptocurrency >> payment_methods
        
        transaction_processor >> transaction_storage
        transaction_storage >> payment_flows
        payment_flows >> refund_processing
        refund_processing >> dispute_management
        
        fraud_detection >> machine_learning_models
        machine_learning_models >> behavioral_analysis
        behavioral_analysis >> device_fingerprinting
        
        aml_compliance >> kyc_verification
        kyc_verification >> sanctions_screening
        sanctions_screening >> regulatory_reporting
        
        risk_scoring >> transaction_monitoring
        transaction_monitoring >> anomaly_detection
        anomaly_detection >> threat_intelligence
        
        event_streaming >> real_time_analytics
        real_time_analytics >> stream_processing
        stream_processing >> event_store
        
        data_warehouse >> data_lake
        data_lake >> etl_pipeline
        etl_pipeline >> data_pipeline
        
        spark_cluster >> hadoop_cluster
        hadoop_cluster >> emr_cluster
        emr_cluster >> data_processing
        
        primary_db >> replica_db
        replica_db >> backup_db
        
        document_db >> key_value_store
        key_value_store >> column_db
        
        redis_cache >> memcached
        memcached >> cdn_cache
        
        business_intelligence >> reporting_dashboard
        reporting_dashboard >> data_visualization
        data_visualization >> kpi_monitoring
        
        ml_platform >> model_training
        model_training >> model_deployment
        model_deployment >> feature_store
        
        experiment_platform >> traffic_splitting
        traffic_splitting >> statistical_analysis
        statistical_analysis >> result_analysis
        
        data_encryption >> pci_compliance
        pci_compliance >> tokenization
        tokenization >> key_management
        
        ddos_protection >> waf
        waf >> network_security
        network_security >> ssl_tls
        
        multi_factor_auth >> biometric_auth
        biometric_auth >> session_management
        session_management >> access_control
        
        bank_apis >> card_networks
        card_networks >> payment_processors
        payment_processors >> fintech_partners
        
        microservices >> service_mesh
        service_mesh >> api_management
        api_management >> event_driven
        
        container_orchestration >> serverless_compute
        serverless_compute >> managed_databases
        managed_databases >> object_storage
        
        application_monitoring >> infrastructure_monitoring
        infrastructure_monitoring >> log_aggregation
        log_aggregation >> alerting_system
        
        ci_cd_pipeline >> infrastructure_as_code
        infrastructure_as_code >> configuration_management
        configuration_management >> deployment_automation
        
        react_apps >> mobile_sdk
        mobile_sdk >> web_sdk
        web_sdk >> widget_library
        
        personalization >> recommendation_engine
        recommendation_engine >> user_onboarding
        user_onboarding >> customer_support
        
        audit_logging >> compliance_monitoring
        compliance_monitoring >> regulatory_reporting
        regulatory_reporting >> data_governance
        
        gdpr_compliance >> data_privacy
        data_privacy >> consent_management
        consent_management >> data_retention

if __name__ == "__main__":
    create_paypal_tech_stack_diagram(filename="paypal_tech_stack", outformat="png")
    create_paypal_tech_stack_diagram(filename="paypal_tech_stack", outformat="pdf")
