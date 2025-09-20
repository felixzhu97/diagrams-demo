from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_iot_system_diagram(filename: str, outformat: str) -> None:
    with Diagram("物联网系统设计图（IoT Ecosystem）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("设备层（Device Layer）"):
            sensors = Server("传感器设备")
            actuators = Server("执行器设备")
            gateways = Server("边缘网关")
            embedded_systems = Server("嵌入式系统")
            smart_devices = Server("智能设备")
            sensors >> gateways
            actuators >> gateways
            embedded_systems >> gateways
            smart_devices >> gateways

        with Cluster("连接层（Connectivity Layer）"):
            wifi_conn = Server("WiFi 连接")
            bluetooth = Server("蓝牙连接")
            cellular = Server("蜂窝网络")
            lora_wan = Server("LoRaWAN")
            nb_iot = Server("NB-IoT")
            zigbee = Server("Zigbee")
            z_wave = Server("Z-Wave")
            ethernet = Server("以太网")
            wifi_conn >> gateways
            bluetooth >> gateways
            cellular >> gateways
            lora_wan >> gateways
            nb_iot >> gateways
            zigbee >> gateways
            z_wave >> gateways
            ethernet >> gateways

        with Cluster("边缘计算层（Edge Computing）"):
            edge_processor = Server("边缘处理器")
            edge_storage = Server("边缘存储")
            edge_analytics = Server("边缘分析")
            local_ai = Server("本地 AI 推理")
            protocol_translation = Server("协议转换")
            data_filtering = Server("数据过滤")
            edge_processor >> edge_storage
            edge_analytics >> local_ai
            protocol_translation >> data_filtering

        with Cluster("网络层（Network Layer）"):
            mqtt_broker = Server("MQTT 代理")
            coap_server = Server("CoAP 服务器")
            http_gateway = Server("HTTP 网关")
            websocket_server = Server("WebSocket 服务器")
            message_queue = Server("消息队列")
            load_balancer = Server("负载均衡器")
            mqtt_broker >> message_queue
            coap_server >> message_queue
            http_gateway >> load_balancer
            websocket_server >> load_balancer

        with Cluster("平台层（Platform Layer）"):
            device_mgmt = Server("设备管理")
            data_ingestion = Server("数据摄取")
            data_processing = Server("数据处理")
            data_storage = Server("数据存储")
            api_gateway = Server("API 网关")
            user_mgmt = Server("用户管理")
            device_mgmt >> data_ingestion
            data_ingestion >> data_processing
            data_processing >> data_storage
            api_gateway >> user_mgmt

        with Cluster("数据处理层（Data Processing）"):
            stream_processing = Server("流处理")
            batch_processing = Server("批处理")
            real_time_analytics = Server("实时分析")
            data_aggregation = Server("数据聚合")
            data_transformation = Server("数据转换")
            data_validation = Server("数据验证")
            stream_processing >> real_time_analytics
            batch_processing >> data_aggregation
            data_transformation >> data_validation

        with Cluster("存储层（Storage Layer）"):
            time_series_db = Server("时序数据库")
            document_db = Server("文档数据库")
            relational_db = Server("关系数据库")
            object_storage = Server("对象存储")
            cache_layer = Server("缓存层")
            data_warehouse = Server("数据仓库")
            time_series_db >> cache_layer
            document_db >> cache_layer
            relational_db >> data_warehouse
            object_storage >> data_warehouse

        with Cluster("分析层（Analytics Layer）"):
            ml_engine = Server("机器学习引擎")
            predictive_analytics = Server("预测分析")
            anomaly_detection = Server("异常检测")
            pattern_recognition = Server("模式识别")
            optimization_engine = Server("优化引擎")
            reporting_engine = Server("报告引擎")
            ml_engine >> predictive_analytics
            predictive_analytics >> anomaly_detection
            pattern_recognition >> optimization_engine
            optimization_engine >> reporting_engine

        with Cluster("应用层（Application Layer）"):
            dashboard = Server("仪表板")
            mobile_app = Server("移动应用")
            web_app = Server("Web 应用")
            api_services = Server("API 服务")
            notification_service = Server("通知服务")
            automation_engine = Server("自动化引擎")
            dashboard >> api_services
            mobile_app >> api_services
            web_app >> api_services
            notification_service >> automation_engine

        with Cluster("安全层（Security Layer）"):
            device_auth = Server("设备认证")
            data_encryption = Server("数据加密")
            access_control = Server("访问控制")
            security_monitoring = Server("安全监控")
            threat_detection = Server("威胁检测")
            compliance_mgmt = Server("合规管理")
            device_auth >> data_encryption
            data_encryption >> access_control
            access_control >> security_monitoring
            security_monitoring >> threat_detection
            threat_detection >> compliance_mgmt

        with Cluster("云服务层（Cloud Services）"):
            cloud_storage = Server("云存储")
            cloud_compute = Server("云计算")
            cloud_ai = Server("云 AI 服务")
            cloud_analytics = Server("云分析")
            cloud_security = Server("云安全")
            cloud_backup = Server("云备份")
            cloud_storage >> cloud_compute
            cloud_compute >> cloud_ai
            cloud_ai >> cloud_analytics
            cloud_analytics >> cloud_security
            cloud_security >> cloud_backup

        with Cluster("集成层（Integration Layer）"):
            enterprise_systems = Server("企业系统")
            third_party_apis = Server("第三方 API")
            legacy_systems = Server("遗留系统")
            external_services = Server("外部服务")
            data_sync = Server("数据同步")
            event_bus = Server("事件总线")
            enterprise_systems >> data_sync
            third_party_apis >> event_bus
            legacy_systems >> data_sync
            external_services >> event_bus

        # 关键数据流连接
        gateways >> Edge(label="设备数据") >> edge_processor
        edge_processor >> Edge(label="预处理数据") >> mqtt_broker
        mqtt_broker >> Edge(label="消息传递") >> device_mgmt
        device_mgmt >> Edge(label="设备数据") >> data_ingestion
        data_ingestion >> Edge(label="原始数据") >> stream_processing
        stream_processing >> Edge(label="流数据") >> time_series_db
        time_series_db >> Edge(label="历史数据") >> ml_engine
        ml_engine >> Edge(label="分析结果") >> dashboard

        # 边缘计算链路
        gateways >> Edge(label="实时数据") >> edge_analytics
        edge_analytics >> Edge(label="边缘洞察") >> local_ai
        local_ai >> Edge(label="智能决策") >> actuators
        edge_storage >> Edge(label="本地缓存") >> edge_processor

        # 网络协议链路
        sensors >> Edge(label="传感器数据") >> wifi_conn
        actuators >> Edge(label="控制指令") >> bluetooth
        embedded_systems >> Edge(label="系统数据") >> cellular
        smart_devices >> Edge(label="设备状态") >> lora_wan

        # 数据处理链路
        data_ingestion >> Edge(label="数据流") >> stream_processing
        data_ingestion >> Edge(label="批量数据") >> batch_processing
        stream_processing >> Edge(label="实时分析") >> real_time_analytics
        batch_processing >> Edge(label="历史分析") >> data_aggregation

        # 存储链路
        data_processing >> Edge(label="处理结果") >> time_series_db
        data_processing >> Edge(label="结构化数据") >> relational_db
        data_processing >> Edge(label="非结构化数据") >> document_db
        data_processing >> Edge(label="文件数据") >> object_storage

        # 分析链路
        time_series_db >> Edge(label="时序数据") >> ml_engine
        ml_engine >> Edge(label="预测模型") >> predictive_analytics
        predictive_analytics >> Edge(label="异常信号") >> anomaly_detection
        anomaly_detection >> Edge(label="优化建议") >> optimization_engine

        # 应用链路
        api_gateway >> Edge(label="API 调用") >> dashboard
        api_gateway >> Edge(label="移动请求") >> mobile_app
        api_gateway >> Edge(label="Web 请求") >> web_app
        reporting_engine >> Edge(label="报告数据") >> dashboard

        # 安全链路
        device_auth >> Edge(label="认证信息") >> access_control
        data_encryption >> Edge(label="加密数据") >> security_monitoring
        security_monitoring >> Edge(label="安全事件") >> threat_detection
        threat_detection >> Edge(label="威胁响应") >> compliance_mgmt

        # 云服务链路
        data_storage >> Edge(label="数据备份") >> cloud_storage
        ml_engine >> Edge(label="AI 计算") >> cloud_ai
        real_time_analytics >> Edge(label="分析服务") >> cloud_analytics
        security_monitoring >> Edge(label="安全服务") >> cloud_security

        # 集成链路
        api_services >> Edge(label="企业集成") >> enterprise_systems
        api_services >> Edge(label="第三方集成") >> third_party_apis
        data_sync >> Edge(label="数据同步") >> legacy_systems
        event_bus >> Edge(label="事件驱动") >> external_services

        # 反馈控制链路
        dashboard >> Edge(label="用户操作") >> automation_engine
        automation_engine >> Edge(label="控制指令") >> actuators
        optimization_engine >> Edge(label="优化策略") >> automation_engine
        notification_service >> Edge(label="告警通知") >> mobile_app


if __name__ == "__main__":
    create_iot_system_diagram(filename="iot_system_design", outformat="png")
    create_iot_system_diagram(filename="iot_system_design", outformat="pdf")
