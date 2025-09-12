from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_sdk_diagram(filename: str, outformat: str) -> None:
    with Diagram("IM 系统 SDK 设计图（细化）", filename=filename, show=False, outformat=outformat, direction="LR"):
        # 应用集成层
        with Cluster("应用集成（App / 客户端业务）"):
            app_ui = Server("App UI")
            sdk_api = Server("SDK Public API")
            event_bus = Server("Event Bus / Callbacks")
            app_ui >> Edge(label="调用/订阅") >> sdk_api
            sdk_api >> Edge(label="事件发布") >> event_bus

        # SDK 核心能力
        with Cluster("SDK 核心（连接/协议/可靠性）"):
            with Cluster("连接管理（WS/HTTP2/长连）"):
                conn_mgr = Server("Connection Manager")
                transport = Server("Transport (WebSocket/HTTP2)")
                heartbeat = Server("Heartbeat / KeepAlive")
                reconnect = Server("Reconnect / Backoff")
                conn_mgr >> transport
                transport >> heartbeat
                conn_mgr >> reconnect

            with Cluster("协议与编解码"):
                protocol = Server("协议栈 / 序列化")
                encrypt = Server("加密/签名")
                compress = Server("压缩/解压")
                protocol >> encrypt
                protocol >> compress

            with Cluster("可靠性与流控"):
                ack = Server("ACK/重传")
                qos = Server("QoS / 重试策略")
                rate = Server("限流 / 节流")
                ack >> qos
                qos >> rate

        # 会话与同步
        with Cluster("会话与同步（多端/离线/漫游）"):
            session_mgr = Server("会话管理")
            sync_mgr = Server("同步管理（增量/快照）")
            offline_mgr = Server("离线消息/漫游")
            multi_device = Server("多端策略（主从/优先级）")
            session_mgr >> sync_mgr
            sync_mgr >> offline_mgr
            session_mgr >> multi_device

        # 本地能力
        with Cluster("本地能力（缓存/存储/系统集成）"):
            local_store = Server("本地存储（SQLite/Realm）")
            msg_queue = Server("消息队列（发送/接收）")
            media_cache = Server("媒体缓存")
            push_bridge = Server("Push 桥接 (APNs/FCM)")
            network_obs = Server("网络监测")
            logger = Server("日志/埋点")
            metrics = Server("指标/Tracing")
            sdk_api >> local_store
            sdk_api >> msg_queue
            sdk_api >> media_cache
            sdk_api >> push_bridge
            sdk_api >> network_obs
            sdk_api >> logger
            sdk_api >> metrics

        # 端到端加密（E2EE）
        with Cluster("端到端加密（E2EE）"):
            device_keys = Server("设备密钥（长期/身份）")
            key_agree = Server("密钥协商（X3DH/Double Ratchet）")
            session_keys = Server("会话密钥（对称）")
            key_rotation = Server("密钥轮换/更新")
            device_keys >> key_agree >> session_keys >> key_rotation

        # 平台桥接
        with Cluster("平台桥接（iOS/Android/Web）"):
            ios_bridge = Server("iOS Bridge")
            android_bridge = Server("Android Bridge")
            js_bridge = Server("JS/TS Bridge")
            ios_bridge >> sdk_api
            android_bridge >> sdk_api
            js_bridge >> sdk_api

        # 服务端交互（抽象，辅助理解 SDK 外部依赖）
        with Cluster("服务端（抽象视图）"):
            auth_svc = Server("Auth / Token")
            route_svc = Server("路由/目录服务")
            msg_svc = Server("消息服务")
            presence_svc = Server("在线状态/订阅")
            media_svc = Server("媒体上传")
            group_svc = Server("群组/关系")
            sync_svc = Server("同步/漫游服务")
            e2ee_svc = Server("密钥目录/公钥服务")

        # 关键链路：对外接口
        sdk_api >> Edge(label="鉴权/刷新Token") >> auth_svc
        sdk_api >> Edge(label="路由/接入点") >> route_svc
        conn_mgr >> Edge(label="建立长连") >> transport
        transport >> Edge(label="协议消息") >> protocol

        # 消息链路
        protocol >> Edge(label="发送消息") >> msg_svc
        protocol >> Edge(label="订阅/Presence") >> presence_svc
        sdk_api >> Edge(label="媒体上传") >> media_svc
        sdk_api >> Edge(label="群组操作") >> group_svc

        # 可靠性与本地协同
        msg_queue >> Edge(label="待发送/重试") >> protocol
        ack >> Edge(label="确认/去重") >> msg_queue
        qos >> Edge(label="退避/重试") >> reconnect
        rate >> Edge(label="限速") >> transport
        network_obs >> Edge(label="状态变更") >> reconnect
        heartbeat >> Edge(label="保活/探测") >> reconnect

        # 会话/同步链路
        protocol >> Edge(label="落库/索引") >> local_store
        protocol >> Edge(label="事件发布") >> event_bus
        session_mgr >> Edge(label="元数据/状态") >> local_store
        sync_mgr >> Edge(label="拉取增量/快照") >> sync_svc
        offline_mgr >> Edge(label="离线/漫游拉取") >> sync_svc
        multi_device >> Edge(label="设备优先/冲突处理") >> session_mgr

        # E2EE 链路
        device_keys >> Edge(label="注册/上传公钥") >> e2ee_svc
        sdk_api >> Edge(label="获取对端公钥") >> e2ee_svc
        key_agree >> Edge(label="派生会话密钥") >> session_keys
        encrypt >> Edge(label="使用会话密钥") >> session_keys
        key_rotation >> Edge(label="更新密钥") >> session_keys
        session_keys >> Edge(label="封装/解封") >> protocol

        # 数据落地与事件
        logger >> Edge(label="上报") >> metrics


if __name__ == "__main__":
    create_im_sdk_diagram(filename="im_sdk_design", outformat="png")
    create_im_sdk_diagram(filename="im_sdk_design", outformat="pdf")
