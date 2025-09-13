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
from diagrams.aws.security import IAM, KMS, SecretsManager, WAF, Shield, Guardduty, Inspector, Cognito
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions, MQ, Appsync
from diagrams.aws.ml import Sagemaker, Rekognition, Comprehend, Translate, Polly, Lex
from diagrams.aws.mobile import Amplify, DeviceFarm, Pinpoint
from diagrams.aws.iot import IotCore, IotDeviceManagement, IotAnalytics, IotEvents
from diagrams.aws.general import General, Users as AWSUsers, Client


def create_aws_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("AWS 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Web 应用"):
                web_apps = Server("Web Applications")
                spa_apps = Server("SPA Applications")
                static_sites = Server("Static Websites")
                
            with Cluster("移动应用"):
                mobile_apps = Server("Mobile Applications")
                ios_apps = Server("iOS Apps")
                android_apps = Server("Android Apps")
                
            with Cluster("桌面应用"):
                desktop_apps = Server("Desktop Applications")
                enterprise_apps = Server("Enterprise Applications")
                
            with Cluster("IoT 设备"):
                iot_devices = Server("IoT Devices")
                sensors = Server("Sensors")
                actuators = Server("Actuators")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                angular = React("Angular")
                vue = React("Vue.js")
                javascript = JavaScript("JavaScript")
                typescript = Server("TypeScript")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                flutter = Server("Flutter")
                ionic = Server("Ionic")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                vite = Server("Vite")
                rollup = Server("Rollup")
                
            with Cluster("UI框架"):
                material_ui = Server("Material-UI")
                ant_design = Server("Ant Design")
                bootstrap = Server("Bootstrap")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                java = Java("Java")
                python = Python("Python")
                javascript_backend = JavaScript("JavaScript")
                go = Go("Go")
                csharp = Server("C#")
                rust = Server("Rust")
                
            with Cluster("Web 框架"):
                spring_boot = Server("Spring Boot")
                django = Django("Django")
                express = Server("Express.js")
                aspnet = Server("ASP.NET")
                gin = Server("Gin")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                graphql = Server("GraphQL")
                grpc = Server("gRPC")
                webhooks = Server("Webhooks")

        # 计算服务层
        with Cluster("AWS 计算服务层"):
            with Cluster("虚拟服务器"):
                ec2 = EC2("Amazon EC2")
                lightsail = Lightsail("Amazon Lightsail")
                batch = Batch("AWS Batch")
                
            with Cluster("容器服务"):
                ecs = ECS("Amazon ECS")
                eks = EKS("Amazon EKS")
                fargate = Fargate("AWS Fargate")
                
            with Cluster("无服务器计算"):
                lambda_aws = Lambda("AWS Lambda")
                lambda_edge = Server("Lambda@Edge")
                
            with Cluster("边缘计算"):
                cloudfront = CloudFront("CloudFront")
                waf = WAF("AWS WAF")

        # 存储服务层
        with Cluster("AWS 存储服务层"):
            with Cluster("对象存储"):
                s3 = S3("Amazon S3")
                glacier = Server("Amazon Glacier")
                s3_ia = Server("S3 Infrequent Access")
                
            with Cluster("块存储"):
                ebs = EBS("Amazon EBS")
                instance_store = Server("Instance Store")
                
            with Cluster("文件存储"):
                efs = EFS("Amazon EFS")
                fsx = FSx("Amazon FSx")
                
            with Cluster("备份和归档"):
                backup = Backup("AWS Backup")
                storage_gateway = StorageGateway("Storage Gateway")

        # 数据库服务层
        with Cluster("AWS 数据库服务层"):
            with Cluster("关系数据库"):
                rds = RDS("Amazon RDS")
                aurora = Aurora("Amazon Aurora")
                redshift = Redshift("Amazon Redshift")
                
            with Cluster("NoSQL 数据库"):
                dynamodb = Dynamodb("Amazon DynamoDB")
                documentdb = DocumentDB("Amazon DocumentDB")
                neptune = Neptune("Amazon Neptune")
                
            with Cluster("缓存服务"):
                elasticache = ElastiCache("Amazon ElastiCache")
                memorydb = Server("Amazon MemoryDB")
                
            with Cluster("数据仓库"):
                redshift_spectrum = Server("Redshift Spectrum")
                athena = Athena("Amazon Athena")

        # 网络服务层
        with Cluster("AWS 网络服务层"):
            with Cluster("虚拟网络"):
                vpc = VPC("Amazon VPC")
                subnets = Server("Subnets")
                route_tables = Server("Route Tables")
                
            with Cluster("负载均衡"):
                elb = ELB("Elastic Load Balancing")
                alb = Server("Application Load Balancer")
                nlb = Server("Network Load Balancer")
                
            with Cluster("DNS 和 CDN"):
                route53 = Route53("Amazon Route 53")
                cloudfront_cdn = CloudFront("CloudFront CDN")
                
            with Cluster("连接服务"):
                direct_connect = DirectConnect("AWS Direct Connect")
                vpn = Server("AWS VPN")
                transit_gateway = Server("Transit Gateway")

        # 安全服务层
        with Cluster("AWS 安全服务层"):
            with Cluster("身份和访问管理"):
                iam = IAM("AWS IAM")
                cognito = Cognito("Amazon Cognito")
                sso = Server("AWS SSO")
                
            with Cluster("加密服务"):
                kms = KMS("AWS KMS")
                secrets_manager = SecretsManager("Secrets Manager")
                certificate_manager = Server("Certificate Manager")
                
            with Cluster("安全监控"):
                guardduty = Guardduty("Amazon GuardDuty")
                inspector = Inspector("Amazon Inspector")
                macie = Server("Amazon Macie")
                
            with Cluster("合规和审计"):
                cloudtrail = Cloudtrail("AWS CloudTrail")
                config = Config("AWS Config")
                security_hub = Server("Security Hub")

        # 分析和数据服务层
        with Cluster("AWS 分析和数据服务层"):
            with Cluster("大数据处理"):
                emr = EMR("Amazon EMR")
                glue = Glue("AWS Glue")
                kinesis = Kinesis("Amazon Kinesis")
                
            with Cluster("数据仓库"):
                redshift_data = Redshift("Amazon Redshift")
                athena_data = Athena("Amazon Athena")
                quicksight = Quicksight("Amazon QuickSight")
                
            with Cluster("机器学习"):
                sagemaker = Sagemaker("Amazon SageMaker")
                rekognition = Rekognition("Amazon Rekognition")
                comprehend = Comprehend("Amazon Comprehend")
                
            with Cluster("数据管道"):
                data_pipeline = DataPipeline("AWS Data Pipeline")
                step_functions = StepFunctions("AWS Step Functions")

        # 集成服务层
        with Cluster("AWS 集成服务层"):
            with Cluster("消息队列"):
                sqs = SQS("Amazon SQS")
                sns = SNS("Amazon SNS")
                eventbridge = Eventbridge("Amazon EventBridge")
                
            with Cluster("API 管理"):
                api_gateway = APIGateway("Amazon API Gateway")
                appsync = Appsync("AWS AppSync")
                
            with Cluster("工作流"):
                step_functions_workflow = StepFunctions("Step Functions")
                mq = MQ("Amazon MQ")
                
            with Cluster("事件驱动"):
                eventbridge_events = Eventbridge("EventBridge")
                lambda_events = Lambda("Lambda Events")

        # 移动和IoT服务层
        with Cluster("AWS 移动和IoT服务层"):
            with Cluster("移动开发"):
                amplify = Amplify("AWS Amplify")
                device_farm = DeviceFarm("AWS Device Farm")
                pinpoint = Pinpoint("Amazon Pinpoint")
                
            with Cluster("IoT 服务"):
                iot_core = IotCore("AWS IoT Core")
                iot_analytics = IotAnalytics("AWS IoT Analytics")
                iot_events = IotEvents("AWS IoT Events")
                
            with Cluster("设备管理"):
                iot_device_management = IotDeviceManagement("IoT Device Management")
                iot_greengrass = Server("AWS IoT Greengrass")

        # 开发工具层
        with Cluster("AWS 开发工具层"):
            with Cluster("代码管理"):
                codecommit = Server("AWS CodeCommit")
                github = Server("GitHub Integration")
                gitlab = Server("GitLab Integration")
                
            with Cluster("CI/CD"):
                codebuild = Server("AWS CodeBuild")
                codedeploy = Server("AWS CodeDeploy")
                codepipeline = Server("AWS CodePipeline")
                
            with Cluster("部署工具"):
                cloudformation = Cloudformation("AWS CloudFormation")
                cdk = Server("AWS CDK")
                sam = Server("AWS SAM")
                
            with Cluster("监控和调试"):
                xray = Server("AWS X-Ray")
                cloudwatch_logs = Cloudwatch("CloudWatch Logs")

        # 管理和监控层
        with Cluster("AWS 管理和监控层"):
            with Cluster("监控服务"):
                cloudwatch = Cloudwatch("Amazon CloudWatch")
                cloudwatch_insights = Server("CloudWatch Insights")
                cloudwatch_synthetics = Server("CloudWatch Synthetics")
                
            with Cluster("日志管理"):
                cloudwatch_logs_management = Cloudwatch("CloudWatch Logs")
                elasticsearch_service = Server("Amazon Elasticsearch Service")
                
            with Cluster("系统管理"):
                systems_manager = SystemsManager("AWS Systems Manager")
                opsworks = Server("AWS OpsWorks")
                trusted_advisor = TrustedAdvisor("AWS Trusted Advisor")
                
            with Cluster("成本管理"):
                cost_explorer = Server("AWS Cost Explorer")
                budgets = Server("AWS Budgets")
                cost_anomaly = Server("Cost Anomaly Detection")

        # 连接关系
        # 客户端到前端技术
        users >> web_apps
        users >> mobile_apps
        users >> desktop_apps
        users >> iot_devices
        
        web_apps >> react
        mobile_apps >> react_native
        desktop_apps >> enterprise_apps
        iot_devices >> iot_core

        # 前端技术到后端技术
        react >> spring_boot
        angular >> django
        vue >> express
        react_native >> lambda_aws
        flutter >> ecs

        # 后端技术到AWS计算服务
        java >> spring_boot
        python >> django
        javascript_backend >> express
        spring_boot >> ec2
        django >> lambda_aws
        express >> ecs
        go >> eks

        # AWS计算服务连接
        ec2 >> lightsail
        lightsail >> batch
        ecs >> eks
        eks >> fargate
        fargate >> lambda_aws
        lambda_aws >> lambda_edge
        cloudfront >> waf

        # 存储服务连接
        s3 >> glacier
        glacier >> s3_ia
        ebs >> instance_store
        efs >> fsx
        backup >> storage_gateway

        # 数据库服务连接
        rds >> aurora
        aurora >> redshift
        dynamodb >> documentdb
        documentdb >> neptune
        elasticache >> memorydb
        redshift >> redshift_spectrum
        redshift_spectrum >> athena

        # 网络服务连接
        vpc >> subnets
        subnets >> route_tables
        elb >> alb
        alb >> nlb
        route53 >> cloudfront_cdn
        direct_connect >> vpn
        vpn >> transit_gateway

        # 安全服务连接
        iam >> cognito
        cognito >> sso
        kms >> secrets_manager
        secrets_manager >> certificate_manager
        guardduty >> inspector
        inspector >> macie
        cloudtrail >> config
        config >> security_hub

        # 分析和数据服务连接
        emr >> glue
        glue >> kinesis
        redshift_data >> athena_data
        athena_data >> quicksight
        sagemaker >> rekognition
        rekognition >> comprehend
        data_pipeline >> step_functions

        # 集成服务连接
        sqs >> sns
        sns >> eventbridge
        api_gateway >> appsync
        step_functions_workflow >> mq
        eventbridge_events >> lambda_events

        # 移动和IoT服务连接
        amplify >> device_farm
        device_farm >> pinpoint
        iot_core >> iot_analytics
        iot_analytics >> iot_events
        iot_device_management >> iot_greengrass

        # 开发工具连接
        codecommit >> github
        github >> gitlab
        codebuild >> codedeploy
        codedeploy >> codepipeline
        cloudformation >> cdk
        cdk >> sam
        xray >> cloudwatch_logs

        # 管理和监控连接
        cloudwatch >> cloudwatch_insights
        cloudwatch_insights >> cloudwatch_synthetics
        cloudwatch_logs_management >> elasticsearch_service
        systems_manager >> opsworks
        opsworks >> trusted_advisor
        cost_explorer >> budgets
        budgets >> cost_anomaly

        # 跨层连接
        ec2 >> Edge(label="计算实例") >> ebs
        s3 >> Edge(label="对象存储") >> cloudfront
        rds >> Edge(label="关系数据库") >> aurora
        lambda_aws >> Edge(label="无服务器") >> dynamodb
        vpc >> Edge(label="虚拟网络") >> elb
        iam >> Edge(label="身份管理") >> kms
        cloudwatch >> Edge(label="监控") >> cloudtrail
        sagemaker >> Edge(label="机器学习") >> rekognition


if __name__ == "__main__":
    create_aws_tech_stack_diagram(filename="aws_tech_stack", outformat="png")
    create_aws_tech_stack_diagram(filename="aws_tech_stack", outformat="pdf")
