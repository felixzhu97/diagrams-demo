from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_big_data_diagram(filename: str, outformat: str) -> None:
    with Diagram("大数据系统设计图（含实时数仓）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("数据接入（实时/批量）"):
            kafka = Server("消息队列（Kafka/ Pulsar）")
            ingestion = Server("采集/接入（Flume/Logstash）")
            api = Server("数据接入 API")
            cdc = Server("CDC（Debezium/Stream）")
            connect = Server("Kafka Connect")
            ingestion >> kafka
            api >> kafka
            cdc >> kafka
            connect >> kafka

        with Cluster("湖仓存储"):
            hdfs = Server("数据湖（HDFS/对象存储）")
            delta = Server("湖仓表（Delta/Iceberg/Hudi）")
            catalog = Server("元数据目录/Metastore")
            hdfs >> delta
            delta >> catalog

        with Cluster("计算引擎"):
            spark = Server("批处理（Spark）")
            flink = Server("流处理（Flink）")
            presto = Server("交互查询（Presto/Trino）")
            spark >> presto
            flink >> delta

        with Cluster("实时数仓/明细-汇总"):
            doris = Server("Doris/StarRocks")
            ck = Server("ClickHouse")
            realtime_agg = Server("实时聚合/物化视图")
            doris >> realtime_agg
            ck >> realtime_agg

        with Cluster("调度与编排"):
            airflow = Server("工作流（Airflow）")
            scheduler = Server("调度/依赖管理")
            airflow >> scheduler

        with Cluster("治理与质量"):
            quality = Server("数据质量/校验")
            lineage = Server("血缘/审计")
            sec = Server("权限/合规")
            quality >> lineage
            sec >> lineage

        with Cluster("特征/服务"):
            feature_store = Server("特征库")
            serving = Server("数据服务 API")
            feature_store >> serving

        # Flows
        kafka >> Edge(label="流写入") >> delta
        kafka >> Edge(label="实时入仓") >> doris
        kafka >> Edge(label="实时入仓") >> ck
        airflow >> Edge(label="批处理/ETL") >> spark
        spark >> Edge(label="写入湖仓") >> delta
        flink >> Edge(label="实时聚合") >> doris
        flink >> Edge(label="实时聚合") >> ck
        presto >> Edge(label="查询") >> delta
        delta >> Edge(label="产出特征") >> feature_store
        catalog >> Edge(label="编目/治理") >> lineage
        quality >> Edge(label="校验规则") >> airflow
        realtime_agg >> Edge(label="服务/OLAP") >> serving


if __name__ == "__main__":
    create_big_data_diagram(filename="big_data_design", outformat="png")
    create_big_data_diagram(filename="big_data_design", outformat="pdf") 
