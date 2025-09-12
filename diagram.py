from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams import Cluster
from diagrams.onprem.client import Users
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.queue import Kafka
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.database import PostgreSQL
# from diagrams.onprem.search import Elasticsearch
from diagrams.onprem.analytics import Spark
from diagrams.onprem.workflow import Airflow
# from diagrams.onprem.storage import Hdfs
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.monitoring import Grafana
# from diagrams.onprem.ml import Mlflow
from diagrams import Edge

with Diagram("Web Service", show=False):
    ELB("Load Balancer") >> EC2("Web Server") >> RDS("Database")


def create_data_intensive_diagram(filename: str, outformat: str) -> None:
    with Diagram("数据密集型系统设计", filename=filename, show=False, outformat=outformat, direction="LR"):
        users = Users("Clients")

        with Cluster("Region A（主区域）"):
            with Cluster("API & App Layer（入口与业务逻辑）"):
                lb = Nginx("API Gateway")
                app = Server("Application Service")
                lb >> Edge(label="Requests") >> app

            with Cluster("Data Integration & ETL（批处理/调度与作业执行）"):
                etl_orch = Airflow("ETL Orchestrator")
                etl_jobs = Server("ETL Jobs")
                etl_orch >> etl_jobs

            with Cluster("Event Ingestion（事件采集与传输）"):
                event_log = Kafka("Kafka Event Log")

            with Cluster("Primary Storage (OLTP)（事务型主存储）"):
                db_primary = PostgreSQL("OLTP Primary")
                db_replica = PostgreSQL("Read Replica")
                db_primary >> Edge(label="Replicate") >> db_replica

            with Cluster("Cache & Index（低延迟读与检索）"):
                cache = Redis("Redis Cache")
                search = Server("Search Index")

            with Cluster("Observability（监控与可视化）"):
                metrics = Prometheus("Metrics")
                dashboards = Grafana("Dashboards")
                metrics >> dashboards

            with Cluster("Stream Processing（实时计算）"):
                stream_proc = Spark("Stream Processing")

            with Cluster("Batch Processing & Analytics（离线计算与分析）"):
                orchestrator = Airflow("Batch Orchestrator")
                data_lake = Server("Data Lake")
                batch_proc = Spark("Batch Processing")
                warehouse = PostgreSQL("Warehouse (OLAP)")
                orchestrator >> data_lake >> batch_proc >> warehouse

            with Cluster("ML Feature Store（特征管理）"):
                feature_store = Server("Feature Store")
                model_registry = Server("Model Registry")
                feature_store >> model_registry

            with Cluster("BI & Serving（分析与对外服务）"):
                bi = Server("BI / Reporting")
                serving_api = Server("Serving API")

            with Cluster("Governance & Security（治理、权限与合规）"):
                iam = Server("IAM / RBAC")
                catalog = Server("Data Catalog")
                audit = Server("Audit / Lineage")
                dlp = Server("DLP / PII Masking")
                catalog >> audit

            with Cluster("Backup & Archival（备份与归档）"):
                backup_svc = Server("Backup Service")
                archive_store = Server("Archive Storage")
                backup_svc >> archive_store

        # 次区域 / 容灾区域
        with Cluster("Region B（容灾区域）"):
            app_b = Server("App (DR)")
            db_dr = PostgreSQL("OLTP DR")
            cache_b = Server("Cache (DR)")
            warehouse_b = Server("Warehouse (DR)")

        # App write/read paths
        app >> Edge(label="Write") >> db_primary
        db_replica >> Edge(label="Reads") >> app

        # Cache & index
        app >> Edge(label="Cache") >> cache
        app >> Edge(label="Index") >> search

        # Ingestion and streaming
        app >> Edge(label="Events") >> event_log
        db_primary >> Edge(label="CDC") >> event_log
        event_log >> Edge(label="Streams") >> stream_proc
        stream_proc >> Edge(label="Materialize") >> cache
        stream_proc >> Edge(label="Materialize") >> search
        stream_proc >> Edge(label="Materialize") >> warehouse
        stream_proc >> Edge(label="Features") >> feature_store

        # Batch & ETL
        etl_jobs >> Edge(label="Batch ETL") >> data_lake
        data_lake >> Edge(label="Batch") >> batch_proc
        batch_proc >> Edge(label="Load") >> warehouse
        warehouse >> Edge(label="Reports") >> bi

        # Serving
        feature_store >> Edge(label="Features") >> serving_api
        serving_api >> Edge(label="Responses") >> users

        # Observability
        app >> Edge(label="Metrics") >> metrics
        stream_proc >> Edge(label="Metrics") >> metrics
        etl_jobs >> Edge(label="Metrics") >> metrics

        # Governance & Security hooks
        users >> Edge(label="AuthN/Z") >> iam
        app >> Edge(label="AuthZ Check") >> iam
        warehouse >> Edge(label="Catalog / Lineage") >> catalog
        data_lake >> Edge(label="Catalog / Lineage") >> catalog
        etl_jobs >> Edge(label="Lineage") >> audit
        db_primary >> Edge(label="Masking Policies") >> dlp

        # Backup & Archival
        db_primary >> Edge(label="Backup") >> backup_svc
        warehouse >> Edge(label="Backup") >> backup_svc
        data_lake >> Edge(label="Snapshots") >> archive_store

        # 跨区域容灾复制
        db_primary >> Edge(label="异步复制") >> db_dr
        warehouse >> Edge(label="快照/复制") >> warehouse_b
        cache >> Edge(label="可选复制") >> cache_b
        app >> Edge(label="蓝绿/热备") >> app_b


# Generate PNG and PDF only for data-intensive diagram
create_data_intensive_diagram(filename="data_intensive_system", outformat="png")
create_data_intensive_diagram(filename="data_intensive_system", outformat="pdf")