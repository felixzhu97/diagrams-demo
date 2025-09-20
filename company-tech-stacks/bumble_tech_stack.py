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


def create_bumble_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Bumble 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("移动应用"):
                bumble_mobile = Server("Bumble Mobile")
                bumble_ios = Server("Bumble iOS")
                bumble_android = Server("Bumble Android")
                
            with Cluster("Web 应用"):
                bumble_web = Server("Bumble Web")
                bumble_date = Server("Bumble Date")
                bumble_bizz = Server("Bumble Bizz")
                bumble_bff = Server("Bumble BFF")
                
            with Cluster("第三方集成"):
                spotify_integration = Server("Spotify Integration")
                facebook_integration = Server("Facebook Integration")
                google_integration = Server("Google Integration")
                apple_integration = Server("Apple Integration")
                
            with Cluster("扩展应用"):
                bumble_spotlight = Server("Bumble Spotlight")
                bumble_snooze = Server("Bumble Snooze")
                bumble_video_chat = Server("Video Chat")
                bumble_voice_notes = Server("Voice Notes")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("Web 技术"):
                react = React("React.js")
                vue = React("Vue.js")
                javascript = JavaScript("JavaScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                typescript = Server("TypeScript")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                metro = Server("Metro")
                
            with Cluster("UI组件库"):
                bumble_ui = Server("Bumble UI")
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
                hapi = Server("HAPI Framework")
                django = Django("Django")
                flask = Server("Flask")
                spring_boot = Server("Spring Boot")
                gin = Server("Gin")
                
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
                cassandra = Cassandra("Apache Cassandra")
                mongodb = MongoDB("MongoDB")
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

        # 匹配和社交层
        with Cluster("匹配和社交层"):
            with Cluster("匹配算法"):
                elo_algorithm = Server("ELO Algorithm")
                collaborative_filtering = Server("Collaborative Filtering")
                content_based = Server("Content-based Filtering")
                hybrid_recommendation = Server("Hybrid Recommendation")
                
            with Cluster("社交功能"):
                messaging_service = Server("Messaging Service")
                photo_sharing = Server("Photo Sharing")
                video_chat = Server("Video Chat")
                voice_notes = Server("Voice Notes")
                
            with Cluster("女性优先机制"):
                first_move_control = Server("First Move Control")
                conversation_initiation = Server("Conversation Initiation")
                gender_based_matching = Server("Gender-based Matching")
                safety_features = Server("Safety Features")
                
            with Cluster("地理位置"):
                location_service = Server("Location Service")
                geofencing = Server("Geofencing")
                distance_calculation = Server("Distance Calculation")
                location_privacy = Server("Location Privacy")

        # 用户和内容管理层
        with Cluster("用户和内容管理层"):
            with Cluster("用户管理"):
                user_service = Server("User Service")
                profile_service = Server("Profile Service")
                authentication_service = Server("Authentication Service")
                verification_service = Server("Verification Service")
                
            with Cluster("内容管理"):
                content_moderation = Server("Content Moderation")
                photo_processing = Server("Photo Processing")
                video_processing = Server("Video Processing")
                media_storage = Server("Media Storage")
                
            with Cluster("安全审核"):
                image_recognition = Server("Image Recognition")
                text_moderation = Server("Text Moderation")
                spam_detection = Server("Spam Detection")
                fake_profile_detection = Server("Fake Profile Detection")
                
            with Cluster("用户验证"):
                photo_verification = Server("Photo Verification")
                phone_verification = Server("Phone Verification")
                email_verification = Server("Email Verification")
                identity_verification = Server("Identity Verification")

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
                super_swipes = Server("Super Swipes")
                spotlight_feature = Server("Spotlight Feature")
                advanced_filters = Server("Advanced Filters")
                unlimited_swipes = Server("Unlimited Swipes")
                
            with Cluster("分析服务"):
                usage_analytics = Server("Usage Analytics")
                conversion_tracking = Server("Conversion Tracking")
                revenue_analytics = Server("Revenue Analytics")

        # 实时通信层
        with Cluster("实时通信层"):
            with Cluster("消息队列"):
                rabbitmq = Server("RabbitMQ")
                mqtt = Server("MQTT")
                kafka = Kafka("Apache Kafka")
                
            with Cluster("实时通信"):
                websocket = Server("WebSocket")
                socket_io = Server("Socket.IO")
                real_time_messaging = Server("Real-time Messaging")
                
            with Cluster("推送通知"):
                fcm = Server("Firebase Cloud Messaging")
                apns = Server("Apple Push Notification Service")
                push_notifications = Server("Push Notifications")
                
            with Cluster("通知服务"):
                email_notifications = Server("Email Notifications")
                sms_notifications = Server("SMS Notifications")
                in_app_notifications = Server("In-app Notifications")

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
                
            with Cluster("女性安全"):
                safety_center = Server("Safety Center")
                block_report = Server("Block & Report")
                photo_verification_safety = Server("Photo Verification")
                emergency_contacts = Server("Emergency Contacts")

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
        users >> bumble_mobile
        users >> bumble_web
        users >> bumble_date
        users >> bumble_bizz
        
        bumble_mobile >> react_native
        bumble_web >> react
        bumble_date >> vue
        bumble_bizz >> javascript

        # 前端技术到后端技术
        react_native >> hapi
        react >> nodejs
        vue >> django
        javascript >> flask

        # 后端技术到数据存储
        nodejs >> hapi
        python >> django
        java >> spring_boot
        hapi >> cassandra
        django >> mongodb
        spring_boot >> redis
        nodejs >> elasticsearch

        # 数据存储连接
        postgresql >> mysql
        mysql >> aurora
        cassandra >> mongodb
        mongodb >> dynamodb
        redis >> memcached
        memcached >> elasticache
        elasticsearch >> solr
        redshift >> bigquery
        bigquery >> snowflake

        # 匹配和社交连接
        elo_algorithm >> collaborative_filtering
        collaborative_filtering >> content_based
        content_based >> hybrid_recommendation
        messaging_service >> photo_sharing
        photo_sharing >> video_chat
        video_chat >> voice_notes
        first_move_control >> conversation_initiation
        conversation_initiation >> gender_based_matching
        gender_based_matching >> safety_features
        location_service >> geofencing
        geofencing >> distance_calculation
        distance_calculation >> location_privacy

        # 用户和内容管理连接
        user_service >> profile_service
        profile_service >> authentication_service
        authentication_service >> verification_service
        content_moderation >> photo_processing
        photo_processing >> video_processing
        video_processing >> media_storage
        image_recognition >> text_moderation
        text_moderation >> spam_detection
        spam_detection >> fake_profile_detection
        photo_verification >> phone_verification
        phone_verification >> email_verification
        email_verification >> identity_verification

        # 支付和订阅连接
        stripe >> apple_pay
        apple_pay >> google_pay
        google_pay >> paypal
        subscription_service >> billing_service
        billing_service >> plan_management
        plan_management >> renewal_service
        super_swipes >> spotlight_feature
        spotlight_feature >> advanced_filters
        advanced_filters >> unlimited_swipes
        usage_analytics >> conversion_tracking
        conversion_tracking >> revenue_analytics

        # 实时通信连接
        rabbitmq >> mqtt
        mqtt >> kafka
        websocket >> socket_io
        socket_io >> real_time_messaging
        fcm >> apns
        apns >> push_notifications
        email_notifications >> sms_notifications
        sms_notifications >> in_app_notifications

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
        safety_center >> block_report
        block_report >> photo_verification_safety
        photo_verification_safety >> emergency_contacts

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
        elo_algorithm >> Edge(label="匹配算法") >> collaborative_filtering
        react_native >> Edge(label="跨平台") >> bumble_mobile
        stripe >> Edge(label="支付处理") >> subscription_service
        oauth >> Edge(label="身份认证") >> user_service
        prometheus >> Edge(label="监控") >> grafana
        s3 >> Edge(label="媒体存储") >> photo_processing
        elasticsearch >> Edge(label="搜索") >> hybrid_recommendation
        kubernetes >> Edge(label="容器编排") >> docker
        first_move_control >> Edge(label="女性优先") >> conversation_initiation
        rabbitmq >> Edge(label="消息队列") >> websocket


if __name__ == "__main__":
    create_bumble_tech_stack_diagram(filename="bumble_tech_stack", outformat="png")
    create_bumble_tech_stack_diagram(filename="bumble_tech_stack", outformat="pdf")
