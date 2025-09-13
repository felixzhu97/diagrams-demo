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


def create_servicenow_tech_stack_diagram(filename: str, outformat: str) -> None:
    with Diagram("ServiceNow 技术栈架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        
        # 客户端层
        with Cluster("客户端层"):
            users = Users("企业用户")
            
            with Cluster("Web 应用"):
                servicenow_web = Server("ServiceNow Web")
                itsm_portal = Server("ITSM Portal")
                hr_portal = Server("HR Portal")
                csm_portal = Server("CSM Portal")
                eam_portal = Server("EAM Portal")
                
            with Cluster("移动应用"):
                servicenow_mobile = Server("ServiceNow Mobile")
                servicenow_ios = Server("ServiceNow iOS")
                servicenow_android = Server("ServiceNow Android")
                
            with Cluster("第三方集成"):
                api_clients = Server("API Clients")
                webhook_clients = Server("Webhook Clients")
                sdk_clients = Server("SDK Clients")
                
            with Cluster("扩展应用"):
                app_engine = Server("App Engine")
                custom_apps = Server("Custom Apps")
                third_party_integrations = Server("Third-party Integrations")

        # 前端技术层
        with Cluster("前端技术层"):
            with Cluster("Web 技术"):
                angular = React("Angular")
                javascript = JavaScript("JavaScript")
                html5 = Server("HTML5")
                css3 = Server("CSS3")
                bootstrap = Server("Bootstrap")
                
            with Cluster("移动技术"):
                ionic = Server("Ionic")
                cordova = Server("Cordova")
                react_native = React("React Native")
                
            with Cluster("构建工具"):
                webpack = Server("Webpack")
                babel = Server("Babel")
                gulp = Server("Gulp")
                
            with Cluster("UI组件库"):
                servicenow_ui = Server("ServiceNow UI")
                angular_material = Server("Angular Material")
                custom_components = Server("Custom Components")

        # 后端技术层
        with Cluster("后端技术层"):
            with Cluster("编程语言"):
                java = Java("Java")
                javascript_backend = JavaScript("JavaScript")
                python = Python("Python")
                groovy = Server("Groovy")
                
            with Cluster("Web 框架"):
                spring_boot = Server("Spring Boot")
                spring_framework = Server("Spring Framework")
                nodejs = Server("Node.js")
                express = Server("Express.js")
                
            with Cluster("微服务"):
                rest_apis = Server("REST APIs")
                graphql = Server("GraphQL")
                soap_apis = Server("SOAP APIs")
                webhooks = Server("Webhooks")
                
            with Cluster("服务发现"):
                eureka = Server("Eureka")
                consul = Server("Consul")
                etcd = Server("etcd")

        # 数据存储层
        with Cluster("数据存储层"):
            with Cluster("关系数据库"):
                mysql = Server("MySQL")
                postgresql = PostgreSQL("PostgreSQL")
                oracle_db = Server("Oracle Database")
                
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
                
            with Cluster("文件存储"):
                s3 = S3("Amazon S3")
                gcs = GCS("Google Cloud Storage")
                ceph = Ceph("Ceph")

        # ITSM和工作流层
        with Cluster("ITSM和工作流层"):
            with Cluster("IT服务管理"):
                incident_management = Server("Incident Management")
                problem_management = Server("Problem Management")
                change_management = Server("Change Management")
                service_catalog = Server("Service Catalog")
                
            with Cluster("工作流引擎"):
                workflow_engine = Server("Workflow Engine")
                business_rules = Server("Business Rules")
                approvals = Server("Approvals")
                notifications = Server("Notifications")
                
            with Cluster("自动化"):
                orchestration = Server("Orchestration")
                runbooks = Server("Runbooks")
                scripts = Server("Scripts")
                integrations = Server("Integrations")
                
            with Cluster("服务目录"):
                service_portal = Server("Service Portal")
                knowledge_base = Server("Knowledge Base")
                self_service = Server("Self-Service")
                service_level_management = Server("Service Level Management")

        # 业务应用层
        with Cluster("业务应用层"):
            with Cluster("人力资源管理"):
                hr_service_delivery = Server("HR Service Delivery")
                employee_center = Server("Employee Center")
                talent_management = Server("Talent Management")
                workforce_analytics = Server("Workforce Analytics")
                
            with Cluster("客户服务管理"):
                customer_service = Server("Customer Service")
                field_service = Server("Field Service")
                case_management = Server("Case Management")
                customer_portal = Server("Customer Portal")
                
            with Cluster("企业资产管理"):
                asset_management = Server("Asset Management")
                configuration_management = Server("Configuration Management")
                discovery = Server("Discovery")
                service_mapping = Server("Service Mapping")
                
            with Cluster("安全运营"):
                security_incident_response = Server("Security Incident Response")
                vulnerability_response = Server("Vulnerability Response")
                threat_intelligence = Server("Threat Intelligence")
                compliance = Server("Compliance")

        # 分析和报告层
        with Cluster("分析和报告层"):
            with Cluster("数据分析"):
                performance_analytics = Server("Performance Analytics")
                reporting = Server("Reporting")
                dashboards = Server("Dashboards")
                data_visualization = Server("Data Visualization")
                
            with Cluster("商业智能"):
                business_intelligence = Server("Business Intelligence")
                predictive_analytics = Server("Predictive Analytics")
                machine_learning = Server("Machine Learning")
                statistical_analysis = Server("Statistical Analysis")
                
            with Cluster("实时分析"):
                real_time_analytics = Server("Real-time Analytics")
                streaming_analytics = Server("Streaming Analytics")
                event_processing = Server("Event Processing")
                
            with Cluster("数据集成"):
                etl_processes = Server("ETL Processes")
                data_warehouse = Server("Data Warehouse")
                data_lake = Server("Data Lake")

        # 安全和多实例层
        with Cluster("安全和多实例层"):
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
                
            with Cluster("多实例管理"):
                instance_isolation = Server("Instance Isolation")
                data_isolation = Server("Data Isolation")
                resource_pooling = Server("Resource Pooling")
                tenant_management = Server("Tenant Management")
                
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
        users >> servicenow_web
        users >> itsm_portal
        users >> hr_portal
        users >> csm_portal
        users >> servicenow_mobile
        users >> app_engine
        
        servicenow_web >> angular
        itsm_portal >> javascript
        hr_portal >> html5
        csm_portal >> css3
        servicenow_mobile >> ionic
        app_engine >> custom_apps

        # 前端技术到后端技术
        angular >> spring_boot
        javascript >> spring_framework
        html5 >> nodejs
        css3 >> express
        ionic >> rest_apis
        custom_apps >> graphql

        # 后端技术到数据存储
        java >> spring_boot
        javascript_backend >> nodejs
        python >> express
        spring_boot >> mysql
        nodejs >> postgresql
        rest_apis >> redis
        graphql >> elasticsearch

        # 数据存储连接
        mysql >> postgresql
        postgresql >> oracle_db
        mongodb >> cassandra
        cassandra >> dynamodb
        redis >> memcached
        memcached >> hazelcast
        elasticsearch >> solr
        s3 >> gcs
        gcs >> ceph

        # ITSM和工作流连接
        incident_management >> problem_management
        problem_management >> change_management
        change_management >> service_catalog
        workflow_engine >> business_rules
        business_rules >> approvals
        approvals >> notifications
        orchestration >> runbooks
        runbooks >> scripts
        scripts >> integrations
        service_portal >> knowledge_base
        knowledge_base >> self_service
        self_service >> service_level_management

        # 业务应用连接
        hr_service_delivery >> employee_center
        employee_center >> talent_management
        talent_management >> workforce_analytics
        customer_service >> field_service
        field_service >> case_management
        case_management >> customer_portal
        asset_management >> configuration_management
        configuration_management >> discovery
        discovery >> service_mapping
        security_incident_response >> vulnerability_response
        vulnerability_response >> threat_intelligence
        threat_intelligence >> compliance

        # 分析和报告连接
        performance_analytics >> reporting
        reporting >> dashboards
        dashboards >> data_visualization
        business_intelligence >> predictive_analytics
        predictive_analytics >> machine_learning
        machine_learning >> statistical_analysis
        real_time_analytics >> streaming_analytics
        streaming_analytics >> event_processing
        etl_processes >> data_warehouse
        data_warehouse >> data_lake

        # 安全和多实例连接
        oauth >> openid_connect
        openid_connect >> saml
        saml >> ldap
        ldap >> active_directory
        rbac >> abac
        abac >> permission_management
        permission_management >> access_control
        instance_isolation >> data_isolation
        data_isolation >> resource_pooling
        resource_pooling >> tenant_management
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
        workflow_engine >> Edge(label="工作流引擎") >> business_rules
        performance_analytics >> Edge(label="性能分析") >> reporting
        oauth >> Edge(label="身份认证") >> rbac
        jenkins >> Edge(label="CI/CD") >> kubernetes
        prometheus >> Edge(label="监控") >> grafana
        instance_isolation >> Edge(label="多实例") >> data_isolation
        app_engine >> Edge(label="应用引擎") >> custom_apps


if __name__ == "__main__":
    create_servicenow_tech_stack_diagram(filename="servicenow_tech_stack", outformat="png")
    create_servicenow_tech_stack_diagram(filename="servicenow_tech_stack", outformat="pdf")
