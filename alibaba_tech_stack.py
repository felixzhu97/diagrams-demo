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

def create_alibaba_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建阿里巴巴技术栈图表
    with Diagram("阿里巴巴技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("阿里巴巴用户")
            merchants = Users("商家")
            developers = Users("开发者")
            enterprises = Users("企业客户")
            
            with Cluster("客户端应用"):
                taobao_app = Server("淘宝App")
                tmall_app = Server("天猫App")
                alipay_app = Server("支付宝App")
                dingtalk_app = Server("钉钉App")
                
        # 接入层
        with Cluster("接入层"):
            with Cluster("负载均衡和CDN"):
                load_balancer = ELB("负载均衡器")
                cdn = CloudFront("CDN")
                edge_computing = Server("边缘计算")
                
            with Cluster("网关服务"):
                api_gateway = Server("API网关")
                service_mesh = Server("服务网格")
                traffic_management = Server("流量管理")
                circuit_breaker = Server("熔断器")
                
        # 电商平台层
        with Cluster("电商平台层"):
            with Cluster("核心电商"):
                taobao_platform = Server("淘宝平台")
                tmall_platform = Server("天猫平台")
                alibaba_com = Server("阿里巴巴国际站")
                platform_1688 = Server("1688平台")
                
            with Cluster("交易系统"):
                order_management = Server("订单管理")
                payment_processing = Server("支付处理")
                inventory_management = Server("库存管理")
                logistics_tracking = Server("物流跟踪")
                
            with Cluster("营销系统"):
                recommendation_engine = Server("推荐引擎")
                search_engine = Server("搜索引擎")
                promotion_system = Server("促销系统")
                user_behavior_analysis = Server("用户行为分析")
                
        # 阿里云服务层
        with Cluster("阿里云服务层"):
            with Cluster("计算服务"):
                ecs = Server("ECS云服务器")
                container_service = Server("容器服务")
                serverless_compute = Server("无服务器计算")
                gpu_compute = Server("GPU计算")
                
            with Cluster("存储服务"):
                oss = Server("对象存储OSS")
                nas = Server("文件存储NAS")
                ebs = Server("块存储EBS")
                table_store = Server("表格存储")
                
            with Cluster("数据库服务"):
                rds = Server("关系型数据库RDS")
                polardb = Server("PolarDB")
                mongodb = Server("MongoDB")
                redis = Server("Redis")
                
            with Cluster("网络服务"):
                vpc = Server("专有网络VPC")
                slb = Server("负载均衡SLB")
                cdn_service = Server("CDN服务")
                dns_service = Server("DNS服务")
                
        # 大数据处理层
        with Cluster("大数据处理层"):
            with Cluster("数据存储"):
                maxcompute = Server("MaxCompute")
                datahub = Server("DataHub")
                data_lake = Server("数据湖")
                real_time_storage = Server("实时存储")
                
            with Cluster("数据处理"):
                dataworks = Server("DataWorks")
                emr = Server("EMR")
                stream_compute = Server("实时计算")
                batch_compute = Server("批计算")
                
            with Cluster("数据服务"):
                quick_bi = Server("Quick BI")
                data_v = Server("DataV")
                machine_learning_platform = Server("机器学习平台")
                data_science_workshop = Server("数据科学工作台")
                
        # AI技术层
        with Cluster("AI技术层"):
            with Cluster("机器学习"):
                pai = Server("PAI机器学习")
                eas = Server("EAS模型服务")
                dsw = Server("DSW开发环境")
                model_training = Server("模型训练")
                
            with Cluster("AI服务"):
                nlp_service = Server("自然语言处理")
                computer_vision = Server("计算机视觉")
                speech_recognition = Server("语音识别")
                recommendation_ai = Server("推荐AI")
                
            with Cluster("智能应用"):
                intelligent_customer_service = Server("智能客服")
                content_moderation = Server("内容审核")
                fraud_detection = Server("欺诈检测")
                personalized_recommendation = Server("个性化推荐")
                
        # 金融科技层
        with Cluster("金融科技层"):
            with Cluster("支付系统"):
                alipay_core = Server("支付宝核心")
                ant_chain = Server("蚂蚁链")
                risk_control = Server("风险控制")
                payment_gateway = Server("支付网关")
                
            with Cluster("金融产品"):
                yuebao = Server("余额宝")
                huabei = Server("花呗")
                jiebei = Server("借呗")
                insurance_platform = Server("保险平台")
                
            with Cluster("区块链"):
                blockchain_platform = Server("区块链平台")
                smart_contracts = Server("智能合约")
                digital_assets = Server("数字资产")
                cross_chain = Server("跨链服务")
                
        # 物流科技层
        with Cluster("物流科技层"):
            with Cluster("菜鸟网络"):
                cainiao_platform = Server("菜鸟平台")
                warehouse_management = Server("仓储管理")
                delivery_optimization = Server("配送优化")
                logistics_tracking = Server("物流追踪")
                
            with Cluster("智能物流"):
                route_optimization = Server("路径优化")
                drone_delivery = Server("无人机配送")
                robot_warehouse = Server("机器人仓库")
                iot_sensors = Server("IoT传感器")
                
        # 企业服务层
        with Cluster("企业服务层"):
            with Cluster("钉钉生态"):
                dingtalk_core = Server("钉钉核心")
                collaboration_tools = Server("协作工具")
                video_conferencing = Server("视频会议")
                workflow_automation = Server("工作流自动化")
                
            with Cluster("企业应用"):
                erp_solutions = Server("ERP解决方案")
                crm_systems = Server("CRM系统")
                hr_management = Server("人力资源管理")
                financial_management = Server("财务管理")
                
        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("开发平台"):
                devops_platform = Server("DevOps平台")
                code_management = Server("代码管理")
                ci_cd_pipeline = Server("CI/CD流水线")
                testing_platform = Server("测试平台")
                
            with Cluster("监控运维"):
                application_monitoring = Server("应用监控")
                infrastructure_monitoring = Server("基础设施监控")
                log_analysis = Server("日志分析")
                alert_management = Server("告警管理")
                
            with Cluster("安全服务"):
                web_application_firewall = Server("Web应用防火墙")
                ddos_protection = Server("DDoS防护")
                security_center = Server("安全中心")
                identity_management = Server("身份管理")
                
        # 数据安全层
        with Cluster("数据安全层"):
            with Cluster("数据保护"):
                data_encryption = Server("数据加密")
                data_masking = Server("数据脱敏")
                access_control = Server("访问控制")
                data_backup = Server("数据备份")
                
            with Cluster("合规审计"):
                audit_logging = Server("审计日志")
                compliance_monitoring = Server("合规监控")
                privacy_protection = Server("隐私保护")
                data_governance = Server("数据治理")
                
        # 国际化服务层
        with Cluster("国际化服务层"):
            with Cluster("全球业务"):
                aliexpress = Server("AliExpress")
                lazada = Server("Lazada")
                daraz = Server("Daraz")
                trendyol = Server("Trendyol")
                
            with Cluster("跨境服务"):
                cross_border_payment = Server("跨境支付")
                international_logistics = Server("国际物流")
                customs_clearance = Server("清关服务")
                multi_currency = Server("多币种支持")
                
        # 连接关系
        users >> taobao_app
        merchants >> tmall_app
        developers >> alipay_app
        enterprises >> dingtalk_app
        
        taobao_app >> load_balancer
        tmall_app >> cdn
        alipay_app >> edge_computing
        dingtalk_app >> api_gateway
        
        load_balancer >> cdn
        cdn >> api_gateway
        
        api_gateway >> service_mesh
        service_mesh >> traffic_management
        traffic_management >> circuit_breaker
        
        circuit_breaker >> taobao_platform
        circuit_breaker >> tmall_platform
        circuit_breaker >> alibaba_com
        circuit_breaker >> platform_1688
        
        taobao_platform >> order_management
        tmall_platform >> payment_processing
        alibaba_com >> inventory_management
        platform_1688 >> logistics_tracking
        
        order_management >> recommendation_engine
        payment_processing >> search_engine
        inventory_management >> promotion_system
        logistics_tracking >> user_behavior_analysis
        
        ecs >> container_service
        container_service >> serverless_compute
        serverless_compute >> gpu_compute
        
        oss >> nas
        nas >> ebs
        ebs >> table_store
        
        rds >> polardb
        polardb >> mongodb
        mongodb >> redis
        
        vpc >> slb
        slb >> cdn_service
        cdn_service >> dns_service
        
        maxcompute >> datahub
        datahub >> data_lake
        data_lake >> real_time_storage
        
        dataworks >> emr
        emr >> stream_compute
        stream_compute >> batch_compute
        
        quick_bi >> data_v
        data_v >> machine_learning_platform
        machine_learning_platform >> data_science_workshop
        
        pai >> eas
        eas >> dsw
        dsw >> model_training
        
        nlp_service >> computer_vision
        computer_vision >> speech_recognition
        speech_recognition >> recommendation_ai
        
        intelligent_customer_service >> content_moderation
        content_moderation >> fraud_detection
        fraud_detection >> personalized_recommendation
        
        alipay_core >> ant_chain
        ant_chain >> risk_control
        risk_control >> payment_gateway
        
        yuebao >> huabei
        huabei >> jiebei
        jiebei >> insurance_platform
        
        blockchain_platform >> smart_contracts
        smart_contracts >> digital_assets
        digital_assets >> cross_chain
        
        cainiao_platform >> warehouse_management
        warehouse_management >> delivery_optimization
        delivery_optimization >> logistics_tracking
        
        route_optimization >> drone_delivery
        drone_delivery >> robot_warehouse
        robot_warehouse >> iot_sensors
        
        dingtalk_core >> collaboration_tools
        collaboration_tools >> video_conferencing
        video_conferencing >> workflow_automation
        
        erp_solutions >> crm_systems
        crm_systems >> hr_management
        hr_management >> financial_management
        
        devops_platform >> code_management
        code_management >> ci_cd_pipeline
        ci_cd_pipeline >> testing_platform
        
        application_monitoring >> infrastructure_monitoring
        infrastructure_monitoring >> log_analysis
        log_analysis >> alert_management
        
        web_application_firewall >> ddos_protection
        ddos_protection >> security_center
        security_center >> identity_management
        
        data_encryption >> data_masking
        data_masking >> access_control
        access_control >> data_backup
        
        audit_logging >> compliance_monitoring
        compliance_monitoring >> privacy_protection
        privacy_protection >> data_governance
        
        aliexpress >> lazada
        lazada >> daraz
        daraz >> trendyol
        
        cross_border_payment >> international_logistics
        international_logistics >> customs_clearance
        customs_clearance >> multi_currency

if __name__ == "__main__":
    create_alibaba_tech_stack_diagram(filename="alibaba_tech_stack", outformat="png")
    create_alibaba_tech_stack_diagram(filename="alibaba_tech_stack", outformat="pdf")
