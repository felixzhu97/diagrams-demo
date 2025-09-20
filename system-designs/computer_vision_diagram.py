from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_computer_vision_diagram(filename: str, outformat: str) -> None:
    with Diagram("计算机视觉系统设计图（CV Pipeline）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("数据采集与预处理"):
            camera = Server("摄像头/传感器")
            video_stream = Server("视频流")
            image_capture = Server("图像采集")
            data_aug = Server("数据增强")
            preprocess = Server("预处理（归一化/缩放）")
            camera >> video_stream >> image_capture
            image_capture >> data_aug >> preprocess

        with Cluster("数据存储与管理"):
            raw_storage = Server("原始数据存储")
            annotation_db = Server("标注数据库")
            dataset_mgr = Server("数据集管理")
            version_control = Server("版本控制")
            raw_storage >> dataset_mgr
            annotation_db >> dataset_mgr
            dataset_mgr >> version_control

        with Cluster("标注与质量控制"):
            auto_label = Server("自动标注")
            manual_label = Server("人工标注")
            quality_check = Server("质量检查")
            label_validation = Server("标注验证")
            auto_label >> quality_check
            manual_label >> quality_check
            quality_check >> label_validation

        with Cluster("特征提取与表示"):
            cnn_backbone = Server("CNN 骨干网络")
            feature_extractor = Server("特征提取器")
            attention_mech = Server("注意力机制")
            multi_scale = Server("多尺度特征")
            cnn_backbone >> feature_extractor
            feature_extractor >> attention_mech
            feature_extractor >> multi_scale

        with Cluster("目标检测与识别"):
            object_detector = Server("目标检测器")
            face_recognition = Server("人脸识别")
            ocr_engine = Server("OCR 引擎")
            scene_analysis = Server("场景分析")
            object_detector >> face_recognition
            object_detector >> ocr_engine
            object_detector >> scene_analysis

        with Cluster("图像分割与理解"):
            semantic_seg = Server("语义分割")
            instance_seg = Server("实例分割")
            depth_estimation = Server("深度估计")
            pose_estimation = Server("姿态估计")
            semantic_seg >> instance_seg
            semantic_seg >> depth_estimation
            semantic_seg >> pose_estimation

        with Cluster("模型训练与优化"):
            trainer = Server("模型训练器")
            optimizer = Server("优化器（Adam/SGD）")
            loss_function = Server("损失函数")
            hyper_tuning = Server("超参数调优")
            model_compression = Server("模型压缩")
            trainer >> optimizer >> loss_function
            loss_function >> hyper_tuning
            hyper_tuning >> model_compression

        with Cluster("模型部署与推理"):
            model_serving = Server("模型服务")
            inference_engine = Server("推理引擎")
            gpu_acceleration = Server("GPU 加速")
            edge_deployment = Server("边缘部署")
            model_serving >> inference_engine
            inference_engine >> gpu_acceleration
            inference_engine >> edge_deployment

        with Cluster("实时处理与流媒体"):
            real_time_proc = Server("实时处理")
            video_analytics = Server("视频分析")
            stream_processing = Server("流处理")
            frame_buffer = Server("帧缓冲")
            real_time_proc >> video_analytics
            video_analytics >> stream_processing
            stream_processing >> frame_buffer

        with Cluster("结果后处理与输出"):
            result_filter = Server("结果过滤")
            confidence_threshold = Server("置信度阈值")
            nms = Server("非极大值抑制")
            output_format = Server("输出格式化")
            result_filter >> confidence_threshold
            confidence_threshold >> nms
            nms >> output_format

        with Cluster("监控与评估"):
            performance_monitor = Server("性能监控")
            accuracy_metrics = Server("准确率指标")
            latency_monitor = Server("延迟监控")
            model_drift = Server("模型漂移检测")
            performance_monitor >> accuracy_metrics
            performance_monitor >> latency_monitor
            performance_monitor >> model_drift

        with Cluster("数据增强与合成"):
            gan_augmentation = Server("GAN 数据增强")
            style_transfer = Server("风格迁移")
            synthetic_data = Server("合成数据生成")
            domain_adaptation = Server("域适应")
            gan_augmentation >> style_transfer
            style_transfer >> synthetic_data
            synthetic_data >> domain_adaptation

        # 关键数据流连接
        preprocess >> Edge(label="预处理数据") >> raw_storage
        raw_storage >> Edge(label="训练数据") >> trainer
        annotation_db >> Edge(label="标注数据") >> trainer
        trainer >> Edge(label="训练模型") >> model_serving
        model_serving >> Edge(label="推理服务") >> real_time_proc
        preprocess >> Edge(label="实时数据") >> real_time_proc
        real_time_proc >> Edge(label="处理结果") >> result_filter
        result_filter >> Edge(label="最终输出") >> output_format

        # 特征提取链路
        preprocess >> Edge(label="输入图像") >> cnn_backbone
        cnn_backbone >> Edge(label="特征图") >> object_detector
        cnn_backbone >> Edge(label="特征图") >> semantic_seg
        feature_extractor >> Edge(label="高级特征") >> object_detector
        attention_mech >> Edge(label="注意力权重") >> object_detector

        # 模型优化链路
        trainer >> Edge(label="模型权重") >> model_compression
        model_compression >> Edge(label="压缩模型") >> model_serving
        hyper_tuning >> Edge(label="最优参数") >> trainer
        loss_function >> Edge(label="梯度更新") >> optimizer

        # 监控与反馈链路
        output_format >> Edge(label="预测结果") >> performance_monitor
        performance_monitor >> Edge(label="性能指标") >> model_drift
        model_drift >> Edge(label="漂移信号") >> trainer
        accuracy_metrics >> Edge(label="准确率反馈") >> hyper_tuning

        # 数据增强链路
        raw_storage >> Edge(label="原始数据") >> gan_augmentation
        gan_augmentation >> Edge(label="增强数据") >> dataset_mgr
        synthetic_data >> Edge(label="合成样本") >> dataset_mgr
        domain_adaptation >> Edge(label="域适应数据") >> trainer

        # 实时处理链路
        video_stream >> Edge(label="视频流") >> real_time_proc
        real_time_proc >> Edge(label="帧数据") >> inference_engine
        inference_engine >> Edge(label="推理结果") >> video_analytics
        frame_buffer >> Edge(label="缓冲帧") >> inference_engine

        # 部署与加速链路
        model_serving >> Edge(label="模型服务") >> gpu_acceleration
        gpu_acceleration >> Edge(label="加速推理") >> inference_engine
        edge_deployment >> Edge(label="边缘模型") >> inference_engine
        model_compression >> Edge(label="轻量化模型") >> edge_deployment


if __name__ == "__main__":
    create_computer_vision_diagram(filename="computer_vision_design", outformat="png")
    create_computer_vision_diagram(filename="computer_vision_design", outformat="pdf")
