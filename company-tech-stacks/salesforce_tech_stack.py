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
from diagrams.programming.language import Python, Java, JavaScript
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

def create_salesforce_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建Salesforce技术栈图表
    with Diagram("Salesforce技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("Salesforce用户")
            admin_users = Users("系统管理员")
            developers = Users("开发者")
            partners = Users("合作伙伴")
            
            with Cluster("客户端应用"):
                web_app = Server("Salesforce Web")
                mobile_app = Server("Salesforce Mobile")
                desktop_app = Server("Salesforce Desktop")
                lightning_app = Server("Lightning App")
                
        # 接入层
        with Cluster("接入层"):
            with Cluster("CDN和负载均衡"):
                cdn = CloudFront("CloudFront CDN")
                load_balancer = ELB("负载均衡器")
                api_gateway = Server("API网关")
                
            with Cluster("安全认证"):
                oauth = Server("OAuth 2.0")
                saml = Server("SAML SSO")
                multi_factor = Server("多因子认证")
                identity_service = Server("身份服务")
                
        # Salesforce平台层
        with Cluster("Salesforce平台层"):
            with Cluster("核心平台服务"):
                core_platform = Server("Salesforce核心平台")
                multi_tenant = Server("多租户架构")
                metadata_api = Server("Metadata API")
                rest_api = Server("REST API")
                soap_api = Server("SOAP API")
                
            with Cluster("Lightning平台"):
                lightning_platform = Server("Lightning平台")
                lightning_web_components = Server("Lightning Web组件")
                aura_components = Server("Aura组件")
                lightning_data_service = Server("Lightning数据服务")
                
            with Cluster("Salesforce Clouds"):
                sales_cloud = Server("Sales Cloud")
                service_cloud = Server("Service Cloud")
                marketing_cloud = Server("Marketing Cloud")
                commerce_cloud = Server("Commerce Cloud")
                analytics_cloud = Server("Analytics Cloud")
                platform_cloud = Server("Platform Cloud")
                
        # 开发平台层
        with Cluster("开发平台层"):
            with Cluster("开发工具"):
                salesforce_cli = Server("Salesforce CLI")
                vs_code = Server("VS Code")
                workbench = Server("Workbench")
                data_loader = Server("Data Loader")
                
            with Cluster("编程语言"):
                apex = Server("Apex")
                javascript = JavaScript("JavaScript")
                java = Java("Java")
                python = Python("Python")
                
            with Cluster("开发框架"):
                lightning_framework = Server("Lightning框架")
                lwc = Server("Lightning Web Components")
                aura = Server("Aura框架")
                visualforce = Server("Visualforce")
                
        # 数据层
        with Cluster("数据层"):
            with Cluster("Salesforce数据库"):
                salesforce_db = Server("Salesforce数据库")
                custom_objects = Server("自定义对象")
                standard_objects = Server("标准对象")
                external_objects = Server("外部对象")
                
            with Cluster("数据集成"):
                data_connector = Server("数据连接器")
                etl_service = Server("ETL服务")
                real_time_sync = Server("实时同步")
                batch_processing = Server("批量处理")
                
            with Cluster("外部数据源"):
                external_db = PostgreSQL("外部数据库")
                api_integration = Server("API集成")
                file_storage = S3("文件存储")
                
        # 分析和AI层
        with Cluster("分析和AI层"):
            with Cluster("Salesforce Einstein"):
                einstein_analytics = Server("Einstein Analytics")
                einstein_ai = Server("Einstein AI")
                einstein_discovery = Server("Einstein Discovery")
                einstein_prediction = Server("Einstein预测")
                
            with Cluster("数据可视化"):
                tableau = Server("Tableau")
                lightning_dashboards = Server("Lightning仪表板")
                reports_service = Server("报表服务")
                
            with Cluster("机器学习"):
                ml_platform = Server("ML平台")
                predictive_analytics = Server("预测分析")
                recommendation_engine = Server("推荐引擎")
                
        # 集成层
        with Cluster("集成层"):
            with Cluster("集成平台"):
                mule_soft = Server("MuleSoft")
                integration_cloud = Server("Integration Cloud")
                event_bus = Server("事件总线")
                
            with Cluster("第三方集成"):
                slack_integration = Slack("Slack集成")
                zoom_integration = Server("Zoom集成")
                google_workspace = Server("Google Workspace")
                microsoft_office = Server("Microsoft Office")
                
            with Cluster("API管理"):
                api_manager = Server("API管理器")
                rate_limiting = Server("速率限制")
                api_monitoring = Server("API监控")
                
        # 安全和合规层
        with Cluster("安全和合规层"):
            with Cluster("数据安全"):
                data_encryption = Server("数据加密")
                field_level_security = Server("字段级安全")
                record_level_security = Server("记录级安全")
                ip_restriction = Server("IP限制")
                
            with Cluster("合规性"):
                gdpr_compliance = Server("GDPR合规")
                ccpa_compliance = Server("CCPA合规")
                audit_trail = Server("审计跟踪")
                data_residency = Server("数据驻留")
                
            with Cluster("安全监控"):
                security_monitoring = Server("安全监控")
                threat_detection = Server("威胁检测")
                incident_response = Server("事件响应")
                
        # 部署和运维层
        with Cluster("部署和运维层"):
            with Cluster("CI/CD"):
                github_integration = Server("GitHub集成")
                gitlab_integration = Server("GitLab集成")
                jenkins = Server("Jenkins")
                circleci = Server("CircleCI")
                
            with Cluster("环境管理"):
                sandbox = Server("沙盒环境")
                dev_environment = Server("开发环境")
                staging_environment = Server("预发布环境")
                production = Server("生产环境")
                
            with Cluster("监控和日志"):
                cloudwatch = Cloudwatch("CloudWatch")
                datadog = Server("Datadog")
                splunk = Datadog("Splunk")
                custom_monitoring = Server("自定义监控")
                
        # 移动和离线层
        with Cluster("移动和离线层"):
            with Cluster("移动平台"):
                ios_app = Server("iOS应用")
                android_app = Server("Android应用")
                mobile_sdk = Server("移动SDK")
                
            with Cluster("离线功能"):
                offline_sync = Server("离线同步")
                local_storage = Server("本地存储")
                conflict_resolution = Server("冲突解决")
                
        # 连接关系
        users >> web_app
        admin_users >> lightning_app
        developers >> vs_code
        partners >> api_gateway
        
        web_app >> cdn
        mobile_app >> cdn
        desktop_app >> cdn
        lightning_app >> cdn
        
        cdn >> load_balancer
        load_balancer >> api_gateway
        
        api_gateway >> oauth
        api_gateway >> saml
        oauth >> identity_service
        saml >> identity_service
        
        identity_service >> core_platform
        core_platform >> multi_tenant
        core_platform >> metadata_api
        core_platform >> rest_api
        core_platform >> soap_api
        
        core_platform >> lightning_platform
        lightning_platform >> lightning_web_components
        lightning_platform >> aura_components
        lightning_platform >> lightning_data_service
        
        core_platform >> sales_cloud
        core_platform >> service_cloud
        core_platform >> marketing_cloud
        core_platform >> commerce_cloud
        core_platform >> analytics_cloud
        core_platform >> platform_cloud
        
        salesforce_cli >> vs_code
        vs_code >> apex
        apex >> lightning_framework
        javascript >> lwc
        java >> visualforce
        
        core_platform >> salesforce_db
        salesforce_db >> custom_objects
        salesforce_db >> standard_objects
        salesforce_db >> external_objects
        
        data_connector >> external_db
        etl_service >> external_db
        real_time_sync >> api_integration
        
        einstein_analytics >> einstein_ai
        einstein_ai >> einstein_discovery
        einstein_ai >> einstein_prediction
        
        tableau >> lightning_dashboards
        reports_service >> lightning_dashboards
        
        ml_platform >> predictive_analytics
        ml_platform >> recommendation_engine
        
        mule_soft >> integration_cloud
        integration_cloud >> event_bus
        
        slack_integration >> api_manager
        zoom_integration >> api_manager
        google_workspace >> api_manager
        
        api_manager >> rate_limiting
        api_manager >> api_monitoring
        
        data_encryption >> field_level_security
        field_level_security >> record_level_security
        record_level_security >> ip_restriction
        
        gdpr_compliance >> audit_trail
        ccpa_compliance >> audit_trail
        audit_trail >> data_residency
        
        security_monitoring >> threat_detection
        threat_detection >> incident_response
        
        github_integration >> jenkins
        gitlab_integration >> jenkins
        jenkins >> circleci
        
        circleci >> sandbox
        sandbox >> dev_environment
        dev_environment >> staging_environment
        staging_environment >> production
        
        cloudwatch >> datadog
        datadog >> splunk
        splunk >> custom_monitoring
        
        mobile_sdk >> ios_app
        mobile_sdk >> android_app
        
        ios_app >> offline_sync
        android_app >> offline_sync
        offline_sync >> local_storage
        local_storage >> conflict_resolution

if __name__ == "__main__":
    create_salesforce_tech_stack_diagram(filename="salesforce_tech_stack", outformat="png")
    create_salesforce_tech_stack_diagram(filename="salesforce_tech_stack", outformat="pdf")
