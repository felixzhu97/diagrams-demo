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


def create_linkedin_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("LinkedIn 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球职场用户")
            
            with Cluster("Web 应用"):
                linkedin_web = Server("LinkedIn Web")
                linkedin_learning = Server("LinkedIn Learning")
                linkedin_sales_navigator = Server("Sales Navigator")
                linkedin_recruiter = Server("LinkedIn Recruiter")
                
            with Cluster("移动应用"):
                linkedin_mobile = Server("LinkedIn Mobile")
                linkedin_learning_mobile = Server("LinkedIn Learning Mobile")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 框架"):
                ember_js = React("Ember.js")
                dust_js = React("Dust.js")
                react_components = React("React Components")
                
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
                java = Java("Java")
                scala = Scala("Scala")
                python = Python("Python")
                javascript = JavaScript("JavaScript")
                
            with Cluster("Web 框架"):
                play_framework = Server("Play Framework")
                spring_boot = Server("Spring Boot")
                finagle = Server("Finagle")
                
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
                voldemort = Server("Voldemort")
                espresso = Server("Espresso")
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                
            with Cluster("图数据库"):
                neo4j = Server("Neo4j")
                titan = Server("Titan")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                hazelcast = Server("Hazelcast")
                
            with Cluster("搜索引擎"):
                galene = Server("Galene")
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")

        # 大数据和流处理层
        with Cluster("大数据和流处理层"):
            with Cluster("流处理"):
                kafka = Kafka("Apache Kafka")
                samza = Server("Apache Samza")
                storm = Server("Apache Storm")
                
            with Cluster("批处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                hive = Server("Apache Hive")
                
            with Cluster("数据仓库"):
                data_warehouse = Server("Data Warehouse")
                teradata = Server("Teradata")
                vertica = Server("Vertica")
                
            with Cluster("实时分析"):
                druid = Server("Apache Druid")
                pinot = Server("Apache Pinot")
                kylin = Server("Apache Kylin")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("容器化"):
                docker = Server("Docker")
                kubernetes = Server("Kubernetes")
                mesos = Server("Apache Mesos")
                
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
                ingraphs = Server("InGraphs")
                prometheus = Prometheus("Prometheus")
                grafana = Grafana("Grafana")
                
            with Cluster("日志系统"):
                kafka_logs = Kafka("Kafka Logs")
                elasticsearch_logs = Server("Elasticsearch Logs")
                logstash = Server("Logstash")
                
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
                
            with Cluster("推荐引擎"):
                recommendation_engine = Server("Recommendation Engine")
                content_filtering = Server("Content Filtering")
                collaborative_filtering = Server("Collaborative Filtering")
                
            with Cluster("自然语言处理"):
                nlp_models = Server("NLP Models")
                text_analysis = Server("Text Analysis")
                sentiment_analysis = Server("Sentiment Analysis")
                
            with Cluster("计算机视觉"):
                image_processing = Server("Image Processing")
                face_recognition = Server("Face Recognition")
                object_detection = Server("Object Detection")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                saml = Server("SAML")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                data_masking = Server("Data Masking")
                privacy_controls = Server("Privacy Controls")
                
            with Cluster("网络安全"):
                waf = Server("Web Application Firewall")
                ddos_protection = Server("DDoS Protection")
                network_security = Server("Network Security")

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
                
            with Cluster("测试工具"):
                junit = Server("JUnit")
                testng = Server("TestNG")
                selenium = Server("Selenium")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                checkstyle = Server("Checkstyle")
                findbugs = Server("FindBugs")

        # 连接关系
        # 客户端到前端技术
        users >> linkedin_web
        users >> linkedin_mobile
        users >> linkedin_learning
        users >> linkedin_sales_navigator
        
        linkedin_web >> ember_js
        linkedin_web >> dust_js
        linkedin_mobile >> react_native
        linkedin_mobile >> swift_ios
        linkedin_mobile >> kotlin_android

        # 前端技术到后端技术
        ember_js >> rest_apis
        dust_js >> graphql
        react_native >> grpc
        webpack >> babel
        babel >> grunt

        # 后端技术到数据存储
        java >> play_framework
        scala >> finagle
        play_framework >> mysql
        finagle >> voldemort
        rest_apis >> espresso
        graphql >> neo4j

        # 数据存储连接
        mysql >> postgresql
        voldemort >> espresso
        espresso >> mongodb
        mongodb >> cassandra
        neo4j >> titan
        redis >> memcached
        memcached >> hazelcast
        galene >> elasticsearch
        elasticsearch >> solr

        # 大数据和流处理连接
        kafka >> samza
        samza >> storm
        hadoop >> spark
        spark >> hive
        data_warehouse >> teradata
        teradata >> vertica
        druid >> pinot
        pinot >> kylin

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> mesos
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd >> consul_config
        consul_config >> vault

        # 监控和日志连接
        ingraphs >> prometheus
        prometheus >> grafana
        kafka_logs >> elasticsearch_logs
        elasticsearch_logs >> logstash
        zipkin >> jaeger
        jaeger >> dapper

        # AI/ML连接
        tensorflow >> pytorch
        pytorch >> scikit_learn
        recommendation_engine >> content_filtering
        content_filtering >> collaborative_filtering
        nlp_models >> text_analysis
        text_analysis >> sentiment_analysis
        image_processing >> face_recognition
        face_recognition >> object_detection

        # 安全连接
        oauth >> openid_connect
        openid_connect >> saml
        rbac >> abac
        encryption >> data_masking
        data_masking >> privacy_controls
        waf >> ddos_protection
        ddos_protection >> network_security

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> bamboo
        bamboo >> circleci
        junit >> testng
        testng >> selenium
        sonarqube >> checkstyle
        checkstyle >> findbugs

        # 跨层连接
        play_framework >> Edge(label="部署到") >> kubernetes
        kafka >> Edge(label="流数据") >> samza
        voldemort >> Edge(label="分布式存储") >> espresso
        galene >> Edge(label="搜索服务") >> elasticsearch
        recommendation_engine >> Edge(label="推荐算法") >> tensorflow
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> docker
        prometheus >> Edge(label="监控") >> grafana


if __name__ == "__main__":
    create_linkedin_tech_stack_diagram(filename="linkedin_tech_stack", outformat="png")
    create_linkedin_tech_stack_diagram(filename="linkedin_tech_stack", outformat="pdf")
