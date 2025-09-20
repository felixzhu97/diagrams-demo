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
from diagrams.aws.analytics import Kinesis, Glue, EMR, Athena, Quicksight, DataPipeline
from diagrams.aws.management import Cloudformation, Cloudwatch, Cloudtrail, Config, TrustedAdvisor, SystemsManager
from diagrams.aws.security import IAM, KMS, SecretsManager, WAF, Shield, Guardduty, Inspector
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions, MQ, Appsync
from diagrams.aws.ml import Sagemaker, Rekognition, Comprehend, Translate, Polly, Lex
from diagrams.aws.mobile import Amplify, DeviceFarm, Pinpoint
from diagrams.aws.iot import IotCore, IotDeviceManagement, IotAnalytics, IotEvents
from diagrams.aws.general import General, Users as AWSUsers, Client


def create_tinder_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Tinder 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("移动应用"):
                tinder_mobile = Server("Tinder Mobile")
                tinder_ios = Server("Tinder iOS")
                tinder_android = Server("Tinder Android")
                
            with Cluster("Web 应用"):
                tinder_web = Server("Tinder Web")
                tinder_plus = Server("Tinder Plus")
                tinder_gold = Server("Tinder Gold")
                tinder_platinum = Server("Tinder Platinum")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")
                
            with Cluster("扩展应用"):
                tinder_social = Server("Tinder Social")
                tinder_swipe_night = Server("Swipe Night")
                tinder_video_chat = Server("Video Chat")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("Web 技术"):
                react = React("React")
                javascript = JavaScript("JavaScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                typescript = Server("TypeScript")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                metro = Server("Metro")
                
            with Cluster("UI组件库"):
                tinder_ui = Server("Tinder UI")
                lottie = Server("Lottie")
                custom_components = Server("Custom Components")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                nodejs = Server("Node.js")
                python = Python("Python")
                java = Java("Java")
                go = Go("Go")
                scala = Server("Scala")
                
            with Cluster("Web 框架"):
                express = Server("Express.js")
                django = Django("Django")
                spring_boot = Server("Spring Boot")
                gin = Server("Gin")
                play_framework = Server("Play Framework")
                
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
                aurora = Aurora("Amazon Aurora")
                
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
                snowflake = Server("Snowflake")

        # 匹配和推荐层
        with Cluster("匹配和推荐层"):
            with Cluster("匹配算法"):
                elo_algorithm = Server("ELO Algorithm")
                gale_shapley = Server("Gale-Shapley")
                collaborative_filtering = Server("Collaborative Filtering")
                content_based = Server("Content-based Filtering")
                
            with Cluster("推荐系统"):
                recommendation_engine = Server("Recommendation Engine")
                preference_learning = Server("Preference Learning")
                behavioral_analysis = Server("Behavioral Analysis")
                similarity_matching = Server("Similarity Matching")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                scikit_learn = Server("Scikit-learn")
                xgboost = Server("XGBoost")
                
            with Cluster("A/B测试"):
                feature_flags = Server("Feature Flags")
                experiment_platform = Server("Experiment Platform")
                statistical_analysis = Server("Statistical Analysis")

        # 用户和社交层
        with Cluster("用户和社交层"):
            with Cluster("用户管理"):
                user_service = Server("User Service")
                profile_service = Server("Profile Service")
                authentication_service = Server("Authentication Service")
                verification_service = Server("Verification Service")
                
            with Cluster("社交功能"):
                messaging_service = Server("Messaging Service")
                photo_sharing = Server("Photo Sharing")
                video_chat = Server("Video Chat")
                social_graph = Server("Social Graph")
                
            with Cluster("内容管理"):
                content_moderation = Server("Content Moderation")
                photo_processing = Server("Photo Processing")
                video_processing = Server("Video Processing")
                media_storage = Server("Media Storage")
                
            with Cluster("地理位置"):
                location_service = Server("Location Service")
                geofencing = Server("Geofencing")
                distance_calculation = Server("Distance Calculation")
                location_privacy = Server("Location Privacy")

        # 支付和订阅层
        with Cluster("支付和订阅层"):
            with Cluster("支付处理"):
                stripe = Server("Stripe")
                apple_pay = Server("Apple Pay")
                google_pay = Server("Google Pay")
                paypal = Server("PayPal")
                
            with Cluster("订阅管理"):
                subscription_service = Server("Subscription Service")
                billing_service = Server("Billing Service")
                plan_management = Server("Plan Management")
                renewal_service = Server("Renewal Service")
                
            with Cluster("高级功能"):
                super_likes = Server("Super Likes")
                boost_service = Server("Boost Service")
                passport_service = Server("Passport Service")
                rewind_service = Server("Rewind Service")
                
            with Cluster("分析服务"):
                usage_analytics = Server("Usage Analytics")
                conversion_tracking = Server("Conversion Tracking")
                revenue_analytics = Server("Revenue Analytics")

        # 安全和隐私层
        with Cluster("安全和隐私层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                jwt = Server("JWT")
                biometric_auth = Server("Biometric Auth")
                two_factor_auth = Server("2FA")
                
            with Cluster("隐私保护"):
                data_encryption = Server("Data Encryption")
                privacy_controls = Server("Privacy Controls")
                gdpr_compliance = Server("GDPR Compliance")
                data_anonymization = Server("Data Anonymization")
                
            with Cluster("安全监控"):
                fraud_detection = Server("Fraud Detection")
                abuse_prevention = Server("Abuse Prevention")
                security_monitoring = Server("Security Monitoring")
                incident_response = Server("Incident Response")
                
            with Cluster("内容安全"):
                image_recognition = Server("Image Recognition")
                text_moderation = Server("Text Moderation")
                spam_detection = Server("Spam Detection")
                fake_profile_detection = Server("Fake Profile Detection")

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
                elb = ELB("Elastic Load Balancing")
                
            with Cluster("配置管理"):
                consul_config = Server("Consul")
                etcd_config = Server("etcd")
                vault = Vault("Vault")

        # 云服务层
        with Cluster("AWS 云服务层"):
            with Cluster("计算服务"):
                ec2 = EC2("Amazon EC2")
                lambda_aws = Lambda("AWS Lambda")
                ecs = ECS("Amazon ECS")
                fargate = Fargate("AWS Fargate")
                
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
                
            with Cluster("性能监控"):
                apm = Server("Application Performance Monitoring")
                real_user_monitoring = Server("Real User Monitoring")
                synthetic_monitoring = Server("Synthetic Monitoring")

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
                jest = Server("Jest")
                pytest = Server("pytest")
                selenium = Server("Selenium")
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                eslint = Server("ESLint")
                sonarqube = Server("SonarQube")
                code_review = Server("Code Review")

        # 连接关系
        # 客户端到前端技术
        users >> tinder_mobile
        users >> tinder_web
        users >> tinder_plus
        users >> tinder_gold
        
        tinder_mobile >> react_native
        tinder_web >> react
        tinder_plus >> javascript
        tinder_gold >> typescript

        # 前端技术到后端技术
        react_native >> express
        react >> nodejs
        javascript >> django
        typescript >> spring_boot

        # 后端技术到数据存储
        nodejs >> express
        python >> django
        java >> spring_boot
        express >> mongodb
        django >> postgresql
        spring_boot >> redis
        nodejs >> elasticsearch

        # 数据存储连接
        postgresql >> mysql
        mysql >> aurora
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> elasticache
        elasticsearch >> solr
        redshift >> bigquery
        bigquery >> snowflake

        # 匹配和推荐连接
        elo_algorithm >> gale_shapley
        gale_shapley >> collaborative_filtering
        collaborative_filtering >> content_based
        recommendation_engine >> preference_learning
        preference_learning >> behavioral_analysis
        behavioral_analysis >> similarity_matching
        tensorflow >> pytorch
        pytorch >> scikit_learn
        scikit_learn >> xgboost
        feature_flags >> experiment_platform
        experiment_platform >> statistical_analysis

        # 用户和社交连接
        user_service >> profile_service
        profile_service >> authentication_service
        authentication_service >> verification_service
        messaging_service >> photo_sharing
        photo_sharing >> video_chat
        video_chat >> social_graph
        content_moderation >> photo_processing
        photo_processing >> video_processing
        video_processing >> media_storage
        location_service >> geofencing
        geofencing >> distance_calculation
        distance_calculation >> location_privacy

        # 支付和订阅连接
        stripe >> apple_pay
        apple_pay >> google_pay
        google_pay >> paypal
        subscription_service >> billing_service
        billing_service >> plan_management
        plan_management >> renewal_service
        super_likes >> boost_service
        boost_service >> passport_service
        passport_service >> rewind_service
        usage_analytics >> conversion_tracking
        conversion_tracking >> revenue_analytics

        # 安全和隐私连接
        oauth >> jwt
        jwt >> biometric_auth
        biometric_auth >> two_factor_auth
        data_encryption >> privacy_controls
        privacy_controls >> gdpr_compliance
        gdpr_compliance >> data_anonymization
        fraud_detection >> abuse_prevention
        abuse_prevention >> security_monitoring
        security_monitoring >> incident_response
        image_recognition >> text_moderation
        text_moderation >> spam_detection
        spam_detection >> fake_profile_detection

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> elb
        consul_config >> etcd_config
        etcd_config >> vault

        # 云服务连接
        ec2 >> lambda_aws
        lambda_aws >> ecs
        ecs >> fargate
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
        apm >> real_user_monitoring
        real_user_monitoring >> synthetic_monitoring

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> circleci
        jest >> pytest
        pytest >> selenium
        selenium >> cypress
        eslint >> sonarqube
        sonarqube >> code_review

        # 跨层连接
        elo_algorithm >> Edge(label="匹配算法") >> recommendation_engine
        react_native >> Edge(label="跨平台") >> tinder_mobile
        stripe >> Edge(label="支付处理") >> subscription_service
        oauth >> Edge(label="身份认证") >> user_service
        prometheus >> Edge(label="监控") >> grafana
        s3 >> Edge(label="媒体存储") >> photo_processing
        elasticsearch >> Edge(label="搜索") >> similarity_matching
        kubernetes >> Edge(label="容器编排") >> docker


if __name__ == "__main__":
    create_tinder_tech_stack_diagram(filename="tinder_tech_stack", outformat="png")
    create_tinder_tech_stack_diagram(filename="tinder_tech_stack", outformat="pdf")
