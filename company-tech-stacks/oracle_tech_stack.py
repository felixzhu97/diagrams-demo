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

def create_oracle_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建Oracle技术栈图表
    with Diagram("Oracle技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("Oracle用户")
            developers = Users("开发者")
            dbas = Users("数据库管理员")
            administrators = Users("系统管理员")
            
            with Cluster("客户端应用"):
                sql_developer = Server("SQL Developer")
                apex_app = Server("Oracle APEX应用")
                oic_console = Server("Oracle Integration Cloud")
                oac_dashboard = Server("Oracle Analytics Cloud")
                
        # 接入层
        with Cluster("接入层"):
            with Cluster("负载均衡和CDN"):
                load_balancer = ELB("负载均衡器")
                cdn = CloudFront("CDN")
                api_gateway = Server("API网关")
                
            with Cluster("安全认证"):
                oid = Server("Oracle Identity Directory")
                oam = Server("Oracle Access Manager")
                oim = Server("Oracle Identity Manager")
                sso = Server("单点登录")
                
        # Oracle数据库层
        with Cluster("Oracle数据库层"):
            with Cluster("数据库引擎"):
                oracle_db = Oracle("Oracle数据库")
                rac_cluster = Server("RAC集群")
                dg_standby = Server("Data Guard备库")
                asm_storage = Server("ASM存储")
                
            with Cluster("数据库服务"):
                listener = Server("数据库监听器")
                sql_net = Server("SQL*Net")
                tns_admin = Server("TNS管理")
                
            with Cluster("数据库工具"):
                rman = Server("RMAN备份")
                expdp = Server("数据泵")
                sql_loader = Server("SQL*Loader")
                db_console = Server("数据库控制台")
                
        # Oracle中间件层
        with Cluster("Oracle中间件层"):
            with Cluster("应用服务器"):
                weblogic = Server("WebLogic Server")
                glassfish = Server("GlassFish")
                oc4j = Server("OC4J")
                
            with Cluster("SOA套件"):
                soa_suite = Server("SOA套件")
                bpel_engine = Server("BPEL引擎")
                esb = Server("企业服务总线")
                bam = Server("业务活动监控")
                
            with Cluster("开发工具"):
                jdeveloper = Server("JDeveloper")
                sql_worksheet = Server("SQL工作表")
                apex_ide = Server("APEX IDE")
                
        # Oracle云服务层
        with Cluster("Oracle云服务层"):
            with Cluster("Oracle Cloud Infrastructure"):
                oci_compute = Server("OCI计算")
                oci_storage = Server("OCI存储")
                oci_network = Server("OCI网络")
                oci_database = Server("OCI数据库")
                
            with Cluster("数据库云服务"):
                dbsaas = Server("数据库即服务")
                autonomous_db = Server("自治数据库")
                exadata_cloud = Server("Exadata云服务")
                golden_gate = Server("GoldenGate")
                
            with Cluster("应用云服务"):
                paas = Server("平台即服务")
                saas_apps = Server("SaaS应用")
                integration_cloud = Server("集成云")
                
            with Cluster("分析和AI服务"):
                analytics_cloud = Server("Oracle Analytics Cloud")
                data_visualization = Server("数据可视化")
                ml_services = Server("机器学习服务")
                ai_services = Server("AI服务")
                
        # Oracle应用层
        with Cluster("Oracle应用层"):
            with Cluster("企业应用"):
                ebs = Server("Oracle EBS")
                peoplesoft = Server("PeopleSoft")
                jd_edwards = Server("JD Edwards")
                siebel = Server("Siebel CRM")
                
            with Cluster("行业解决方案"):
                retail_suite = Server("Retail套件")
                financial_services = Server("金融服务")
                healthcare_suite = Server("医疗保健套件")
                manufacturing_suite = Server("制造套件")
                
            with Cluster("协作应用"):
                webcenter = Server("WebCenter")
                content_management = Server("内容管理")
                portal_suite = Server("门户套件")
                
        # 数据管理层
        with Cluster("数据管理层"):
            with Cluster("数据仓库"):
                owh = Server("Oracle数据仓库")
                odi = Server("Oracle数据集成器")
                owb = Server("Oracle仓库构建器")
                
            with Cluster("大数据平台"):
                big_data_appliance = Server("大数据设备")
                hadoop_distribution = Server("Hadoop发行版")
                nosql_database = Server("NoSQL数据库")
                
            with Cluster("数据质量"):
                data_quality = Server("数据质量服务")
                data_profiling = Server("数据剖析")
                master_data_mgmt = Server("主数据管理")
                
        # 集成层
        with Cluster("集成层"):
            with Cluster("集成平台"):
                oracle_soa = Server("Oracle SOA")
                osb = Server("Oracle服务总线")
                mft = Server("托管文件传输")
                
            with Cluster("API管理"):
                api_gateway_platform = Server("API网关平台")
                api_publisher = Server("API发布器")
                api_analytics = Server("API分析")
                
            with Cluster("消息队列"):
                aq = Server("Oracle高级队列")
                jms = Server("JMS")
                mq_series = Server("MQ Series")
                
        # 安全和治理层
        with Cluster("安全和治理层"):
            with Cluster("数据安全"):
                transparent_encryption = Server("透明数据加密")
                vault = Vault("Oracle Vault")
                data_redaction = Server("数据脱敏")
                audit_vault = Server("审计库")
                
            with Cluster("访问控制"):
                row_level_security = Server("行级安全")
                virtual_private_database = Server("虚拟私有数据库")
                fine_grained_access = Server("细粒度访问控制")
                
            with Cluster("合规性"):
                compliance_framework = Server("合规框架")
                audit_trail = Server("审计跟踪")
                data_governance = Server("数据治理")
                
        # 监控和运维层
        with Cluster("监控和运维层"):
            with Cluster("监控工具"):
                oem = Server("Oracle企业管理器")
                cloudwatch = Cloudwatch("CloudWatch")
                prometheus = Prometheus("Prometheus")
                grafana = Grafana("Grafana")
                
            with Cluster("性能调优"):
                awr = Server("AWR报告")
                ash = Server("ASH报告")
                sql_tuning = Server("SQL调优顾问")
                stats_advisor = Server("统计信息顾问")
                
            with Cluster("备份恢复"):
                rman_backup = Server("RMAN备份")
                flashback = Server("闪回技术")
                point_in_time = Server("时间点恢复")
                
        # 开发和部署层
        with Cluster("开发和部署层"):
            with Cluster("开发工具"):
                sqlcl = Server("SQLcl")
                sql_plus = Server("SQL*Plus")
                oracle_forms = Server("Oracle Forms")
                oracle_reports = Server("Oracle Reports")
                
            with Cluster("版本控制"):
                github_integration = Server("GitHub集成")
                svn_integration = Server("SVN集成")
                gitlab_integration = Server("GitLab集成")
                
            with Cluster("CI/CD"):
                jenkins = Server("Jenkins")
                maven = Server("Maven")
                ant = Server("Apache Ant")
                gradle = Server("Gradle")
                
        # 移动和Web层
        with Cluster("移动和Web层"):
            with Cluster("Web技术"):
                apache_http = Server("Apache HTTP")
                nginx = Server("Nginx")
                iis = Server("IIS")
                
            with Cluster("移动开发"):
                mobile_framework = Server("Oracle移动框架")
                mcs = Server("移动云服务")
                mobile_backend = Server("移动后端服务")
                
        # 连接关系
        users >> sql_developer
        developers >> apex_app
        dbas >> oic_console
        administrators >> oac_dashboard
        
        sql_developer >> load_balancer
        apex_app >> load_balancer
        oic_console >> load_balancer
        oac_dashboard >> load_balancer
        
        load_balancer >> cdn
        cdn >> api_gateway
        
        api_gateway >> oid
        oid >> oam
        oam >> oim
        oim >> sso
        
        sso >> oracle_db
        oracle_db >> rac_cluster
        oracle_db >> dg_standby
        oracle_db >> asm_storage
        
        listener >> oracle_db
        sql_net >> listener
        tns_admin >> sql_net
        
        rman >> oracle_db
        expdp >> oracle_db
        sql_loader >> oracle_db
        db_console >> oracle_db
        
        weblogic >> oracle_db
        glassfish >> oracle_db
        oc4j >> oracle_db
        
        soa_suite >> weblogic
        bpel_engine >> soa_suite
        esb >> soa_suite
        bam >> soa_suite
        
        jdeveloper >> weblogic
        sql_worksheet >> oracle_db
        apex_ide >> apex_app
        
        oci_compute >> oci_storage
        oci_storage >> oci_network
        oci_network >> oci_database
        
        dbsaas >> autonomous_db
        autonomous_db >> exadata_cloud
        exadata_cloud >> golden_gate
        
        paas >> saas_apps
        saas_apps >> integration_cloud
        
        analytics_cloud >> data_visualization
        data_visualization >> ml_services
        ml_services >> ai_services
        
        ebs >> oracle_db
        peoplesoft >> oracle_db
        jd_edwards >> oracle_db
        siebel >> oracle_db
        
        retail_suite >> ebs
        financial_services >> peoplesoft
        healthcare_suite >> jd_edwards
        manufacturing_suite >> siebel
        
        webcenter >> ebs
        content_management >> webcenter
        portal_suite >> content_management
        
        owh >> oracle_db
        odi >> owh
        owb >> odi
        
        big_data_appliance >> hadoop_distribution
        hadoop_distribution >> nosql_database
        
        data_quality >> master_data_mgmt
        data_profiling >> data_quality
        
        oracle_soa >> osb
        osb >> mft
        
        api_gateway_platform >> api_publisher
        api_publisher >> api_analytics
        
        aq >> jms
        jms >> mq_series
        
        transparent_encryption >> vault
        vault >> data_redaction
        data_redaction >> audit_vault
        
        row_level_security >> virtual_private_database
        virtual_private_database >> fine_grained_access
        
        compliance_framework >> audit_trail
        audit_trail >> data_governance
        
        oem >> cloudwatch
        cloudwatch >> prometheus
        prometheus >> grafana
        
        awr >> ash
        ash >> sql_tuning
        sql_tuning >> stats_advisor
        
        rman_backup >> flashback
        flashback >> point_in_time
        
        sqlcl >> sql_plus
        oracle_forms >> oracle_reports
        
        github_integration >> jenkins
        svn_integration >> jenkins
        gitlab_integration >> jenkins
        
        jenkins >> maven
        maven >> ant
        ant >> gradle
        
        apache_http >> nginx
        nginx >> iis
        
        mobile_framework >> mcs
        mcs >> mobile_backend

if __name__ == "__main__":
    create_oracle_tech_stack_diagram(filename="oracle_tech_stack", outformat="png")
    create_oracle_tech_stack_diagram(filename="oracle_tech_stack", outformat="pdf")
