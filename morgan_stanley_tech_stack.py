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
from diagrams.programming.language import Python, JavaScript, Java, Go, Cpp
from diagrams.programming.framework import React, Django
from diagrams.aws.compute import EC2, Lambda, ECS, Fargate
from diagrams.aws.database import RDS, Dynamodb, Aurora
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_morgan_stanley_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Morgan Stanley 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球客户")
            
            with Cluster("交易平台"):
                matrix = Server("Matrix")
                athena = Server("Athena")
                wealth_management = Server("Wealth Management")
                institutional_securities = Server("Institutional Securities")
                
            with Cluster("移动应用"):
                ms_mobile = Server("MS Mobile")
                wealth_mobile = Server("Wealth Mobile")
                trading_mobile = Server("Trading Mobile")
                
            with Cluster("Web 应用"):
                ms_web = Server("MS Web Portal")
                research_portal = Server("Research Portal")
                client_portal = Server("Client Portal")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                angular = React("Angular")
                typescript = JavaScript("TypeScript")
                vue_js = React("Vue.js")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("数据可视化"):
                d3_js = Server("D3.js")
                tableau = Server("Tableau")
                power_bi = Server("Power BI")
                plotly = Server("Plotly")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                java = Java("Java")
                cpp = Cpp("C++")
                python = Python("Python")
                scala = Server("Scala")
                javascript = JavaScript("JavaScript")
                
            with Cluster("Web 框架"):
                spring_boot = Server("Spring Boot")
                spring_framework = Server("Spring Framework")
                django = Django("Django")
                express = Server("Express.js")
                akka = Server("Akka")
                
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
                oracle_db = Server("Oracle Database")
                sql_server = Server("SQL Server")
                
            with Cluster("NoSQL 数据库"):
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                dynamodb = Dynamodb("DynamoDB")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                hazelcast = Server("Hazelcast")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                
            with Cluster("数据湖"):
                s3_data_lake = S3("S3 Data Lake")
                hdfs = Server("HDFS")
                delta_lake = Server("Delta Lake")

        # 金融交易和风控层
        with Cluster("金融交易和风控层"):
            with Cluster("交易系统"):
                trading_engine = Server("Trading Engine")
                order_management = Server("Order Management")
                execution_management = Server("Execution Management")
                market_data = Server("Market Data")
                
            with Cluster("风险管理系统"):
                var_model = Server("VaR Model")
                stress_testing = Server("Stress Testing")
                credit_risk = Server("Credit Risk")
                market_risk = Server("Market Risk")
                operational_risk = Server("Operational Risk")
                
            with Cluster("合规系统"):
                kyc = Server("Know Your Customer")
                aml = Server("Anti-Money Laundering")
                sanctions_screening = Server("Sanctions Screening")
                regulatory_reporting = Server("Regulatory Reporting")
                trade_surveillance = Server("Trade Surveillance")
                
            with Cluster("清算系统"):
                settlement = Server("Settlement")
                clearing = Server("Clearing")
                custody = Server("Custody")
                reconciliation = Server("Reconciliation")
                collateral_management = Server("Collateral Management")

        # 大数据和AI层
        with Cluster("大数据和AI层"):
            with Cluster("数据处理"):
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                kafka = Kafka("Apache Kafka")
                flink = Server("Apache Flink")
                
            with Cluster("数据仓库"):
                data_warehouse = Server("Data Warehouse")
                redshift = Server("Redshift")
                snowflake = Server("Snowflake")
                teradata = Server("Teradata")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                xgboost = Server("XGBoost")
                
            with Cluster("AI 平台"):
                ai_platform = Server("AI Platform")
                ml_pipeline = Server("ML Pipeline")
                model_serving = Server("Model Serving")
                feature_store = Server("Feature Store")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                market_data_analysis = Server("Market Data Analysis")
                trading_analytics = Server("Trading Analytics")
                risk_analytics = Server("Risk Analytics")
                client_analytics = Server("Client Analytics")

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
            with Cluster("AWS 服务"):
                ec2 = EC2("EC2")
                lambda_aws = Lambda("Lambda")
                ecs = ECS("ECS")
                fargate = Fargate("Fargate")
                
            with Cluster("数据服务"):
                rds = RDS("RDS")
                aurora = Aurora("Aurora")
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

        # 安全和合规层
        with Cluster("安全和合规层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                jwt = Server("JWT")
                ldap = Server("LDAP")
                saml = Server("SAML")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                pdp = Server("Policy Decision Point")
                
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
                bamboo = Server("Bamboo")
                
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
        users >> matrix
        users >> athena
        users >> wealth_management
        users >> institutional_securities
        users >> ms_mobile
        
        matrix >> react
        athena >> angular
        wealth_management >> typescript
        institutional_securities >> vue_js
        ms_mobile >> react_native

        # 前端技术到后端技术
        react >> spring_boot
        angular >> spring_framework
        typescript >> django
        vue_js >> express
        react_native >> rest_apis

        # 后端技术到数据存储
        java >> spring_boot
        cpp >> spring_framework
        python >> django
        scala >> akka
        spring_boot >> postgresql
        django >> mongodb
        rest_apis >> redis
        graphql >> elasticsearch

        # 数据存储连接
        postgresql >> mysql
        mysql >> oracle_db
        oracle_db >> sql_server
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> hazelcast
        elasticsearch >> solr
        s3_data_lake >> hdfs
        hdfs >> delta_lake

        # 金融交易和风控连接
        trading_engine >> order_management
        order_management >> execution_management
        execution_management >> market_data
        var_model >> stress_testing
        stress_testing >> credit_risk
        credit_risk >> market_risk
        market_risk >> operational_risk
        kyc >> aml
        aml >> sanctions_screening
        sanctions_screening >> regulatory_reporting
        regulatory_reporting >> trade_surveillance
        settlement >> clearing
        clearing >> custody
        custody >> reconciliation
        reconciliation >> collateral_management

        # 大数据和AI连接
        hadoop >> spark
        spark >> kafka
        kafka >> flink
        data_warehouse >> redshift
        redshift >> snowflake
        snowflake >> teradata
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> xgboost
        ai_platform >> ml_pipeline
        ml_pipeline >> model_serving
        model_serving >> feature_store
        real_time_analytics >> market_data_analysis
        market_data_analysis >> trading_analytics
        trading_analytics >> risk_analytics
        risk_analytics >> client_analytics

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
        rds >> aurora
        aurora >> s3
        s3 >> dynamodb_cloud
        cloudfront >> route53
        route53 >> elb
        kinesis >> glue
        glue >> emr
        cloudwatch >> prometheus

        # 监控连接
        prometheus >> grafana
        grafana >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> dapper

        # 安全连接
        oauth >> openid_connect
        openid_connect >> jwt
        jwt >> ldap
        ldap >> saml
        rbac >> abac
        abac >> pdp
        encryption >> key_management
        key_management >> data_masking
        data_masking >> privacy_controls
        waf >> ddos_protection
        ddos_protection >> ssl_tls
        ssl_tls >> vpn
        vpn >> firewall

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> bamboo
        junit >> pytest
        pytest >> selenium
        selenium >> cypress
        sonarqube >> checkstyle
        checkstyle >> findbugs
        findbugs >> eslint

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> fargate
        redis >> Edge(label="缓存加速") >> postgresql
        trading_engine >> Edge(label="交易系统") >> order_management
        oauth >> Edge(label="身份认证") >> kyc
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana
        kafka >> Edge(label="实时数据") >> spark
        ai_platform >> Edge(label="AI服务") >> ml_pipeline


if __name__ == "__main__":
    create_morgan_stanley_tech_stack_diagram(filename="morgan_stanley_tech_stack", outformat="png")
    create_morgan_stanley_tech_stack_diagram(filename="morgan_stanley_tech_stack", outformat="pdf")
