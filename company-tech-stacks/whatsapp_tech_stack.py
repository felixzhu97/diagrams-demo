from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Users, User
from diagrams.onprem.network import Internet
from diagrams.onprem.database import PostgreSQL, MongoDB
from diagrams.onprem.storage import Ceph
from diagrams.onprem.queue import Kafka
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.security import Vault
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Erlang, Java, Python, JavaScript
from diagrams.programming.framework import React
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_whatsapp_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("WhatsApp 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            mobile_users = Users("移动用户")
            web_users = User("Web用户")
            desktop_users = User("桌面用户")
            
            with Cluster("移动端"):
                android_app = Server("Android App")
                ios_app = Server("iOS App")
                
            with Cluster("Web端"):
                web_app = Server("WhatsApp Web")
                
            with Cluster("桌面端"):
                desktop_app = Server("WhatsApp Desktop")

        # CDN和负载均衡
        with Cluster("CDN & 负载均衡"):
            cdn = CloudFront("CloudFront CDN")
            load_balancer = Router("负载均衡器")
            cdn >> load_balancer

        # 接入层
        with Cluster("接入层"):
            with Cluster("API网关"):
                api_gateway = Server("API Gateway")
                rate_limiter = Firewall("限流器")
                
            with Cluster("消息路由"):
                message_router = Router("消息路由器")
                presence_service = Server("在线状态服务")
                
            api_gateway >> rate_limiter >> message_router >> presence_service

        # 核心业务层
        with Cluster("核心业务层 (Erlang/OTP)"):
            with Cluster("消息处理引擎"):
                ejabberd = Server("Ejabberd (修改版)")
                message_queue = Kafka("消息队列")
                message_processor = Erlang("消息处理器")
                
            with Cluster("实时通信"):
                websocket_gateway = Server("WebSocket网关")
                xmpp_protocol = Server("XMPP协议栈")
                
            with Cluster("媒体处理"):
                media_server = Server("媒体服务器")
                image_processor = Python("图像处理器")
                video_processor = Python("视频处理器")
                
            ejabberd >> message_queue >> message_processor
            websocket_gateway >> xmpp_protocol
            media_server >> image_processor
            media_server >> video_processor

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("用户数据"):
                user_db = PostgreSQL("用户数据库")
                profile_cache = Storage("用户缓存")
                
            with Cluster("消息存储"):
                message_db = MongoDB("消息数据库")
                message_archive = Ceph("消息归档")
                
            with Cluster("媒体存储"):
                media_storage = S3("媒体存储")
                thumbnail_cache = Storage("缩略图缓存")
                
            with Cluster("会话管理"):
                session_store = Storage("会话存储")
                device_registry = SQL("设备注册表")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("操作系统"):
                freebsd_servers = Rack("FreeBSD 服务器集群")
                
            with Cluster("容器化"):
                erlang_vm = Server("BEAM VM")
                process_supervisor = Server("进程监控器")
                
            with Cluster("监控告警"):
                prometheus_monitor = Prometheus("Prometheus")
                grafana_dashboard = Grafana("Grafana仪表板")
                alert_manager = Server("告警管理器")
                
            freebsd_servers >> erlang_vm >> process_supervisor
            prometheus_monitor >> grafana_dashboard >> alert_manager

        # 安全层
        with Cluster("安全层"):
            with Cluster("认证授权"):
                auth_service = Vault("认证服务")
                encryption_service = Server("端到端加密")
                
            with Cluster("安全防护"):
                ddos_protection = Firewall("DDoS防护")
                content_filter = Server("内容过滤")
                
            auth_service >> encryption_service
            ddos_protection >> content_filter

        # 外部集成
        with Cluster("外部集成"):
            with Cluster("第三方服务"):
                push_notifications = Server("推送通知")
                sms_gateway = Router("SMS网关")
                payment_gateway = Server("支付网关")
                
            with Cluster("云服务"):
                aws_services = EC2("AWS服务")
                gcp_services = ComputeEngine("GCP服务")

        # 连接关系
        # 客户端到CDN
        mobile_users >> android_app
        mobile_users >> ios_app
        web_users >> web_app
        desktop_users >> desktop_app
        
        android_app >> cdn
        ios_app >> cdn
        web_app >> cdn
        desktop_app >> cdn

        # CDN到接入层
        cdn >> Edge(label="HTTPS") >> api_gateway
        api_gateway >> Edge(label="WebSocket") >> websocket_gateway

        # 接入层到核心业务层
        message_router >> Edge(label="消息路由") >> ejabberd
        presence_service >> Edge(label="状态更新") >> ejabberd
        websocket_gateway >> Edge(label="实时消息") >> message_processor

        # 核心业务层到数据存储
        message_processor >> Edge(label="消息存储") >> message_db
        message_processor >> Edge(label="用户数据") >> user_db
        ejabberd >> Edge(label="会话管理") >> session_store
        media_server >> Edge(label="媒体存储") >> media_storage

        # 数据存储关联
        user_db >> profile_cache
        message_db >> message_archive
        media_storage >> thumbnail_cache
        session_store >> device_registry

        # 基础设施支撑
        freebsd_servers >> Edge(label="运行环境") >> ejabberd
        erlang_vm >> Edge(label="进程管理") >> message_processor
        process_supervisor >> Edge(label="健康检查") >> ejabberd

        # 监控关联
        prometheus_monitor >> Edge(label="指标收集") >> ejabberd
        prometheus_monitor >> Edge(label="指标收集") >> message_processor
        prometheus_monitor >> Edge(label="指标收集") >> user_db
        grafana_dashboard >> Edge(label="可视化") >> prometheus_monitor

        # 安全关联
        api_gateway >> Edge(label="认证") >> auth_service
        message_processor >> Edge(label="加密") >> encryption_service
        load_balancer >> Edge(label="防护") >> ddos_protection

        # 外部集成
        message_processor >> Edge(label="推送") >> push_notifications
        auth_service >> Edge(label="短信验证") >> sms_gateway
        media_storage >> Edge(label="存储") >> aws_services
        message_archive >> Edge(label="大数据") >> gcp_services


if __name__ == "__main__":
    create_whatsapp_tech_stack_diagram(filename="whatsapp_tech_stack", outformat="png")
    create_whatsapp_tech_stack_diagram(filename="whatsapp_tech_stack", outformat="pdf")
