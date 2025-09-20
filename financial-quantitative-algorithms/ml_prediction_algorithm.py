from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_ml_prediction_algorithm(filename: str, outformat: str) -> None:
    with Diagram("机器学习预测与量化模型架构", filename=filename, show=False, outformat=outformat, direction="TB"):
        with Cluster("数据源层"):
            market_data = Server("市场数据")
            fundamental_data = Server("基本面数据")
            alternative_data = Server("替代数据")
            news_sentiment = Server("新闻情感")
            
        with Cluster("特征工程"):
            feature_extraction = Server("特征提取")
            feature_selection = Server("特征选择")
            feature_scaling = Server("特征缩放")
            feature_engineering = Server("特征工程")
            
        with Cluster("传统机器学习"):
            linear_models = Server("线性模型")
            tree_models = Server("树模型")
            ensemble_methods = Server("集成方法")
            svm_models = Server("SVM模型")
            
        with Cluster("深度学习"):
            neural_networks = Server("神经网络")
            lstm_networks = Server("LSTM网络")
            transformer_models = Server("Transformer")
            attention_mechanisms = Server("注意力机制")
            
        with Cluster("时间序列模型"):
            arima_models = Server("ARIMA模型")
            garch_models = Server("GARCH模型")
            state_space_models = Server("状态空间模型")
            regime_switching = Server("状态切换模型")
            
        with Cluster("模型训练"):
            cross_validation = Server("交叉验证")
            hyperparameter_tuning = Server("超参数调优")
            model_selection = Server("模型选择")
            ensemble_learning = Server("集成学习")
            
        with Cluster("模型评估"):
            backtesting = Server("回测验证")
            performance_metrics = Server("绩效指标")
            risk_metrics = Server("风险指标")
            model_diagnostics = Server("模型诊断")
            
        with Cluster("预测与部署"):
            prediction_engine = Server("预测引擎")
            model_serving = Server("模型服务")
            real_time_inference = Server("实时推理")
            batch_prediction = Server("批量预测")
            
        with Cluster("监控与更新"):
            model_monitoring = Server("模型监控")
            drift_detection = Server("漂移检测")
            model_retraining = Server("模型重训练")
            performance_tracking = Server("绩效跟踪")
            
        # 连接关系
        market_data >> Edge(label="价格数据") >> feature_extraction
        fundamental_data >> Edge(label="财务数据") >> feature_extraction
        alternative_data >> Edge(label="另类数据") >> feature_extraction
        news_sentiment >> Edge(label="情感数据") >> feature_extraction
        
        feature_extraction >> Edge(label="特征构建") >> feature_selection
        feature_selection >> Edge(label="特征筛选") >> feature_scaling
        feature_scaling >> Edge(label="特征标准化") >> feature_engineering
        
        feature_engineering >> Edge(label="特征输入") >> linear_models
        feature_engineering >> Edge(label="特征输入") >> tree_models
        feature_engineering >> Edge(label="特征输入") >> ensemble_methods
        feature_engineering >> Edge(label="特征输入") >> svm_models
        
        feature_engineering >> Edge(label="特征输入") >> neural_networks
        neural_networks >> Edge(label="序列建模") >> lstm_networks
        lstm_networks >> Edge(label="注意力机制") >> transformer_models
        transformer_models >> Edge(label="注意力计算") >> attention_mechanisms
        
        market_data >> Edge(label="时间序列") >> arima_models
        market_data >> Edge(label="波动率建模") >> garch_models
        market_data >> Edge(label="状态建模") >> state_space_models
        state_space_models >> Edge(label="状态切换") >> regime_switching
        
        linear_models >> Edge(label="模型训练") >> cross_validation
        tree_models >> Edge(label="模型训练") >> cross_validation
        neural_networks >> Edge(label="模型训练") >> cross_validation
        arima_models >> Edge(label="模型训练") >> cross_validation
        
        cross_validation >> Edge(label="验证结果") >> hyperparameter_tuning
        hyperparameter_tuning >> Edge(label="参数优化") >> model_selection
        model_selection >> Edge(label="模型选择") >> ensemble_learning
        
        ensemble_learning >> Edge(label="集成模型") >> backtesting
        backtesting >> Edge(label="回测结果") >> performance_metrics
        performance_metrics >> Edge(label="绩效评估") >> risk_metrics
        risk_metrics >> Edge(label="风险分析") >> model_diagnostics
        
        model_diagnostics >> Edge(label="模型验证") >> prediction_engine
        prediction_engine >> Edge(label="预测服务") >> model_serving
        model_serving >> Edge(label="实时服务") >> real_time_inference
        model_serving >> Edge(label="批量服务") >> batch_prediction
        
        real_time_inference >> Edge(label="实时监控") >> model_monitoring
        batch_prediction >> Edge(label="批量监控") >> model_monitoring
        model_monitoring >> Edge(label="漂移检测") >> drift_detection
        drift_detection >> Edge(label="模型更新") >> model_retraining
        
        model_retraining >> Edge(label="重训练") >> performance_tracking
        performance_tracking >> Edge(label="绩效反馈") >> model_selection
        
        # 反馈循环
        model_diagnostics >> Edge(label="反馈") >> feature_engineering
        performance_tracking >> Edge(label="反馈") >> hyperparameter_tuning


if __name__ == "__main__":
    create_ml_prediction_algorithm(filename="ml_prediction_algorithm", outformat="png")
    create_ml_prediction_algorithm(filename="ml_prediction_algorithm", outformat="pdf")
