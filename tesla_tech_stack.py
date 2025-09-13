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
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python, Java, JavaScript, Cpp, Rust
from diagrams.programming.framework import React, Django, Spring
from diagrams.aws.compute import EC2, Lambda, ECS, EKS
from diagrams.aws.database import RDS, Dynamodb, Aurora
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB, VPC
from diagrams.aws.analytics import Kinesis, Glue, EMR, Redshift
from diagrams.aws.management import Cloudwatch, Organizations
from diagrams.aws.security import IAM, WAF, Shield
from diagrams.aws.devtools import Codebuild, Codedeploy
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.storage import EBS, EFS
from diagrams.gcp.compute import ComputeEngine, GKE, Run, Functions
from diagrams.gcp.database import Bigtable, Firestore, Spanner, SQL
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Dataproc

def create_tesla_tech_stack_diagram(filename: str, outformat: str) -> None: 
    # 创建特斯拉技术栈图表
    with Diagram("特斯拉技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("特斯拉车主")
            mobile_app = Server("Tesla App")
            web_portal = Server("Tesla 官网")
            service_center = Server("服务中心")
            
        # 车辆层
        with Cluster("车辆层"):
            with Cluster("车辆硬件"):
                vehicle_computer = Server("车辆计算机")
                autopilot_hw = Server("Autopilot 硬件")
                battery_management = Server("电池管理系统")
                charging_port = Server("充电接口")
                
            with Cluster("车辆软件"):
                vehicle_os = Server("车辆操作系统")
                autopilot_sw = Server("Autopilot 软件")
                infotainment = Server("信息娱乐系统")
                ota_updates = Server("OTA 更新系统")
                
        # 网络层
        with Cluster("网络层"):
            with Cluster("通信协议"):
                cellular = Server("蜂窝网络")
                wifi = Server("WiFi 连接")
                bluetooth = Server("蓝牙连接")
                can_bus = Server("CAN 总线")
                
            with Cluster("数据采集"):
                sensors = Server("传感器数据")
                telemetry = Server("遥测数据")
                logs = Server("车辆日志")
                
        # 云端服务层
        with Cluster("云端服务层"):
            with Cluster("API 网关"):
                api_gateway = Server("API 网关")
                load_balancer = ELB("负载均衡")
                
            with Cluster("核心服务"):
                with Cluster("车辆管理"):
                    vehicle_service = Server("车辆管理服务")
                    user_service = Server("用户管理服务")
                    charging_service = Server("充电服务")
                    
                with Cluster("自动驾驶"):
                    autopilot_service = Server("Autopilot 服务")
                    neural_network = Server("神经网络")
                    computer_vision = Server("计算机视觉")
                    path_planning = Server("路径规划")
                    
                with Cluster("能源管理"):
                    energy_service = Server("能源管理服务")
                    solar_service = Server("太阳能服务")
                    grid_service = Server("电网服务")
                    
            with Cluster("数据服务"):
                with Cluster("实时数据"):
                    telemetry_service = Server("遥测服务")
                    sensor_service = Server("传感器服务")
                    location_service = Server("位置服务")
                    
                with Cluster("数据分析"):
                    analytics_service = Server("分析服务")
                    ml_service = Server("机器学习服务")
                    prediction_service = Server("预测服务")
                    
        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系型数据库"):
                vehicle_db = PostgreSQL("车辆数据库")
                user_db = PostgreSQL("用户数据库")
                service_db = PostgreSQL("服务数据库")
                
            with Cluster("NoSQL 数据库"):
                telemetry_db = MongoDB("遥测数据库")
                sensor_db = Cassandra("传感器数据库")
                logs_db = MongoDB("日志数据库")
                
            with Cluster("数据仓库"):
                data_warehouse = Redshift("数据仓库")
                bigquery = BigQuery("BigQuery")
                
            with Cluster("对象存储"):
                s3_storage = S3("S3 存储")
                gcs_storage = GCS("GCS 存储")
                
        # 消息队列层
        with Cluster("消息队列层"):
            with Cluster("消息队列"):
                kafka_cluster = Kafka("Kafka 集群")
                sqs_queue = SQS("SQS 队列")
                sns_topic = SNS("SNS 主题")
                
            with Cluster("事件流"):
                kinesis_stream = Kinesis("Kinesis 流")
                pubsub_stream = PubSub("Pub/Sub 流")
                
        # 大数据处理层
        with Cluster("大数据处理层"):
            with Cluster("批处理"):
                spark_cluster = Spark("Spark 集群")
                hadoop_cluster = Hadoop("Hadoop 集群")
                emr_cluster = EMR("EMR 集群")
                
            with Cluster("流处理"):
                kafka_streams = Server("Kafka Streams")
                flink_cluster = Server("Flink 集群")
                storm_cluster = Server("Storm 集群")
                
            with Cluster("机器学习"):
                tensorflow = Server("TensorFlow")
                pytorch = Server("PyTorch")
                mlflow = Server("MLflow")
                
        # 监控和运维层
        with Cluster("监控和运维层"):
            with Cluster("监控系统"):
                prometheus = Prometheus("Prometheus")
                grafana = Grafana("Grafana")
                cloudwatch = Cloudwatch("CloudWatch")
                
            with Cluster("日志管理"):
                elk_stack = Server("ELK 栈")
                splunk = Server("Splunk")
                cloudwatch_logs = Server("CloudWatch Logs")
                
            with Cluster("安全系统"):
                vault = Vault("Vault")
                iam = IAM("IAM")
                waf = WAF("WAF")
                
        # 开发和部署层
        with Cluster("开发和部署层"):
            with Cluster("CI/CD"):
                jenkins = Server("Jenkins")
                gitlab_ci = Server("GitLab CI")
                codebuild = Codebuild("CodeBuild")
                codedeploy = Codedeploy("CodeDeploy")
                
            with Cluster("容器化"):
                docker = Server("Docker")
                kubernetes = GKE("Kubernetes")
                ecs = ECS("ECS")
                
            with Cluster("基础设施"):
                terraform = Server("Terraform")
                ansible = Server("Ansible")
                cloudformation = Server("CloudFormation")
                
        # 连接关系
        users >> mobile_app
        users >> web_portal
        users >> service_center
        
        mobile_app >> api_gateway
        web_portal >> api_gateway
        service_center >> api_gateway
        
        api_gateway >> load_balancer
        load_balancer >> vehicle_service
        load_balancer >> user_service
        load_balancer >> charging_service
        
        vehicle_computer >> cellular
        vehicle_computer >> wifi
        vehicle_computer >> bluetooth
        
        cellular >> api_gateway
        wifi >> api_gateway
        
        sensors >> telemetry_service
        telemetry >> telemetry_service
        logs >> logs_db
        
        vehicle_service >> vehicle_db
        user_service >> user_db
        charging_service >> service_db
        
        autopilot_service >> neural_network
        autopilot_service >> computer_vision
        autopilot_service >> path_planning
        
        telemetry_service >> kafka_cluster
        sensor_service >> kafka_cluster
        
        kafka_cluster >> spark_cluster
        kafka_cluster >> hadoop_cluster
        
        spark_cluster >> data_warehouse
        hadoop_cluster >> data_warehouse
        
        analytics_service >> ml_service
        ml_service >> prediction_service
        
        tensorflow >> ml_service
        pytorch >> ml_service
        
        prometheus >> grafana
        cloudwatch >> grafana
        
        vault >> iam
        waf >> api_gateway
        
        jenkins >> codebuild
        codebuild >> codedeploy
        codedeploy >> kubernetes

if __name__ == "__main__":
    create_tesla_tech_stack_diagram(filename="tesla_tech_stack", outformat="png")
    create_tesla_tech_stack_diagram(filename="tesla_tech_stack", outformat="pdf")