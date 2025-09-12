from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_k8s_diagram(filename: str, outformat: str) -> None:
    with Diagram("Kubernetes 子系统", filename=filename, show=False, outformat=outformat, direction="LR"):
        # 控制面
        with Cluster("控制面（API/调度/控制器）"):
            k8s_api = Server("kube-apiserver")
            scheduler = Server("kube-scheduler")
            controller = Server("kube-controller-manager")
            etcd = Server("etcd")
            k8s_api >> controller
            k8s_api >> scheduler
            k8s_api >> etcd

        # 工作负载
        with Cluster("工作负载（Pods/Deployments/Jobs）"):
            pods = Server("Pods")
            deployments = Server("Deployments")
            jobs = Server("Jobs")
            deployments >> pods
            jobs >> pods

        # 存储
        with Cluster("存储（CSI/PV/PVC）"):
            csi = Server("CSI Driver")
            pv = Server("PersistentVolume")
            pvc = Server("PersistentVolumeClaim")
            pvc >> pv
            csi >> pv

        # 网络
        with Cluster("网络（CNI/Ingress/Service）"):
            cni = Server("CNI")
            svc = Server("Service")
            ingress = Server("Ingress")
            ingress_ctl = Server("Ingress Controller")
            ingress_ctl >> ingress
            cni >> svc
            ingress >> svc

        # 节点组件
        with Cluster("节点组件（kubelet/kube-proxy/CRI）"):
            kubelet = Server("kubelet")
            kube_proxy = Server("kube-proxy")
            cri = Server("CRI (containerd/CRI-O)")
            kubelet >> cri
            kube_proxy >> cni

        # 命名空间
        with Cluster("命名空间（多租户隔离）"):
            ns_prod = Server("namespace: prod")
            ns_dev = Server("namespace: dev")

        # 自动伸缩
        with Cluster("自动伸缩（HPA/VPA）"):
            hpa = Server("HPA")
            vpa = Server("VPA")

        # 扩展
        with Cluster("扩展（Operator/CRD）"):
            crd = Server("CRD")
            operator = Server("Operator")
            operator >> crd

        # Service Mesh
        with Cluster("Service Mesh（Istio）"):
            istiod = Server("istiod")
            sidecar = Server("Envoy Sidecar")
            istiod >> sidecar

        # 关键链路
        ingress_ctl >> Edge(label="L7 控制") >> ingress
        ingress >> Edge(label="L4/L7 路由") >> svc
        svc >> Edge(label="Pods 负载均衡") >> pods
        kubelet >> Edge(label="管理 Pod/容器") >> pods
        hpa >> Edge(label="水平伸缩") >> deployments
        vpa >> Edge(label="垂直伸缩") >> deployments
        operator >> Edge(label="编排/自定义逻辑") >> pods
        crd >> Edge(label="扩展 API") >> k8s_api
        sidecar >> Edge(label="东西向流量/可观测") >> pods
        k8s_api >> Edge(label="调度") >> scheduler
        k8s_api >> Edge(label="协调/控制") >> controller
        controller >> Edge(label="状态存储") >> etcd
        scheduler >> Edge(label="分配节点/创建 Pod") >> pods


if __name__ == "__main__":
    create_k8s_diagram(filename="k8s_design", outformat="png")
    create_k8s_diagram(filename="k8s_design", outformat="pdf")
