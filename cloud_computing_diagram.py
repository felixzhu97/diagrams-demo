from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_cloud_diagram(filename: str, outformat: str) -> None:
    with Diagram("云计算架构设计图", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("控制面（Control Plane）"):
            cp_api = Server("API/Console")
            cp_iam = Server("IAM/Policy")
            cp_cmdb = Server("CMDB/资源目录")
            cp_billing = Server("计费/配额")
            cp_api >> cp_iam >> cp_cmdb >> cp_billing

        with Cluster("计算（Compute）"):
            vm = Server("虚拟机/Auto Scaling")
            container = Server("容器/K8s")
            faas = Server("函数计算/Serverless")
            vm >> container >> faas

        with Cluster("存储（Storage）"):
            block = Server("块存储")
            object_store = Server("对象存储")
            file_store = Server("文件存储")
            cache = Server("缓存/分布式缓存")
            block >> file_store
            object_store >> cache

        with Cluster("网络（Networking）"):
            vpc = Server("VPC/子网")
            lb = Server("负载均衡")
            gw = Server("网关/NAT/IGW")
            dns = Server("DNS/解析")
            vpc >> lb >> gw >> dns

        with Cluster("数据库与中间件"):
            rdb = Server("关系型数据库")
            nosql = Server("NoSQL/Key-Value")
            mq = Server("消息队列")
            search = Server("搜索/索引")
            rdb >> mq
            nosql >> search

        with Cluster("可观测性"):
            logs = Server("日志")
            metrics = Server("指标")
            trace = Server("链路追踪")
            logs >> metrics >> trace

        with Cluster("安全与合规"):
            waf = Server("WAF/防护")
            kms = Server("KMS/密钥")
            audit = Server("审计/合规")
            waf >> audit
            kms >> audit

        with Cluster("Region A（主区域）"):
            app_a = Server("应用集群 A")
            db_a = Server("数据库 A")
            cache_a = Server("缓存 A")
            app_a >> db_a
            app_a >> cache_a

        with Cluster("Region B（容灾区域）"):
            app_b = Server("应用集群 B")
            db_b = Server("数据库 B")
            cache_b = Server("缓存 B")

        # 访问与发布
        cp_api >> Edge(label="创建/管理") >> vpc
        lb >> Edge(label="入口流量") >> app_a
        dns >> Edge(label="解析/权重") >> lb

        # 数据与中间件
        app_a >> Edge(label="读写") >> rdb
        app_a >> Edge(label="缓存") >> cache
        app_a >> Edge(label="消息") >> mq
        app_a >> Edge(label="对象读写") >> object_store

        # 可观测与安全
        app_a >> Edge(label="日志") >> logs
        app_a >> Edge(label="指标") >> metrics
        app_a >> Edge(label="追踪") >> trace
        lb >> Edge(label="防护") >> waf
        kms >> Edge(label="加解密") >> object_store

        # 多区域容灾
        db_a >> Edge(label="异步复制") >> db_b
        object_store >> Edge(label="跨区域复制") >> app_b
        cache_a >> Edge(label="可选复制") >> cache_b
        app_a >> Edge(label="蓝绿/热备") >> app_b


if __name__ == "__main__":
    create_cloud_diagram(filename="cloud_computing", outformat="png")
    create_cloud_diagram(filename="cloud_computing", outformat="pdf")
