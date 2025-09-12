from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_business_admin_diagram(filename: str, outformat: str) -> None:
    with Diagram("工商管理系统设计图", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("门户与中台"):
            portal = Server("统一门户/SSO")
            bpm = Server("流程引擎/BPM")
            esb = Server("集成总线/ESB")
            portal >> bpm >> esb

        with Cluster("人力资源 HRM"):
            hr_core = Server("员工主数据")
            payroll = Server("薪酬/社保")
            attendance = Server("考勤/排班")
            performance = Server("绩效/考核")
            hr_core >> payroll
            attendance >> payroll
            performance >> hr_core

        with Cluster("财务 Finance"):
            gl = Server("总账/财务核算")
            ap = Server("应付/费用")
            ar = Server("应收/发票")
            asset = Server("固定资产")
            budget = Server("预算管理")
            ap >> gl
            ar >> gl
            asset >> gl
            budget >> gl

        with Cluster("客户与销售 CRM/Sales"):
            crm = Server("客户管理/线索/商机")
            sales = Server("销售订单/报价")
            contract = Server("合同/回款")
            crm >> sales >> contract

        with Cluster("采购与供应链 SCM"):
            procurement = Server("采购申请/询价/下单")
            supplier = Server("供应商管理")
            wms = Server("仓储/入库/出库")
            logistics = Server("物流/配送")
            procurement >> supplier
            procurement >> wms >> logistics

        with Cluster("库存与生产 MRP/ERP"):
            bom = Server("BOM/物料")
            mrp = Server("MRP/计划")
            mes = Server("生产执行 MES")
            qc = Server("质检/QC")
            wms2 = Server("库存/库位")
            bom >> mrp >> mes >> qc >> wms2

        with Cluster("项目与协作"):
            pm = Server("项目管理/里程碑")
            doc = Server("文档/知识库")
            pm >> doc

        with Cluster("合规与审计"):
            compliance = Server("合规模型/制度")
            audit = Server("审计/内控")
            risk = Server("风险/权限治理")
            compliance >> audit >> risk

        with Cluster("报表与分析"):
            dwh = Server("数据仓库/DW")
            bi = Server("BI/可视化")
            plan = Server("经营分析/预测")
            dwh >> bi >> plan

        with Cluster("对外集成"):
            tax = Server("税务平台/电子发票")
            bank = Server("银行/银企直连")
            gov = Server("监管/政府平台")
            courier = Server("三方物流/快递")

        # 关键链路
        esb >> Edge(label="主数据") >> hr_core
        esb >> Edge(label="主数据") >> supplier
        esb >> Edge(label="主数据") >> bom
        sales >> Edge(label="采购触发") >> procurement
        contract >> Edge(label="应收/回款") >> ar
        ap >> Edge(label="付款") >> bank
        ar >> Edge(label="收款") >> bank
        asset >> Edge(label="发票/票据") >> tax
        wms >> Edge(label="出入库回传") >> dwh
        wms2 >> Edge(label="库存回传") >> dwh
        gl >> Edge(label="财务报表") >> dwh
        mes >> Edge(label="产线数据") >> dwh
        bi >> Edge(label="指标/看板") >> portal
        bpm >> Edge(label="审批/流程") >> procurement
        bpm >> Edge(label="审批/流程") >> ap
        bpm >> Edge(label="审批/流程") >> ar
        compliance >> Edge(label="制度/准入") >> esb
        risk >> Edge(label="权限策略") >> portal
        audit >> Edge(label="审计记录") >> dwh


if __name__ == "__main__":
    create_business_admin_diagram(filename="business_admin", outformat="png")
    create_business_admin_diagram(filename="business_admin", outformat="pdf")
