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
from diagrams.programming.language import Python, JavaScript, Java, Cpp
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


def create_meta_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Meta 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                facebook_web = Server("Facebook Web")
                instagram_web = Server("Instagram Web")
                whatsapp_web = Server("WhatsApp Web")
                messenger_web = Server("Messenger Web")
                oculus_web = Server("Oculus Web")
                
            with Cluster("移动应用"):
                facebook_mobile = Server("Facebook Mobile")
                instagram_mobile = Server("Instagram Mobile")
                whatsapp_mobile = Server("WhatsApp Mobile")
                messenger_mobile = Server("Messenger Mobile")
                oculus_mobile = Server("Oculus Mobile")
                
            with Cluster("VR/AR 设备"):
                oculus_quest = Server("Oculus Quest")
                oculus_rift = Server("Oculus Rift")
                portal = Server("Portal")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("React 生态"):
                react = React("React")
                react_native = React("React Native")
                nextjs = React("Next.js")
                
            with Cluster("移动开发"):
                react_native_mobile = React("React Native")
                hermes_engine = Server("Hermes Engine")
                metro_bundler = Server("Metro Bundler")
                
            with Cluster("Web 技术"):
                javascript_engine = JavaScript("JavaScript")
                typescript = JavaScript("TypeScript")
                flow = Server("Flow")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                yarn = Server("Yarn")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                hack = Server("Hack")
                php = Server("PHP")
                rust = Server("Rust")
                cpp = Cpp("C++")
                
            with Cluster("虚拟机"):
                hhvm = Server("HHVM")
                hiphop = Server("HipHop")
                
            with Cluster("API 服务"):
                graphql = Server("GraphQL")
                rest_api = Server("REST API")
                thrift = Server("Apache Thrift")
                
            with Cluster("微服务"):
                service_mesh = Server("Service Mesh")
                load_balancer = Server("Load Balancer")
                circuit_breaker = Server("Circuit Breaker")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                mysql_udb = Server("MySQL UDB")
                postgresql = PostgreSQL("PostgreSQL")
                
            with Cluster("NoSQL 数据库"):
                cassandra = Cassandra("Cassandra")
                mongodb = MongoDB("MongoDB")
                hbase = Server("HBase")
                
            with Cluster("图数据库"):
                tao = Server("TAO")
                neo4j = Server("Neo4j")
                
            with Cluster("键值存储"):
                zippydb = Server("ZippyDB")
                rocksdb = Server("RocksDB")
                memcached = Memcached("Memcached")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                mcrouter = Server("Mcrouter")
                
            with Cluster("对象存储"):
                haystack = Server("Haystack")
                f4 = Server("F4")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据仓库"):
                presto = Server("Presto")
                hive = Server("Hive")
                spark = Spark("Apache Spark")
                
            with Cluster("流处理"):
                scribe = Server("Scribe")
                puma = Server("Puma")
                kafka = Kafka("Apache Kafka")
                
            with Cluster("机器学习"):
                pytorch = Server("PyTorch")
                caffe2 = Server("Caffe2")
                fairseq = Server("Fairseq")
                
            with Cluster("数据分析"):
                scuba = Server("Scuba")
                aries = Server("Aries")
                pythia = Server("Pythia")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("计算资源"):
                data_centers = Server("Data Centers")
                edge_servers = Server("Edge Servers")
                cdn_nodes = Server("CDN Nodes")
                
            with Cluster("容器化"):
                docker = Server("Docker")
                kubernetes = Server("Kubernetes")
                borg = Server("Borg")
                
            with Cluster("服务发现"):
                consul = Server("Consul")
                etcd = Server("etcd")
                
            with Cluster("配置管理"):
                config_management = Server("Config Management")
                feature_flags = Server("Feature Flags")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("构建系统"):
                buck = Server("Buck")
                bazel = Server("Bazel")
                
            with Cluster("版本控制"):
                git = Server("Git")
                mercurial = Server("Mercurial")
                
            with Cluster("测试工具"):
                jest = Server("Jest")
                phpunit = Server("PHPUnit")
                cpp_unit = Server("C++ Unit Tests")
                
            with Cluster("监控工具"):
                osquery = Server("Osquery")
                scuba_monitoring = Server("Scuba Monitoring")
                oculus_insights = Server("Oculus Insights")

        # 安全和隐私层
        with Cluster("安全和隐私层"):
            with Cluster("身份认证"):
                facebook_login = Server("Facebook Login")
                oauth_service = Server("OAuth Service")
                sso_service = Server("SSO Service")
                
            with Cluster("数据安全"):
                encryption_service = Server("Encryption Service")
                data_classification = Server("Data Classification")
                privacy_controls = Server("Privacy Controls")
                
            with Cluster("网络安全"):
                ddos_protection = Server("DDoS Protection")
                waf = Server("Web Application Firewall")
                network_security = Server("Network Security")

        # AI/ML 平台层
        with Cluster("AI/ML 平台层"):
            with Cluster("机器学习框架"):
                pytorch_ml = Server("PyTorch")
                detectron2 = Server("Detectron2")
                transformers = Server("Transformers")
                
            with Cluster("AI 服务"):
                computer_vision = Server("Computer Vision")
                natural_language = Server("Natural Language Processing")
                speech_recognition = Server("Speech Recognition")
                
            with Cluster("推荐系统"):
                recommendation_engine = Server("Recommendation Engine")
                content_filtering = Server("Content Filtering")
                personalization = Server("Personalization")
                
            with Cluster("AR/VR AI"):
                hand_tracking = Server("Hand Tracking")
                eye_tracking = Server("Eye Tracking")
                spatial_audio = Server("Spatial Audio")

        # 连接关系
        # 客户端到前端技术
        users >> facebook_web
        users >> instagram_web
        users >> whatsapp_web
        users >> facebook_mobile
        users >> instagram_mobile
        users >> oculus_quest
        
        facebook_web >> react
        instagram_web >> react
        facebook_mobile >> react_native
        instagram_mobile >> react_native
        oculus_quest >> react_native

        # 前端技术到后端技术
        react >> javascript_engine
        react_native >> hermes_engine
        javascript_engine >> typescript
        typescript >> flow
        webpack >> babel
        babel >> yarn

        # 后端技术到数据存储
        hack >> hhvm
        hhvm >> mysql_udb
        php >> cassandra
        graphql >> tao
        thrift >> zippydb
        rest_api >> rocksdb

        # 数据存储连接
        mysql_udb >> postgresql
        cassandra >> mongodb
        tao >> neo4j
        zippydb >> rocksdb
        memcached >> redis
        haystack >> f4

        # 大数据分析连接
        presto >> hive
        hive >> spark
        scribe >> puma
        puma >> kafka
        pytorch >> caffe2
        caffe2 >> fairseq

        # 基础设施连接
        data_centers >> edge_servers
        edge_servers >> cdn_nodes
        docker >> kubernetes
        kubernetes >> borg
        consul >> etcd

        # 开发工具连接
        buck >> bazel
        git >> mercurial
        jest >> phpunit
        phpunit >> cpp_unit
        osquery >> scuba_monitoring

        # 安全连接
        facebook_login >> oauth_service
        oauth_service >> sso_service
        encryption_service >> data_classification
        data_classification >> privacy_controls
        ddos_protection >> waf

        # AI/ML连接
        pytorch_ml >> detectron2
        detectron2 >> transformers
        computer_vision >> natural_language
        natural_language >> speech_recognition
        recommendation_engine >> content_filtering
        content_filtering >> personalization

        # AR/VR AI连接
        hand_tracking >> eye_tracking
        eye_tracking >> spatial_audio

        # 跨层连接
        react >> Edge(label="前端渲染") >> javascript_engine
        graphql >> Edge(label="数据查询") >> tao
        hhvm >> Edge(label="代码执行") >> mysql_udb
        pytorch >> Edge(label="机器学习") >> recommendation_engine
        presto >> Edge(label="数据分析") >> scuba
        buck >> Edge(label="构建部署") >> docker
        facebook_login >> Edge(label="身份认证") >> oauth_service


if __name__ == "__main__":
    create_meta_tech_stack_diagram(filename="meta_tech_stack", outformat="png")
    create_meta_tech_stack_diagram(filename="meta_tech_stack", outformat="pdf")
