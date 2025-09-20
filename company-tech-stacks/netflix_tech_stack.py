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
from diagrams.programming.language import Java, Python, JavaScript
from diagrams.programming.framework import React, Spring
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3 as AWSS3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_netflix_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Netflix 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("多平台客户端"):
                mobile_app = Server("移动端 App")
                web_app = Server("Web 端")
                smart_tv = Server("智能电视")
                gaming_console = Server("游戏主机")
                streaming_device = Server("流媒体设备")

        # CDN和边缘计算
        with Cluster("CDN & 边缘计算"):
            with Cluster("内容分发网络"):
                cloudfront = CloudFront("CloudFront CDN")
                akamai = Router("Akamai CDN")
                edge_cache = Storage("边缘缓存")
                
            with Cluster("负载均衡"):
                route53 = Route53("Route53 DNS")
                elb = ELB("负载均衡器")
                
            route53 >> elb >> cloudfront
            cloudfront >> edge_cache
            akamai >> edge_cache

        # API网关层
        with Cluster("API 网关层"):
            with Cluster("服务发现与路由"):
                zuul = Server("Zuul API网关")
                eureka = Server("Eureka 服务注册中心")
                
            with Cluster("断路器模式"):
                hystrix = Server("Hystrix 断路器")
                ribbon = Server("Ribbon 负载均衡")
                
            zuul >> eureka >> hystrix >> ribbon

        # 微服务层
        with Cluster("微服务层 (Spring Boot)"):
            with Cluster("用户服务"):
                user_service = Spring("用户服务")
                auth_service = Spring("认证服务")
                profile_service = Spring("用户画像服务")
                
            with Cluster("内容服务"):
                catalog_service = Spring("内容目录服务")
                search_service = Spring("搜索服务")
                recommendation_service = Spring("推荐引擎")
                
            with Cluster("播放服务"):
                playback_service = Spring("播放服务")
                encoding_service = Spring("编码服务")
                quality_service = Spring("视频质量服务")
                
            with Cluster("订阅服务"):
                billing_service = Spring("计费服务")
                subscription_service = Spring("订阅服务")
                payment_service = Spring("支付服务")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("用户数据"):
                user_db = PostgreSQL("用户数据库")
                user_cache = Storage("用户缓存")
                
            with Cluster("内容数据"):
                content_db = Cassandra("内容数据库")
                metadata_db = MongoDB("元数据数据库")
                
            with Cluster("分析数据"):
                analytics_db = Bigtable("分析数据库")
                event_store = Kafka("事件存储")
                
            with Cluster("媒体存储"):
                media_storage = AWSS3("媒体存储")
                thumbnail_cache = Storage("缩略图缓存")
                subtitle_store = Storage("字幕存储")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据收集"):
                data_collector = Kinesis("实时数据流")
                log_aggregator = Server("日志聚合器")
                
            with Cluster("数据处理"):
                spark_cluster = Spark("Spark 集群")
                hadoop_cluster = Hadoop("Hadoop 集群")
                etl_pipeline = Glue("ETL 管道")
                
            with Cluster("机器学习"):
                ml_platform = Server("ML 平台")
                recommendation_engine = Server("推荐算法")
                a_b_testing = Server("A/B 测试")
                
            with Cluster("数据仓库"):
                data_warehouse = EMR("数据仓库")
                data_lake = Storage("数据湖")
                
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
                docker_containers = Server("Docker 容器")
                kubernetes = Server("Kubernetes")
                
            with Cluster("监控告警"):
                cloudwatch = Cloudwatch("CloudWatch")
                prometheus_monitor = Prometheus("Prometheus")
                grafana_dashboard = Grafana("Grafana")
                
            ec2_instances >> auto_scaling >> docker_containers
            docker_containers >> kubernetes
            cloudwatch >> prometheus_monitor >> grafana_dashboard

        # 安全层
        with Cluster("安全层"):
            with Cluster("认证授权"):
                oauth_service = Vault("OAuth 服务")
                jwt_service = Server("JWT 令牌服务")
                
            with Cluster("数据安全"):
                encryption_service = Server("数据加密")
                key_management = Server("密钥管理")
                
            with Cluster("网络安全"):
                waf = Firewall("Web应用防火墙")
                vpc = Router("VPC 网络")
                
            oauth_service >> jwt_service
            encryption_service >> key_management
            waf >> vpc

        # 内容制作与分发
        with Cluster("内容制作与分发"):
            with Cluster("内容制作"):
                content_studio = Server("内容工作室")
                post_production = Server("后期制作")
                
            with Cluster("编码转码"):
                encoding_farm = Server("编码农场")
                adaptive_streaming = Server("自适应流媒体")
                
            with Cluster("质量保证"):
                qa_testing = Server("质量测试")
                performance_monitoring = Server("性能监控")
                
            content_studio >> post_production >> encoding_farm
            encoding_farm >> adaptive_streaming >> qa_testing

        # 连接关系
        # 客户端到CDN
        users >> mobile_app
        users >> web_app
        users >> smart_tv
        users >> gaming_console
        users >> streaming_device
        
        mobile_app >> route53
        web_app >> route53
        smart_tv >> route53
        gaming_console >> route53
        streaming_device >> route53

        # CDN到API网关
        elb >> Edge(label="API请求") >> zuul
        zuul >> Edge(label="服务发现") >> eureka
        eureka >> Edge(label="负载均衡") >> ribbon

        # API网关到微服务
        zuul >> Edge(label="用户请求") >> user_service
        zuul >> Edge(label="内容请求") >> catalog_service
        zuul >> Edge(label="播放请求") >> playback_service
        zuul >> Edge(label="订阅请求") >> billing_service

        # 微服务到数据存储
        user_service >> Edge(label="用户数据") >> user_db
        auth_service >> Edge(label="认证数据") >> user_cache
        catalog_service >> Edge(label="内容数据") >> content_db
        search_service >> Edge(label="元数据") >> metadata_db
        playback_service >> Edge(label="播放数据") >> analytics_db

        # 数据存储关联
        user_db >> user_cache
        content_db >> metadata_db
        analytics_db >> event_store
        media_storage >> thumbnail_cache
        media_storage >> subtitle_store

        # 大数据分析关联
        event_store >> Edge(label="实时数据") >> data_collector
        data_collector >> Edge(label="流处理") >> spark_cluster
        log_aggregator >> Edge(label="批处理") >> hadoop_cluster
        spark_cluster >> Edge(label="机器学习") >> ml_platform
        ml_platform >> Edge(label="推荐") >> recommendation_engine

        # 基础设施支撑
        ec2_instances >> Edge(label="运行环境") >> user_service
        ec2_instances >> Edge(label="运行环境") >> catalog_service
        docker_containers >> Edge(label="容器化") >> playback_service
        kubernetes >> Edge(label="编排") >> billing_service

        # 监控关联
        cloudwatch >> Edge(label="监控") >> user_service
        cloudwatch >> Edge(label="监控") >> catalog_service
        prometheus_monitor >> Edge(label="指标收集") >> playback_service
        grafana_dashboard >> Edge(label="可视化") >> prometheus_monitor

        # 安全关联
        zuul >> Edge(label="认证") >> oauth_service
        user_service >> Edge(label="授权") >> jwt_service
        elb >> Edge(label="防护") >> waf
        ec2_instances >> Edge(label="网络隔离") >> vpc

        # 内容分发关联
        encoding_farm >> Edge(label="媒体文件") >> media_storage
        adaptive_streaming >> Edge(label="CDN分发") >> cloudfront
        qa_testing >> Edge(label="质量数据") >> analytics_db
        performance_monitoring >> Edge(label="性能指标") >> cloudwatch


if __name__ == "__main__":
    create_netflix_tech_stack_diagram(filename="netflix_tech_stack", outformat="png")
    create_netflix_tech_stack_diagram(filename="netflix_tech_stack", outformat="pdf")
