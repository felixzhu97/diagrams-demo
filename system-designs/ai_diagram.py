from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_ai_diagram(filename: str, outformat: str) -> None:
    with Diagram("人工智能系统设计图（ML + LLM/RAG/对齐）", filename=filename, show=False, outformat=outformat, direction="LR"):
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

        with Cluster("在线特征服务"):
            feature_online = Server("在线特征服务")
            feature_monitor = Server("特征监控/分布可视化")
            feature_online >> feature_monitor

        with Cluster("经典 ML"):
            trainer = Server("训练（GBDT/NN）")
            hp_search = Server("超参搜索")
            eval_metrics = Server("评估（AUC/F1）")
            registry = Server("模型仓库")
            hp_search >> trainer >> eval_metrics >> registry

        with Cluster("LLM 与 RAG"):
            llm = Server("LLM 模型（推理）")
            retrieval = Server("向量检索")
            bm25 = Server("BM25/关键词召回")
            fusion = Server("分层召回/Fusion")
            rewrite = Server("查询重写/扩展")
            prompt = Server("Prompt 构造/模板")
            rerank = Server("重排/检索增强")
            tools = Server("函数调用/工具集成")
            retr_viz = Server("检索参数可视化（TopK/阈值）")
            bm25 >> fusion
            retrieval >> fusion >> rerank >> prompt >> llm
            rewrite >> retrieval
            rewrite >> bm25
            llm >> tools
            retrieval >> retr_viz
            bm25 >> retr_viz

        with Cluster("服务与编排"):
            api = Server("统一推理 API")
            gateway = Server("网关/鉴权")
            workflow = Server("编排/Agent")
            cache = Server("缓存/会话上下文")
            gateway >> api >> workflow
            workflow >> cache

        with Cluster("Agent 工具链"):
            func_lib = Server("函数库/工具适配")
            ext_api = Server("外部 API/DB")
            wf_nodes = Server("工作流节点/子任务")
            tools >> func_lib >> ext_api
            workflow >> wf_nodes >> func_lib

        with Cluster("评测与数据集"):
            eval_set = Server("评测集/对照集")
            eval_auto = Server("自动化评测/打分")
            eval_set >> eval_auto

        with Cluster("微调与对齐"):
            sft = Server("SFT 微调")
            dpo = Server("DPO/对齐")
            rlhf = Server("RLHF")
            distill = Server("蒸馏/LoRA")
            sft >> dpo >> rlhf >> distill

        with Cluster("监控与治理"):
            guard = Server("Guardrails/安全过滤")
            observ = Server("质量/监控/反馈")
            guard >> observ

        # 关键链路
        feature_store >> Edge(label="特征供给") >> api
        feature_store >> Edge(label="在线物化") >> feature_online
        registry >> Edge(label="在线推理") >> api
        api >> Edge(label="查询重写") >> rewrite
        api >> Edge(label="RAG 检索") >> retrieval
        vector_store >> Edge(label="语义检索") >> retrieval
        doc_store >> Edge(label="关键词召回") >> bm25
        func_lib >> Edge(label="执行") >> ext_api
        wf_nodes >> Edge(label="编排") >> tools
        api >> Edge(label="Prompt 构造") >> prompt
        llm >> Edge(label="输出") >> guard
        guard >> Edge(label="响应") >> gateway
        observ >> Edge(label="反馈数据") >> labeling
        feature_monitor >> Edge(label="分布/质量反馈") >> feature_eng

        # 评测与对齐
        eval_set >> Edge(label="离线评测") >> eval_auto
        eval_auto >> Edge(label="指标反馈") >> prompt
        eval_auto >> Edge(label="指标反馈") >> rewrite
        eval_auto >> Edge(label="选择最佳") >> registry
        labeling >> Edge(label="监督数据") >> sft
        sft >> Edge(label="对齐/偏好数据") >> dpo
        dpo >> Edge(label="奖励建模/策略优化") >> rlhf
        rlhf >> Edge(label="压缩/适配") >> distill
        distill >> Edge(label="新模型/权重") >> registry


if __name__ == "__main__":
    create_ai_diagram(filename="ai_design", outformat="png")
    create_ai_diagram(filename="ai_design", outformat="pdf")
