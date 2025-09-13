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
from diagrams.programming.language import Python, Java, JavaScript, Cpp, Rust, Go, Ruby
from diagrams.programming.framework import React, Django, Spring, Rails
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

def create_stripe_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建Stripe技术栈图表
    with Diagram("Stripe技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("Stripe用户")
            merchants = Users("商户")
            developers = Users("开发者")
            partners = Users("合作伙伴")
            
            with Cluster("客户端应用"):
                stripe_dashboard = Server("Stripe Dashboard")
                mobile_sdk = Server("Stripe Mobile SDK")
                web_sdk = Server("Stripe Web SDK")
                cli_tools = Server("Stripe CLI")
                
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
                webhook_delivery = Server("Webhook交付")
                
        # Stripe API层
        with Cluster("Stripe API层"):
            with Cluster("核心支付API"):
                payments_api = Server("Payments API")
                charges_api = Server("Charges API")
                refunds_api = Server("Refunds API")
                disputes_api = Server("Disputes API")
                
            with Cluster("支付方式API"):
                cards_api = Server("Cards API")
                bank_accounts_api = Server("Bank Accounts API")
                wallets_api = Server("Digital Wallets API")
                crypto_api = Server("Crypto API")
                
            with Cluster("订阅和计费API"):
                subscriptions_api = Server("Subscriptions API")
                invoices_api = Server("Invoices API")
                billing_api = Server("Billing API")
                tax_api = Server("Tax API")
                
            with Cluster("Connect API"):
                connect_api = Server("Connect API")
                oauth_api = Server("OAuth API")
                marketplace_api = Server("Marketplace API")
                platform_api = Server("Platform API")
                
        # 支付处理层
        with Cluster("支付处理层"):
            with Cluster("支付引擎"):
                payment_engine = Server("支付引擎")
                transaction_processor = Server("交易处理器")
                payment_methods = Server("支付方式管理")
                currency_support = Server("多币种支持")
                
            with Cluster("支付流程"):
                payment_intents = Server("Payment Intents")
                payment_confirmations = Server("支付确认")
                payment_method_attachments = Server("支付方式绑定")
                customer_management = Server("客户管理")
                
            with Cluster("国际支付"):
                cross_border_payments = Server("跨境支付")
                currency_conversion = Server("货币转换")
                local_payment_methods = Server("本地支付方式")
                regulatory_compliance = Server("监管合规")
                
        # 风险控制层
        with Cluster("风险控制层"):
            with Cluster("机器学习"):
                radar_ml = Server("Radar机器学习")
                fraud_detection = Server("欺诈检测")
                risk_scoring = Server("风险评分")
                behavioral_analysis = Server("行为分析")
                
            with Cluster("安全工具"):
                dispute_management = Server("争议管理")
                chargeback_prevention = Server("拒付预防")
                authentication_framework = Server("认证框架")
                data_protection = Server("数据保护")
                
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系型数据库"):
                primary_db = PostgreSQL("主数据库")
                replica_db = PostgreSQL("只读副本")
                backup_db = PostgreSQL("备份数据库")
                
            with Cluster("NoSQL数据库"):
                document_db = MongoDB("文档数据库")
                key_value_store = Dynamodb("键值存储")
                time_series_db = Server("时序数据库")
                
            with Cluster("缓存层"):
                redis_cache = Server("Redis缓存")
                memcached = Server("Memcached")
                cdn_cache = Server("CDN缓存")
                
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
                
            with Cluster("大数据处理"):
                spark_cluster = Spark("Spark集群")
                hadoop_cluster = Hadoop("Hadoop集群")
                data_processing = Server("数据处理")
                
        # 分析层
        with Cluster("分析层"):
            with Cluster("业务分析"):
                revenue_analytics = Server("收入分析")
                transaction_analytics = Server("交易分析")
                customer_analytics = Server("客户分析")
                performance_metrics = Server("性能指标")
                
            with Cluster("机器学习"):
                ml_platform = Server("机器学习平台")
                model_training = Server("模型训练")
                model_deployment = Server("模型部署")
                feature_engineering = Server("特征工程")
                
            with Cluster("A/B测试"):
                experiment_platform = Server("实验平台")
                traffic_splitting = Server("流量分割")
                statistical_analysis = Server("统计分析")
                result_analysis = Server("结果分析")
                
        # 开发者工具层
        with Cluster("开发者工具层"):
            with Cluster("SDK和库"):
                stripe_js = JavaScript("Stripe.js")
                stripe_ios = Server("Stripe iOS SDK")
                stripe_android = Server("Stripe Android SDK")
                stripe_react_native = React("Stripe React Native")
                
            with Cluster("开发工具"):
                stripe_cli = Server("Stripe CLI")
                webhook_testing = Server("Webhook测试")
                api_explorer = Server("API Explorer")
                documentation = Server("文档系统")
                
            with Cluster("集成工具"):
                plugins = Server("插件系统")
                extensions = Server("扩展")
                webhooks = Server("Webhooks")
                api_versioning = Server("API版本管理")
                
        # 安全层
        with Cluster("安全层"):
            with Cluster("数据安全"):
                encryption_at_rest = Server("静态数据加密")
                encryption_in_transit = Server("传输加密")
                pci_compliance = Server("PCI DSS合规")
                tokenization = Server("令牌化")
                
            with Cluster("网络安全"):
                ddos_protection = Server("DDoS防护")
                waf = WAF("Web应用防火墙")
                network_security = Server("网络安全")
                ssl_tls = Server("SSL/TLS")
                
            with Cluster("身份安全"):
                api_key_management = Server("API密钥管理")
                oauth_2_0 = Server("OAuth 2.0")
                multi_factor_auth = Server("多因子认证")
                session_management = Server("会话管理")
                
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
                
        # 合规和审计层
        with Cluster("合规和审计层"):
            with Cluster("合规框架"):
                soc_compliance = Server("SOC合规")
                iso_compliance = Server("ISO合规")
                gdpr_compliance = Server("GDPR合规")
                regulatory_reporting = Server("监管报告")
                
            with Cluster("审计和治理"):
                audit_logging = Server("审计日志")
                compliance_monitoring = Server("合规监控")
                data_governance = Server("数据治理")
                risk_management = Server("风险管理")
                
        # 产品和服务层
        with Cluster("产品和服务层"):
            with Cluster("核心产品"):
                payments = Server("Payments")
                billing = Server("Billing")
                connect = Server("Connect")
                terminal = Server("Terminal")
                
            with Cluster("扩展产品"):
                atlas = Server("Atlas")
                sigma = Server("Sigma")
                radar = Server("Radar")
                tax = Server("Tax")
                
            with Cluster("企业服务"):
                custom_integrations = Server("定制集成")
                dedicated_support = Server("专属支持")
                sla_guarantees = Server("SLA保证")
                white_label_solutions = Server("白标解决方案")
                
        # 连接关系
        users >> stripe_dashboard
        merchants >> mobile_sdk
        developers >> web_sdk
        partners >> cli_tools
        
        stripe_dashboard >> load_balancer
        mobile_sdk >> cdn
        web_sdk >> edge_locations
        cli_tools >> api_gateway
        
        load_balancer >> cdn
        cdn >> api_gateway
        
        api_gateway >> rate_limiting
        rate_limiting >> authentication
        authentication >> webhook_delivery
        
        webhook_delivery >> payments_api
        payments_api >> charges_api
        charges_api >> refunds_api
        refunds_api >> disputes_api
        
        cards_api >> bank_accounts_api
        bank_accounts_api >> wallets_api
        wallets_api >> crypto_api
        
        subscriptions_api >> invoices_api
        invoices_api >> billing_api
        billing_api >> tax_api
        
        connect_api >> oauth_api
        oauth_api >> marketplace_api
        marketplace_api >> platform_api
        
        payments_api >> payment_engine
        payment_engine >> transaction_processor
        transaction_processor >> payment_methods
        payment_methods >> currency_support
        
        payment_intents >> payment_confirmations
        payment_confirmations >> payment_method_attachments
        payment_method_attachments >> customer_management
        
        cross_border_payments >> currency_conversion
        currency_conversion >> local_payment_methods
        local_payment_methods >> regulatory_compliance
        
        radar_ml >> fraud_detection
        fraud_detection >> risk_scoring
        risk_scoring >> behavioral_analysis
        
        dispute_management >> chargeback_prevention
        chargeback_prevention >> authentication_framework
        authentication_framework >> data_protection
        
        primary_db >> replica_db
        replica_db >> backup_db
        
        document_db >> key_value_store
        key_value_store >> time_series_db
        
        redis_cache >> memcached
        memcached >> cdn_cache
        
        event_streaming >> real_time_analytics
        real_time_analytics >> stream_processing
        stream_processing >> event_store
        
        data_warehouse >> data_lake
        data_lake >> etl_pipeline
        
        spark_cluster >> hadoop_cluster
        hadoop_cluster >> data_processing
        
        revenue_analytics >> transaction_analytics
        transaction_analytics >> customer_analytics
        customer_analytics >> performance_metrics
        
        ml_platform >> model_training
        model_training >> model_deployment
        model_deployment >> feature_engineering
        
        experiment_platform >> traffic_splitting
        traffic_splitting >> statistical_analysis
        statistical_analysis >> result_analysis
        
        stripe_js >> stripe_ios
        stripe_ios >> stripe_android
        stripe_android >> stripe_react_native
        
        stripe_cli >> webhook_testing
        webhook_testing >> api_explorer
        api_explorer >> documentation
        
        plugins >> extensions
        extensions >> webhooks
        webhooks >> api_versioning
        
        encryption_at_rest >> encryption_in_transit
        encryption_in_transit >> pci_compliance
        pci_compliance >> tokenization
        
        ddos_protection >> waf
        waf >> network_security
        network_security >> ssl_tls
        
        api_key_management >> oauth_2_0
        oauth_2_0 >> multi_factor_auth
        multi_factor_auth >> session_management
        
        container_orchestration >> serverless_compute
        serverless_compute >> managed_databases
        managed_databases >> object_storage
        
        application_monitoring >> infrastructure_monitoring
        infrastructure_monitoring >> log_aggregation
        log_aggregation >> alerting_system
        
        ci_cd_pipeline >> infrastructure_as_code
        infrastructure_as_code >> configuration_management
        configuration_management >> deployment_automation
        
        soc_compliance >> iso_compliance
        iso_compliance >> gdpr_compliance
        gdpr_compliance >> regulatory_reporting
        
        audit_logging >> compliance_monitoring
        compliance_monitoring >> data_governance
        data_governance >> risk_management
        
        payments >> billing
        billing >> connect
        connect >> terminal
        
        atlas >> sigma
        sigma >> radar
        radar >> tax
        
        custom_integrations >> dedicated_support
        dedicated_support >> sla_guarantees
        sla_guarantees >> white_label_solutions

if __name__ == "__main__":
    create_stripe_tech_stack_diagram(filename="stripe_tech_stack", outformat="png")
    create_stripe_tech_stack_diagram(filename="stripe_tech_stack", outformat="pdf")
