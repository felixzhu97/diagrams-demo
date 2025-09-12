from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Users, User
from diagrams.onprem.network import Internet
from diagrams.onprem.database import PostgreSQL, MongoDB, MSSQL
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
from diagrams.programming.language import Csharp, JavaScript, Python, Cpp
from diagrams.programming.framework import React, DotNet
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
# Azure specific icons not fully available in diagrams library
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_microsoft_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Microsoft 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("Windows 生态"):
                windows_desktop = Server("Windows Desktop")
                windows_server = Server("Windows Server")
                windows_iot = Server("Windows IoT")
                xbox = Server("Xbox")
                hololens = Server("HoloLens")
                
            with Cluster("移动设备"):
                surface_device = Server("Surface 设备")
                windows_phone = Server("Windows Phone")
                
            with Cluster("Web 客户端"):
                edge_browser = Server("Microsoft Edge")
                web_apps = Server("Web 应用")

        # 操作系统层
        with Cluster("操作系统层"):
            with Cluster("Windows 操作系统"):
                windows_os = Server("Windows OS")
                windows_server_os = Server("Windows Server OS")
                wsl = Server("WSL (Windows Subsystem for Linux)")
                
            with Cluster("移动操作系统"):
                windows_mobile = Server("Windows Mobile")
                
            with Cluster("游戏系统"):
                xbox_os = Server("Xbox OS")

        # 开发框架层
        with Cluster("开发框架层 (.NET)"):
            with Cluster(".NET 生态"):
                dotnet_framework = DotNet(".NET Framework")
                dotnet_core = DotNet(".NET Core")
                dotnet_5_plus = DotNet(".NET 5+")
                
            with Cluster("Web 框架"):
                aspnet = DotNet("ASP.NET")
                aspnet_core = DotNet("ASP.NET Core")
                blazor = DotNet("Blazor")
                
            with Cluster("桌面框架"):
                wpf = DotNet("WPF")
                winforms = DotNet("WinForms")
                uwp = DotNet("UWP")
                
            with Cluster("移动框架"):
                xamarin = DotNet("Xamarin")
                maui = DotNet(".NET MAUI")

        # 编程语言层
        with Cluster("编程语言层"):
            with Cluster("主要语言"):
                csharp = Csharp("C#")
                typescript = JavaScript("TypeScript")
                fsharp = Server("F#")
                
            with Cluster("系统语言"):
                cpp = Cpp("C++")
                rust = Server("Rust")
                
            with Cluster("脚本语言"):
                javascript = JavaScript("JavaScript")
                python = Python("Python")
                powershell = Server("PowerShell")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("IDE"):
                visual_studio = Server("Visual Studio")
                visual_studio_code = Server("Visual Studio Code")
                visual_studio_mac = Server("Visual Studio for Mac")
                
            with Cluster("构建工具"):
                msbuild = Server("MSBuild")
                dotnet_cli = Server(".NET CLI")
                
            with Cluster("测试工具"):
                nunit = Server("NUnit")
                xunit = Server("xUnit")
                mstest = Server("MSTest")
                
            with Cluster("性能分析"):
                dotnet_trace = Server(".NET Trace")
                dotnet_counters = Server(".NET Counters")
                visual_studio_profiler = Server("Visual Studio Profiler")

        # 云服务层 (Azure)
        with Cluster("云服务层 (Microsoft Azure)"):
            with Cluster("计算服务"):
                virtual_machines = Server("Virtual Machines")
                app_service = Server("App Service")
                azure_functions = Server("Azure Functions")
                container_instances = Server("Container Instances")
                aks = Server("Azure Kubernetes Service")
                
            with Cluster("数据服务"):
                sql_databases = Server("SQL Databases")
                cosmos_db = Server("Cosmos DB")
                storage_accounts = Server("Storage Accounts")
                redis_cache = Server("Azure Cache for Redis")
                
            with Cluster("网络服务"):
                cdn_profiles = Server("Azure CDN")
                load_balancers = Server("Load Balancers")
                application_gateway = Server("Application Gateway")
                
            with Cluster("AI 服务"):
                cognitive_services = Server("Cognitive Services")
                machine_learning = Server("Machine Learning")
                bot_framework = Server("Bot Framework")
                
            with Cluster("身份服务"):
                active_directory = Server("Azure Active Directory")
                key_vault = Server("Azure Key Vault")
                b2c = Server("Azure AD B2C")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                sql_server = MSSQL("SQL Server")
                azure_sql = Server("Azure SQL Database")
                postgresql = PostgreSQL("Azure Database for PostgreSQL")
                
            with Cluster("NoSQL 数据库"):
                cosmos_db_storage = Server("Cosmos DB")
                mongodb = MongoDB("Azure Database for MongoDB")
                
            with Cluster("文件存储"):
                blob_storage = Server("Blob Storage")
                file_storage = Storage("File Storage")
                disk_storage = Storage("Disk Storage")
                
            with Cluster("缓存存储"):
                redis_cache_storage = Redis("Azure Cache for Redis")
                app_service_cache = Storage("App Service Cache")

        # 大数据分析层
        with Cluster("大数据分析层"):
            with Cluster("数据工厂"):
                data_factory = Server("Azure Data Factory")
                data_bricks = Server("Azure Databricks")
                synapse = Server("Azure Synapse Analytics")
                
            with Cluster("流处理"):
                stream_analytics = Server("Stream Analytics")
                event_hubs = Server("Event Hubs")
                service_bus = Server("Service Bus")
                
            with Cluster("数据仓库"):
                sql_data_warehouse = Server("SQL Data Warehouse")
                analysis_services = Server("Analysis Services")
                
            with Cluster("BI 工具"):
                power_bi = Server("Power BI")
                power_query = Server("Power Query")
                power_pivot = Server("Power Pivot")

        # 办公和协作层
        with Cluster("办公和协作层"):
            with Cluster("Office 365"):
                office_365 = Server("Office 365")
                word = Server("Word")
                excel = Server("Excel")
                powerpoint = Server("PowerPoint")
                outlook = Server("Outlook")
                
            with Cluster("协作工具"):
                teams = Server("Microsoft Teams")
                sharepoint = Server("SharePoint")
                onedrive = Server("OneDrive")
                yammer = Server("Yammer")
                
            with Cluster("开发协作"):
                azure_devops = Server("Azure DevOps")
                github = Server("GitHub")
                visual_studio_team_services = Server("Visual Studio Team Services")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份管理"):
                azure_ad = Server("Azure AD")
                azure_ad_b2c = Server("Azure AD B2C")
                azure_ad_b2b = Server("Azure AD B2B")
                
            with Cluster("安全服务"):
                security_center = Server("Azure Security Center")
                key_vault_security = Server("Key Vault")
                defender = Server("Microsoft Defender")
                
            with Cluster("合规性"):
                compliance_manager = Server("Compliance Manager")
                privacy_dashboard = Server("Privacy Dashboard")

        # 连接关系
        # 客户端到操作系统
        users >> windows_desktop
        users >> windows_server
        users >> surface_device
        users >> edge_browser
        users >> web_apps
        
        windows_desktop >> windows_os
        windows_server >> windows_server_os
        surface_device >> windows_mobile
        edge_browser >> windows_os

        # 操作系统到开发框架
        windows_os >> dotnet_framework
        windows_os >> dotnet_core
        windows_os >> dotnet_5_plus
        windows_server_os >> aspnet
        windows_os >> aspnet_core

        # 开发框架到编程语言
        dotnet_framework >> csharp
        dotnet_core >> csharp
        aspnet >> csharp
        aspnet_core >> csharp
        blazor >> typescript
        wpf >> csharp
        xamarin >> csharp

        # 编程语言到开发工具
        csharp >> visual_studio
        typescript >> visual_studio_code
        cpp >> visual_studio
        javascript >> visual_studio_code
        python >> visual_studio_code

        # 开发工具到构建
        visual_studio >> msbuild
        visual_studio_code >> dotnet_cli
        msbuild >> nunit
        dotnet_cli >> xunit

        # 云服务连接
        app_service >> virtual_machines
        azure_functions >> Server("Azure Functions")
        container_instances >> aks
        sql_databases >> cosmos_db
        storage_accounts >> blob_storage

        # 数据存储连接
        sql_server >> azure_sql
        cosmos_db_storage >> mongodb
        blob_storage >> file_storage
        redis_cache_storage >> app_service_cache

        # 大数据分析连接
        data_factory >> data_bricks
        data_bricks >> synapse
        stream_analytics >> event_hubs
        service_bus >> sql_data_warehouse
        power_bi >> analysis_services

        # 办公协作连接
        office_365 >> word
        office_365 >> excel
        office_365 >> powerpoint
        office_365 >> outlook
        teams >> sharepoint
        sharepoint >> onedrive
        azure_devops >> github

        # 安全连接
        azure_ad >> azure_ad_b2c
        azure_ad >> azure_ad_b2b
        security_center >> key_vault_security
        defender >> compliance_manager

        # 跨层连接
        aspnet_core >> Edge(label="部署到") >> app_service
        azure_functions >> Edge(label="使用") >> cosmos_db
        teams >> Edge(label="集成") >> azure_ad
        power_bi >> Edge(label="连接") >> sql_databases
        visual_studio >> Edge(label="发布到") >> azure_devops
        cognitive_services >> Edge(label="AI服务") >> bot_framework


if __name__ == "__main__":
    create_microsoft_tech_stack_diagram(filename="microsoft_tech_stack", outformat="png")
    create_microsoft_tech_stack_diagram(filename="microsoft_tech_stack", outformat="pdf")
