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


def create_feishu_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("飞书技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("企业用户")
            
            with Cluster("桌面应用"):
                feishu_desktop = Server("飞书桌面版")
                feishu_windows = Server("飞书 Windows")
                feishu_mac = Server("飞书 macOS")
                feishu_linux = Server("飞书 Linux")
                
            with Cluster("移动应用"):
                feishu_mobile = Server("飞书移动版")
                feishu_ios = Server("飞书 iOS")
                feishu_android = Server("飞书 Android")
                
            with Cluster("Web 应用"):
                feishu_web = Server("飞书 Web")
                feishu_browser = Server("飞书浏览器版")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                vue_js = React("Vue.js")
                typescript = JavaScript("TypeScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                java_android = Java("Java (Android)")
                objective_c = Server("Objective-C")
                
            with Cluster("桌面技术"):
                electron = Server("Electron")
                cpp_desktop = Server("C++")
                qt = Server("Qt")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")
                metro = Server("Metro")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                go_lang = Go("Go")
                java = Java("Java")
                python = Python("Python")
                cpp = Server("C++")
                rust = Server("Rust")
                
            with Cluster("Web 框架"):
                gin = Server("Gin")
                echo = Server("Echo")
                spring_boot = Server("Spring Boot")
                django = Django("Django")
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
                
            with Cluster("文件存储"):
                object_storage = Server("Object Storage")
                file_storage = Storage("File Storage")
                cdn_storage = Server("CDN Storage")

        # 企业协作和通讯层
        with Cluster("企业协作和通讯层"):
            with Cluster("即时通讯"):
                im_service = Server("IM Service")
                message_queue = Server("Message Queue")
                real_time_chat = Server("Real-time Chat")
                group_chat = Server("Group Chat")
                
            with Cluster("音视频通讯"):
                video_call = Server("Video Call")
                voice_call = Server("Voice Call")
                screen_share = Server("Screen Share")
                webrtc = Server("WebRTC")
                
            with Cluster("文档协作"):
                document_editor = Server("Document Editor")
                spreadsheet_editor = Server("Spreadsheet Editor")
                presentation_editor = Server("Presentation Editor")
                collaborative_editing = Server("Collaborative Editing")
                
            with Cluster("项目管理"):
                task_management = Server("Task Management")
                project_tracking = Server("Project Tracking")
                workflow_automation = Server("Workflow Automation")
                calendar_sync = Server("Calendar Sync")
                
            with Cluster("知识管理"):
                wiki_system = Server("Wiki System")
                knowledge_base = Server("Knowledge Base")
                search_engine = Server("Search Engine")
                content_management = Server("Content Management")

        # 安全和合规层
        with Cluster("安全和合规层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                jwt = Server("JWT")
                sso = Server("Single Sign-On")
                ldap = Server("LDAP")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                permission_management = Server("Permission Management")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                key_management = Server("Key Management")
                data_masking = Server("Data Masking")
                privacy_controls = Server("Privacy Controls")
                
            with Cluster("网络安全"):
                waf = Server("Web Application Firewall")
                ddos_protection = Server("DDoS Protection")
                ssl_tls = Server("SSL/TLS")
                vpn = Server("VPN")
                firewall = Firewall("Firewall")
                
            with Cluster("合规系统"):
                audit_logging = Server("Audit Logging")
                compliance_monitoring = Server("Compliance Monitoring")
                data_retention = Server("Data Retention")
                gdpr_compliance = Server("GDPR Compliance")

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

        # 云服务层
        with Cluster("云服务层"):
            with Cluster("计算服务"):
                virtual_machines = Server("Virtual Machines")
                container_instances = Server("Container Instances")
                serverless = Server("Serverless")
                
            with Cluster("存储服务"):
                block_storage = Server("Block Storage")
                object_storage_cloud = Server("Object Storage")
                file_storage_cloud = Server("File Storage")
                
            with Cluster("网络服务"):
                load_balancer = Server("Load Balancer")
                cdn = Server("CDN")
                vpc = Server("VPC")
                
            with Cluster("数据库服务"):
                managed_database = Server("Managed Database")
                database_backup = Server("Database Backup")
                read_replicas = Server("Read Replicas")

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
                skywalking = Server("Apache SkyWalking")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                kafka = Kafka("Apache Kafka")
                flink = Server("Apache Flink")
                
            with Cluster("数据仓库"):
                data_warehouse = Server("Data Warehouse")
                clickhouse = Server("ClickHouse")
                druid = Server("Apache Druid")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                user_behavior_analysis = Server("User Behavior Analysis")
                usage_analytics = Server("Usage Analytics")
                performance_metrics = Server("Performance Metrics")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                recommendation_engine = Server("Recommendation Engine")

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
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                checkstyle = Server("CheckStyle")
                findbugs = Server("FindBugs")
                eslint = Server("ESLint")

        # 连接关系
        # 客户端到前端技术
        users >> feishu_desktop
        users >> feishu_mobile
        users >> feishu_web
        users >> feishu_ios
        users >> feishu_android
        
        feishu_desktop >> electron
        feishu_mobile >> react_native
        feishu_web >> react
        feishu_ios >> swift_ios
        feishu_android >> kotlin_android

        # 前端技术到后端技术
        react >> gin
        vue_js >> echo
        typescript >> spring_boot
        react_native >> django
        electron >> actix

        # 后端技术到数据存储
        go_lang >> gin
        java >> spring_boot
        python >> django
        gin >> mysql
        spring_boot >> mongodb
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
        object_storage >> file_storage
        file_storage >> cdn_storage

        # 企业协作和通讯连接
        im_service >> message_queue
        message_queue >> real_time_chat
        real_time_chat >> group_chat
        video_call >> voice_call
        voice_call >> screen_share
        screen_share >> webrtc
        document_editor >> spreadsheet_editor
        spreadsheet_editor >> presentation_editor
        presentation_editor >> collaborative_editing
        task_management >> project_tracking
        project_tracking >> workflow_automation
        workflow_automation >> calendar_sync
        wiki_system >> knowledge_base
        knowledge_base >> search_engine
        search_engine >> content_management

        # 安全连接
        oauth >> openid_connect
        openid_connect >> jwt
        jwt >> sso
        sso >> ldap
        rbac >> abac
        abac >> permission_management
        encryption >> key_management
        key_management >> data_masking
        data_masking >> privacy_controls
        waf >> ddos_protection
        ddos_protection >> ssl_tls
        ssl_tls >> vpn
        vpn >> firewall
        audit_logging >> compliance_monitoring
        compliance_monitoring >> data_retention
        data_retention >> gdpr_compliance

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd_config >> consul_config
        consul_config >> vault

        # 云服务连接
        virtual_machines >> container_instances
        container_instances >> serverless
        block_storage >> object_storage_cloud
        object_storage_cloud >> file_storage_cloud
        load_balancer >> cdn
        cdn >> vpc
        managed_database >> database_backup
        database_backup >> read_replicas

        # 监控连接
        prometheus >> grafana
        grafana >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> skywalking

        # 大数据分析连接
        hadoop >> spark
        spark >> kafka
        kafka >> flink
        data_warehouse >> clickhouse
        clickhouse >> druid
        real_time_analytics >> user_behavior_analysis
        user_behavior_analysis >> usage_analytics
        usage_analytics >> performance_metrics
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> recommendation_engine

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> tekton
        junit >> pytest
        pytest >> selenium
        selenium >> cypress
        sonarqube >> checkstyle
        checkstyle >> findbugs
        findbugs >> eslint

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> docker
        redis >> Edge(label="缓存加速") >> mysql
        im_service >> Edge(label="即时通讯") >> message_queue
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana
        kafka >> Edge(label="实时数据") >> spark
        recommendation_engine >> Edge(label="智能推荐") >> tensorflow


if __name__ == "__main__":
    create_feishu_tech_stack_diagram(filename="feishu_tech_stack", outformat="png")
    create_feishu_tech_stack_diagram(filename="feishu_tech_stack", outformat="pdf")
