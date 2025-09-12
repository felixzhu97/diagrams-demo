from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_ai_diagram(filename: str, outformat: str) -> None:
    with Diagram("人工智能系统设计图（ML + LLM/RAG）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("数据层"):
            raw_data = Server("原始数据（DW/Logs/Docs）")
            labeling = Server("标注/对齐")
            vector_store = Server("向量库")
            doc_store = Server("文档库")
            raw_data >> labeling
            raw_data >> doc_store

        with Cluster("特征与索引"):
            feature_eng = Server("特征工程")
            feature_store = Server("特征存储")
            embedding = Server("Embedding 生成")
            feature_eng >> feature_store
            doc_store >> embedding >> vector_store

        with Cluster("经典 ML"):
            trainer = Server("训练（GBDT/NN）")
            hp_search = Server("超参搜索")
            eval_metrics = Server("评估（AUC/F1）")
            registry = Server("模型仓库")
            hp_search >> trainer >> eval_metrics >> registry

        with Cluster("LLM 与 RAG"):
            llm = Server("LLM 模型（推理）")
            retrieval = Server("向量检索/重排序")
            prompt = Server("Prompt 构造/模板")
            rerank = Server("重排/检索增强")
            retrieval >> rerank >> prompt >> llm

        with Cluster("服务与编排"):
            api = Server("统一推理 API")
            gateway = Server("网关/鉴权")
            workflow = Server("编排/Agent")
            cache = Server("缓存/会话上下文")
            gateway >> api >> workflow
            workflow >> cache

        with Cluster("监控与治理"):
            guard = Server("Guardrails/安全过滤")
            observ = Server("质量/监控/反馈")
            guard >> observ

        # 关键链路
        feature_store >> Edge(label="特征供给") >> api
        registry >> Edge(label="在线推理") >> api
        api >> Edge(label="RAG 检索") >> retrieval
        vector_store >> Edge(label="语义检索") >> retrieval
        api >> Edge(label="Prompt 构造") >> prompt
        llm >> Edge(label="输出") >> guard
        guard >> Edge(label="响应") >> gateway
        observ >> Edge(label="反馈数据") >> labeling


if __name__ == "__main__":
    create_ai_diagram(filename="ai_design", outformat="png")
    create_ai_diagram(filename="ai_design", outformat="pdf")
