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
from diagrams.onprem.inmemory import Redis
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Swift, JavaScript, Python, Cpp
from diagrams.programming.framework import React
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_apple_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Apple 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("硬件设备"):
                iphone = Server("iPhone")
                ipad = Server("iPad")
                mac = Server("Mac")
                apple_watch = Server("Apple Watch")
                apple_tv = Server("Apple TV")
                airpods = Server("AirPods")
                homepod = Server("HomePod")

        # 操作系统层
        with Cluster("操作系统层"):
            with Cluster("移动操作系统"):
                ios = Server("iOS")
                ipados = Server("iPadOS")
                watchos = Server("watchOS")
                
            with Cluster("桌面操作系统"):
                macos = Server("macOS")
                
            with Cluster("电视操作系统"):
                tvos = Server("tvOS")
                
            with Cluster("音频操作系统"):
                audioos = Server("audioOS")

        # 开发框架层
        with Cluster("开发框架层"):
            with Cluster("UI框架"):
                swiftui = Swift("SwiftUI")
                uikit = Swift("UIKit")
                appkit = Swift("AppKit")
                
            with Cluster("核心框架"):
                foundation = Swift("Foundation")
                core_data = Swift("Core Data")
                core_animation = Swift("Core Animation")
                core_ml = Swift("Core ML")
                
            with Cluster("多媒体框架"):
                av_foundation = Swift("AVFoundation")
                core_graphics = Swift("Core Graphics")
                metal = Swift("Metal")
                
            with Cluster("网络框架"):
                url_session = Swift("URLSession")
                network_framework = Swift("Network Framework")

        # 编程语言层
        with Cluster("编程语言层"):
            with Cluster("主要语言"):
                swift_lang = Swift("Swift")
                objective_c = Cpp("Objective-C")
                
            with Cluster("脚本语言"):
                javascript = JavaScript("JavaScript")
                python_lang = Python("Python")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("IDE"):
                xcode = Server("Xcode")
                interface_builder = Server("Interface Builder")
                
            with Cluster("构建工具"):
                xcode_build = Server("Xcode Build")
                fastlane = Server("Fastlane")
                
            with Cluster("测试工具"):
                xctest = Server("XCTest")
                ui_test = Server("UI Testing")
                
            with Cluster("性能分析"):
                instruments = Server("Instruments")
                memory_graph = Server("Memory Graph")

        # 云服务层
        with Cluster("云服务层 (iCloud)"):
            with Cluster("存储服务"):
                icloud_drive = Storage("iCloud Drive")
                icloud_backup = Storage("iCloud Backup")
                icloud_photos = Storage("iCloud Photos")
                
            with Cluster("同步服务"):
                cloudkit = Server("CloudKit")
                core_data_sync = Server("Core Data Sync")
                keychain_sync = Server("Keychain Sync")
                
            with Cluster("推送服务"):
                apns = Server("Apple Push Notification")
                push_kit = Server("PushKit")
                
            with Cluster("身份服务"):
                sign_in_apple = Server("Sign in with Apple")
                apple_id = Server("Apple ID")
                
            with Cluster("支付服务"):
                apple_pay = Server("Apple Pay")
                app_store_connect = Server("App Store Connect")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("本地存储"):
                sqlite = SQL("SQLite")
                core_data_db = Server("Core Data")
                user_defaults = Storage("UserDefaults")
                
            with Cluster("云端存储"):
                cloudkit_db = Server("CloudKit Database")
                icloud_storage = S3("iCloud Storage")
                
            with Cluster("缓存存储"):
                nscache = Storage("NSCache")
                image_cache = Storage("Image Cache")

        # 网络层
        with Cluster("网络层"):
            with Cluster("网络协议"):
                http_https = Router("HTTP/HTTPS")
                websocket = Router("WebSocket")
                bluetooth = Router("Bluetooth")
                wifi = Router("Wi-Fi")
                
            with Cluster("CDN"):
                akamai = CloudFront("Akamai CDN")
                apple_cdn = Server("Apple CDN")
                
            with Cluster("负载均衡"):
                load_balancer = ELB("负载均衡器")
                edge_cache = Storage("边缘缓存")

        # 安全和隐私层
        with Cluster("安全和隐私层"):
            with Cluster("加密服务"):
                keychain = Vault("Keychain")
                filevault = Vault("FileVault")
                secure_enclave = Server("Secure Enclave")
                
            with Cluster("生物识别"):
                touch_id = Server("Touch ID")
                face_id = Server("Face ID")
                watch_unlock = Server("Watch Unlock")
                
            with Cluster("隐私保护"):
                app_transparency = Server("App Tracking Transparency")
                privacy_labels = Server("Privacy Labels")
                differential_privacy = Server("Differential Privacy")

        # 机器学习层
        with Cluster("机器学习层"):
            with Cluster("ML框架"):
                core_ml_framework = Server("Core ML")
                create_ml = Server("Create ML")
                ml_kit = Server("ML Kit")
                
            with Cluster("AI服务"):
                siri = Server("Siri")
                natural_language = Server("Natural Language")
                vision_framework = Server("Vision Framework")
                
            with Cluster("设备端AI"):
                neural_engine = Server("Neural Engine")
                gpu_acceleration = Server("GPU Acceleration")

        # 媒体处理层
        with Cluster("媒体处理层"):
            with Cluster("图像处理"):
                core_image = Server("Core Image")
                image_io = Server("Image I/O")
                photo_kit = Server("PhotoKit")
                
            with Cluster("视频处理"):
                av_foundation_media = Server("AVFoundation")
                video_toolbox = Server("Video Toolbox")
                
            with Cluster("音频处理"):
                audio_toolbox = Server("Audio Toolbox")
                core_audio = Server("Core Audio")

        # 连接关系
        # 客户端到操作系统
        users >> iphone
        users >> ipad
        users >> mac
        users >> apple_watch
        users >> apple_tv
        users >> airpods
        users >> homepod
        
        iphone >> ios
        ipad >> ipados
        mac >> macos
        apple_watch >> watchos
        apple_tv >> tvos
        airpods >> audioos

        # 操作系统到开发框架
        ios >> swiftui
        ios >> uikit
        macos >> appkit
        ios >> foundation
        macos >> core_data
        ios >> core_animation
        ios >> core_ml

        # 开发框架到编程语言
        swiftui >> swift_lang
        uikit >> swift_lang
        uikit >> objective_c
        foundation >> swift_lang
        core_data >> swift_lang

        # 编程语言到开发工具
        swift_lang >> xcode
        objective_c >> xcode
        xcode >> interface_builder
        xcode >> xcode_build
        xcode >> fastlane

        # 开发工具到测试
        xcode >> xctest
        xcode >> ui_test
        xcode >> instruments
        xcode >> memory_graph

        # 云服务连接
        ios >> cloudkit
        macos >> icloud_drive
        ios >> icloud_backup
        ios >> icloud_photos
        cloudkit >> core_data_sync
        cloudkit >> keychain_sync

        # 推送服务
        apns >> ios
        apns >> macos
        push_kit >> apple_watch
        sign_in_apple >> apple_id
        apple_pay >> app_store_connect

        # 数据存储连接
        core_data >> sqlite
        core_data >> core_data_db
        cloudkit >> cloudkit_db
        icloud_drive >> icloud_storage
        swiftui >> nscache
        uikit >> image_cache

        # 网络连接
        ios >> http_https
        macos >> wifi
        apple_watch >> bluetooth
        ios >> websocket
        http_https >> akamai
        http_https >> apple_cdn
        akamai >> edge_cache

        # 安全连接
        ios >> keychain
        macos >> filevault
        ios >> secure_enclave
        ios >> touch_id
        iphone >> face_id
        apple_watch >> watch_unlock
        ios >> app_transparency
        ios >> privacy_labels

        # 机器学习连接
        ios >> core_ml_framework
        macos >> create_ml
        ios >> siri
        ios >> natural_language
        ios >> vision_framework
        ios >> neural_engine
        mac >> gpu_acceleration

        # 媒体处理连接
        ios >> core_image
        ios >> image_io
        ios >> photo_kit
        ios >> av_foundation_media
        ios >> video_toolbox
        ios >> audio_toolbox
        ios >> core_audio

        # 云服务到基础设施
        icloud_storage >> Edge(label="AWS基础设施") >> S3("AWS S3")
        cloudkit >> Edge(label="数据同步") >> load_balancer
        apns >> Edge(label="推送服务") >> akamai


if __name__ == "__main__":
    create_apple_tech_stack_diagram(filename="apple_tech_stack", outformat="png")
    create_apple_tech_stack_diagram(filename="apple_tech_stack", outformat="pdf")
