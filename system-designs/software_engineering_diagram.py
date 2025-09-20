from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_software_engineering_diagram(filename: str, outformat: str) -> None:
    with Diagram("软件工程体系设计图（含质量门禁与SRE）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("需求与规划"):
            stakeholders = Server("干系人/需求")
            roadmap = Server("Roadmap/OKR")
            backlog = Server("Backlog/故事")
            stakeholders >> roadmap >> backlog

        with Cluster("架构与设计"):
            adr = Server("ADR/设计评审")
            diagrams = Server("架构图/建模")
            standards = Server("编码规范/指南")
            adr >> diagrams >> standards

        with Cluster("开发与协作"):
            vcs = Server("代码仓库（Git）")
            pr = Server("分支/PR 评审")
            deps = Server("依赖管理")
            precommit = Server("Pre-commit/Lint/Format")
            vcs >> pr
            pr >> precommit
            deps >> precommit

        with Cluster("测试质量"):
            unit = Server("单元测试")
            it = Server("集成测试")
            e2e = Server("端到端测试")
            unit >> it >> e2e

        with Cluster("安全与合规"):
            sast = Server("SAST/依赖扫描")
            dast = Server("DAST")
            secrets = Server("Secrets 检测")
            licenses = Server("License 合规")
            sast >> licenses
            secrets >> sast

        with Cluster("CI/CD 流水线"):
            build = Server("构建/制品")
            test = Server("测试执行")
            scan = Server("安全/质量扫描")
            artifact = Server("制品库/镜像仓库")
            deploy = Server("部署/发布")
            build >> test >> scan >> artifact >> deploy

        with Cluster("发布与配置"):
            feature_flag = Server("特性开关")
            config = Server("配置中心")
            release = Server("灰度/蓝绿/回滚")
            feature_flag >> release
            config >> release

        with Cluster("运行环境"):
            env_dev = Server("开发环境")
            env_stg = Server("预生产")
            env_prod = Server("生产")
            env_dev >> env_stg >> env_prod

        with Cluster("可观测性"):
            logging = Server("日志")
            metrics = Server("指标")
            tracing = Server("链路追踪")
            logging >> metrics >> tracing

        with Cluster("运维与响应"):
            incident = Server("告警/事件响应")
            postmortem = Server("复盘/改进")
            incident >> postmortem

        with Cluster("项目管理"):
            board = Server("迭代/看板")
            velocity = Server("速率/燃尽")
            board >> velocity

        with Cluster("质量门禁矩阵"):
            coverage = Server("覆盖率阈值")
            dup_code = Server("重复代码阈值")
            sec_gate = Server("安全阈值（高危=0）")
            style_gate = Server("风格/静态检查")
            coverage >> dup_code >> sec_gate >> style_gate

        with Cluster("SRE 实践"):
            slo = Server("SLO/错误预算")
            circuit = Server("熔断/降级")
            rate_limit = Server("限流")
            chaos = Server("混沌演练")
            slo >> circuit >> rate_limit >> chaos

        # 主链路
        backlog >> Edge(label="方案/设计") >> adr
        standards >> Edge(label="实现") >> vcs
        vcs >> Edge(label="PR/代码评审") >> pr
        precommit >> Edge(label="质量门禁") >> unit
        unit >> Edge(label="触发 CI") >> build
        test >> Edge(label="质量反馈") >> pr
        scan >> Edge(label="安全反馈") >> pr
        artifact >> Edge(label="部署制品") >> deploy
        deploy >> Edge(label="到各环境") >> env_stg
        env_stg >> Edge(label="验证/演练") >> env_prod
        env_prod >> Edge(label="遥测") >> logging
        metrics >> Edge(label="SLO/报警") >> incident
        incident >> Edge(label="行动项") >> backlog
        release >> Edge(label="流量控制") >> env_prod
        feature_flag >> Edge(label="动态开关") >> env_prod
        tracing >> Edge(label="瓶颈定位") >> postmortem

        # 质量门禁与流水线联动
        coverage >> Edge(label="阈值校验") >> test
        dup_code >> Edge(label="阈值校验") >> scan
        sec_gate >> Edge(label="阻断风险") >> scan
        style_gate >> Edge(label="规范校验") >> precommit

        # SRE 与生产联动
        slo >> Edge(label="预算消耗/报警") >> metrics
        circuit >> Edge(label="保护下游") >> env_prod
        rate_limit >> Edge(label="稳定性") >> env_prod
        chaos >> Edge(label="演练/验证") >> env_stg


if __name__ == "__main__":
    create_software_engineering_diagram(filename="software_engineering", outformat="png")
    create_software_engineering_diagram(filename="software_engineering", outformat="pdf")
