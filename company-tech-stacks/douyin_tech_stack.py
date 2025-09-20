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
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_douyin_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("抖音技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("移动应用"):
                douyin_mobile = Server("抖音 App")
                douyin_ios = Server("抖音 iOS")
                douyin_android = Server("抖音 Android")
                douyin_ipad = Server("抖音 iPad")
                
            with Cluster("Web 应用"):
                douyin_web = Server("抖音 Web")
                douyin_pc = Server("抖音 PC")
                douyin_h5 = Server("抖音 H5")
                
            with Cluster("小程序"):
                wechat_miniprogram = Server("微信小程序")
                alipay_miniprogram = Server("支付宝小程序")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("移动开发"):
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                java_android = Java("Java (Android)")
                objective_c = Server("Objective-C")
                
            with Cluster("Web 技术"):
                react = React("React")
                vue_js = React("Vue.js")
                typescript = JavaScript("TypeScript")
                next_js = React("Next.js")
                
            with Cluster("小程序技术"):
                taro = Server("Taro")
                uni_app = Server("uni-app")
                wechat_devtools = Server("微信开发者工具")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")
                metro = Server("Metro")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                go_lang = Go("Go")
                python = Python("Python")
                java = Java("Java")
                cpp = Server("C++")
                rust = Server("Rust")
                
            with Cluster("Web 框架"):
                gin = Server("Gin")
                echo = Server("Echo")
                django = Django("Django")
                spring_boot = Server("Spring Boot")
                actix = Server("Actix")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                grpc = Server("gRPC")
                graphql = Server("GraphQL")
                webhooks = Server("Webhooks")
                
            with Cluster("服务发现"):
                consul = Server("Consul")
                etcd = Server("etcd")
                zookeeper = Server("ZooKeeper")
                nacos = Server("Nacos")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                mysql = Server("MySQL")
                postgresql = PostgreSQL("PostgreSQL")
                tidb = Server("TiDB")
                
            with Cluster("NoSQL 数据库"):
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                hbase = Server("HBase")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                hazelcast = Server("Hazelcast")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                lucene = Server("Apache Lucene")
                
            with Cluster("图数据库"):
                neo4j = Server("Neo4j")
                janusgraph = Server("JanusGraph")

        # 音视频处理层
        with Cluster("音视频处理层"):
            with Cluster("视频上传"):
                video_upload = Server("Video Upload")
                chunked_upload = Server("Chunked Upload")
                resumable_upload = Server("Resumable Upload")
                
            with Cluster("视频转码"):
                transcoding_service = Server("Transcoding Service")
                ffmpeg = Server("FFmpeg")
                media_convert = Server("Media Convert")
                hardware_encoder = Server("Hardware Encoder")
                
            with Cluster("视频存储"):
                video_storage = Server("Video Storage")
                thumbnail_storage = Server("Thumbnail Storage")
                metadata_storage = Server("Metadata Storage")
                cdn_storage = Server("CDN Storage")
                
            with Cluster("音视频编解码"):
                h264_encoder = Server("H.264 Encoder")
                h265_encoder = Server("H.265 Encoder")
                aac_encoder = Server("AAC Encoder")
                opus_encoder = Server("Opus Encoder")
                
            with Cluster("实时特效"):
                real_time_filter = Server("Real-time Filter")
                beauty_filter = Server("Beauty Filter")
                sticker_overlay = Server("Sticker Overlay")
                ar_effects = Server("AR Effects")
                
            with Cluster("图形渲染"):
                opengl_es = Server("OpenGL ES")
                vulkan = Server("Vulkan")
                metal = Server("Metal")
                gpu_rendering = Server("GPU Rendering")

        # 推荐系统和AI层
        with Cluster("推荐系统和AI层"):
            with Cluster("推荐引擎"):
                recommendation_engine = Server("Recommendation Engine")
                content_based_filtering = Server("Content-Based Filtering")
                collaborative_filtering = Server("Collaborative Filtering")
                deep_learning_recs = Server("Deep Learning Recommendations")
                
            with Cluster("机器学习框架"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                xgboost = Server("XGBoost")
                
            with Cluster("自然语言处理"):
                nlp_models = Server("NLP Models")
                text_analysis = Server("Text Analysis")
                sentiment_analysis = Server("Sentiment Analysis")
                keyword_extraction = Server("Keyword Extraction")
                
            with Cluster("计算机视觉"):
                image_classification = Server("Image Classification")
                object_detection = Server("Object Detection")
                face_recognition = Server("Face Recognition")
                content_moderation = Server("Content Moderation")
                
            with Cluster("模型部署"):
                tensorflow_lite = Server("TensorFlow Lite")
                onnx = Server("ONNX")
                model_serving = Server("Model Serving")
                edge_inference = Server("Edge Inference")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                flink = Server("Apache Flink")
                kafka = Kafka("Apache Kafka")
                
            with Cluster("数据仓库"):
                data_warehouse = Server("Data Warehouse")
                clickhouse = Server("ClickHouse")
                druid = Server("Apache Druid")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                user_behavior_analysis = Server("User Behavior Analysis")
                content_performance = Server("Content Performance")
                engagement_metrics = Server("Engagement Metrics")
                
            with Cluster("数据可视化"):
                superset = Superset("Apache Superset")
                grafana = Grafana("Grafana")
                tableau = Server("Tableau")

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
                etcd_config = Server("etcd")
                consul_config = Server("Consul")
                vault = Vault("Vault")

        # 监控和日志层
        with Cluster("监控和日志层"):
            with Cluster("监控系统"):
                prometheus = Prometheus("Prometheus")
                grafana_monitoring = Grafana("Grafana")
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
                skywalking = Server("Apache SkyWalking")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                jwt = Server("JWT")
                sso = Server("Single Sign-On")
                
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
                spam_detection = Server("Spam Detection")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("版本控制"):
                git = Server("Git")
                github = Server("GitHub")
                gitlab = Server("GitLab")
                
            with Cluster("CI/CD"):
                jenkins = Server("Jenkins")
                gitlab_ci = Server("GitLab CI")
                github_actions = Server("GitHub Actions")
                tekton = Server("Tekton")
                
            with Cluster("测试工具"):
                junit = Server("JUnit")
                pytest = Server("pytest")
                selenium = Server("Selenium")
                fastbot = Server("Fastbot")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                checkstyle = Server("CheckStyle")
                findbugs = Server("FindBugs")
                eslint = Server("ESLint")

        # 连接关系
        # 客户端到前端技术
        users >> douyin_mobile
        users >> douyin_web
        users >> wechat_miniprogram
        users >> douyin_ios
        users >> douyin_android
        
        douyin_mobile >> swift_ios
        douyin_web >> react
        wechat_miniprogram >> taro
        douyin_ios >> kotlin_android
        douyin_android >> java_android

        # 前端技术到后端技术
        react >> gin
        vue_js >> echo
        typescript >> django
        next_js >> spring_boot
        swift_ios >> actix

        # 后端技术到数据存储
        go_lang >> gin
        python >> django
        java >> spring_boot
        gin >> mysql
        django >> mongodb
        rest_apis >> redis
        grpc >> elasticsearch

        # 数据存储连接
        mysql >> postgresql
        postgresql >> tidb
        mongodb >> cassandra
        cassandra >> hbase
        redis >> memcached
        memcached >> hazelcast
        elasticsearch >> solr
        solr >> lucene
        neo4j >> janusgraph

        # 音视频处理连接
        video_upload >> chunked_upload
        chunked_upload >> resumable_upload
        transcoding_service >> ffmpeg
        ffmpeg >> media_convert
        media_convert >> hardware_encoder
        video_storage >> thumbnail_storage
        thumbnail_storage >> metadata_storage
        metadata_storage >> cdn_storage
        h264_encoder >> h265_encoder
        h265_encoder >> aac_encoder
        aac_encoder >> opus_encoder
        real_time_filter >> beauty_filter
        beauty_filter >> sticker_overlay
        sticker_overlay >> ar_effects
        opengl_es >> vulkan
        vulkan >> metal
        metal >> gpu_rendering

        # 推荐系统和AI连接
        recommendation_engine >> content_based_filtering
        content_based_filtering >> collaborative_filtering
        collaborative_filtering >> deep_learning_recs
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> xgboost
        nlp_models >> text_analysis
        text_analysis >> sentiment_analysis
        sentiment_analysis >> keyword_extraction
        image_classification >> object_detection
        object_detection >> face_recognition
        face_recognition >> content_moderation
        tensorflow_lite >> onnx
        onnx >> model_serving
        model_serving >> edge_inference

        # 大数据分析连接
        hadoop >> spark
        spark >> flink
        flink >> kafka
        data_warehouse >> clickhouse
        clickhouse >> druid
        real_time_analytics >> user_behavior_analysis
        user_behavior_analysis >> content_performance
        content_performance >> engagement_metrics
        superset >> grafana
        grafana >> tableau

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd_config >> consul_config
        consul_config >> vault

        # 监控连接
        prometheus >> grafana_monitoring
        grafana_monitoring >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> skywalking

        # 安全连接
        oauth >> openid_connect
        openid_connect >> jwt
        jwt >> sso
        rbac >> abac
        abac >> content_ownership
        encryption >> key_management
        key_management >> privacy_controls
        content_policy >> age_restrictions
        age_restrictions >> community_guidelines
        community_guidelines >> spam_detection

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> tekton
        junit >> pytest
        pytest >> selenium
        selenium >> fastbot
        sonarqube >> checkstyle
        checkstyle >> findbugs
        findbugs >> eslint

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> docker
        redis >> Edge(label="缓存加速") >> mysql
        recommendation_engine >> Edge(label="智能推荐") >> tensorflow
        cdn_storage >> Edge(label="内容分发") >> nginx
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana_monitoring
        kafka >> Edge(label="实时数据") >> spark
        tensorflow_lite >> Edge(label="移动AI") >> edge_inference


if __name__ == "__main__":
    create_douyin_tech_stack_diagram(filename="douyin_tech_stack", outformat="png")
    create_douyin_tech_stack_diagram(filename="douyin_tech_stack", outformat="pdf")
