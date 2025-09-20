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
from diagrams.onprem.inmemory import Redis, Memcached
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python, JavaScript, Java, Go
from diagrams.programming.framework import React, Django
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
from diagrams.gcp.compute import ComputeEngine, GKE, Run, Functions
from diagrams.gcp.database import Bigtable, Firestore, Spanner, SQL as GCP_SQL
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Dataproc
from diagrams.gcp.network import LoadBalancing, CDN, VPC
from diagrams.gcp.ml import AIPlatform, AutoML, VideoIntelligenceAPI


def create_youtube_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("YouTube 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                youtube_web = Server("YouTube Web")
                youtube_tv = Server("YouTube TV")
                youtube_music = Server("YouTube Music")
                youtube_kids = Server("YouTube Kids")
                youtube_gaming = Server("YouTube Gaming")
                
            with Cluster("移动应用"):
                youtube_mobile = Server("YouTube Mobile")
                youtube_music_mobile = Server("YouTube Music Mobile")
                youtube_tv_mobile = Server("YouTube TV Mobile")
                
            with Cluster("智能设备"):
                smart_tv = Server("Smart TV")
                chromecast = Server("Chromecast")
                android_tv = Server("Android TV")
                roku = Server("Roku")
                
            with Cluster("开发者平台"):
                youtube_api = Server("YouTube API")
                youtube_data_api = Server("YouTube Data API")
                youtube_analytics_api = Server("YouTube Analytics API")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                polymer = React("Polymer")
                angular = React("Angular")
                react_components = React("React Components")
                
            with Cluster("移动技术"):
                flutter = Server("Flutter")
                react_native = React("React Native")
                android_sdk = Server("Android SDK")
                ios_sdk = Server("iOS SDK")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                closure_compiler = Server("Closure Compiler")
                
            with Cluster("样式和UI"):
                material_design = Server("Material Design")
                sass = Server("Sass")
                css_framework = Server("CSS Framework")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                python = Python("Python")
                java = Java("Java")
                go_lang = Go("Go")
                javascript = JavaScript("JavaScript")
                cpp = Server("C++")
                
            with Cluster("Web 框架"):
                django = Django("Django")
                spring_boot = Server("Spring Boot")
                flask = Server("Flask")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                grpc = Server("gRPC")
                graphql = Server("GraphQL")
                
            with Cluster("服务发现"):
                consul = Server("Consul")
                etcd = Server("etcd")
                zookeeper = Server("ZooKeeper")

        # Google Cloud 基础设施层
        with Cluster("Google Cloud 基础设施层"):
            with Cluster("计算服务"):
                compute_engine = ComputeEngine("Compute Engine")
                gke = GKE("Google Kubernetes Engine")
                cloud_run = Run("Cloud Run")
                cloud_functions = Functions("Cloud Functions")
                app_engine = Server("App Engine")
                
            with Cluster("存储服务"):
                cloud_storage = GCS("Cloud Storage")
                persistent_disk = Server("Persistent Disk")
                cloud_filestore = Server("Cloud Filestore")
                
            with Cluster("数据库服务"):
                cloud_sql = GCP_SQL("Cloud SQL")
                firestore = Firestore("Firestore")
                bigtable = Bigtable("Bigtable")
                spanner = Spanner("Spanner")
                
            with Cluster("网络服务"):
                load_balancer = LoadBalancing("Cloud Load Balancing")
                cloud_cdn = CDN("Cloud CDN")
                cloud_vpc = VPC("VPC Network")
                cloud_nat = Server("Cloud NAT")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                mysql = Server("MySQL")
                postgresql = PostgreSQL("PostgreSQL")
                cloud_sql_db = GCP_SQL("Cloud SQL")
                
            with Cluster("NoSQL 数据库"):
                bigtable_storage = Bigtable("Bigtable")
                firestore_db = Firestore("Firestore")
                mongodb = MongoDB("MongoDB")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                cloud_memorystore = Server("Cloud Memorystore")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                cloud_search = Server("Cloud Search")

        # 视频处理和流媒体层
        with Cluster("视频处理和流媒体层"):
            with Cluster("视频上传"):
                upload_service = Server("Upload Service")
                chunked_upload = Server("Chunked Upload")
                resumable_upload = Server("Resumable Upload")
                
            with Cluster("视频转码"):
                transcoding_service = Server("Transcoding Service")
                ffmpeg = Server("FFmpeg")
                media_convert = Server("Media Convert")
                
            with Cluster("视频存储"):
                video_storage = Server("Video Storage")
                thumbnail_storage = Server("Thumbnail Storage")
                metadata_storage = Server("Metadata Storage")
                
            with Cluster("流媒体服务"):
                adaptive_streaming = Server("Adaptive Streaming")
                hls = Server("HLS (HTTP Live Streaming)")
                dash = Server("DASH (Dynamic Adaptive Streaming)")
                webrtc = Server("WebRTC")
                
            with Cluster("视频分析"):
                video_intelligence = VideoIntelligenceAPI("Video Intelligence")
                content_id = Server("Content ID")
                copyright_detection = Server("Copyright Detection")

        # 内容分发层
        with Cluster("内容分发层"):
            with Cluster("CDN 网络"):
                google_cdn = CDN("Google CDN")
                edge_caching = Server("Edge Caching")
                global_distribution = Server("Global Distribution")
                
            with Cluster("负载均衡"):
                global_lb = LoadBalancing("Global Load Balancer")
                regional_lb = LoadBalancing("Regional Load Balancer")
                ssl_termination = Server("SSL Termination")
                
            with Cluster("网络优化"):
                tcp_optimization = Server("TCP Optimization")
                http2 = Server("HTTP/2")
                quic = Server("QUIC Protocol")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据处理"):
                bigquery = BigQuery("BigQuery")
                dataflow = Dataflow("Dataflow")
                dataproc = Dataproc("Dataproc")
                beam = Server("Apache Beam")
                
            with Cluster("流处理"):
                pubsub = PubSub("Pub/Sub")
                cloud_dataflow = Dataflow("Cloud Dataflow")
                kafka = Kafka("Apache Kafka")
                
            with Cluster("数据仓库"):
                bigquery_warehouse = BigQuery("BigQuery Data Warehouse")
                cloud_dataprep = Server("Cloud Dataprep")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                user_behavior_analysis = Server("User Behavior Analysis")
                content_performance = Server("Content Performance")

        # AI/ML 和推荐系统层
        with Cluster("AI/ML 和推荐系统层"):
            with Cluster("机器学习框架"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                ai_platform = AIPlatform("AI Platform")
                
            with Cluster("推荐引擎"):
                recommendation_engine = Server("Recommendation Engine")
                content_filtering = Server("Content Filtering")
                collaborative_filtering = Server("Collaborative Filtering")
                deep_learning_recs = Server("Deep Learning Recommendations")
                
            with Cluster("自然语言处理"):
                nlp_models = Server("NLP Models")
                text_analysis = Server("Text Analysis")
                sentiment_analysis = Server("Sentiment Analysis")
                auto_ml = AutoML("AutoML")
                
            with Cluster("计算机视觉"):
                image_processing = Server("Image Processing")
                thumbnail_generation = Server("Thumbnail Generation")
                content_moderation = Server("Content Moderation")
                video_intelligence_ai = VideoIntelligenceAPI("Video Intelligence AI")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                google_identity = Server("Google Identity")
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                two_factor_auth = Server("Two-Factor Authentication")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                content_ownership = Server("Content Ownership")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                key_management = Server("Key Management")
                privacy_controls = Server("Privacy Controls")
                
            with Cluster("内容安全"):
                content_policy = Server("Content Policy")
                age_restrictions = Server("Age Restrictions")
                community_guidelines = Server("Community Guidelines")

        # 监控和日志层
        with Cluster("监控和日志层"):
            with Cluster("监控系统"):
                cloud_monitoring = Server("Cloud Monitoring")
                cloud_logging = Server("Cloud Logging")
                cloud_trace = Server("Cloud Trace")
                error_reporting = Server("Error Reporting")
                
            with Cluster("性能监控"):
                apm = Server("Application Performance Monitoring")
                real_user_monitoring = Server("Real User Monitoring")
                synthetic_monitoring = Server("Synthetic Monitoring")
                
            with Cluster("业务指标"):
                analytics_dashboard = Server("Analytics Dashboard")
                revenue_tracking = Server("Revenue Tracking")
                user_engagement = Server("User Engagement")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("版本控制"):
                git = Server("Git")
                github = Server("GitHub")
                gitlab = Server("GitLab")
                
            with Cluster("CI/CD"):
                cloud_build = Server("Cloud Build")
                jenkins = Server("Jenkins")
                spinnaker = Server("Spinnaker")
                
            with Cluster("测试工具"):
                junit = Server("JUnit")
                pytest = Server("pytest")
                selenium = Server("Selenium")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                code_review = Server("Code Review")
                static_analysis = Server("Static Analysis")

        # 连接关系
        # 客户端到前端技术
        users >> youtube_web
        users >> youtube_mobile
        users >> youtube_tv
        users >> youtube_music
        users >> smart_tv
        users >> chromecast
        
        youtube_web >> polymer
        youtube_web >> angular
        youtube_mobile >> flutter
        youtube_mobile >> react_native
        smart_tv >> android_tv
        chromecast >> roku

        # 前端技术到后端技术
        polymer >> django
        angular >> spring_boot
        flutter >> python
        react_native >> java
        webpack >> babel
        babel >> closure_compiler

        # 后端技术到Google Cloud
        django >> compute_engine
        spring_boot >> gke
        python >> cloud_run
        java >> cloud_functions
        rest_apis >> app_engine

        # Google Cloud连接
        compute_engine >> gke
        gke >> cloud_run
        cloud_run >> cloud_functions
        cloud_storage >> persistent_disk
        persistent_disk >> cloud_filestore
        cloud_sql >> firestore
        firestore >> bigtable
        bigtable >> spanner

        # 网络连接
        load_balancer >> cloud_cdn
        cloud_cdn >> cloud_vpc
        cloud_vpc >> cloud_nat

        # 数据存储连接
        mysql >> postgresql
        bigtable_storage >> firestore_db
        firestore_db >> mongodb
        redis >> memcached
        memcached >> cloud_memorystore
        elasticsearch >> solr
        solr >> cloud_search

        # 视频处理连接
        upload_service >> chunked_upload
        chunked_upload >> resumable_upload
        transcoding_service >> ffmpeg
        ffmpeg >> media_convert
        video_storage >> thumbnail_storage
        thumbnail_storage >> metadata_storage
        adaptive_streaming >> hls
        hls >> dash
        dash >> webrtc
        video_intelligence >> content_id
        content_id >> copyright_detection

        # 内容分发连接
        google_cdn >> edge_caching
        edge_caching >> global_distribution
        global_lb >> regional_lb
        regional_lb >> ssl_termination
        tcp_optimization >> http2
        http2 >> quic

        # 大数据分析连接
        bigquery >> dataflow
        dataflow >> dataproc
        dataproc >> beam
        pubsub >> cloud_dataflow
        cloud_dataflow >> kafka
        bigquery_warehouse >> cloud_dataprep
        real_time_analytics >> user_behavior_analysis
        user_behavior_analysis >> content_performance

        # AI/ML连接
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> ai_platform
        recommendation_engine >> content_filtering
        content_filtering >> collaborative_filtering
        collaborative_filtering >> deep_learning_recs
        nlp_models >> text_analysis
        text_analysis >> sentiment_analysis
        sentiment_analysis >> auto_ml
        image_processing >> thumbnail_generation
        thumbnail_generation >> content_moderation
        content_moderation >> video_intelligence_ai

        # 安全连接
        google_identity >> oauth
        oauth >> openid_connect
        openid_connect >> two_factor_auth
        rbac >> abac
        abac >> content_ownership
        encryption >> key_management
        key_management >> privacy_controls
        content_policy >> age_restrictions
        age_restrictions >> community_guidelines

        # 监控连接
        cloud_monitoring >> cloud_logging
        cloud_logging >> cloud_trace
        cloud_trace >> error_reporting
        apm >> real_user_monitoring
        real_user_monitoring >> synthetic_monitoring
        analytics_dashboard >> revenue_tracking
        revenue_tracking >> user_engagement

        # 开发工具连接
        git >> github
        github >> gitlab
        cloud_build >> jenkins
        jenkins >> spinnaker
        junit >> pytest
        pytest >> selenium
        sonarqube >> code_review
        code_review >> static_analysis

        # 跨层连接
        gke >> Edge(label="容器编排") >> cloud_run
        bigtable >> Edge(label="大数据存储") >> bigquery
        video_intelligence >> Edge(label="AI分析") >> recommendation_engine
        cloud_cdn >> Edge(label="全球分发") >> google_cdn
        oauth >> Edge(label="身份认证") >> rbac
        cloud_build >> Edge(label="CI/CD") >> gke
        cloud_monitoring >> Edge(label="监控") >> analytics_dashboard


if __name__ == "__main__":
    create_youtube_tech_stack_diagram(filename="youtube_tech_stack", outformat="png")
    create_youtube_tech_stack_diagram(filename="youtube_tech_stack", outformat="pdf")
