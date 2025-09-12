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
from diagrams.onprem.inmemory import Redis
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Java, Python, JavaScript
from diagrams.programming.framework import React, Spring
from diagrams.aws.compute import EC2, Lambda, ECS, EKS
from diagrams.aws.database import RDS, Dynamodb, Aurora
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB, VPC
from diagrams.aws.analytics import Kinesis, Glue, EMR, Redshift
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAM, WAF
from diagrams.aws.mobile import APIGateway
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.devtools import Codebuild, Codedeploy
from diagrams.aws.storage import EBS, EFS
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_amazon_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Amazon 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            customers = Users("全球客户")
            
            with Cluster("多平台客户端"):
                web_app = Server("Web 应用")
                mobile_app = Server("移动端 App")
                tablet_app = Server("平板应用")
                smart_tv = Server("智能电视")
                alexa_device = Server("Alexa 设备")
                kindle_device = Server("Kindle 设备")

        # CDN和边缘计算
        with Cluster("CDN & 边缘计算"):
            with Cluster("内容分发网络"):
                cloudfront = CloudFront("CloudFront CDN")
                edge_cache = Storage("边缘缓存")
                image_optimization = Server("图像优化")
                
            with Cluster("DNS和负载均衡"):
                route53 = Route53("Route53 DNS")
                elb = ELB("负载均衡器")
                alb = ELB("应用负载均衡器")
                
            route53 >> elb >> cloudfront
            cloudfront >> edge_cache
            cloudfront >> image_optimization
            elb >> alb

        # API网关层
        with Cluster("API 网关层"):
            with Cluster("API管理"):
                api_gateway = APIGateway("API Gateway")
                waf = WAF("Web应用防火墙")
                
            with Cluster("服务发现"):
                service_registry = Server("服务注册中心")
                load_balancer = Router("服务负载均衡")
                
            api_gateway >> waf >> service_registry >> load_balancer

        # 微服务层
        with Cluster("微服务层 (Java/Spring)"):
            with Cluster("用户服务"):
                user_service = Spring("用户服务")
                auth_service = Spring("认证服务")
                profile_service = Spring("用户画像服务")
                
            with Cluster("商品服务"):
                catalog_service = Spring("商品目录服务")
                inventory_service = Spring("库存服务")
                pricing_service = Spring("定价服务")
                search_service = Spring("搜索服务")
                
            with Cluster("订单服务"):
                order_service = Spring("订单服务")
                payment_service = Spring("支付服务")
                fulfillment_service = Spring("履约服务")
                shipping_service = Spring("配送服务")
                
            with Cluster("推荐服务"):
                recommendation_service = Spring("推荐引擎")
                personalization_service = Spring("个性化服务")
                ml_service = Spring("机器学习服务")
                
            with Cluster("内容服务"):
                content_service = Spring("内容管理")
                media_service = Spring("媒体服务")
                review_service = Spring("评价服务")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("用户数据"):
                user_db = Aurora("用户数据库")
                user_cache = Redis("用户缓存")
                session_store = Redis("会话存储")
                
            with Cluster("商品数据"):
                catalog_db = Dynamodb("商品数据库")
                inventory_db = RDS("库存数据库")
                search_index = Server("搜索索引")
                
            with Cluster("订单数据"):
                order_db = Aurora("订单数据库")
                payment_db = RDS("支付数据库")
                transaction_log = S3("交易日志")
                
            with Cluster("分析数据"):
                analytics_db = Redshift("分析数据仓库")
                event_store = Kinesis("事件流")
                data_lake = S3("数据湖")
                
            with Cluster("媒体存储"):
                media_storage = S3("媒体存储")
                thumbnail_cache = Storage("缩略图缓存")
                backup_storage = EBS("备份存储")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据收集"):
                data_collector = Kinesis("实时数据流")
                log_aggregator = Server("日志聚合器")
                metrics_collector = Server("指标收集器")
                
            with Cluster("数据处理"):
                spark_cluster = Spark("Spark 集群")
                hadoop_cluster = Hadoop("Hadoop 集群")
                etl_pipeline = Glue("ETL 管道")
                
            with Cluster("机器学习"):
                ml_platform = Server("ML 平台")
                recommendation_engine = Server("推荐算法")
                fraud_detection = Server("欺诈检测")
                demand_forecasting = Server("需求预测")
                
            with Cluster("数据仓库"):
                data_warehouse = Redshift("数据仓库")
                olap_cube = Server("OLAP 多维分析")
                
            data_collector >> spark_cluster >> data_warehouse
            log_aggregator >> hadoop_cluster >> data_lake
            etl_pipeline >> ml_platform >> recommendation_engine

        # 基础设施层
        with Cluster("基础设施层 (AWS)"):
            with Cluster("计算资源"):
                ec2_instances = EC2("EC2 实例集群")
                auto_scaling = Server("自动扩缩容")
                spot_instances = Server("Spot 实例")
                
            with Cluster("容器化"):
                docker_containers = ECS("ECS 容器服务")
                kubernetes = EKS("EKS Kubernetes")
                fargate = Lambda("AWS Fargate")
                
            with Cluster("无服务器"):
                lambda_functions = Lambda("Lambda 函数")
                step_functions = Server("Step Functions")
                
            with Cluster("监控告警"):
                cloudwatch = Cloudwatch("CloudWatch")
                prometheus_monitor = Prometheus("Prometheus")
                grafana_dashboard = Grafana("Grafana")
                
            ec2_instances >> auto_scaling >> docker_containers
            docker_containers >> kubernetes
            lambda_functions >> step_functions
            cloudwatch >> prometheus_monitor >> grafana_dashboard

        # 安全层
        with Cluster("安全层"):
            with Cluster("认证授权"):
                iam_service = IAM("IAM 身份管理")
                oauth_service = Vault("OAuth 服务")
                jwt_service = Server("JWT 令牌服务")
                
            with Cluster("数据安全"):
                encryption_service = Server("数据加密")
                key_management = Server("密钥管理")
                secrets_manager = Server("密钥管理服务")
                
            with Cluster("网络安全"):
                vpc_network = VPC("VPC 网络")
                security_groups = Firewall("安全组")
                
            iam_service >> oauth_service >> jwt_service
            encryption_service >> key_management >> secrets_manager
            vpc_network >> security_groups

        # 消息队列和事件驱动
        with Cluster("消息队列和事件驱动"):
            with Cluster("消息队列"):
                sqs_queue = SQS("SQS 消息队列")
                dead_letter_queue = SQS("死信队列")
                
            with Cluster("事件通知"):
                sns_topic = SNS("SNS 通知服务")
                event_bridge = Server("EventBridge")
                
            with Cluster("流处理"):
                kinesis_streams = Kinesis("Kinesis 数据流")
                stream_processor = Server("流处理器")
                
            sqs_queue >> dead_letter_queue
            sns_topic >> event_bridge
            kinesis_streams >> stream_processor

        # DevOps和CI/CD
        with Cluster("DevOps & CI/CD"):
            with Cluster("持续集成"):
                code_build = Codebuild("CodeBuild")
                jenkins = Server("Jenkins")
                
            with Cluster("持续部署"):
                code_deploy = Codebuild("CodeDeploy")
                blue_green = Server("蓝绿部署")
                
            with Cluster("基础设施即代码"):
                terraform = Server("Terraform")
                cloudformation = Server("CloudFormation")
                
            code_build >> jenkins >> code_deploy >> blue_green
            terraform >> cloudformation

        # 连接关系
        # 客户端到CDN
        customers >> web_app
        customers >> mobile_app
        customers >> tablet_app
        customers >> smart_tv
        customers >> alexa_device
        customers >> kindle_device
        
        web_app >> route53
        mobile_app >> route53
        tablet_app >> route53
        smart_tv >> route53
        alexa_device >> route53
        kindle_device >> route53

        # CDN到API网关
        alb >> Edge(label="API请求") >> api_gateway
        api_gateway >> Edge(label="安全过滤") >> waf
        waf >> Edge(label="服务发现") >> service_registry

        # API网关到微服务
        load_balancer >> Edge(label="用户请求") >> user_service
        load_balancer >> Edge(label="商品请求") >> catalog_service
        load_balancer >> Edge(label="订单请求") >> order_service
        load_balancer >> Edge(label="推荐请求") >> recommendation_service
        load_balancer >> Edge(label="内容请求") >> content_service

        # 微服务到数据存储
        user_service >> Edge(label="用户数据") >> user_db
        user_service >> Edge(label="用户缓存") >> user_cache
        catalog_service >> Edge(label="商品数据") >> catalog_db
        inventory_service >> Edge(label="库存数据") >> inventory_db
        order_service >> Edge(label="订单数据") >> order_db
        payment_service >> Edge(label="支付数据") >> payment_db

        # 数据存储关联
        user_db >> user_cache
        catalog_db >> search_index
        order_db >> transaction_log
        analytics_db >> event_store
        media_storage >> thumbnail_cache
        media_storage >> backup_storage

        # 大数据分析关联
        event_store >> Edge(label="实时数据") >> data_collector
        data_collector >> Edge(label="流处理") >> spark_cluster
        log_aggregator >> Edge(label="批处理") >> hadoop_cluster
        spark_cluster >> Edge(label="机器学习") >> ml_platform
        ml_platform >> Edge(label="推荐") >> recommendation_engine

        # 基础设施支撑
        ec2_instances >> Edge(label="运行环境") >> user_service
        ec2_instances >> Edge(label="运行环境") >> catalog_service
        docker_containers >> Edge(label="容器化") >> order_service
        kubernetes >> Edge(label="编排") >> recommendation_service
        lambda_functions >> Edge(label="无服务器") >> ml_service

        # 监控关联
        cloudwatch >> Edge(label="监控") >> user_service
        cloudwatch >> Edge(label="监控") >> catalog_service
        prometheus_monitor >> Edge(label="指标收集") >> order_service
        grafana_dashboard >> Edge(label="可视化") >> prometheus_monitor

        # 安全关联
        api_gateway >> Edge(label="认证") >> iam_service
        user_service >> Edge(label="授权") >> oauth_service
        alb >> Edge(label="网络防护") >> waf
        ec2_instances >> Edge(label="网络隔离") >> vpc_network

        # 消息队列关联
        order_service >> Edge(label="订单事件") >> sqs_queue
        payment_service >> Edge(label="支付通知") >> sns_topic
        catalog_service >> Edge(label="商品更新") >> kinesis_streams
        sqs_queue >> Edge(label="失败重试") >> dead_letter_queue

        # DevOps关联
        code_build >> Edge(label="构建") >> jenkins
        jenkins >> Edge(label="部署") >> code_deploy
        code_deploy >> Edge(label="蓝绿部署") >> blue_green
        terraform >> Edge(label="基础设施") >> cloudformation


if __name__ == "__main__":
    create_amazon_tech_stack_diagram(filename="amazon_tech_stack", outformat="png")
    create_amazon_tech_stack_diagram(filename="amazon_tech_stack", outformat="pdf")
