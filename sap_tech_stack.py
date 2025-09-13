from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Users, User
from diagrams.onprem.network import Internet
from diagrams.onprem.database import PostgreSQL, MongoDB, Cassandra, Oracle
from diagrams.onprem.storage import Ceph
from diagrams.onprem.queue import Kafka
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.security import Vault
from diagrams.onprem.analytics import Spark, Hadoop, Superset
from diagrams.onprem.workflow import Airflow
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python, Java, JavaScript, Cpp
from diagrams.programming.framework import React, Django, Spring
from diagrams.aws.compute import EC2, Lambda, ECS, EKS
from diagrams.aws.database import RDS, Dynamodb, Aurora
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, ELB, VPC
from diagrams.aws.analytics import Kinesis, Glue, EMR, Redshift
from diagrams.aws.management import Cloudwatch, Organizations
from diagrams.aws.security import IAM, WAF, Shield
from diagrams.aws.devtools import Codebuild, Codedeploy
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.storage import EBS, EFS
from diagrams.gcp.compute import ComputeEngine, GKE, Run, Functions
from diagrams.gcp.database import Bigtable, Firestore, Spanner, SQL
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Dataproc
from diagrams.saas.cdn import Cloudflare
from diagrams.saas.identity import Auth0
from diagrams.saas.logging import Datadog
from diagrams.saas.chat import Slack

def create_sap_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建SAP技术栈图表
    with Diagram("SAP技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("SAP用户")
            administrators = Users("系统管理员")
            developers = Users("SAP开发者")
            business_users = Users("业务用户")
            
            with Cluster("客户端应用"):
                sap_gui = Server("SAP GUI")
                fiori_apps = Server("Fiori应用")
                web_browser = Server("Web浏览器")
                mobile_apps = Server("移动应用")
                
        # 接入层
        with Cluster("接入层"):
            with Cluster("负载均衡"):
                load_balancer = ELB("负载均衡器")
                web_dispatcher = Server("Web Dispatcher")
                gateway = Server("SAP Gateway")
                
            with Cluster("身份认证"):
                sap_idm = Server("SAP Identity Management")
                sap_auth = Server("SAP认证服务")
                ldap = Server("LDAP")
                active_directory = Server("Active Directory")
                
        # SAP应用层
        with Cluster("SAP应用层"):
            with Cluster("核心ERP系统"):
                sap_ecc = Server("SAP ECC")
                sap_s4hana = Server("SAP S/4HANA")
                sap_business_one = Server("SAP Business One")
                sap_by_design = Server("SAP Business ByDesign")
                
            with Cluster("业务应用"):
                sap_crm = Server("SAP CRM")
                sap_scm = Server("SAP SCM")
                sap_srm = Server("SAP SRM")
                sap_plm = Server("SAP PLM")
                
            with Cluster("人力资源"):
                sap_hcm = Server("SAP HCM")
                sap_successfactors = Server("SAP SuccessFactors")
                sap_fieldglass = Server("SAP Fieldglass")
                
        # SAP云平台层
        with Cluster("SAP云平台层"):
            with Cluster("BTP核心服务"):
                btp_platform = Server("SAP BTP平台")
                cloud_foundry = Server("Cloud Foundry")
                kubernetes = Server("Kubernetes")
                hyperscaler = Server("超大规模云服务")
                
            with Cluster("集成服务"):
                cloud_integration = Server("SAP Cloud Integration")
                api_management = Server("API管理")
                event_mesh = Server("Event Mesh")
                data_intelligence = Server("SAP Data Intelligence")
                
            with Cluster("开发服务"):
                business_application_studio = Server("Business Application Studio")
                web_ide = Server("Web IDE")
                mobile_services = Server("Mobile Services")
                
        # SAP数据库层
        with Cluster("SAP数据库层"):
            with Cluster("SAP数据库"):
                hana_database = Server("SAP HANA数据库")
                maxdb = Server("SAP MaxDB")
                ase = Server("SAP ASE")
                
            with Cluster("数据仓库"):
                bw4hana = Server("SAP BW/4HANA")
                data_hub = Server("SAP Data Hub")
                data_warehouse_cloud = Server("SAP Data Warehouse Cloud")
                
            with Cluster("大数据"):
                vora = Server("SAP Vora")
                hana_spatial = Server("HANA Spatial")
                graph_engine = Server("Graph Engine")
                
        # SAP中间件层
        with Cluster("SAP中间件层"):
            with Cluster("集成平台"):
                process_orchestration = Server("SAP Process Orchestration")
                cloud_integration_platform = Server("Cloud Integration Platform")
                enterprise_service_bus = Server("企业服务总线")
                
            with Cluster("消息处理"):
                sap_xi = Server("SAP XI/PI")
                cloud_connector = Server("SAP Cloud Connector")
                message_server = Server("Message Server")
                
            with Cluster("工作流"):
                workflow_engine = Server("工作流引擎")
                business_process_management = Server("业务流程管理")
                rules_engine = Server("规则引擎")
                
        # SAP分析层
        with Cluster("SAP分析层"):
            with Cluster("商务智能"):
                business_objects = Server("SAP BusinessObjects")
                crystal_reports = Server("Crystal Reports")
                web_intelligence = Server("Web Intelligence")
                dashboards = Server("Dashboards")
                
            with Cluster("预测分析"):
                predictive_analytics = Server("SAP Predictive Analytics")
                machine_learning = Server("机器学习")
                artificial_intelligence = Server("人工智能")
                
            with Cluster("数据可视化"):
                analytics_cloud = Server("SAP Analytics Cloud")
                lumira = Server("SAP Lumira")
                design_studio = Server("Design Studio")
                
        # SAP开发平台层
        with Cluster("SAP开发平台层"):
            with Cluster("开发语言"):
                abap = Server("ABAP")
                java = Java("Java")
                python = Python("Python")
                javascript = JavaScript("JavaScript")
                
            with Cluster("开发工具"):
                abap_development_tools = Server("ABAP Development Tools")
                eclipse_ide = Server("Eclipse IDE")
                visual_studio_code = Server("Visual Studio Code")
                sap_hana_studio = Server("SAP HANA Studio")
                
            with Cluster("版本控制"):
                git_integration = Server("Git集成")
                abap_git = Server("ABAP Git")
                transport_management = Server("传输管理")
                
        # SAP安全层
        with Cluster("SAP安全层"):
            with Cluster("访问控制"):
                sap_authorization = Server("SAP授权管理")
                role_management = Server("角色管理")
                user_management = Server("用户管理")
                profile_generator = Server("Profile Generator")
                
            with Cluster("数据安全"):
                data_encryption = Server("数据加密")
                secure_network_communication = Server("SNC")
                ssl_tls = Server("SSL/TLS")
                digital_certificates = Server("数字证书")
                
            with Cluster("审计和合规"):
                security_audit_log = Server("安全审计日志")
                compliance_monitoring = Server("合规监控")
                vulnerability_management = Server("漏洞管理")
                
        # SAP监控层
        with Cluster("SAP监控层"):
            with Cluster("系统监控"):
                solution_manager = Server("SAP Solution Manager")
                focus_run = Server("SAP Focused Run")
                cloud_alm = Server("SAP Cloud ALM")
                
            with Cluster("性能监控"):
                performance_monitoring = Server("性能监控")
                workload_analysis = Server("工作负载分析")
                database_monitoring = Server("数据库监控")
                
            with Cluster("日志管理"):
                system_log = Server("系统日志")
                security_log = Server("安全日志")
                application_log = Server("应用日志")
                
        # SAP部署层
        with Cluster("SAP部署层"):
            with Cluster("安装和配置"):
                sap_installer = Server("SAP安装器")
                system_configuration = Server("系统配置")
                landscape_setup = Server("Landscape设置")
                
            with Cluster("升级和迁移"):
                system_upgrade = Server("系统升级")
                data_migration = Server("数据迁移")
                code_migration = Server("代码迁移")
                
            with Cluster("备份和恢复"):
                backup_system = Server("备份系统")
                recovery_manager = Server("恢复管理器")
                disaster_recovery = Server("灾难恢复")
                
        # SAP移动层
        with Cluster("SAP移动层"):
            with Cluster("移动平台"):
                sap_mobile_platform = Server("SAP Mobile Platform")
                mobile_development_kit = Server("Mobile Development Kit")
                offline_capability = Server("离线功能")
                
            with Cluster("移动应用"):
                fiori_mobile = Server("Fiori Mobile")
                sap_ariba = Server("SAP Ariba")
                concur = Server("Concur")
                
        # SAP集成层
        with Cluster("SAP集成层"):
            with Cluster("第三方集成"):
                rest_api = Server("REST API")
                soap_web_services = Server("SOAP Web Services")
                odata_services = Server("OData服务")
                
            with Cluster("数据集成"):
                sap_data_services = Server("SAP Data Services")
                information_steward = Server("Information Steward")
                data_quality_services = Server("数据质量服务")
                
            with Cluster("主数据管理"):
                master_data_governance = Server("Master Data Governance")
                master_data_hub = Server("Master Data Hub")
                data_unification = Server("数据统一")
                
        # 连接关系
        users >> sap_gui
        administrators >> fiori_apps
        developers >> web_browser
        business_users >> mobile_apps
        
        sap_gui >> load_balancer
        fiori_apps >> web_dispatcher
        web_browser >> gateway
        mobile_apps >> gateway
        
        load_balancer >> web_dispatcher
        web_dispatcher >> gateway
        
        gateway >> sap_idm
        sap_idm >> sap_auth
        sap_auth >> ldap
        ldap >> active_directory
        
        sap_idm >> sap_ecc
        sap_idm >> sap_s4hana
        sap_idm >> sap_business_one
        sap_idm >> sap_by_design
        
        sap_ecc >> sap_crm
        sap_s4hana >> sap_scm
        sap_business_one >> sap_srm
        sap_by_design >> sap_plm
        
        sap_crm >> sap_hcm
        sap_scm >> sap_successfactors
        sap_srm >> sap_fieldglass
        
        btp_platform >> cloud_foundry
        cloud_foundry >> kubernetes
        kubernetes >> hyperscaler
        
        cloud_integration >> api_management
        api_management >> event_mesh
        event_mesh >> data_intelligence
        
        business_application_studio >> web_ide
        web_ide >> mobile_services
        
        hana_database >> maxdb
        maxdb >> ase
        
        bw4hana >> data_hub
        data_hub >> data_warehouse_cloud
        
        vora >> hana_spatial
        hana_spatial >> graph_engine
        
        process_orchestration >> cloud_integration_platform
        cloud_integration_platform >> enterprise_service_bus
        
        sap_xi >> cloud_connector
        cloud_connector >> message_server
        
        workflow_engine >> business_process_management
        business_process_management >> rules_engine
        
        business_objects >> crystal_reports
        crystal_reports >> web_intelligence
        web_intelligence >> dashboards
        
        predictive_analytics >> machine_learning
        machine_learning >> artificial_intelligence
        
        analytics_cloud >> lumira
        lumira >> design_studio
        
        abap >> java
        java >> python
        python >> javascript
        
        abap_development_tools >> eclipse_ide
        eclipse_ide >> visual_studio_code
        visual_studio_code >> sap_hana_studio
        
        git_integration >> abap_git
        abap_git >> transport_management
        
        sap_authorization >> role_management
        role_management >> user_management
        user_management >> profile_generator
        
        data_encryption >> secure_network_communication
        secure_network_communication >> ssl_tls
        ssl_tls >> digital_certificates
        
        security_audit_log >> compliance_monitoring
        compliance_monitoring >> vulnerability_management
        
        solution_manager >> focus_run
        focus_run >> cloud_alm
        
        performance_monitoring >> workload_analysis
        workload_analysis >> database_monitoring
        
        system_log >> security_log
        security_log >> application_log
        
        sap_installer >> system_configuration
        system_configuration >> landscape_setup
        
        system_upgrade >> data_migration
        data_migration >> code_migration
        
        backup_system >> recovery_manager
        recovery_manager >> disaster_recovery
        
        sap_mobile_platform >> mobile_development_kit
        mobile_development_kit >> offline_capability
        
        fiori_mobile >> sap_ariba
        sap_ariba >> concur
        
        rest_api >> soap_web_services
        soap_web_services >> odata_services
        
        sap_data_services >> information_steward
        information_steward >> data_quality_services
        
        master_data_governance >> master_data_hub
        master_data_hub >> data_unification

if __name__ == "__main__":
    create_sap_tech_stack_diagram(filename="sap_tech_stack", outformat="png")
    create_sap_tech_stack_diagram(filename="sap_tech_stack", outformat="pdf")
