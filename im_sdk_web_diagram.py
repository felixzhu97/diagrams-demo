from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_sdk_web(filename: str, outformat: str) -> None:
    with Diagram("IM SDK（Web）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("Web App（浏览器）"):
            app_ui = Server("SPA/SSR UI")
            sdk_api = Server("SDK API")
            event_bus = Server("Event Bus")
            app_ui >> Edge(label="调用/订阅") >> sdk_api >> Edge(label="事件") >> event_bus

        with Cluster("浏览器运行时"):
            sw = Server("Service Worker")
            webcrypto = Server("WebCrypto")
            idb = Server("IndexedDB")
            notif = Server("Notifications")
            sdk_api >> sw
            sdk_api >> webcrypto
            sdk_api >> idb
            sdk_api >> notif

        with Cluster("连接与降级"):
            ws = Server("WebSocket")
            http2 = Server("HTTP/2")
            sse = Server("SSE")
            longpoll = Server("Long Polling")
            ws >> http2
            http2 >> sse
            sse >> longpoll

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
        ws >> Edge(label="协议消息") >> protocol
        http2 >> Edge(label="协议消息") >> protocol
        sse >> Edge(label="事件") >> protocol
        longpoll >> Edge(label="事件") >> protocol
        protocol >> Edge(label="发送/接收") >> msg
        sdk_api >> Edge(label="上传") >> media
        protocol >> Edge(label="订阅") >> presence
        protocol >> Edge(label="落地/索引") >> idb


if __name__ == "__main__":
    create_im_sdk_web(filename="im_sdk_web", outformat="png")
    create_im_sdk_web(filename="im_sdk_web", outformat="pdf")
