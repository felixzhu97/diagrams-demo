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


def create_workday_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("Workday 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("企业用户")
            
            with Cluster("Web 应用"):
                workday_web = Server("Workday Web")
                hcm_portal = Server("HCM Portal")
                financial_portal = Server("Financial Portal")
                analytics_portal = Server("Analytics Portal")
                
            with Cluster("移动应用"):
                workday_mobile = Server("Workday Mobile")
                workday_ios = Server("Workday iOS")
                workday_android = Server("Workday Android")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")
                
            with Cluster("扩展应用"):
                workday_extend = Server("Workday Extend")
                custom_apps = Server("Custom Apps")
                third_party_integrations = Server("Third-party Integrations")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                react = React("React")
                angular = React("Angular")
                typescript = JavaScript("TypeScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                
            with Cluster("移动技术"):
                react_native = React("React Native")
                swift_ios = Server("Swift (iOS)")
                kotlin_android = Server("Kotlin (Android)")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                vite = Server("Vite")
                
            with Cluster("UI组件库"):
                material_ui = Server("Material-UI")
                ant_design = Server("Ant Design")
                custom_components = Server("Custom Components")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                java = Java("Java")
                python = Python("Python")
                javascript = JavaScript("JavaScript")
                groovy = Server("Groovy")
                
            with Cluster("Web 框架"):
                spring_boot = Server("Spring Boot")
                spring_framework = Server("Spring Framework")
                django = Django("Django")
                express = Server("Express.js")
                
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
                oracle_db = Server("Oracle Database")
                postgresql = PostgreSQL("PostgreSQL")
                mysql = Server("MySQL")
                
            with Cluster("内存数据库"):
                oms = Server("Object Management Service (OMS)")
                in_memory_cache = Server("In-Memory Cache")
                distributed_cache = Server("Distributed Cache")
                
            with Cluster("NoSQL 数据库"):
                mongodb = MongoDB("MongoDB")
                cassandra = Cassandra("Cassandra")
                dynamodb = Dynamodb("DynamoDB")
                
            with Cluster("缓存系统"):
                redis = Redis("Redis")
                memcached = Memcached("Memcached")
                hazelcast = Server("Hazelcast")
                
            with Cluster("搜索引擎"):
                elasticsearch = Server("Elasticsearch")
                solr = Server("Apache Solr")

        # HCM和财务管理层
        with Cluster("HCM和财务管理层"):
            with Cluster("人力资源"):
                employee_management = Server("Employee Management")
                payroll_system = Server("Payroll System")
                benefits_administration = Server("Benefits Administration")
                performance_management = Server("Performance Management")
                
            with Cluster("财务管理"):
                general_ledger = Server("General Ledger")
                accounts_payable = Server("Accounts Payable")
                accounts_receivable = Server("Accounts Receivable")
                financial_reporting = Server("Financial Reporting")
                
            with Cluster("人才管理"):
                recruitment = Server("Recruitment")
                onboarding = Server("Onboarding")
                learning_management = Server("Learning Management")
                succession_planning = Server("Succession Planning")
                
            with Cluster("时间管理"):
                time_tracking = Server("Time Tracking")
                attendance_management = Server("Attendance Management")
                leave_management = Server("Leave Management")
                scheduling = Server("Scheduling")

        # 分析和报告层
        with Cluster("分析和报告层"):
            with Cluster("数据分析"):
                prism_analytics = Server("Prism Analytics")
                hadoop = Hadoop("Apache Hadoop")
                spark = Spark("Apache Spark")
                hdfs = Server("HDFS")
                
            with Cluster("商业智能"):
                business_intelligence = Server("Business Intelligence")
                data_visualization = Server("Data Visualization")
                dashboard_engine = Server("Dashboard Engine")
                report_builder = Server("Report Builder")
                
            with Cluster("预测分析"):
                predictive_analytics = Server("Predictive Analytics")
                machine_learning = Server("Machine Learning")
                statistical_analysis = Server("Statistical Analysis")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                streaming_analytics = Server("Streaming Analytics")
                event_processing = Server("Event Processing")

        # 安全和多租户层
        with Cluster("安全和多租户层"):
            with Cluster("身份认证"):
                oauth = Server("OAuth 2.0")
                openid_connect = Server("OpenID Connect")
                saml = Server("SAML")
                ldap = Server("LDAP")
                
            with Cluster("授权管理"):
                rbac = Server("Role-Based Access Control")
                abac = Server("Attribute-Based Access Control")
                permission_management = Server("Permission Management")
                
            with Cluster("多租户管理"):
                tenant_isolation = Server("Tenant Isolation")
                data_encoding = Server("Data Encoding")
                user_id_management = Server("User ID Management")
                tenant_configuration = Server("Tenant Configuration")
                
            with Cluster("数据安全"):
                encryption = Server("Data Encryption")
                key_management = Server("Key Management")
                data_masking = Server("Data Masking")
                privacy_controls = Server("Privacy Controls")
                
            with Cluster("审计和合规"):
                audit_logging = Server("Audit Logging")
                compliance_monitoring = Server("Compliance Monitoring")
                regulatory_reporting = Server("Regulatory Reporting")
                sox_compliance = Server("SOX Compliance")

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
            with Cluster("计算服务"):
                virtual_machines = Server("Virtual Machines")
                container_instances = Server("Container Instances")
                serverless = Server("Serverless")
                
            with Cluster("存储服务"):
                block_storage = Server("Block Storage")
                object_storage = Server("Object Storage")
                file_storage = Server("File Storage")
                
            with Cluster("网络服务"):
                load_balancer = Server("Load Balancer")
                cdn = Server("CDN")
                vpc = Server("VPC")
                
            with Cluster("数据库服务"):
                managed_database = Server("Managed Database")
                database_backup = Server("Database Backup")
                read_replicas = Server("Read Replicas")

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
                bamboo = Server("Bamboo")
                
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
        users >> workday_web
        users >> hcm_portal
        users >> financial_portal
        users >> workday_mobile
        users >> workday_extend
        
        workday_web >> react
        hcm_portal >> angular
        financial_portal >> typescript
        workday_mobile >> react_native
        workday_extend >> custom_apps

        # 前端技术到后端技术
        react >> spring_boot
        angular >> spring_framework
        typescript >> django
        react_native >> express
        custom_apps >> rest_apis

        # 后端技术到数据存储
        java >> spring_boot
        python >> django
        javascript >> express
        spring_boot >> oracle_db
        django >> oms
        rest_apis >> redis
        graphql >> elasticsearch

        # 数据存储连接
        oracle_db >> postgresql
        postgresql >> mysql
        oms >> in_memory_cache
        in_memory_cache >> distributed_cache
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> hazelcast
        elasticsearch >> solr

        # HCM和财务管理连接
        employee_management >> payroll_system
        payroll_system >> benefits_administration
        benefits_administration >> performance_management
        general_ledger >> accounts_payable
        accounts_payable >> accounts_receivable
        accounts_receivable >> financial_reporting
        recruitment >> onboarding
        onboarding >> learning_management
        learning_management >> succession_planning
        time_tracking >> attendance_management
        attendance_management >> leave_management
        leave_management >> scheduling

        # 分析和报告连接
        prism_analytics >> hadoop
        hadoop >> spark
        spark >> hdfs
        business_intelligence >> data_visualization
        data_visualization >> dashboard_engine
        dashboard_engine >> report_builder
        predictive_analytics >> machine_learning
        machine_learning >> statistical_analysis
        real_time_analytics >> streaming_analytics
        streaming_analytics >> event_processing

        # 安全和多租户连接
        oauth >> openid_connect
        openid_connect >> saml
        saml >> ldap
        rbac >> abac
        abac >> permission_management
        tenant_isolation >> data_encoding
        data_encoding >> user_id_management
        user_id_management >> tenant_configuration
        encryption >> key_management
        key_management >> data_masking
        data_masking >> privacy_controls
        audit_logging >> compliance_monitoring
        compliance_monitoring >> regulatory_reporting
        regulatory_reporting >> sox_compliance

        # 基础设施连接
        docker >> kubernetes
        kubernetes >> helm
        istio >> linkerd
        nginx >> haproxy
        haproxy >> envoy
        etcd_config >> consul_config
        consul_config >> vault

        # 云服务连接
        virtual_machines >> container_instances
        container_instances >> serverless
        block_storage >> object_storage
        object_storage >> file_storage
        load_balancer >> cdn
        cdn >> vpc
        managed_database >> database_backup
        database_backup >> read_replicas

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
        github_actions >> bamboo
        junit >> pytest
        pytest >> selenium
        selenium >> cypress
        sonarqube >> checkstyle
        checkstyle >> findbugs
        findbugs >> eslint

        # 跨层连接
        kubernetes >> Edge(label="容器编排") >> docker
        oms >> Edge(label="内存数据库") >> in_memory_cache
        prism_analytics >> Edge(label="数据分析") >> spark
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana
        tenant_isolation >> Edge(label="多租户") >> data_encoding
        workday_extend >> Edge(label="低代码平台") >> custom_apps


if __name__ == "__main__":
    create_workday_tech_stack_diagram(filename="workday_tech_stack", outformat="png")
    create_workday_tech_stack_diagram(filename="workday_tech_stack", outformat="pdf")
