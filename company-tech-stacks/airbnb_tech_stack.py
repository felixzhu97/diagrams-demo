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
from diagrams.aws.management import Cloudformation, Cloudwatch, Cloudtrail, Config, TrustedAdvisor, SystemsManager
from diagrams.aws.analytics import Kinesis, Glue, EMR, Athena, Quicksight, DataPipeline
from diagrams.aws.security import IAM, KMS, SecretsManager, WAF, Shield, Guardduty, Inspector
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions, MQ, Appsync
from diagrams.aws.ml import Sagemaker, Rekognition, Comprehend, Translate, Polly, Lex
from diagrams.aws.mobile import Amplify, DeviceFarm, Pinpoint
from diagrams.aws.iot import IotCore, IotDeviceManagement, IotAnalytics, IotEvents
from diagrams.aws.general import General, Users as AWSUsers, Client


def create_airbnb_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Airbnb 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                airbnb_web = Server("Airbnb Web")
                host_portal = Server("Host Portal")
                guest_portal = Server("Guest Portal")
                admin_portal = Server("Admin Portal")
                
            with Cluster("移动应用"):
                airbnb_mobile = Server("Airbnb Mobile")
                airbnb_ios = Server("Airbnb iOS")
                airbnb_android = Server("Airbnb Android")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")
                
            with Cluster("扩展应用"):
                airbnb_experiences = Server("Airbnb Experiences")
                airbnb_plus = Server("Airbnb Plus")
                airbnb_work = Server("Airbnb Work")

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
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                metro = Server("Metro")
                
            with Cluster("UI组件库"):
                airbnb_ui = Server("Airbnb UI")
                lottie = Server("Lottie")
                custom_components = Server("Custom Components")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                ruby = Server("Ruby")
                java = Java("Java")
                python = Python("Python")
                javascript_backend = JavaScript("JavaScript")
                go = Go("Go")
                
            with Cluster("Web 框架"):
                rails = Server("Ruby on Rails")
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
                smartstack = Server("SmartStack")
                nerve = Server("Nerve")
                synapse = Server("Synapse")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                aurora = Aurora("Amazon Aurora")
                mysql = Server("MySQL")
                postgresql = PostgreSQL("PostgreSQL")
                oracle = Server("Oracle")
                
            with Cluster("NoSQL 数据库"):
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                dynamodb = Dynamodb("DynamoDB")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                elasticache = ElastiCache("ElastiCache")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                
            with Cluster("数据仓库"):
                redshift = Redshift("Amazon Redshift")
                bigquery = Server("BigQuery")
                hive = Server("Apache Hive")

        # 微服务和宏服务层
        with Cluster("微服务和宏服务层"):
            with Cluster("数据获取服务"):
                listing_service = Server("Listing Service")
                user_service = Server("User Service")
                booking_service = Server("Booking Service")
                payment_service = Server("Payment Service")
                
            with Cluster("业务逻辑服务"):
                search_service = Server("Search Service")
                recommendation_service = Server("Recommendation Service")
                pricing_service = Server("Pricing Service")
                review_service = Server("Review Service")
                
            with Cluster("工作流服务"):
                booking_workflow = Server("Booking Workflow")
                payment_workflow = Server("Payment Workflow")
                notification_workflow = Server("Notification Workflow")
                
            with Cluster("UI聚合服务"):
                ui_aggregator = Server("UI Aggregator")
                data_aggregator = Server("Data Aggregator")
                service_blocks = Server("Service Blocks")

        # 大数据和分析层
        with Cluster("大数据和分析层"):
            with Cluster("数据处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                hive_data = Server("Apache Hive")
                presto = Server("Presto")
                
            with Cluster("工作流管理"):
                airflow = Airflow("Apache Airflow")
                luigi = Server("Luigi")
                
            with Cluster("数据可视化"):
                superset = Superset("Apache Superset")
                tableau = Server("Tableau")
                custom_dashboards = Server("Custom Dashboards")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")

        # 搜索和推荐层
        with Cluster("搜索和推荐层"):
            with Cluster("搜索引擎"):
                elasticsearch_search = Server("Elasticsearch Search")
                solr_search = Server("Solr Search")
                custom_search = Server("Custom Search Engine")
                
            with Cluster("推荐系统"):
                collaborative_filtering = Server("Collaborative Filtering")
                content_based = Server("Content-based Filtering")
                hybrid_recommendation = Server("Hybrid Recommendation")
                
            with Cluster("个性化"):
                user_profiling = Server("User Profiling")
                behavioral_analysis = Server("Behavioral Analysis")
                a_b_testing = Server("A/B Testing")

        # 支付和金融层
        with Cluster("支付和金融层"):
            with Cluster("支付处理"):
                stripe = Server("Stripe")
                paypal = Server("PayPal")
                apple_pay = Server("Apple Pay")
                google_pay = Server("Google Pay")
                
            with Cluster("金融系统"):
                accounting_system = Server("Accounting System")
                tax_calculation = Server("Tax Calculation")
                payout_system = Server("Payout System")
                
            with Cluster("风险控制"):
                fraud_detection = Server("Fraud Detection")
                risk_assessment = Server("Risk Assessment")
                compliance_monitoring = Server("Compliance Monitoring")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                jwt = Server("JWT")
                saml = Server("SAML")
                ldap = Server("LDAP")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                permission_management = Server("Permission Management")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                key_management = Server("Key Management")
                data_masking = Server("Data Masking")
                
            with Cluster("审计和合规"):
                audit_logging = Server("Audit Logging")
                compliance_monitoring = Server("Compliance Monitoring")
                regulatory_reporting = Server("Regulatory Reporting")

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
                elb = ELB("Elastic Load Balancing")
                
            with Cluster("配置管理"):
                consul = Server("Consul")
                etcd = Server("etcd")
                vault = Vault("Vault")

        # 云服务层
        with Cluster("AWS 云服务层"):
            with Cluster("计算服务"):
                ec2 = EC2("Amazon EC2")
                lambda_aws = Lambda("AWS Lambda")
                ecs = ECS("Amazon ECS")
                
            with Cluster("存储服务"):
                s3 = S3("Amazon S3")
                ebs = EBS("Amazon EBS")
                efs = EFS("Amazon EFS")
                
            with Cluster("网络服务"):
                vpc = VPC("Amazon VPC")
                cloudfront = CloudFront("CloudFront")
                route53 = Route53("Route 53")
                
            with Cluster("数据库服务"):
                rds = RDS("Amazon RDS")
                aurora_aws = Aurora("Amazon Aurora")
                elasticache_aws = ElastiCache("ElastiCache")

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
                rspec = Server("RSpec")
                jest = Server("Jest")
                selenium = Server("Selenium")
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                rubocop = Server("RuboCop")
                eslint = Server("ESLint")
                sonarqube = Server("SonarQube")

        # 连接关系
        # 客户端到前端技术
        users >> airbnb_web
        users >> host_portal
        users >> guest_portal
        users >> airbnb_mobile
        users >> airbnb_experiences
        
        airbnb_web >> react
        host_portal >> javascript
        guest_portal >> html5
        airbnb_mobile >> react_native
        airbnb_experiences >> airbnb_ui

        # 前端技术到后端技术
        react >> rails
        javascript >> spring_boot
        html5 >> django
        react_native >> express
        airbnb_ui >> gin

        # 后端技术到数据存储
        ruby >> rails
        java >> spring_boot
        python >> django
        javascript_backend >> express
        rails >> aurora
        spring_boot >> mysql
        django >> postgresql
        express >> redis
        gin >> elasticsearch

        # 数据存储连接
        aurora >> mysql
        mysql >> postgresql
        postgresql >> oracle
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> elasticache
        elasticsearch >> solr
        redshift >> bigquery
        bigquery >> hive

        # 微服务和宏服务连接
        listing_service >> user_service
        user_service >> booking_service
        booking_service >> payment_service
        search_service >> recommendation_service
        recommendation_service >> pricing_service
        pricing_service >> review_service
        booking_workflow >> payment_workflow
        payment_workflow >> notification_workflow
        ui_aggregator >> data_aggregator
        data_aggregator >> service_blocks

        # 大数据和分析连接
        hadoop >> spark
        spark >> hive_data
        hive_data >> presto
        airflow >> luigi
        superset >> tableau
        tableau >> custom_dashboards
        tensorflow >> pytorch
        pytorch >> scikit_learn

        # 搜索和推荐连接
        elasticsearch_search >> solr_search
        solr_search >> custom_search
        collaborative_filtering >> content_based
        content_based >> hybrid_recommendation
        user_profiling >> behavioral_analysis
        behavioral_analysis >> a_b_testing

        # 支付和金融连接
        stripe >> paypal
        paypal >> apple_pay
        apple_pay >> google_pay
        accounting_system >> tax_calculation
        tax_calculation >> payout_system
        fraud_detection >> risk_assessment
        risk_assessment >> compliance_monitoring

        # 安全和身份连接
        oauth >> jwt
        jwt >> saml
        saml >> ldap
        rbac >> abac
        abac >> permission_management
        encryption >> key_management
        key_management >> data_masking
        audit_logging >> compliance_monitoring
        compliance_monitoring >> regulatory_reporting

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> mesos
        istio >> linkerd
        nginx >> haproxy
        haproxy >> elb
        consul >> etcd
        etcd >> vault

        # 云服务连接
        ec2 >> lambda_aws
        lambda_aws >> ecs
        s3 >> ebs
        ebs >> efs
        vpc >> cloudfront
        cloudfront >> route53
        rds >> aurora_aws
        aurora_aws >> elasticache_aws

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
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> circleci
        rspec >> jest
        jest >> selenium
        selenium >> cypress
        rubocop >> eslint
        eslint >> sonarqube

        # 跨层连接
        smartstack >> Edge(label="服务发现") >> nerve
        nerve >> Edge(label="服务注册") >> synapse
        rails >> Edge(label="单体架构") >> aurora
        airflow >> Edge(label="工作流管理") >> hadoop
        superset >> Edge(label="数据可视化") >> spark
        react_native >> Edge(label="跨平台") >> airbnb_mobile
        elasticsearch >> Edge(label="搜索") >> elasticsearch_search
        stripe >> Edge(label="支付处理") >> payment_service
        prometheus >> Edge(label="监控") >> grafana


if __name__ == "__main__":
    create_airbnb_tech_stack_diagram(filename="airbnb_tech_stack", outformat="png")
    create_airbnb_tech_stack_diagram(filename="airbnb_tech_stack", outformat="pdf")
