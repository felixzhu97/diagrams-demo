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
from diagrams.programming.language import Go, Python, Java, JavaScript
from diagrams.programming.framework import React, Django
from diagrams.gcp.compute import ComputeEngine, GKE, Run, Functions
from diagrams.gcp.database import Bigtable, Firestore, Spanner, SQL
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Dataproc
# GCP specific icons not fully available in diagrams library
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront


def create_google_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Google 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 服务"):
                google_search = Server("Google Search")
                gmail = Server("Gmail")
                youtube = Server("YouTube")
                google_drive = Server("Google Drive")
                google_maps = Server("Google Maps")
                google_photos = Server("Google Photos")
                
            with Cluster("移动应用"):
                android_apps = Server("Android Apps")
                chrome_mobile = Server("Chrome Mobile")
                
            with Cluster("开发者工具"):
                chrome_devtools = Server("Chrome DevTools")
                firebase_console = Server("Firebase Console")

        # 前端层
        with Cluster("前端层"):
            with Cluster("Web 技术"):
                angular = React("Angular")
                polymer = React("Polymer")
                flutter_web = React("Flutter Web")
                
            with Cluster("移动技术"):
                flutter = Server("Flutter")
                android_sdk = Server("Android SDK")
                kotlin = Server("Kotlin")
                
            with Cluster("浏览器引擎"):
                blink = Server("Blink")
                v8_engine = Server("V8 Engine")
                chromium = Server("Chromium")

        # 编程语言层
        with Cluster("编程语言层"):
            with Cluster("主要语言"):
                go_lang = Go("Go")
                java_lang = Java("Java")
                cpp = Server("C++")
                
            with Cluster("脚本语言"):
                python = Python("Python")
                javascript = JavaScript("JavaScript")
                typescript = JavaScript("TypeScript")
                
            with Cluster("系统语言"):
                rust = Server("Rust")
                dart = Server("Dart")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("分布式存储"):
                gfs = Server("Google File System (GFS)")
                colossus = Server("Colossus")
                
            with Cluster("分布式计算"):
                borg = Server("Borg")
                omega = Server("Omega")
                kubernetes = GKE("Kubernetes")
                
            with Cluster("分布式数据库"):
                bigtable_internal = Bigtable("Bigtable")
                spanner_internal = Spanner("Spanner")
                megastore = Server("Megastore")
                
            with Cluster("消息队列"):
                pubsub_internal = PubSub("Pub/Sub")
                chubby = Server("Chubby")

        # 云服务层 (GCP)
        with Cluster("云服务层 (Google Cloud Platform)"):
            with Cluster("计算服务"):
                compute_engine = ComputeEngine("Compute Engine")
                gke_service = GKE("Google Kubernetes Engine")
                cloud_run = Run("Cloud Run")
                cloud_functions = Functions("Cloud Functions")
                
            with Cluster("存储服务"):
                cloud_storage = GCS("Cloud Storage")
                persistent_disk = Server("Persistent Disk")
                cloud_filestore = Server("Cloud Filestore")
                
            with Cluster("数据库服务"):
                cloud_sql = SQL("Cloud SQL")
                firestore_db = Firestore("Firestore")
                bigtable_cloud = Bigtable("Cloud Bigtable")
                spanner_cloud = Spanner("Cloud Spanner")
                
            with Cluster("网络服务"):
                load_balancer = Server("Cloud Load Balancing")
                cloud_cdn = Server("Cloud CDN")
                cloud_vpc = Server("VPC Network")
                
            with Cluster("AI/ML 服务"):
                ai_platform = Server("AI Platform")
                automl = Server("AutoML")
                dialogflow_service = Server("Dialogflow")
                tensorflow_cloud = Functions("TensorFlow Cloud")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据处理"):
                bigquery = BigQuery("BigQuery")
                dataflow = Dataflow("Dataflow")
                dataproc = Dataproc("Dataproc")
                beam = Server("Apache Beam")
                
            with Cluster("流处理"):
                pubsub_streaming = PubSub("Pub/Sub Streaming")
                cloud_dataflow = Dataflow("Cloud Dataflow")
                
            with Cluster("数据仓库"):
                bigquery_warehouse = BigQuery("BigQuery Data Warehouse")
                cloud_dataprep = Server("Cloud Dataprep")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                keras = Server("Keras")
                pytorch = Server("PyTorch")
                jax = Server("JAX")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("CI/CD"):
                cloud_build = Server("Cloud Build")
                container_registry = Server("Container Registry")
                artifact_registry = Server("Artifact Registry")
                
            with Cluster("监控日志"):
                cloud_monitoring = Server("Cloud Monitoring")
                cloud_logging = Server("Cloud Logging")
                cloud_trace = Server("Cloud Trace")
                
            with Cluster("开发环境"):
                cloud_shell = Server("Cloud Shell")
                cloud_code = Server("Cloud Code")
                firebase_tools = Server("Firebase Tools")

        # Firebase 生态
        with Cluster("Firebase 生态"):
            with Cluster("后端服务"):
                firebase_auth = Server("Firebase Auth")
                firebase_firestore = Firestore("Firebase Firestore")
                firebase_storage = Server("Firebase Storage")
                firebase_functions = Functions("Firebase Functions")
                
            with Cluster("移动服务"):
                firebase_analytics = Server("Firebase Analytics")
                firebase_crashlytics = Server("Firebase Crashlytics")
                firebase_messaging = Server("Firebase Messaging")
                firebase_remote_config = Server("Firebase Remote Config")
                
            with Cluster("测试工具"):
                firebase_test_lab = Server("Firebase Test Lab")
                firebase_app_distribution = Server("Firebase App Distribution")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份管理"):
                google_identity = Server("Google Identity")
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                
            with Cluster("安全服务"):
                cloud_kms = Server("Cloud KMS")
                cloud_security_scanner = Server("Cloud Security Scanner")
                binary_authorization = Server("Binary Authorization")
                
            with Cluster("合规性"):
                cloud_audit_logs = Server("Cloud Audit Logs")
                access_transparency = Server("Access Transparency")

        # 连接关系
        # 客户端到Web服务
        users >> google_search
        users >> gmail
        users >> youtube
        users >> google_drive
        users >> google_maps
        users >> google_photos
        users >> android_apps
        users >> chrome_mobile

        # Web服务到前端技术
        google_search >> angular
        gmail >> polymer
        youtube >> flutter_web
        google_drive >> angular
        google_maps >> polymer

        # 前端技术到编程语言
        angular >> typescript
        polymer >> javascript
        flutter >> dart
        android_sdk >> java_lang
        android_sdk >> kotlin

        # 编程语言到基础设施
        go_lang >> borg
        java_lang >> kubernetes
        cpp >> gfs
        python >> bigtable_internal

        # 基础设施连接
        gfs >> colossus
        borg >> omega >> kubernetes
        bigtable_internal >> spanner_internal >> megastore
        pubsub_internal >> chubby

        # 云服务连接
        compute_engine >> gke_service
        gke_service >> cloud_run
        cloud_run >> cloud_functions
        cloud_storage >> persistent_disk
        cloud_storage >> cloud_filestore

        # 数据库连接
        cloud_sql >> firestore_db
        firestore_db >> bigtable_cloud
        bigtable_cloud >> spanner_cloud

        # 网络连接
        load_balancer >> cloud_cdn
        cloud_cdn >> cloud_vpc

        # AI/ML连接
        ai_platform >> automl
        automl >> dialogflow_service
        dialogflow_service >> tensorflow_cloud

        # 大数据分析连接
        bigquery >> dataflow
        dataflow >> dataproc
        dataproc >> beam
        pubsub_streaming >> cloud_dataflow
        bigquery_warehouse >> cloud_dataprep

        # 机器学习连接
        tensorflow >> keras
        keras >> pytorch
        pytorch >> jax

        # 开发工具连接
        cloud_build >> container_registry
        container_registry >> artifact_registry
        cloud_monitoring >> cloud_logging
        cloud_logging >> cloud_trace

        # Firebase连接
        firebase_auth >> firebase_firestore
        firebase_firestore >> firebase_storage
        firebase_storage >> firebase_functions
        firebase_analytics >> firebase_crashlytics
        firebase_messaging >> firebase_remote_config

        # 安全连接
        google_identity >> oauth
        oauth >> openid_connect
        cloud_kms >> cloud_security_scanner
        cloud_security_scanner >> binary_authorization

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> gke_service
        bigtable_internal >> Edge(label="数据库服务") >> bigtable_cloud
        tensorflow >> Edge(label="ML服务") >> ai_platform
        firebase_firestore >> Edge(label="后端服务") >> firestore_db
        google_identity >> Edge(label="身份管理") >> oauth
        cloud_build >> Edge(label="CI/CD") >> cloud_functions


if __name__ == "__main__":
    create_google_tech_stack_diagram(filename="google_tech_stack", outformat="png")
    create_google_tech_stack_diagram(filename="google_tech_stack", outformat="pdf")
