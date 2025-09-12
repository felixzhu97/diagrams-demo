from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_os_design_diagram(filename: str, outformat: str) -> None:
    with Diagram("操作系统设计图（细化）", filename=filename, show=False, outformat=outformat, direction="LR"):
        # 用户空间
        with Cluster("用户空间（进程/线程/服务）"):
            shell = Server("Shell / CLI")
            user_procs = Server("User Processes")
            threads = Server("Threads")
            system_daemons = Server("System Daemons")
            runtimes = Server("语言运行时 VM")
            user_procs >> Edge(label="spawn/join") >> threads
            user_procs >> Edge(label="执行") >> runtimes

        # 系统调用接口与事件
        with Cluster("系统调用与事件机制（ABI/入口/事件）"):
            libc = Server("C Library / ABI")
            vDSO = Server("vDSO")
            syscall_gate = Server("Syscall Gate")
            epoll_kqueue = Server("epoll/kqueue 事件环")
            libc >> Edge(label="fast path") >> vDSO
            libc >> Edge(label="syscall") >> syscall_gate
            syscall_gate >> Edge(label="事件注册/等待") >> epoll_kqueue

        # 内核核心
        with Cluster("内核（调度/内存/文件/网络/I/O/安全）"):
            # 调度
            with Cluster("调度（多级反馈队列）"):
                runqueue = Server("运行队列")
                scheduler = Server("调度器")
                scheduler >> runqueue
            # 内存
            with Cluster("内存管理（MMU/分页/交换）"):
                mm = Server("内存管理器")
                page_cache = Server("页缓存")
                swap = Server("交换区")
                mm >> page_cache
                mm >> swap
            # 文件
            with Cluster("文件子系统（VFS/FS 实现）"):
                vfs = Server("VFS")
                fs_impl = Server("FS 实现")
                vfs >> fs_impl
            # I/O
            with Cluster("I/O 子系统（块/字符）"):
                io = Server("I/O 管理器")
            # 网络
            with Cluster("网络栈（L2-L4）"):
                net = Server("网络栈")
            # 安全
            with Cluster("安全（权限/审计/防护）"):
                sec = Server("安全模块")
                audit = Server("审计/日志")
                selinux = Server("SELinux/AppArmor")
                sec >> audit
                sec >> selinux

        # 可观测与程序化内核（eBPF）
        with Cluster("可观测与可编程内核（eBPF）"):
            ebpf_prog = Server("eBPF 程序")
            ebpf_maps = Server("eBPF Maps")
            ebpf_loader = Server("加载器/bpf 系统调用")
            ebpf_prog >> ebpf_maps

        # 容器与隔离
        with Cluster("隔离与资源控制（Namespace/CGroup/容器）"):
            ns = Server("Namespaces")
            cgroup = Server("CGroup")
            oci = Server("OCI 规范")
            runc = Server("runc")
            containerd = Server("containerd")
            ns >> cgroup
            oci >> runc >> containerd

        # 中断与时钟
        with Cluster("中断与时钟（IRQ/Timer）"):
            apic = Server("APIC/中断控制器")
            timer = Server("系统定时器")

        # 设备与驱动
        with Cluster("设备与驱动（HAL/驱动框架）"):
            hal = Server("硬件抽象层")
            drivers = Server("设备驱动")
            drivers >> hal

        # 存储介质
        with Cluster("存储与介质（块设备）"):
            disk = Server("磁盘/SSD/NVMe")

        # 网络与外设
        with Cluster("网络与外设（NIC/TTY）"):
            nic = Server("网卡/驱动")
            tty = Server("终端/串口")

        # 用户到内核
        shell >> Edge(label="启动/控制") >> user_procs
        user_procs >> Edge(label="库调用") >> libc
        system_daemons >> Edge(label="服务调用") >> libc

        # 进入内核
        vDSO >> Edge(label="时间/系统信息") >> user_procs
        syscall_gate >> Edge(label="进入内核") >> scheduler

        # 调度与内存
        scheduler >> Edge(label="排队/切换") >> runqueue
        scheduler >> Edge(label="内存分配") >> mm
        scheduler >> Edge(label="文件操作") >> vfs
        scheduler >> Edge(label="I/O 请求") >> io
        scheduler >> Edge(label="网络 I/O") >> net
        scheduler >> Edge(label="权限校验") >> sec

        # I/O 路径
        io >> Edge(label="页缓存协同") >> page_cache
        vfs >> Edge(label="读写缓存") >> page_cache
        vfs >> Edge(label="挂载/读写") >> fs_impl
        io >> Edge(label="驱动调用") >> drivers
        net >> Edge(label="驱动调用") >> nic
        tty >> Edge(label="字符 I/O") >> io

        # 存储路径
        fs_impl >> Edge(label="块设备 I/O") >> disk
        mm >> Edge(label="换出/换入") >> swap

        # 事件环
        epoll_kqueue >> Edge(label="事件触发") >> user_procs

        # 中断
        apic >> Edge(label="中断分发") >> scheduler
        timer >> Edge(label="调度时钟/定时") >> scheduler

        # 容器与安全/隔离
        ns >> Edge(label="隔离") >> scheduler
        cgroup >> Edge(label="资源限额") >> scheduler
        selinux >> Edge(label="策略执行") >> sec

        # eBPF 观测/网络/安全挂载
        ebpf_loader >> Edge(label="加载/附加") >> ebpf_prog
        ebpf_prog >> Edge(label="kprobe/tracepoint") >> scheduler
        ebpf_prog >> Edge(label="tc/XDP") >> net
        ebpf_prog >> Edge(label="LSM hook") >> sec

        # 返回用户空间
        libc >> Edge(label="返回值") >> user_procs


if __name__ == "__main__":
    create_os_design_diagram(filename="os_design", outformat="png")
    create_os_design_diagram(filename="os_design", outformat="pdf")
