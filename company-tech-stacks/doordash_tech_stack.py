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


def create_doordash_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("DoorDash 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("消费者应用"):
                doordash_consumer = Server("DoorDash Consumer")
                doordash_ios = Server("DoorDash iOS")
                doordash_android = Server("DoorDash Android")
                doordash_web = Server("DoorDash Web")
                
            with Cluster("商家应用"):
                doordash_merchant = Server("DoorDash Merchant")
                merchant_portal = Server("Merchant Portal")
                pos_integration = Server("POS Integration")
                
            with Cluster("配送员应用"):
                doordash_dasher = Server("DoorDash Dasher")
                dasher_ios = Server("Dasher iOS")
                dasher_android = Server("Dasher Android")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("移动开发"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                java_android = Java("Java (Android)")
                
            with Cluster("Web 技术"):
                react = React("React")
                vue_js = React("Vue.js")
                typescript = JavaScript("TypeScript")
                next_js = React("Next.js")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")
                metro = Server("Metro")
                
            with Cluster("地图和定位"):
                google_maps = Server("Google Maps")
                mapbox = Server("Mapbox")
                location_services = Server("Location Services")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                python = Python("Python")
                java = Java("Java")
                go_lang = Go("Go")
                javascript = JavaScript("JavaScript")
                scala = Server("Scala")
                
            with Cluster("Web 框架"):
                django = Django("Django")
                flask = Server("Flask")
                spring_boot = Server("Spring Boot")
                gin = Server("Gin")
                express = Server("Express.js")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                graphql = Server("GraphQL")
                grpc = Server("gRPC")
                webhooks = Server("Webhooks")
                
            with Cluster("服务发现"):
                consul = Server("Consul")
                etcd = Server("etcd")
                zookeeper = Server("ZooKeeper")
                eureka = Server("Eureka")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                postgresql = PostgreSQL("PostgreSQL")
                mysql = Server("MySQL")
                aurora = Server("Amazon Aurora")
                
            with Cluster("NoSQL 数据库"):
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                dynamodb = Dynamodb("DynamoDB")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                elasticache = Server("ElastiCache")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                
            with Cluster("数据仓库"):
                redshift = Server("Redshift")
                snowflake = Server("Snowflake")
                bigquery = Server("BigQuery")

        # 配送和物流层
        with Cluster("配送和物流层"):
            with Cluster("订单管理"):
                order_management = Server("Order Management")
                order_tracking = Server("Order Tracking")
                order_fulfillment = Server("Order Fulfillment")
                inventory_management = Server("Inventory Management")
                
            with Cluster("配送调度"):
                delivery_scheduling = Server("Delivery Scheduling")
                route_optimization = Server("Route Optimization")
                driver_matching = Server("Driver Matching")
                eta_calculation = Server("ETA Calculation")
                
            with Cluster("实时追踪"):
                real_time_tracking = Server("Real-time Tracking")
                gps_tracking = Server("GPS Tracking")
                location_updates = Server("Location Updates")
                delivery_status = Server("Delivery Status")
                
            with Cluster("地图服务"):
                geocoding = Server("Geocoding")
                reverse_geocoding = Server("Reverse Geocoding")
                distance_calculation = Server("Distance Calculation")
                traffic_data = Server("Traffic Data")

        # 支付和风控层
        with Cluster("支付和风控层"):
            with Cluster("支付处理"):
                payment_gateway = Server("Payment Gateway")
                payment_processing = Server("Payment Processing")
                payment_methods = Server("Payment Methods")
                refund_processing = Server("Refund Processing")
                
            with Cluster("风控系统"):
                fraud_detection = Server("Fraud Detection")
                risk_assessment = Server("Risk Assessment")
                transaction_monitoring = Server("Transaction Monitoring")
                chargeback_management = Server("Chargeback Management")
                
            with Cluster("财务系统"):
                accounting = Server("Accounting")
                billing = Server("Billing")
                invoicing = Server("Invoicing")
                tax_calculation = Server("Tax Calculation")
                
            with Cluster("合规系统"):
                pci_compliance = Server("PCI Compliance")
                kyc = Server("Know Your Customer")
                aml = Server("Anti-Money Laundering")
                regulatory_reporting = Server("Regulatory Reporting")

        # 推荐和AI层
        with Cluster("推荐和AI层"):
            with Cluster("推荐引擎"):
                recommendation_engine = Server("Recommendation Engine")
                restaurant_recommendation = Server("Restaurant Recommendation")
                food_recommendation = Server("Food Recommendation")
                personalized_search = Server("Personalized Search")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                xgboost = Server("XGBoost")
                
            with Cluster("自然语言处理"):
                nlp_models = Server("NLP Models")
                text_analysis = Server("Text Analysis")
                sentiment_analysis = Server("Sentiment Analysis")
                review_analysis = Server("Review Analysis")
                
            with Cluster("计算机视觉"):
                image_recognition = Server("Image Recognition")
                food_detection = Server("Food Detection")
                quality_assessment = Server("Quality Assessment")
                ocr = Server("OCR")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                kafka = Kafka("Apache Kafka")
                flink = Server("Apache Flink")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                user_behavior_analysis = Server("User Behavior Analysis")
                delivery_performance = Server("Delivery Performance")
                restaurant_analytics = Server("Restaurant Analytics")
                
            with Cluster("数据可视化"):
                superset = Superset("Apache Superset")
                grafana = Grafana("Grafana")
                tableau = Server("Tableau")
                
            with Cluster("A/B测试"):
                ab_testing = Server("A/B Testing")
                feature_flags = Server("Feature Flags")
                experiment_platform = Server("Experiment Platform")

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

        # 云服务层 (AWS)
        with Cluster("云服务层 (AWS)"):
            with Cluster("计算服务"):
                ec2 = EC2("EC2")
                lambda_aws = Lambda("Lambda")
                ecs = Server("ECS")
                fargate = Server("Fargate")
                
            with Cluster("数据服务"):
                rds = RDS("RDS")
                aurora_cloud = Server("Aurora")
                s3 = S3("S3")
                dynamodb_cloud = Dynamodb("DynamoDB")
                
            with Cluster("网络服务"):
                cloudfront = CloudFront("CloudFront")
                route53 = Route53("Route 53")
                elb = ELB("Elastic Load Balancer")
                
            with Cluster("分析服务"):
                kinesis = Kinesis("Kinesis")
                glue = Glue("Glue")
                emr = EMR("EMR")
                
            with Cluster("监控服务"):
                cloudwatch = Cloudwatch("CloudWatch")

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
                x_ray = Server("X-Ray")

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
                api_gateway = Server("API Gateway")
                
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
                circleci = Server("CircleCI")
                
            with Cluster("测试工具"):
                pytest = Server("pytest")
                junit = Server("JUnit")
                selenium = Server("Selenium")
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                pylint = Server("Pylint")
                eslint = Server("ESLint")
                black = Server("Black")

        # 连接关系
        # 客户端到前端技术
        users >> doordash_consumer
        users >> doordash_merchant
        users >> doordash_dasher
        users >> doordash_ios
        users >> doordash_android
        
        doordash_consumer >> react_native
        doordash_merchant >> react
        doordash_dasher >> swift_ios
        doordash_ios >> kotlin_android
        doordash_android >> java_android

        # 前端技术到后端技术
        react >> django
        vue_js >> flask
        typescript >> spring_boot
        react_native >> gin
        next_js >> express

        # 后端技术到数据存储
        python >> django
        java >> spring_boot
        go_lang >> gin
        django >> postgresql
        spring_boot >> mongodb
        rest_apis >> redis
        graphql >> elasticsearch

        # 数据存储连接
        postgresql >> mysql
        mysql >> aurora
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> elasticache
        elasticsearch >> solr
        redshift >> snowflake
        snowflake >> bigquery

        # 配送和物流连接
        order_management >> order_tracking
        order_tracking >> order_fulfillment
        order_fulfillment >> inventory_management
        delivery_scheduling >> route_optimization
        route_optimization >> driver_matching
        driver_matching >> eta_calculation
        real_time_tracking >> gps_tracking
        gps_tracking >> location_updates
        location_updates >> delivery_status
        geocoding >> reverse_geocoding
        reverse_geocoding >> distance_calculation
        distance_calculation >> traffic_data

        # 支付和风控连接
        payment_gateway >> payment_processing
        payment_processing >> payment_methods
        payment_methods >> refund_processing
        fraud_detection >> risk_assessment
        risk_assessment >> transaction_monitoring
        transaction_monitoring >> chargeback_management
        accounting >> billing
        billing >> invoicing
        invoicing >> tax_calculation
        pci_compliance >> kyc
        kyc >> aml
        aml >> regulatory_reporting

        # 推荐和AI连接
        recommendation_engine >> restaurant_recommendation
        restaurant_recommendation >> food_recommendation
        food_recommendation >> personalized_search
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> xgboost
        nlp_models >> text_analysis
        text_analysis >> sentiment_analysis
        sentiment_analysis >> review_analysis
        image_recognition >> food_detection
        food_detection >> quality_assessment
        quality_assessment >> ocr

        # 大数据分析连接
        hadoop >> spark
        spark >> kafka
        kafka >> flink
        real_time_analytics >> user_behavior_analysis
        user_behavior_analysis >> delivery_performance
        delivery_performance >> restaurant_analytics
        superset >> grafana
        grafana >> tableau
        ab_testing >> feature_flags
        feature_flags >> experiment_platform

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd_config >> consul_config
        consul_config >> vault

        # 云服务连接
        ec2 >> lambda_aws
        lambda_aws >> ecs
        ecs >> fargate
        rds >> aurora_cloud
        aurora_cloud >> s3
        s3 >> dynamodb_cloud
        cloudfront >> route53
        route53 >> elb
        kinesis >> glue
        glue >> emr
        cloudwatch >> prometheus

        # 监控连接
        prometheus >> grafana_monitoring
        grafana_monitoring >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> x_ray

        # 安全连接
        oauth >> openid_connect
        openid_connect >> jwt
        jwt >> sso
        rbac >> abac
        abac >> api_gateway
        encryption >> key_management
        key_management >> data_masking
        data_masking >> privacy_controls
        waf >> ddos_protection
        ddos_protection >> ssl_tls
        ssl_tls >> vpn

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> circleci
        pytest >> junit
        junit >> selenium
        selenium >> cypress
        sonarqube >> pylint
        pylint >> eslint
        eslint >> black

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> fargate
        redis >> Edge(label="缓存加速") >> postgresql
        order_management >> Edge(label="订单处理") >> delivery_scheduling
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana_monitoring
        kafka >> Edge(label="实时数据") >> spark
        recommendation_engine >> Edge(label="智能推荐") >> tensorflow


if __name__ == "__main__":
    create_doordash_tech_stack_diagram(filename="doordash_tech_stack", outformat="png")
    create_doordash_tech_stack_diagram(filename="doordash_tech_stack", outformat="pdf")
