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
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.network import Router, Firewall
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python, Java, JavaScript, Cpp, Rust, Go
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

def create_openai_tech_stack_diagram(filename: str, outformat: str) -> None:
    # 创建OpenAI技术栈图表
    with Diagram("OpenAI技术栈", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            users = Users("OpenAI用户")
            developers = Users("开发者")
            researchers = Users("研究人员")
            enterprises = Users("企业用户")
            
            with Cluster("客户端应用"):
                chatgpt_app = Server("ChatGPT应用")
                api_clients = Server("API客户端")
                playground = Server("OpenAI Playground")
                cli_tools = Server("CLI工具")
                
        # 接入层
        with Cluster("接入层"):
            with Cluster("负载均衡和CDN"):
                load_balancer = ELB("负载均衡器")
                cdn = CloudFront("CDN")
                edge_locations = Server("边缘节点")
                
            with Cluster("API网关"):
                api_gateway = Server("API网关")
                rate_limiting = Server("速率限制")
                authentication = Server("身份认证")
                request_routing = Server("请求路由")
                
        # AI模型层
        with Cluster("AI模型层"):
            with Cluster("大型语言模型"):
                gpt4 = Server("GPT-4")
                gpt35_turbo = Server("GPT-3.5 Turbo")
                gpt3 = Server("GPT-3")
                codex = Server("Codex")
                
            with Cluster("专用模型"):
                dall_e = Server("DALL-E")
                whisper = Server("Whisper")
                claude = Server("Claude")
                embedding_models = Server("Embedding模型")
                
            with Cluster("模型管理"):
                model_serving = Server("模型服务")
                model_versioning = Server("模型版本管理")
                model_deployment = Server("模型部署")
                model_monitoring = Server("模型监控")
                
        # 训练基础设施层
        with Cluster("训练基础设施层"):
            with Cluster("计算集群"):
                gpu_clusters = Server("GPU集群")
                tpu_clusters = Server("TPU集群")
                distributed_training = Server("分布式训练")
                job_scheduler = Server("作业调度器")
                
            with Cluster("存储系统"):
                training_data_storage = Server("训练数据存储")
                model_checkpoints = Server("模型检查点")
                experiment_logs = Server("实验日志")
                dataset_management = Server("数据集管理")
                
            with Cluster("训练框架"):
                pytorch = Server("PyTorch")
                tensorflow = Server("TensorFlow")
                jax = Server("JAX")
                custom_frameworks = Server("自定义框架")
                
        # API服务层
        with Cluster("API服务层"):
            with Cluster("核心API"):
                completions_api = Server("Completions API")
                chat_api = Server("Chat API")
                embeddings_api = Server("Embeddings API")
                images_api = Server("Images API")
                
            with Cluster("专用API"):
                audio_api = Server("Audio API")
                fine_tuning_api = Server("Fine-tuning API")
                moderation_api = Server("Moderation API")
                assistants_api = Server("Assistants API")
                
            with Cluster("API管理"):
                api_versioning = Server("API版本管理")
                request_validation = Server("请求验证")
                response_formatting = Server("响应格式化")
                error_handling = Server("错误处理")
                
        # 数据处理层
        with Cluster("数据处理层"):
            with Cluster("数据预处理"):
                data_ingestion = Server("数据摄取")
                data_cleaning = Server("数据清洗")
                data_tokenization = Server("数据标记化")
                data_filtering = Server("数据过滤")
                
            with Cluster("数据存储"):
                vector_database = Server("向量数据库")
                document_store = Server("文档存储")
                cache_layer = Server("缓存层")
                backup_storage = Server("备份存储")
                
            with Cluster("数据管道"):
                etl_pipeline = Server("ETL管道")
                stream_processing = Server("流处理")
                batch_processing = Server("批处理")
                data_validation = Server("数据验证")
                
        # 推理服务层
        with Cluster("推理服务层"):
            with Cluster("推理引擎"):
                inference_server = Server("推理服务器")
                model_optimization = Server("模型优化")
                quantization = Server("量化")
                pruning = Server("剪枝")
                
            with Cluster("负载均衡"):
                request_distribution = Server("请求分发")
                auto_scaling = Server("自动扩缩容")
                health_checks = Server("健康检查")
                circuit_breaker = Server("熔断器")
                
            with Cluster("缓存系统"):
                response_cache = Server("响应缓存")
                model_cache = Server("模型缓存")
                prompt_cache = Server("提示缓存")
                result_cache = Server("结果缓存")
                
        # 安全层
        with Cluster("安全层"):
            with Cluster("内容安全"):
                content_moderation = Server("内容审核")
                safety_classifier = Server("安全分类器")
                harmful_content_detection = Server("有害内容检测")
                bias_detection = Server("偏见检测")
                
            with Cluster("数据安全"):
                data_encryption = Server("数据加密")
                access_control = Server("访问控制")
                audit_logging = Server("审计日志")
                privacy_protection = Server("隐私保护")
                
            with Cluster("API安全"):
                api_key_management = Server("API密钥管理")
                rate_limiting = Server("速率限制")
                ddos_protection = Server("DDoS防护")
                input_validation = Server("输入验证")
                
        # 监控和观测层
        with Cluster("监控和观测层"):
            with Cluster("性能监控"):
                latency_monitoring = Server("延迟监控")
                throughput_monitoring = Server("吞吐量监控")
                resource_utilization = Server("资源利用率")
                error_rate_monitoring = Server("错误率监控")
                
            with Cluster("模型监控"):
                model_performance = Server("模型性能")
                drift_detection = Server("漂移检测")
                quality_metrics = Server("质量指标")
                usage_analytics = Server("使用分析")
                
            with Cluster("基础设施监控"):
                system_health = Server("系统健康")
                capacity_planning = Server("容量规划")
                alerting = Server("告警系统")
                dashboards = Server("监控仪表板")
                
        # 研究工具层
        with Cluster("研究工具层"):
            with Cluster("实验管理"):
                experiment_tracking = Server("实验跟踪")
                hyperparameter_tuning = Server("超参数调优")
                model_comparison = Server("模型比较")
                reproducibility = Server("可重现性")
                
            with Cluster("数据分析"):
                statistical_analysis = Server("统计分析")
                visualization_tools = Server("可视化工具")
                data_exploration = Server("数据探索")
                hypothesis_testing = Server("假设检验")
                
            with Cluster("协作工具"):
                version_control = Server("版本控制")
                code_review = Server("代码审查")
                documentation = Server("文档系统")
                knowledge_sharing = Server("知识共享")
                
        # 云基础设施层
        with Cluster("云基础设施层"):
            with Cluster("计算资源"):
                kubernetes = GKE("Kubernetes")
                container_registry = Server("容器注册表")
                serverless_compute = Lambda("无服务器计算")
                edge_computing = Server("边缘计算")
                
            with Cluster("存储服务"):
                object_storage = S3("对象存储")
                block_storage = EBS("块存储")
                file_storage = EFS("文件存储")
                database_services = RDS("数据库服务")
                
            with Cluster("网络服务"):
                vpc = VPC("虚拟私有云")
                load_balancers = ELB("负载均衡器")
                dns_service = Route53("DNS服务")
                cdn_service = CloudFront("CDN服务")
                
        # 开发者工具层
        with Cluster("开发者工具层"):
            with Cluster("SDK和库"):
                python_sdk = Python("Python SDK")
                nodejs_sdk = JavaScript("Node.js SDK")
                curl_examples = Server("cURL示例")
                postman_collections = Server("Postman集合")
                
            with Cluster("开发工具"):
                openai_cli = Server("OpenAI CLI")
                playground_ide = Server("Playground IDE")
                api_explorer = Server("API Explorer")
                documentation_portal = Server("文档门户")
                
            with Cluster("测试工具"):
                sandbox_environment = Server("沙盒环境")
                mock_services = Server("模拟服务")
                testing_framework = Server("测试框架")
                performance_testing = Server("性能测试")
                
        # 企业服务层
        with Cluster("企业服务层"):
            with Cluster("企业功能"):
                sso_integration = Server("SSO集成")
                custom_deployment = Server("自定义部署")
                dedicated_infrastructure = Server("专用基础设施")
                sla_guarantees = Server("SLA保证")
                
            with Cluster("合规和安全"):
                enterprise_security = Server("企业安全")
                compliance_frameworks = Server("合规框架")
                data_residency = Server("数据驻留")
                audit_capabilities = Server("审计能力")
                
            with Cluster("支持和培训"):
                dedicated_support = Server("专属支持")
                training_programs = Server("培训计划")
                best_practices = Server("最佳实践")
                consulting_services = Server("咨询服务")
                
        # 连接关系
        users >> chatgpt_app
        developers >> api_clients
        researchers >> playground
        enterprises >> cli_tools
        
        chatgpt_app >> load_balancer
        api_clients >> cdn
        playground >> edge_locations
        cli_tools >> api_gateway
        
        load_balancer >> cdn
        cdn >> api_gateway
        
        api_gateway >> rate_limiting
        rate_limiting >> authentication
        authentication >> request_routing
        
        request_routing >> gpt4
        request_routing >> gpt35_turbo
        request_routing >> gpt3
        request_routing >> codex
        
        dall_e >> whisper
        whisper >> claude
        claude >> embedding_models
        
        gpt4 >> model_serving
        model_serving >> model_versioning
        model_versioning >> model_deployment
        model_deployment >> model_monitoring
        
        gpu_clusters >> tpu_clusters
        tpu_clusters >> distributed_training
        distributed_training >> job_scheduler
        
        training_data_storage >> model_checkpoints
        model_checkpoints >> experiment_logs
        experiment_logs >> dataset_management
        
        pytorch >> tensorflow
        tensorflow >> jax
        jax >> custom_frameworks
        
        completions_api >> chat_api
        chat_api >> embeddings_api
        embeddings_api >> images_api
        
        audio_api >> fine_tuning_api
        fine_tuning_api >> moderation_api
        moderation_api >> assistants_api
        
        api_versioning >> request_validation
        request_validation >> response_formatting
        response_formatting >> error_handling
        
        data_ingestion >> data_cleaning
        data_cleaning >> data_tokenization
        data_tokenization >> data_filtering
        
        vector_database >> document_store
        document_store >> cache_layer
        cache_layer >> backup_storage
        
        etl_pipeline >> stream_processing
        stream_processing >> batch_processing
        batch_processing >> data_validation
        
        inference_server >> model_optimization
        model_optimization >> quantization
        quantization >> pruning
        
        request_distribution >> auto_scaling
        auto_scaling >> health_checks
        health_checks >> circuit_breaker
        
        response_cache >> model_cache
        model_cache >> prompt_cache
        prompt_cache >> result_cache
        
        content_moderation >> safety_classifier
        safety_classifier >> harmful_content_detection
        harmful_content_detection >> bias_detection
        
        data_encryption >> access_control
        access_control >> audit_logging
        audit_logging >> privacy_protection
        
        api_key_management >> rate_limiting
        rate_limiting >> ddos_protection
        ddos_protection >> input_validation
        
        latency_monitoring >> throughput_monitoring
        throughput_monitoring >> resource_utilization
        resource_utilization >> error_rate_monitoring
        
        model_performance >> drift_detection
        drift_detection >> quality_metrics
        quality_metrics >> usage_analytics
        
        system_health >> capacity_planning
        capacity_planning >> alerting
        alerting >> dashboards
        
        experiment_tracking >> hyperparameter_tuning
        hyperparameter_tuning >> model_comparison
        model_comparison >> reproducibility
        
        statistical_analysis >> visualization_tools
        visualization_tools >> data_exploration
        data_exploration >> hypothesis_testing
        
        version_control >> code_review
        code_review >> documentation
        documentation >> knowledge_sharing
        
        kubernetes >> container_registry
        container_registry >> serverless_compute
        serverless_compute >> edge_computing
        
        object_storage >> block_storage
        block_storage >> file_storage
        file_storage >> database_services
        
        vpc >> load_balancers
        load_balancers >> dns_service
        dns_service >> cdn_service
        
        python_sdk >> nodejs_sdk
        nodejs_sdk >> curl_examples
        curl_examples >> postman_collections
        
        openai_cli >> playground_ide
        playground_ide >> api_explorer
        api_explorer >> documentation_portal
        
        sandbox_environment >> mock_services
        mock_services >> testing_framework
        testing_framework >> performance_testing
        
        sso_integration >> custom_deployment
        custom_deployment >> dedicated_infrastructure
        dedicated_infrastructure >> sla_guarantees
        
        enterprise_security >> compliance_frameworks
        compliance_frameworks >> data_residency
        data_residency >> audit_capabilities
        
        dedicated_support >> training_programs
        training_programs >> best_practices
        best_practices >> consulting_services

if __name__ == "__main__":
    create_openai_tech_stack_diagram(filename="openai_tech_stack", outformat="png")
    create_openai_tech_stack_diagram(filename="openai_tech_stack", outformat="pdf")
