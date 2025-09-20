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
from diagrams.programming.language import Python, JavaScript, Java
from diagrams.programming.framework import React, Django, FastAPI
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS
# Facebook specific icons not available in diagrams library


def create_instagram_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Instagram 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("多平台客户端"):
                ios_app = Server("iOS App")
                android_app = Server("Android App")
                web_app = Server("Web 端")
                instagram_stories = Server("Instagram Stories")
                instagram_tv = Server("Instagram TV")
                instagram_reels = Server("Instagram Reels")

        # CDN和边缘计算
        with Cluster("CDN & 边缘计算"):
            with Cluster("内容分发网络"):
                cloudfront = CloudFront("CloudFront CDN")
                edge_cache = Storage("边缘缓存")
                image_optimization = Server("图像优化服务")
                
            with Cluster("负载均衡"):
                route53 = Route53("Route53 DNS")
                elb = ELB("负载均衡器")
                
            route53 >> elb >> cloudfront
            cloudfront >> edge_cache
            cloudfront >> image_optimization

        # API网关层
        with Cluster("API 网关层"):
            with Cluster("API管理"):
                api_gateway = Server("API Gateway")
                rate_limiter = Firewall("限流器")
                auth_gateway = Server("认证网关")
                
            with Cluster("请求路由"):
                load_balancer = Router("请求路由器")
                circuit_breaker = Server("断路器")
                
            api_gateway >> rate_limiter >> load_balancer
            auth_gateway >> circuit_breaker

        # 后端服务层
        with Cluster("后端服务层"):
            with Cluster("核心服务 (Python/Django)"):
                user_service = Django("用户服务")
                post_service = Django("帖子服务")
                story_service = Django("故事服务")
                feed_service = Django("动态流服务")
                
            with Cluster("媒体处理服务"):
                image_service = Python("图像处理服务")
                video_service = Python("视频处理服务")
                thumbnail_service = Python("缩略图服务")
                compression_service = Python("压缩服务")
                
            with Cluster("社交功能服务"):
                follow_service = Django("关注服务")
                like_service = Django("点赞服务")
                comment_service = Django("评论服务")
                message_service = Django("私信服务")
                
            with Cluster("推荐系统"):
                recommendation_engine = Python("推荐引擎")
                content_discovery = Python("内容发现")
                trending_service = Python("热门服务")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("用户数据"):
                user_db = PostgreSQL("用户数据库")
                user_cache = Redis("用户缓存")
                session_store = Redis("会话存储")
                
            with Cluster("内容数据"):
                post_db = Cassandra("帖子数据库")
                media_metadata = MongoDB("媒体元数据")
                content_index = SQL("内容索引")
                
            with Cluster("社交数据"):
                social_graph = Cassandra("社交图谱")
                interaction_data = Redis("互动数据")
                notification_queue = Kafka("通知队列")
                
            with Cluster("媒体存储"):
                media_storage = S3("媒体存储")
                thumbnail_cache = Storage("缩略图缓存")
                backup_storage = Ceph("备份存储")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据收集"):
                event_collector = Kinesis("事件收集器")
                log_processor = Server("日志处理器")
                metrics_collector = Server("指标收集器")
                
            with Cluster("数据处理"):
                spark_cluster = Spark("Spark 集群")
                hadoop_cluster = Hadoop("Hadoop 集群")
                etl_pipeline = Glue("ETL 管道")
                
            with Cluster("机器学习"):
                ml_platform = Python("ML 平台")
                content_recommendation = Python("内容推荐")
                user_behavior_analysis = Python("用户行为分析")
                spam_detection = Python("垃圾内容检测")
                
            with Cluster("数据仓库"):
                data_warehouse = EMR("数据仓库")
                analytics_db = Bigtable("分析数据库")
                
            event_collector >> spark_cluster >> data_warehouse
            log_processor >> hadoop_cluster >> analytics_db
            etl_pipeline >> ml_platform >> content_recommendation

        # 基础设施层
        with Cluster("基础设施层 (Meta/Facebook)"):
            with Cluster("计算资源"):
                meta_servers = Server("Meta 服务器集群")
                auto_scaling = Server("自动扩缩容")
                container_orchestration = Server("容器编排")
                
            with Cluster("容器化"):
                docker_containers = Server("Docker 容器")
                kubernetes = Server("Kubernetes")
                
            with Cluster("监控告警"):
                internal_monitoring = Server("内部监控系统")
                prometheus_monitor = Prometheus("Prometheus")
                grafana_dashboard = Grafana("Grafana")
                
            meta_servers >> auto_scaling >> docker_containers
            docker_containers >> kubernetes
            internal_monitoring >> prometheus_monitor >> grafana_dashboard

        # 安全层
        with Cluster("安全层"):
            with Cluster("认证授权"):
                oauth_service = Vault("OAuth 服务")
                jwt_service = Server("JWT 令牌服务")
                two_factor_auth = Server("双因素认证")
                
            with Cluster("内容安全"):
                content_moderation = Server("内容审核")
                spam_filter = Server("垃圾内容过滤")
                copyright_detection = Server("版权检测")
                
            with Cluster("数据安全"):
                encryption_service = Server("数据加密")
                privacy_controls = Server("隐私控制")
                
            oauth_service >> jwt_service >> two_factor_auth
            content_moderation >> spam_filter >> copyright_detection
            encryption_service >> privacy_controls

        # 实时功能层
        with Cluster("实时功能层"):
            with Cluster("实时通信"):
                websocket_gateway = Server("WebSocket 网关")
                real_time_notifications = Server("实时通知")
                live_streaming = Server("直播服务")
                
            with Cluster("实时数据处理"):
                stream_processor = Server("流处理器")
                real_time_analytics = Server("实时分析")
                event_sourcing = Server("事件溯源")
                
            websocket_gateway >> real_time_notifications
            live_streaming >> stream_processor >> real_time_analytics

        # 广告系统
        with Cluster("广告系统"):
            with Cluster("广告投放"):
                ad_server = Server("广告服务器")
                ad_targeting = Server("广告定向")
                ad_auction = Server("广告竞价")
                
            with Cluster("广告分析"):
                ad_analytics = Server("广告分析")
                conversion_tracking = Server("转化追踪")
                revenue_optimization = Server("收入优化")
                
            ad_server >> ad_targeting >> ad_auction
            ad_analytics >> conversion_tracking >> revenue_optimization

        # 连接关系
        # 客户端到CDN
        users >> ios_app
        users >> android_app
        users >> web_app
        users >> instagram_stories
        users >> instagram_tv
        users >> instagram_reels
        
        ios_app >> route53
        android_app >> route53
        web_app >> route53
        instagram_stories >> route53
        instagram_tv >> route53
        instagram_reels >> route53

        # CDN到API网关
        elb >> Edge(label="API请求") >> api_gateway
        api_gateway >> Edge(label="认证") >> auth_gateway
        auth_gateway >> Edge(label="路由") >> load_balancer

        # API网关到后端服务
        load_balancer >> Edge(label="用户请求") >> user_service
        load_balancer >> Edge(label="帖子请求") >> post_service
        load_balancer >> Edge(label="故事请求") >> story_service
        load_balancer >> Edge(label="动态流请求") >> feed_service

        # 后端服务到数据存储
        user_service >> Edge(label="用户数据") >> user_db
        user_service >> Edge(label="用户缓存") >> user_cache
        post_service >> Edge(label="帖子数据") >> post_db
        story_service >> Edge(label="故事数据") >> media_metadata
        feed_service >> Edge(label="动态流数据") >> content_index

        # 媒体处理关联
        post_service >> Edge(label="图像处理") >> image_service
        story_service >> Edge(label="视频处理") >> video_service
        image_service >> Edge(label="缩略图") >> thumbnail_service
        video_service >> Edge(label="压缩") >> compression_service

        # 社交功能关联
        follow_service >> Edge(label="社交图谱") >> social_graph
        like_service >> Edge(label="互动数据") >> interaction_data
        comment_service >> Edge(label="评论数据") >> post_db
        message_service >> Edge(label="私信数据") >> notification_queue

        # 推荐系统关联
        recommendation_engine >> Edge(label="推荐数据") >> content_discovery
        content_discovery >> Edge(label="热门内容") >> trending_service
        trending_service >> Edge(label="动态流") >> feed_service

        # 数据存储关联
        user_db >> user_cache
        post_db >> media_metadata
        social_graph >> interaction_data
        media_storage >> thumbnail_cache
        media_storage >> backup_storage

        # 大数据分析关联
        notification_queue >> Edge(label="事件数据") >> event_collector
        event_collector >> Edge(label="流处理") >> spark_cluster
        log_processor >> Edge(label="批处理") >> hadoop_cluster
        spark_cluster >> Edge(label="机器学习") >> ml_platform
        ml_platform >> Edge(label="内容推荐") >> content_recommendation

        # 基础设施支撑
        meta_servers >> Edge(label="运行环境") >> user_service
        meta_servers >> Edge(label="运行环境") >> post_service
        docker_containers >> Edge(label="容器化") >> story_service
        kubernetes >> Edge(label="编排") >> feed_service

        # 监控关联
        internal_monitoring >> Edge(label="监控") >> user_service
        internal_monitoring >> Edge(label="监控") >> post_service
        prometheus_monitor >> Edge(label="指标收集") >> story_service
        grafana_dashboard >> Edge(label="可视化") >> prometheus_monitor

        # 安全关联
        auth_gateway >> Edge(label="认证") >> oauth_service
        user_service >> Edge(label="授权") >> jwt_service
        api_gateway >> Edge(label="防护") >> content_moderation
        post_service >> Edge(label="内容审核") >> spam_filter

        # 实时功能关联
        websocket_gateway >> Edge(label="实时通知") >> real_time_notifications
        live_streaming >> Edge(label="直播数据") >> stream_processor
        stream_processor >> Edge(label="实时分析") >> real_time_analytics

        # 广告系统关联
        feed_service >> Edge(label="广告请求") >> ad_server
        ad_server >> Edge(label="广告定向") >> ad_targeting
        ad_analytics >> Edge(label="广告数据") >> conversion_tracking
        conversion_tracking >> Edge(label="收入数据") >> revenue_optimization


if __name__ == "__main__":
    create_instagram_tech_stack_diagram(filename="instagram_tech_stack", outformat="png")
    create_instagram_tech_stack_diagram(filename="instagram_tech_stack", outformat="pdf")
