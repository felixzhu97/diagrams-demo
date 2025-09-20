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
from diagrams.programming.language import Python, JavaScript, Java, Scala
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


def create_x_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("X (Twitter) 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                x_web = Server("X Web")
                twitter_web = Server("Twitter Web")
                x_spaces = Server("X Spaces")
                x_live = Server("X Live")
                
            with Cluster("移动应用"):
                x_mobile = Server("X Mobile")
                twitter_mobile = Server("Twitter Mobile")
                x_ios = Server("X iOS")
                x_android = Server("X Android")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                embed_widgets = Server("Embed Widgets")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 框架"):
                react = React("React")
                backbone_js = React("Backbone.js")
                ember_js = React("Ember.js")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                grunt = Server("Grunt")
                
            with Cluster("样式和UI"):
                sass = Server("Sass")
                less = Server("Less")
                bootstrap = Server("Bootstrap")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                scala = Scala("Scala")
                java = Java("Java")
                python = Python("Python")
                ruby = Server("Ruby")
                javascript = JavaScript("JavaScript")
                
            with Cluster("Web 框架"):
                finagle = Server("Finagle")
                play_framework = Server("Play Framework")
                ruby_on_rails = Server("Ruby on Rails")
                spring_boot = Server("Spring Boot")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                graphql = Server("GraphQL")
                grpc = Server("gRPC")
                
            with Cluster("服务发现"):
                eureka = Server("Eureka")
                consul = Server("Consul")
                zookeeper = Server("ZooKeeper")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                mysql = Server("MySQL")
                postgresql = PostgreSQL("PostgreSQL")
                oracle_db = Server("Oracle Database")
                
            with Cluster("NoSQL 数据库"):
                cassandra = Cassandra("Cassandra")
                mongodb = MongoDB("MongoDB")
                dynamodb = Dynamodb("DynamoDB")
                
            with Cluster("图数据库"):
                neo4j = Server("Neo4j")
                titan = Server("Titan")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                hazelcast = Server("Hazelcast")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                lucene = Server("Apache Lucene")

        # 大数据和流处理层
        with Cluster("大数据和流处理层"):
            with Cluster("流处理"):
                kafka = Kafka("Apache Kafka")
                storm = Server("Apache Storm")
                heron = Server("Apache Heron")
                flink = Server("Apache Flink")
                
            with Cluster("批处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                hive = Server("Apache Hive")
                pig = Server("Apache Pig")
                
            with Cluster("数据仓库"):
                data_warehouse = Server("Data Warehouse")
                redshift = Server("Amazon Redshift")
                bigquery = Server("BigQuery")
                
            with Cluster("实时分析"):
                druid = Server("Apache Druid")
                kylin = Server("Apache Kylin")
                pinot = Server("Apache Pinot")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("容器化"):
                docker = Server("Docker")
                kubernetes = Server("Kubernetes")
                mesos = Server("Apache Mesos")
                aurora = Server("Apache Aurora")
                
            with Cluster("服务网格"):
                istio = Server("Istio")
                linkerd = Server("Linkerd")
                
            with Cluster("负载均衡"):
                nginx = Server("Nginx")
                haproxy = Server("HAProxy")
                envoy = Server("Envoy")
                
            with Cluster("配置管理"):
                etcd = Server("etcd")
                consul_config = Server("Consul")
                vault = Vault("Vault")

        # 监控和日志层
        with Cluster("监控和日志层"):
            with Cluster("监控系统"):
                prometheus = Prometheus("Prometheus")
                grafana = Grafana("Grafana")
                datadog = Server("Datadog")
                new_relic = Server("New Relic")
                
            with Cluster("日志系统"):
                kafka_logs = Kafka("Kafka Logs")
                elasticsearch_logs = Server("Elasticsearch Logs")
                logstash = Server("Logstash")
                fluentd = Server("Fluentd")
                
            with Cluster("追踪系统"):
                zipkin = Server("Zipkin")
                jaeger = Server("Jaeger")
                dapper = Server("Dapper")

        # AI/ML 和推荐系统层
        with Cluster("AI/ML 和推荐系统层"):
            with Cluster("机器学习框架"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                mlflow = Server("MLflow")
                
            with Cluster("推荐引擎"):
                recommendation_engine = Server("Recommendation Engine")
                content_filtering = Server("Content Filtering")
                collaborative_filtering = Server("Collaborative Filtering")
                deep_learning_recs = Server("Deep Learning Recommendations")
                
            with Cluster("自然语言处理"):
                nlp_models = Server("NLP Models")
                text_analysis = Server("Text Analysis")
                sentiment_analysis = Server("Sentiment Analysis")
                topic_modeling = Server("Topic Modeling")
                
            with Cluster("计算机视觉"):
                image_processing = Server("Image Processing")
                face_recognition = Server("Face Recognition")
                object_detection = Server("Object Detection")
                content_moderation = Server("Content Moderation")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                saml = Server("SAML")
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
                spam_detection = Server("Spam Detection")
                abuse_detection = Server("Abuse Detection")
                hate_speech_detection = Server("Hate Speech Detection")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("版本控制"):
                git = Server("Git")
                github = Server("GitHub")
                gitlab = Server("GitLab")
                
            with Cluster("CI/CD"):
                jenkins = Server("Jenkins")
                bamboo = Server("Bamboo")
                circleci = Server("CircleCI")
                travis_ci = Server("Travis CI")
                
            with Cluster("测试工具"):
                junit = Server("JUnit")
                scalatest = Server("ScalaTest")
                selenium = Server("Selenium")
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                checkstyle = Server("CheckStyle")
                findbugs = Server("FindBugs")
                scalastyle = Server("ScalaStyle")

        # 连接关系
        # 客户端到前端技术
        users >> x_web
        users >> x_mobile
        users >> twitter_web
        users >> x_spaces
        users >> x_live
        
        x_web >> react
        x_web >> backbone_js
        x_mobile >> react_native
        x_mobile >> swift_ios
        x_mobile >> kotlin_android

        # 前端技术到后端技术
        react >> finagle
        backbone_js >> play_framework
        react_native >> ruby_on_rails
        webpack >> babel
        babel >> grunt

        # 后端技术到数据存储
        scala >> finagle
        java >> spring_boot
        finagle >> mysql
        play_framework >> cassandra
        rest_apis >> redis
        graphql >> neo4j

        # 数据存储连接
        mysql >> postgresql
        cassandra >> mongodb
        mongodb >> dynamodb
        neo4j >> titan
        redis >> memcached
        memcached >> hazelcast
        elasticsearch >> solr
        solr >> lucene

        # 大数据和流处理连接
        kafka >> storm
        storm >> heron
        heron >> flink
        hadoop >> spark
        spark >> hive
        hive >> pig
        data_warehouse >> redshift
        redshift >> bigquery
        druid >> kylin
        kylin >> pinot

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> mesos
        mesos >> aurora
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd >> consul_config
        consul_config >> vault

        # 监控和日志连接
        prometheus >> grafana
        grafana >> datadog
        datadog >> new_relic
        kafka_logs >> elasticsearch_logs
        elasticsearch_logs >> logstash
        logstash >> fluentd
        zipkin >> jaeger
        jaeger >> dapper

        # AI/ML连接
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> mlflow
        recommendation_engine >> content_filtering
        content_filtering >> collaborative_filtering
        collaborative_filtering >> deep_learning_recs
        nlp_models >> text_analysis
        text_analysis >> sentiment_analysis
        sentiment_analysis >> topic_modeling
        image_processing >> face_recognition
        face_recognition >> object_detection
        object_detection >> content_moderation

        # 安全连接
        oauth >> openid_connect
        openid_connect >> saml
        saml >> two_factor_auth
        rbac >> abac
        abac >> content_ownership
        encryption >> key_management
        key_management >> privacy_controls
        content_policy >> spam_detection
        spam_detection >> abuse_detection
        abuse_detection >> hate_speech_detection

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> bamboo
        bamboo >> circleci
        circleci >> travis_ci
        junit >> scalatest
        scalatest >> selenium
        selenium >> cypress
        sonarqube >> checkstyle
        checkstyle >> findbugs
        findbugs >> scalastyle

        # 跨层连接
        finagle >> Edge(label="微服务") >> kubernetes
        kafka >> Edge(label="流数据") >> storm
        cassandra >> Edge(label="分布式存储") >> redis
        elasticsearch >> Edge(label="搜索服务") >> lucene
        recommendation_engine >> Edge(label="推荐算法") >> tensorflow
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> docker
        prometheus >> Edge(label="监控") >> grafana


if __name__ == "__main__":
    create_x_tech_stack_diagram(filename="x_tech_stack", outformat="png")
    create_x_tech_stack_diagram(filename="x_tech_stack", outformat="pdf")
