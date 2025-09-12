from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_data_mining_diagram(filename: str, outformat: str) -> None:
    with Diagram("数据挖掘系统设计图（含 AutoML/特征治理）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("数据准备"):
            datasource = Server("数据源（DW/ODS/Logs）")
            cleaning = Server("清洗/缺失值处理")
            sampling = Server("采样/分层")
            datasource >> cleaning >> sampling

        with Cluster("特征工程"):
            fe_transform = Server("变换/编码/归一化")
            fe_select = Server("特征选择/降维")
            fe_store = Server("特征存储")
            fe_transform >> fe_select >> fe_store

        with Cluster("AutoML 流水线"):
            search_space = Server("搜索空间/模板")
            automl = Server("AutoML 编排")
            trials = Server("试验/并行评估")
            search_space >> automl >> trials

        with Cluster("模型训练"):
            train = Server("训练（GBDT/NN/SVM）")
            hp_search = Server("超参搜索（Grid/Random/Bayes）")
            cv = Server("交叉验证")
            hp_search >> train >> cv

        with Cluster("评估与解释"):
            metrics = Server("评估指标（AUC/F1/Recall）")
            explain = Server("模型解释（SHAP/LIME）")
            cv >> metrics
            train >> explain

        with Cluster("部署与服务"):
            model_registry = Server("模型仓库/版本")
            batch_infer = Server("批量推理")
            online_infer = Server("在线推理 API")
            model_registry >> batch_infer
            model_registry >> online_infer

        with Cluster("特征治理"):
            dq_checks = Server("特征质量校验")
            dist_monitor = Server("分布监控")
            drift_alerts = Server("漂移检测/报警")
            dq_checks >> dist_monitor >> drift_alerts

        with Cluster("监控与反馈"):
            monitor = Server("监控/漂移检测")
            feedback = Server("反馈闭环")
            monitor >> feedback

        # Flows
        sampling >> Edge(label="特征构建") >> fe_transform
        fe_store >> Edge(label="训练数据") >> train
        automl >> Edge(label="生成候选方案") >> hp_search
        trials >> Edge(label="选优") >> cv
        cv >> Edge(label="最佳模型") >> model_registry
        online_infer >> Edge(label="实时指标") >> monitor
        batch_infer >> Edge(label="离线指标") >> monitor
        dq_checks >> Edge(label="数据规则") >> fe_transform
        dist_monitor >> Edge(label="特征分布") >> monitor
        drift_alerts >> Edge(label="告警/回滚") >> model_registry
        feedback >> Edge(label="改进数据/规则") >> cleaning


if __name__ == "__main__":
    create_data_mining_diagram(filename="data_mining_design", outformat="png")
    create_data_mining_diagram(filename="data_mining_design", outformat="pdf")
