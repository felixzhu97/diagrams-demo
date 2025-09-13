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
from diagrams.programming.language import Python, JavaScript, Java, Go, Ruby
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


def create_coinbase_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Coinbase 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                coinbase_web = Server("Coinbase Web")
                coinbase_pro = Server("Coinbase Pro")
                coinbase_advanced_trade = Server("Advanced Trade")
                coinbase_earn = Server("Coinbase Earn")
                
            with Cluster("移动应用"):
                coinbase_mobile = Server("Coinbase Mobile")
                coinbase_wallet = Server("Coinbase Wallet")
                coinbase_dapp_wallet = Server("Coinbase dApp Wallet")
                
            with Cluster("开发者工具"):
                coinbase_api = Server("Coinbase API")
                coinbase_cloud = Server("Coinbase Cloud")
                coinbase_connect = Server("Coinbase Connect")
                
            with Cluster("硬件设备"):
                coinbase_card = Server("Coinbase Card")
                hardware_wallet = Server("Hardware Wallet")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                typescript = JavaScript("TypeScript")
                next_js = React("Next.js")
                web3_js = Server("Web3.js")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("区块链集成"):
                ethers_js = Server("Ethers.js")
                web3_react = Server("Web3-React")
                wallet_connect = Server("WalletConnect")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                ruby = Ruby("Ruby")
                python = Python("Python")
                go_lang = Go("Go")
                java = Java("Java")
                javascript = JavaScript("JavaScript")
                
            with Cluster("Web 框架"):
                ruby_on_rails = Server("Ruby on Rails")
                django = Django("Django")
                gin = Server("Gin")
                spring_boot = Server("Spring Boot")
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
                
            with Cluster("时间序列数据库"):
                influxdb = Server("InfluxDB")
                timescaledb = Server("TimescaleDB")

        # 区块链和加密货币层
        with Cluster("区块链和加密货币层"):
            with Cluster("区块链网络"):
                bitcoin = Server("Bitcoin")
                ethereum = Server("Ethereum")
                polygon = Server("Polygon")
                solana = Server("Solana")
                avalanche = Server("Avalanche")
                
            with Cluster("Layer 2 解决方案"):
                optimism = Server("Optimism")
                arbitrum = Server("Arbitrum")
                polygon_hermez = Server("Polygon Hermez")
                
            with Cluster("跨链桥"):
                hop_protocol = Server("Hop Protocol")
                synapse = Server("Synapse")
                wormhole = Server("Wormhole")
                
            with Cluster("智能合约"):
                solidity = Server("Solidity")
                vyper = Server("Vyper")
                rust = Server("Rust")
                
            with Cluster("DeFi 协议"):
                uniswap = Server("Uniswap")
                compound = Server("Compound")
                aave = Server("Aave")
                curve = Server("Curve")

        # 安全和合规层
        with Cluster("安全和合规层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                jwt = Server("JWT")
                multi_factor_auth = Server("Multi-Factor Authentication")
                
            with Cluster("密钥管理"):
                hsm = Server("Hardware Security Module")
                key_vault = Server("Key Vault")
                wallet_sdk = Server("Wallet SDK")
                mpc = Server("Multi-Party Computation")
                
            with Cluster("合规系统"):
                kyc = Server("Know Your Customer")
                aml = Server("Anti-Money Laundering")
                sanctions_screening = Server("Sanctions Screening")
                transaction_monitoring = Server("Transaction Monitoring")
                
            with Cluster("安全监控"):
                fraud_detection = Server("Fraud Detection")
                risk_management = Server("Risk Management")
                security_audit = Server("Security Audit")
                penetration_testing = Server("Penetration Testing")

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
                rds = RDS("RDS")
                s3 = S3("S3")
                cloudfront = CloudFront("CloudFront")
                
            with Cluster("计算服务"):
                ecs = Server("ECS")
                fargate = Server("Fargate")
                batch = Server("Batch")
                
            with Cluster("数据服务"):
                redshift = Server("Redshift")
                kinesis = Kinesis("Kinesis")
                glue = Glue("Glue")
                
            with Cluster("监控服务"):
                cloudwatch = Cloudwatch("CloudWatch")
                x_ray = Server("X-Ray")

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
                x_ray_tracing = Server("X-Ray Tracing")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据处理"):
                spark = Spark("Apache Spark")
                hadoop = Hadoop("Apache Hadoop")
                kafka = Kafka("Apache Kafka")
                flink = Server("Apache Flink")
                
            with Cluster("数据仓库"):
                data_warehouse = Server("Data Warehouse")
                redshift_analytics = Server("Redshift")
                snowflake = Server("Snowflake")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                market_data_analysis = Server("Market Data Analysis")
                trading_analytics = Server("Trading Analytics")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")

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
                sonarqube = Server("SonarQube")
                rubocop = Server("RuboCop")
                eslint = Server("ESLint")

        # 连接关系
        # 客户端到前端技术
        users >> coinbase_web
        users >> coinbase_mobile
        users >> coinbase_wallet
        users >> coinbase_pro
        users >> coinbase_api
        
        coinbase_web >> react
        coinbase_mobile >> react_native
        coinbase_wallet >> ethers_js
        coinbase_pro >> typescript
        coinbase_api >> web3_js

        # 前端技术到后端技术
        react >> ruby_on_rails
        react_native >> django
        ethers_js >> gin
        typescript >> spring_boot
        web3_js >> express

        # 后端技术到数据存储
        ruby >> ruby_on_rails
        python >> django
        go_lang >> gin
        ruby_on_rails >> postgresql
        django >> mongodb
        gin >> redis
        rest_apis >> elasticsearch

        # 数据存储连接
        postgresql >> mysql
        mysql >> aurora
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> elasticache
        elasticsearch >> solr
        influxdb >> timescaledb

        # 区块链连接
        bitcoin >> ethereum
        ethereum >> polygon
        polygon >> solana
        solana >> avalanche
        optimism >> arbitrum
        arbitrum >> polygon_hermez
        hop_protocol >> synapse
        synapse >> wormhole
        solidity >> vyper
        vyper >> rust
        uniswap >> compound
        compound >> aave
        aave >> curve

        # 安全连接
        oauth >> openid_connect
        openid_connect >> jwt
        jwt >> multi_factor_auth
        hsm >> key_vault
        key_vault >> wallet_sdk
        wallet_sdk >> mpc
        kyc >> aml
        aml >> sanctions_screening
        sanctions_screening >> transaction_monitoring
        fraud_detection >> risk_management
        risk_management >> security_audit
        security_audit >> penetration_testing

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
        lambda_aws >> rds
        rds >> s3
        s3 >> cloudfront
        ecs >> fargate
        fargate >> batch
        redshift >> kinesis
        kinesis >> glue
        cloudwatch >> x_ray

        # 监控连接
        prometheus >> grafana
        grafana >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> x_ray_tracing

        # 大数据分析连接
        spark >> hadoop
        hadoop >> kafka
        kafka >> flink
        data_warehouse >> redshift_analytics
        redshift_analytics >> snowflake
        real_time_analytics >> market_data_analysis
        market_data_analysis >> trading_analytics
        tensorflow >> pytorch
        pytorch >> scikit_learn

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> circleci
        rspec >> jest
        jest >> selenium
        selenium >> cypress
        sonarqube >> rubocop
        rubocop >> eslint

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> docker
        redis >> Edge(label="缓存加速") >> postgresql
        ethereum >> Edge(label="区块链集成") >> solidity
        oauth >> Edge(label="身份认证") >> kyc
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana
        kafka >> Edge(label="实时数据") >> spark
        hsm >> Edge(label="密钥安全") >> wallet_sdk


if __name__ == "__main__":
    create_coinbase_tech_stack_diagram(filename="coinbase_tech_stack", outformat="png")
    create_coinbase_tech_stack_diagram(filename="coinbase_tech_stack", outformat="pdf")
