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
from diagrams.aws.compute import EC2, Lambda, ECS, EKS, Fargate, Batch, Lightsail
from diagrams.aws.database import RDS, Dynamodb, Redshift, Aurora, ElastiCache, DocumentDB, Neptune
from diagrams.aws.storage import S3, EBS, EFS, FSx, Backup, StorageGateway
from diagrams.aws.network import CloudFront, Route53, ELB, VPC, DirectConnect, APIGateway
from diagrams.aws.analytics import Kinesis, Glue, EMR, Athena, Quicksight, DataPipeline
from diagrams.aws.management import Cloudformation, Cloudwatch, Cloudtrail, Config, TrustedAdvisor, SystemsManager
from diagrams.aws.security import IAM, KMS, SecretsManager, WAF, Shield, Guardduty, Inspector
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions, MQ, Appsync
from diagrams.aws.ml import Sagemaker, Rekognition, Comprehend, Translate, Polly, Lex
from diagrams.aws.mobile import Amplify, DeviceFarm, Pinpoint
from diagrams.aws.iot import IotCore, IotDeviceManagement, IotAnalytics, IotEvents
from diagrams.aws.general import General, Users as AWSUsers, Client


def create_spotify_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Spotify 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                spotify_web = Server("Spotify Web")
                spotify_for_artists = Server("Spotify for Artists")
                spotify_for_podcasters = Server("Spotify for Podcasters")
                spotify_ad_studio = Server("Spotify Ad Studio")
                
            with Cluster("移动应用"):
                spotify_mobile = Server("Spotify Mobile")
                spotify_ios = Server("Spotify iOS")
                spotify_android = Server("Spotify Android")
                
            with Cluster("桌面应用"):
                spotify_desktop = Server("Spotify Desktop")
                spotify_windows = Server("Spotify Windows")
                spotify_mac = Server("Spotify macOS")
                spotify_linux = Server("Spotify Linux")
                
            with Cluster("智能设备"):
                spotify_connect = Server("Spotify Connect")
                smart_speakers = Server("Smart Speakers")
                car_integration = Server("Car Integration")
                gaming_consoles = Server("Gaming Consoles")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                javascript = JavaScript("JavaScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                typescript = Server("TypeScript")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("桌面技术"):
                electron = Server("Electron")
                cpp = Server("C++")
                qt = Server("Qt")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                metro = Server("Metro")
                
            with Cluster("UI组件库"):
                spotify_ui = Server("Spotify UI")
                lottie = Server("Lottie")
                custom_components = Server("Custom Components")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                java = Java("Java")
                python = Python("Python")
                javascript_backend = JavaScript("JavaScript")
                go = Go("Go")
                scala = Server("Scala")
                cpp_backend = Server("C++")
                
            with Cluster("Web 框架"):
                apollo = Server("Apollo")
                spring_boot = Server("Spring Boot")
                django = Django("Django")
                express = Server("Express.js")
                gin = Server("Gin")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                graphql = Server("GraphQL")
                grpc = Server("gRPC")
                webhooks = Server("Webhooks")
                
            with Cluster("服务发现"):
                consul = Server("Consul")
                etcd = Server("etcd")
                zookeeper = Server("ZooKeeper")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                postgresql = PostgreSQL("PostgreSQL")
                mysql = Server("MySQL")
                aurora = Aurora("Amazon Aurora")
                
            with Cluster("NoSQL 数据库"):
                cassandra = Cassandra("Apache Cassandra")
                mongodb = MongoDB("MongoDB")
                dynamodb = Dynamodb("DynamoDB")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                elasticache = ElastiCache("ElastiCache")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                
            with Cluster("数据仓库"):
                bigquery = Server("BigQuery")
                redshift = Redshift("Amazon Redshift")
                snowflake = Server("Snowflake")

        # 微服务层
        with Cluster("微服务层"):
            with Cluster("音乐服务"):
                catalog_service = Server("Catalog Service")
                metadata_service = Server("Metadata Service")
                audio_service = Server("Audio Service")
                streaming_service = Server("Streaming Service")
                
            with Cluster("用户服务"):
                user_service = Server("User Service")
                authentication_service = Server("Authentication Service")
                profile_service = Server("Profile Service")
                social_service = Server("Social Service")
                
            with Cluster("播放服务"):
                playback_service = Server("Playback Service")
                queue_service = Server("Queue Service")
                session_service = Server("Session Service")
                sync_service = Server("Sync Service")
                
            with Cluster("推荐服务"):
                recommendation_service = Server("Recommendation Service")
                discovery_service = Server("Discovery Service")
                personalization_service = Server("Personalization Service")
                ml_service = Server("ML Service")

        # 推荐系统层
        with Cluster("推荐系统层"):
            with Cluster("机器学习"):
                latent_factor_models = Server("Latent Factor Models")
                collaborative_filtering = Server("Collaborative Filtering")
                content_based = Server("Content-based Filtering")
                deep_learning = Server("Deep Learning")
                
            with Cluster("相似性搜索"):
                annoy = Server("Annoy")
                faiss = Server("Faiss")
                elasticsearch_search = Server("Elasticsearch Search")
                
            with Cluster("特征工程"):
                feature_store = Server("Feature Store")
                feature_pipeline = Server("Feature Pipeline")
                feature_monitoring = Server("Feature Monitoring")
                
            with Cluster("模型服务"):
                model_serving = Server("Model Serving")
                a_b_testing = Server("A/B Testing")
                model_monitoring = Server("Model Monitoring")

        # 数据处理层
        with Cluster("数据处理层"):
            with Cluster("大数据处理"):
                scio = Server("Scio")
                apache_beam = Server("Apache Beam")
                spark = Spark("Apache Spark")
                hadoop = Hadoop("Apache Hadoop")
                
            with Cluster("数据管道"):
                luigi = Server("Luigi")
                airflow = Airflow("Apache Airflow")
                dataflow = Server("Google Dataflow")
                
            with Cluster("流处理"):
                kafka = Kafka("Apache Kafka")
                kinesis = Kinesis("Amazon Kinesis")
                flink = Server("Apache Flink")
                
            with Cluster("数据存储"):
                sparkey = Server("Sparkey")
                hdfs = Server("HDFS")
                gcs = Server("Google Cloud Storage")

        # 音频处理层
        with Cluster("音频处理层"):
            with Cluster("音频编码"):
                opus = Server("Opus")
                aac = Server("AAC")
                mp3 = Server("MP3")
                ogg = Server("Ogg Vorbis")
                
            with Cluster("音频分析"):
                audio_fingerprinting = Server("Audio Fingerprinting")
                music_analysis = Server("Music Analysis")
                tempo_detection = Server("Tempo Detection")
                
            with Cluster("音频流媒体"):
                adaptive_streaming = Server("Adaptive Streaming")
                cdn_optimization = Server("CDN Optimization")
                bandwidth_adaptation = Server("Bandwidth Adaptation")
                
            with Cluster("音频质量"):
                quality_control = Server("Quality Control")
                audio_enhancement = Server("Audio Enhancement")
                noise_reduction = Server("Noise Reduction")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                jwt = Server("JWT")
                saml = Server("SAML")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                permission_management = Server("Permission Management")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                key_management = Server("Key Management")
                data_masking = Server("Data Masking")
                
            with Cluster("版权保护"):
                drm = Server("Digital Rights Management")
                content_protection = Server("Content Protection")
                license_management = Server("License Management")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("容器化"):
                docker = Server("Docker")
                kubernetes = Server("Kubernetes")
                helm = Server("Helm")
                
            with Cluster("服务网格"):
                istio = Server("Istio")
                linkerd = Server("Linkerd")
                
            with Cluster("负载均衡"):
                nginx = Server("Nginx")
                haproxy = Server("HAProxy")
                envoy = Server("Envoy")
                
            with Cluster("配置管理"):
                consul_config = Server("Consul")
                etcd_config = Server("etcd")
                vault = Vault("Vault")

        # 云服务层
        with Cluster("云服务层"):
            with Cluster("计算服务"):
                gcp_compute = Server("Google Compute Engine")
                aws_ec2 = EC2("Amazon EC2")
                kubernetes_engine = Server("Google Kubernetes Engine")
                
            with Cluster("存储服务"):
                gcs_storage = Server("Google Cloud Storage")
                s3_storage = S3("Amazon S3")
                cloud_sql = Server("Google Cloud SQL")
                
            with Cluster("网络服务"):
                cloud_cdn = Server("Google Cloud CDN")
                cloudfront = CloudFront("CloudFront")
                load_balancer = Server("Google Load Balancer")
                
            with Cluster("数据库服务"):
                bigtable = Server("Google Bigtable")
                firestore = Server("Cloud Firestore")
                spanner = Server("Cloud Spanner")

        # 监控和日志层
        with Cluster("监控和日志层"):
            with Cluster("监控系统"):
                prometheus = Prometheus("Prometheus")
                grafana = Grafana("Grafana")
                datadog = Server("Datadog")
                new_relic = Server("New Relic")
                
            with Cluster("日志系统"):
                elasticsearch_logs = Server("Elasticsearch Logs")
                logstash = Server("Logstash")
                kibana = Server("Kibana")
                fluentd = Server("Fluentd")
                
            with Cluster("追踪系统"):
                zipkin = Server("Zipkin")
                jaeger = Server("Jaeger")
                dapper = Server("Dapper")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("开发者平台"):
                backstage = Server("Backstage")
                golden_paths = Server("Golden Paths")
                tingle_cicd = Server("Tingle CI/CD")
                
            with Cluster("版本控制"):
                git = Server("Git")
                github = Server("GitHub")
                gitlab = Server("GitLab")
                
            with Cluster("CI/CD"):
                jenkins = Server("Jenkins")
                gitlab_ci = Server("GitLab CI")
                github_actions = Server("GitHub Actions")
                circleci = Server("CircleCI")
                
            with Cluster("测试工具"):
                jest = Server("Jest")
                pytest = Server("pytest")
                selenium = Server("Selenium")
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                eslint = Server("ESLint")
                sonarqube = Server("SonarQube")
                test_certification = Server("Test Certification")

        # 连接关系
        # 客户端到前端技术
        users >> spotify_web
        users >> spotify_mobile
        users >> spotify_desktop
        users >> spotify_connect
        
        spotify_web >> react
        spotify_mobile >> react_native
        spotify_desktop >> electron
        spotify_connect >> smart_speakers

        # 前端技术到后端技术
        react >> apollo
        javascript >> spring_boot
        react_native >> express
        electron >> gin

        # 后端技术到数据存储
        java >> apollo
        python >> django
        javascript_backend >> express
        apollo >> cassandra
        spring_boot >> postgresql
        django >> redis
        express >> elasticsearch

        # 数据存储连接
        postgresql >> mysql
        mysql >> aurora
        cassandra >> mongodb
        mongodb >> dynamodb
        redis >> memcached
        memcached >> elasticache
        elasticsearch >> solr
        bigquery >> redshift
        redshift >> snowflake

        # 微服务连接
        catalog_service >> metadata_service
        metadata_service >> audio_service
        audio_service >> streaming_service
        user_service >> authentication_service
        authentication_service >> profile_service
        profile_service >> social_service
        playback_service >> queue_service
        queue_service >> session_service
        session_service >> sync_service
        recommendation_service >> discovery_service
        discovery_service >> personalization_service
        personalization_service >> ml_service

        # 推荐系统连接
        latent_factor_models >> collaborative_filtering
        collaborative_filtering >> content_based
        content_based >> deep_learning
        annoy >> faiss
        faiss >> elasticsearch_search
        feature_store >> feature_pipeline
        feature_pipeline >> feature_monitoring
        model_serving >> a_b_testing
        a_b_testing >> model_monitoring

        # 数据处理连接
        scio >> apache_beam
        apache_beam >> spark
        spark >> hadoop
        luigi >> airflow
        airflow >> dataflow
        kafka >> kinesis
        kinesis >> flink
        sparkey >> hdfs
        hdfs >> gcs

        # 音频处理连接
        opus >> aac
        aac >> mp3
        mp3 >> ogg
        audio_fingerprinting >> music_analysis
        music_analysis >> tempo_detection
        adaptive_streaming >> cdn_optimization
        cdn_optimization >> bandwidth_adaptation
        quality_control >> audio_enhancement
        audio_enhancement >> noise_reduction

        # 安全和身份连接
        oauth >> openid_connect
        openid_connect >> jwt
        jwt >> saml
        rbac >> abac
        abac >> permission_management
        encryption >> key_management
        key_management >> data_masking
        drm >> content_protection
        content_protection >> license_management

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        consul_config >> etcd_config
        etcd_config >> vault

        # 云服务连接
        gcp_compute >> aws_ec2
        aws_ec2 >> kubernetes_engine
        gcs_storage >> s3_storage
        s3_storage >> cloud_sql
        cloud_cdn >> cloudfront
        cloudfront >> load_balancer
        bigtable >> firestore
        firestore >> spanner

        # 监控连接
        prometheus >> grafana
        grafana >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> dapper

        # 开发工具连接
        backstage >> golden_paths
        golden_paths >> tingle_cicd
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> circleci
        jest >> pytest
        pytest >> selenium
        selenium >> cypress
        eslint >> sonarqube
        sonarqube >> test_certification

        # 跨层连接
        apollo >> Edge(label="后端框架") >> cassandra
        scio >> Edge(label="数据处理") >> apache_beam
        annoy >> Edge(label="相似性搜索") >> latent_factor_models
        backstage >> Edge(label="开发者平台") >> golden_paths
        spotify_connect >> Edge(label="设备连接") >> smart_speakers
        opus >> Edge(label="音频编码") >> adaptive_streaming
        prometheus >> Edge(label="监控") >> grafana
        drm >> Edge(label="版权保护") >> content_protection


if __name__ == "__main__":
    create_spotify_tech_stack_diagram(filename="spotify_tech_stack", outformat="png")
    create_spotify_tech_stack_diagram(filename="spotify_tech_stack", outformat="pdf")
