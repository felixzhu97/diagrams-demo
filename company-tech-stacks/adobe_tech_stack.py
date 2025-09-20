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
from diagrams.onprem.inmemory import Redis, Memcached
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python, JavaScript, Java, Go
from diagrams.programming.framework import React, Django
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB
from diagrams.aws.analytics import Kinesis, Glue, EMR
from diagrams.aws.management import Cloudwatch
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS


def create_adobe_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Adobe 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("全球用户")
            
            with Cluster("桌面应用"):
                photoshop = Server("Adobe Photoshop")
                illustrator = Server("Adobe Illustrator")
                premiere_pro = Server("Adobe Premiere Pro")
                after_effects = Server("Adobe After Effects")
                indesign = Server("Adobe InDesign")
                lightroom = Server("Adobe Lightroom")
                
            with Cluster("Web 应用"):
                creative_cloud_web = Server("Creative Cloud Web")
                document_cloud = Server("Document Cloud")
                experience_cloud = Server("Experience Cloud")
                analytics_workspace = Server("Analytics Workspace")
                
            with Cluster("移动应用"):
                photoshop_express = Server("Photoshop Express")
                lightroom_mobile = Server("Lightroom Mobile")
                adobe_scan = Server("Adobe Scan")
                acrobat_reader = Server("Acrobat Reader")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                angular = React("Angular")
                javascript = JavaScript("JavaScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                typescript = Server("TypeScript")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                ionic = Server("Ionic")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")
                rollup = Server("Rollup")
                
            with Cluster("UI组件库"):
                material_ui = Server("Material-UI")
                ant_design = Server("Ant Design")
                adobe_spectrum = Server("Adobe Spectrum")
                custom_components = Server("Custom Components")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                java = Java("Java")
                python = Python("Python")
                javascript_backend = JavaScript("JavaScript")
                cpp = Server("C++")
                go = Go("Go")
                
            with Cluster("Web 框架"):
                spring_boot = Server("Spring Boot")
                spring_framework = Server("Spring Framework")
                django = Django("Django")
                express = Server("Express.js")
                nodejs = Server("Node.js")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                graphql = Server("GraphQL")
                grpc = Server("gRPC")
                webhooks = Server("Webhooks")
                
            with Cluster("服务发现"):
                eureka = Server("Eureka")
                consul = Server("Consul")
                etcd = Server("etcd")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                sql_server = Server("Microsoft SQL Server")
                postgresql = PostgreSQL("PostgreSQL")
                mysql = Server("MySQL")
                oracle_db = Server("Oracle Database")
                
            with Cluster("NoSQL 数据库"):
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                dynamodb = Dynamodb("DynamoDB")
                bigtable = Bigtable("Bigtable")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                hazelcast = Server("Hazelcast")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")
                
            with Cluster("文件存储"):
                s3 = S3("Amazon S3")
                gcs = GCS("Google Cloud Storage")
                azure_blob = Server("Azure Blob Storage")

        # Creative Cloud层
        with Cluster("Creative Cloud层"):
            with Cluster("创意工具"):
                image_editing = Server("Image Editing")
                vector_graphics = Server("Vector Graphics")
                video_editing = Server("Video Editing")
                motion_graphics = Server("Motion Graphics")
                layout_design = Server("Layout Design")
                photo_management = Server("Photo Management")
                
            with Cluster("云服务"):
                creative_cloud_libraries = Server("Creative Cloud Libraries")
                creative_cloud_sync = Server("Creative Cloud Sync")
                creative_cloud_storage = Server("Creative Cloud Storage")
                creative_cloud_collaboration = Server("Creative Cloud Collaboration")
                
            with Cluster("AI和机器学习"):
                adobe_sensei = Server("Adobe Sensei")
                content_aware_fill = Server("Content-Aware Fill")
                auto_reframe = Server("Auto Reframe")
                neural_filters = Server("Neural Filters")
                
            with Cluster("字体和资源"):
                adobe_fonts = Server("Adobe Fonts")
                stock_photos = Server("Adobe Stock")
                creative_cloud_assets = Server("Creative Cloud Assets")

        # Experience Cloud层
        with Cluster("Experience Cloud层"):
            with Cluster("内容管理"):
                aem = Server("Adobe Experience Manager")
                aem_assets = Server("AEM Assets")
                aem_sites = Server("AEM Sites")
                aem_forms = Server("AEM Forms")
                
            with Cluster("营销自动化"):
                campaign = Server("Adobe Campaign")
                target = Server("Adobe Target")
                audience_manager = Server("Adobe Audience Manager")
                real_time_cdp = Server("Real-time CDP")
                
            with Cluster("分析平台"):
                analytics = Server("Adobe Analytics")
                customer_journey_analytics = Server("Customer Journey Analytics")
                attribution_ai = Server("Attribution AI")
                customer_ai = Server("Customer AI")
                
            with Cluster("商务平台"):
                commerce = Server("Adobe Commerce")
                magento = Server("Magento")
                payment_services = Server("Payment Services")
                inventory_management = Server("Inventory Management")

        # Document Cloud层
        with Cluster("Document Cloud层"):
            with Cluster("PDF处理"):
                pdf_creation = Server("PDF Creation")
                pdf_editing = Server("PDF Editing")
                pdf_forms = Server("PDF Forms")
                pdf_signatures = Server("PDF Signatures")
                
            with Cluster("文档管理"):
                document_storage = Server("Document Storage")
                document_sharing = Server("Document Sharing")
                document_collaboration = Server("Document Collaboration")
                document_security = Server("Document Security")
                
            with Cluster("扫描和识别"):
                document_scanning = Server("Document Scanning")
                ocr_technology = Server("OCR Technology")
                text_recognition = Server("Text Recognition")
                form_recognition = Server("Form Recognition")

        # 分析和报告层
        with Cluster("分析和报告层"):
            with Cluster("数据分析"):
                experience_platform = Server("Adobe Experience Platform")
                data_lake = Server("Data Lake")
                data_warehouse = Server("Data Warehouse")
                etl_processes = Server("ETL Processes")
                
            with Cluster("商业智能"):
                business_intelligence = Server("Business Intelligence")
                data_visualization = Server("Data Visualization")
                dashboard_engine = Server("Dashboard Engine")
                report_builder = Server("Report Builder")
                
            with Cluster("预测分析"):
                predictive_analytics = Server("Predictive Analytics")
                machine_learning = Server("Machine Learning")
                statistical_analysis = Server("Statistical Analysis")
                ai_insights = Server("AI Insights")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                streaming_analytics = Server("Streaming Analytics")
                event_processing = Server("Event Processing")

        # 安全和身份层
        with Cluster("安全和身份层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                saml = Server("SAML")
                ldap = Server("LDAP")
                active_directory = Server("Active Directory")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                permission_management = Server("Permission Management")
                access_control = Server("Access Control")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                key_management = Server("Key Management")
                data_masking = Server("Data Masking")
                privacy_controls = Server("Privacy Controls")
                
            with Cluster("审计和合规"):
                audit_logging = Server("Audit Logging")
                compliance_monitoring = Server("Compliance Monitoring")
                regulatory_reporting = Server("Regulatory Reporting")
                gdpr_compliance = Server("GDPR Compliance")

        # 基础设施层
        with Cluster("基础设施层"):
            with Cluster("容器化"):
                docker = Server("Docker")
                kubernetes = Server("Kubernetes")
                helm = Server("Helm")
                
            with Cluster("服务网格"):
                istio = Server("Istio")
                linkerd = Server("Linkerd")
                
            with Cluster("负载均衡"):
                nginx = Server("Nginx")
                haproxy = Server("HAProxy")
                envoy = Server("Envoy")
                
            with Cluster("配置管理"):
                etcd_config = Server("etcd")
                consul_config = Server("Consul")
                vault = Vault("Vault")

        # 云服务层
        with Cluster("云服务层"):
            with Cluster("AWS服务"):
                ec2 = EC2("EC2")
                lambda_aws = Lambda("Lambda")
                rds = RDS("RDS")
                s3_aws = S3("S3")
                cloudfront = CloudFront("CloudFront")
                
            with Cluster("Azure服务"):
                azure_vm = Server("Azure VMs")
                azure_functions = Server("Azure Functions")
                azure_sql = Server("Azure SQL")
                azure_storage = Server("Azure Storage")
                
            with Cluster("GCP服务"):
                compute_engine = ComputeEngine("Compute Engine")
                cloud_functions = Server("Cloud Functions")
                cloud_sql = Server("Cloud SQL")
                gcs_gcp = GCS("Cloud Storage")
                
            with Cluster("CDN和WAF"):
                fastly = Server("Fastly CDN")
                cloudflare = Server("Cloudflare")
                waf = Server("Web Application Firewall")

        # 监控和日志层
        with Cluster("监控和日志层"):
            with Cluster("监控系统"):
                prometheus = Prometheus("Prometheus")
                grafana = Grafana("Grafana")
                datadog = Server("Datadog")
                new_relic = Server("New Relic")
                
            with Cluster("日志系统"):
                elasticsearch_logs = Server("Elasticsearch Logs")
                logstash = Server("Logstash")
                kibana = Server("Kibana")
                fluentd = Server("Fluentd")
                
            with Cluster("追踪系统"):
                zipkin = Server("Zipkin")
                jaeger = Server("Jaeger")
                dapper = Server("Dapper")

        # 开发工具层
        with Cluster("开发工具层"):
            with Cluster("版本控制"):
                git = Server("Git")
                github = Server("GitHub")
                gitlab = Server("GitLab")
                
            with Cluster("CI/CD"):
                jenkins = Server("Jenkins")
                gitlab_ci = Server("GitLab CI")
                github_actions = Server("GitHub Actions")
                azure_devops = Server("Azure DevOps")
                
            with Cluster("测试工具"):
                junit = Server("JUnit")
                pytest = Server("pytest")
                selenium = Server("Selenium")
                cypress = Server("Cypress")
                
            with Cluster("代码质量"):
                sonarqube = Server("SonarQube")
                checkstyle = Server("CheckStyle")
                findbugs = Server("FindBugs")
                eslint = Server("ESLint")

        # 连接关系
        # 客户端到前端技术
        users >> photoshop
        users >> illustrator
        users >> creative_cloud_web
        users >> document_cloud
        users >> photoshop_express
        users >> lightroom_mobile
        
        photoshop >> react
        illustrator >> angular
        creative_cloud_web >> javascript
        document_cloud >> html5
        photoshop_express >> react_native
        lightroom_mobile >> swift_ios

        # 前端技术到后端技术
        react >> spring_boot
        angular >> spring_framework
        javascript >> django
        html5 >> express
        react_native >> nodejs
        swift_ios >> rest_apis

        # 后端技术到数据存储
        java >> spring_boot
        python >> django
        javascript_backend >> express
        spring_boot >> sql_server
        django >> postgresql
        rest_apis >> redis
        graphql >> elasticsearch

        # 数据存储连接
        sql_server >> postgresql
        postgresql >> mysql
        mysql >> oracle_db
        mongodb >> cassandra
        cassandra >> dynamodb
        dynamodb >> bigtable
        redis >> memcached
        memcached >> hazelcast
        elasticsearch >> solr
        s3 >> gcs
        gcs >> azure_blob

        # Creative Cloud连接
        image_editing >> vector_graphics
        vector_graphics >> video_editing
        video_editing >> motion_graphics
        motion_graphics >> layout_design
        layout_design >> photo_management
        creative_cloud_libraries >> creative_cloud_sync
        creative_cloud_sync >> creative_cloud_storage
        creative_cloud_storage >> creative_cloud_collaboration
        adobe_sensei >> content_aware_fill
        content_aware_fill >> auto_reframe
        auto_reframe >> neural_filters
        adobe_fonts >> stock_photos
        stock_photos >> creative_cloud_assets

        # Experience Cloud连接
        aem >> aem_assets
        aem_assets >> aem_sites
        aem_sites >> aem_forms
        campaign >> target
        target >> audience_manager
        audience_manager >> real_time_cdp
        analytics >> customer_journey_analytics
        customer_journey_analytics >> attribution_ai
        attribution_ai >> customer_ai
        commerce >> magento
        magento >> payment_services
        payment_services >> inventory_management

        # Document Cloud连接
        pdf_creation >> pdf_editing
        pdf_editing >> pdf_forms
        pdf_forms >> pdf_signatures
        document_storage >> document_sharing
        document_sharing >> document_collaboration
        document_collaboration >> document_security
        document_scanning >> ocr_technology
        ocr_technology >> text_recognition
        text_recognition >> form_recognition

        # 分析和报告连接
        experience_platform >> data_lake
        data_lake >> data_warehouse
        data_warehouse >> etl_processes
        business_intelligence >> data_visualization
        data_visualization >> dashboard_engine
        dashboard_engine >> report_builder
        predictive_analytics >> machine_learning
        machine_learning >> statistical_analysis
        statistical_analysis >> ai_insights
        real_time_analytics >> streaming_analytics
        streaming_analytics >> event_processing

        # 安全和身份连接
        oauth >> openid_connect
        openid_connect >> saml
        saml >> ldap
        ldap >> active_directory
        rbac >> abac
        abac >> permission_management
        permission_management >> access_control
        encryption >> key_management
        key_management >> data_masking
        data_masking >> privacy_controls
        audit_logging >> compliance_monitoring
        compliance_monitoring >> regulatory_reporting
        regulatory_reporting >> gdpr_compliance

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd_config >> consul_config
        consul_config >> vault

        # 云服务连接
        ec2 >> lambda_aws
        lambda_aws >> rds
        rds >> s3_aws
        s3_aws >> cloudfront
        azure_vm >> azure_functions
        azure_functions >> azure_sql
        azure_sql >> azure_storage
        compute_engine >> cloud_functions
        cloud_functions >> cloud_sql
        cloud_sql >> gcs_gcp
        fastly >> cloudflare
        cloudflare >> waf

        # 监控连接
        prometheus >> grafana
        grafana >> datadog
        datadog >> new_relic
        elasticsearch_logs >> logstash
        logstash >> kibana
        kibana >> fluentd
        zipkin >> jaeger
        jaeger >> dapper

        # 开发工具连接
        git >> github
        github >> gitlab
        jenkins >> gitlab_ci
        gitlab_ci >> github_actions
        github_actions >> azure_devops
        junit >> pytest
        pytest >> selenium
        selenium >> cypress
        sonarqube >> checkstyle
        checkstyle >> findbugs
        findbugs >> eslint

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> docker
        adobe_sensei >> Edge(label="AI引擎") >> machine_learning
        experience_platform >> Edge(label="数据平台") >> data_lake
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana
        fastly >> Edge(label="CDN") >> cloudfront
        creative_cloud_libraries >> Edge(label="云同步") >> creative_cloud_sync


if __name__ == "__main__":
    create_adobe_tech_stack_diagram(filename="adobe_tech_stack", outformat="png")
    create_adobe_tech_stack_diagram(filename="adobe_tech_stack", outformat="pdf")
