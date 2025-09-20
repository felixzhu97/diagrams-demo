from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_recommendation_system_algorithm(filename: str, outformat: str) -> None:
    with Diagram("推荐系统算法架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        # 用户层
        with Cluster("用户层"):
            web_app = Server("Web应用")
            mobile_app = Server("移动应用")
            api_gateway = Server("API网关")
            
        # 推荐服务层
        with Cluster("推荐服务层"):
            with Cluster("实时推荐服务"):
                realtime_rec = Server("实时推荐引擎")
                online_serving = Server("在线服务")
                
            with Cluster("离线推荐服务"):
                offline_rec = Server("离线推荐引擎")
                batch_processing = Server("批处理服务")
                
            with Cluster("混合推荐策略"):
                hybrid_engine = Server("混合推荐引擎")
                ensemble_model = Server("集成模型")
                
        # 算法层
        with Cluster("推荐算法层"):
            with Cluster("协同过滤"):
                cf_user = Server("用户协同过滤")
                cf_item = Server("物品协同过滤")
                cf_matrix = Server("矩阵分解")
                
            with Cluster("内容推荐"):
                content_based = Server("基于内容推荐")
                tf_idf = Server("TF-IDF")
                word2vec = Server("Word2Vec")
                
            with Cluster("深度学习"):
                deep_fm = Server("DeepFM")
                wide_deep = Server("Wide&Deep")
                neural_cf = Server("神经协同过滤")
                
            with Cluster("序列推荐"):
                rnn_rec = Server("RNN推荐")
                transformer = Server("Transformer")
                attention = Server("注意力机制")
                
        # 特征工程层
        with Cluster("特征工程层"):
            with Cluster("用户特征"):
                user_profile = Server("用户画像")
                user_behavior = Server("行为特征")
                user_demographic = Server("人口统计")
                
            with Cluster("物品特征"):
                item_content = Server("物品内容")
                item_metadata = Server("元数据")
                item_category = Server("分类标签")
                
            with Cluster("上下文特征"):
                time_context = Server("时间上下文")
                location_context = Server("位置上下文")
                session_context = Server("会话上下文")
                
        # 数据处理层
        with Cluster("数据处理层"):
            with Cluster("实时数据流"):
                kafka_stream = Server("Kafka流")
                flink = Server("Flink流处理")
                storm = Server("Storm流处理")
                
            with Cluster("批处理"):
                spark_batch = Server("Spark批处理")
                hadoop = Server("Hadoop")
                hive = Server("Hive数据仓库")
                
            with Cluster("特征存储"):
                feature_store = Server("特征存储")
                feature_cache = Server("特征缓存")
                
        # 存储层
        with Cluster("存储层"):
            with Cluster("用户数据"):
                user_db = Server("用户数据库")
                user_behavior_db = Server("行为数据库")
                
            with Cluster("物品数据"):
                item_db = Server("物品数据库")
                content_db = Server("内容数据库")
                
            with Cluster("推荐结果"):
                rec_cache = Server("推荐缓存")
                rec_db = Server("推荐数据库")
                
        # 监控与日志
        with Cluster("监控与日志"):
            monitoring = Server("监控系统")
            logging = Server("日志收集")
            metrics = Server("指标统计")
            
        # 连接关系
        # 用户请求流
        web_app >> Edge(label="HTTP请求") >> api_gateway
        mobile_app >> Edge(label="API调用") >> api_gateway
        api_gateway >> Edge(label="路由") >> realtime_rec
        
        # 实时推荐流程
        realtime_rec >> Edge(label="特征查询") >> feature_cache
        realtime_rec >> Edge(label="模型推理") >> online_serving
        online_serving >> Edge(label="结果缓存") >> rec_cache
        
        # 离线推荐流程
        offline_rec >> Edge(label="批处理") >> batch_processing
        batch_processing >> Edge(label="模型训练") >> spark_batch
        spark_batch >> Edge(label="特征计算") >> feature_store
        
        # 算法调用
        hybrid_engine >> Edge(label="协同过滤") >> cf_user
        hybrid_engine >> Edge(label="内容推荐") >> content_based
        hybrid_engine >> Edge(label="深度学习") >> deep_fm
        hybrid_engine >> Edge(label="序列推荐") >> rnn_rec
        
        # 特征工程
        cf_user >> Edge(label="用户特征") >> user_profile
        content_based >> Edge(label="物品特征") >> item_content
        deep_fm >> Edge(label="上下文特征") >> time_context
        
        # 数据流
        kafka_stream >> Edge(label="实时流") >> flink
        flink >> Edge(label="特征更新") >> feature_cache
        
        spark_batch >> Edge(label="批处理") >> hadoop
        hadoop >> Edge(label="数据存储") >> hive
        
        # 存储访问
        user_profile >> Edge(label="用户数据") >> user_db
        item_content >> Edge(label="物品数据") >> item_db
        rec_cache >> Edge(label="推荐结果") >> rec_db
        
        # 监控
        realtime_rec >> Edge(label="指标上报") >> monitoring
        offline_rec >> Edge(label="日志记录") >> logging
        monitoring >> Edge(label="统计") >> metrics


if __name__ == "__main__":
    create_recommendation_system_algorithm(filename="recommendation_system_algorithm", outformat="png")
    create_recommendation_system_algorithm(filename="recommendation_system_algorithm", outformat="pdf")