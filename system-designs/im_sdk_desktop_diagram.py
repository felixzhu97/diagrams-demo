from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_sdk_desktop(filename: str, outformat: str) -> None:
    with Diagram("IM SDK（桌面端）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("App（桌面端）"):
            app_ui = Server("Desktop UI")
            sdk_api = Server("SDK API")
            event_bus = Server("Event Bus")
            app_ui >> Edge(label="调用/订阅") >> sdk_api >> Edge(label="事件") >> event_bus

        with Cluster("系统集成（桌面）"):
            fs_watch = Server("文件系统监控")
            keychain = Server("钥匙串/凭证库")
            proxy = Server("系统代理/证书")
            multi_window = Server("多窗口/托盘")
            sdk_api >> fs_watch
            sdk_api >> keychain
            sdk_api >> proxy
            sdk_api >> multi_window

        with Cluster("连接与可靠性"):
            conn = Server("Connection Manager")
            transport = Server("WebSocket/HTTP2")
            heartbeat = Server("Heartbeat")
            reconnect = Server("Reconnect")
            ack = Server("ACK/重传")
            conn >> transport >> heartbeat
            conn >> reconnect

        with Cluster("本地存储与媒体"):
            local_store = Server("SQLite/LevelDB")
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
    create_im_sdk_desktop(filename="im_sdk_desktop", outformat="png")
    create_im_sdk_desktop(filename="im_sdk_desktop", outformat="pdf")
