from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_sdk_mobile(filename: str, outformat: str) -> None:
    with Diagram("IM SDK（移动端）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("App（移动端）"):
            app_ui = Server("App UI")
            sdk_api = Server("SDK API")
            event_bus = Server("Event Bus")
            app_ui >> Edge(label="调用/订阅") >> sdk_api >> Edge(label="事件") >> event_bus

        with Cluster("移动特性（后台/权限/系统服务）"):
            bg_task = Server("后台任务/保活")
            permissions = Server("权限（通知/麦克风/存储）")
            os_services = Server("系统服务（电量/前后台）")
            sdk_api >> bg_task
            sdk_api >> permissions
            sdk_api >> os_services

        with Cluster("连接与可靠性"):
            conn = Server("Connection Manager")
            transport = Server("WebSocket/HTTP2")
            heartbeat = Server("Heartbeat")
            reconnect = Server("Reconnect")
            ack = Server("ACK/重传")
            conn >> transport >> heartbeat
            conn >> reconnect

        with Cluster("Push 集成"):
            apns = Server("APNs")
            fcm = Server("FCM")
            push_bridge = Server("Push Bridge")
            push_bridge >> apns
            push_bridge >> fcm
            sdk_api >> push_bridge

        with Cluster("本地存储与媒体"):
            local_store = Server("SQLite/Realm")
            media_cache = Server("Media Cache")
            msg_queue = Server("Msg Queue")
            sdk_api >> local_store
            sdk_api >> media_cache
            sdk_api >> msg_queue

        with Cluster("协议与安全"):
            protocol = Server("协议/序列化")
            e2ee = Server("E2EE 会话密钥")
            compress = Server("压缩")
            protocol >> e2ee
            protocol >> compress

        with Cluster("服务端（抽象）"):
            auth = Server("Auth/Token")
            route = Server("路由")
            msg = Server("消息服务")
            media = Server("媒体上传")
            presence = Server("在线状态")

        # flows
        sdk_api >> Edge(label="鉴权") >> auth
        sdk_api >> Edge(label="接入点") >> route
        transport >> Edge(label="协议消息") >> protocol
        protocol >> Edge(label="发送/接收") >> msg
        sdk_api >> Edge(label="上传") >> media
        protocol >> Edge(label="订阅") >> presence
        msg_queue >> Edge(label="重试") >> protocol
        ack >> Edge(label="确认") >> msg_queue
        heartbeat >> Edge(label="保活") >> reconnect


if __name__ == "__main__":
    create_im_sdk_mobile(filename="im_sdk_mobile", outformat="png")
    create_im_sdk_mobile(filename="im_sdk_mobile", outformat="pdf")
