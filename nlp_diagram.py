from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_nlp_diagram(filename: str, outformat: str) -> None:
    with Diagram("自然语言处理系统设计图（含多语言/对话/IR/QA）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("数据管道"):
            corpus = Server("语料来源（爬取/日志/标注）")
            cleaning = Server("清洗/去噪/脱敏")
            labeling = Server("标注/审核")
            corpus >> cleaning >> labeling

        with Cluster("预处理"):
            normalization = Server("规范化/大小写/Unicode")
            lang_detect = Server("语言识别/分段")
            sentence_split = Server("分句/分段")
            normalization >> lang_detect >> sentence_split

        with Cluster("分词与表示"):
            tokenization = Server("分词/子词（BPE/WordPiece）")
            vocab = Server("词表/停用词")
            embedding = Server("词向量/上下文向量")
            tokenization >> vocab
            tokenization >> embedding

        with Cluster("经典 NLP 任务"):
            pos = Server("词性标注 POS")
            ner = Server("命名实体识别 NER")
            parse = Server("依存/成分句法")
            tfidf = Server("TF-IDF/关键词")
            embedding >> pos
            embedding >> ner
            embedding >> parse
            embedding >> tfidf

        with Cluster("神经网络模型"):
            rnn = Server("RNN/LSTM/GRU")
            cnn = Server("Text CNN")
            transformer = Server("Transformer/BERT/RoBERTa")
            seq2seq = Server("Seq2Seq/Attention")
            transformer >> seq2seq

        with Cluster("多语言与机器翻译"):
            mbert = Server("mBERT/XLM-R")
            mt_model = Server("NMT/Transformer")
            align = Server("词对齐/术语表")
            mbert >> mt_model >> align

        with Cluster("对话系统"):
            nlu = Server("NLU 意图/槽位")
            dm = Server("对话管理/策略")
            nlg = Server("NLG 文本生成")
            kb = Server("知识库/FAQ")
            nlu >> dm >> nlg
            kb >> dm

        with Cluster("信息检索与问答"):
            index = Server("倒排索引/向量索引")
            retriever = Server("检索器（BM25/ANN）")
            reader = Server("阅读理解/抽取式 QA")
            reranker = Server("重排器")
            index >> retriever >> reranker >> reader

        with Cluster("训练与评估"):
            train = Server("训练/微调")
            metrics = Server("评估指标（BLEU/F1/ROUGE）")
            registry = Server("模型仓库")
            train >> metrics >> registry

        with Cluster("部署与服务"):
            online = Server("在线推理 API")
            batch = Server("批量离线推理")
            cache = Server("缓存/索引")
            registry >> online
            registry >> batch
            online >> cache

        with Cluster("监控与反馈"):
            logging = Server("日志/质量监控")
            feedback = Server("用户反馈/抽样标注")
            logging >> feedback

        # Flows
        labeling >> Edge(label="训练数据") >> tokenization
        sentence_split >> Edge(label="切分/标注输入") >> tokenization
        embedding >> Edge(label="特征供给") >> train
        tfidf >> Edge(label="特征供给") >> train
        seq2seq >> Edge(label="编码器/解码器") >> train
        transformer >> Edge(label="上下文表示") >> train
        mbert >> Edge(label="跨语言表示") >> train
        mt_model >> Edge(label="平行语料训练") >> train
        nlu >> Edge(label="特征/标签") >> train
        retriever >> Edge(label="召回样本") >> train

        # 服务链路
        online >> Edge(label="日志/指标") >> logging
        batch >> Edge(label="结果分析") >> logging
        feedback >> Edge(label="数据改进") >> cleaning
        online >> Edge(label="多语言翻译") >> mt_model
        online >> Edge(label="对话理解") >> nlu
        dm >> Edge(label="检索答案") >> retriever
        retriever >> Edge(label="阅读/抽取") >> reader
        reader >> Edge(label="答案/证据") >> online
        nlg >> Edge(label="回复文本") >> online
        align >> Edge(label="术语/短语表") >> nlg
        index >> Edge(label="索引更新") >> cache


if __name__ == "__main__":
    create_nlp_diagram(filename="nlp_design", outformat="png")
    create_nlp_diagram(filename="nlp_design", outformat="pdf")
