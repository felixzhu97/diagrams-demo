from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_blockchain_system_diagram(filename: str, outformat: str) -> None:
    with Diagram("区块链系统设计图（Blockchain Ecosystem）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("应用层（Application Layer）"):
            dapp_frontend = Server("DApp 前端")
            mobile_wallet = Server("移动钱包")
            web_wallet = Server("Web 钱包")
            desktop_wallet = Server("桌面钱包")
            browser_extension = Server("浏览器扩展")
            api_client = Server("API 客户端")
            dapp_frontend >> api_client
            mobile_wallet >> api_client
            web_wallet >> api_client
            desktop_wallet >> api_client
            browser_extension >> api_client

        with Cluster("智能合约层（Smart Contract Layer）"):
            solidity_contracts = Server("Solidity 合约")
            rust_contracts = Server("Rust 合约")
            go_contracts = Server("Go 合约")
            wasm_contracts = Server("WASM 合约")
            contract_compiler = Server("合约编译器")
            contract_verifier = Server("合约验证器")
            solidity_contracts >> contract_compiler
            rust_contracts >> contract_compiler
            go_contracts >> contract_compiler
            wasm_contracts >> contract_compiler
            contract_compiler >> contract_verifier

        with Cluster("虚拟机层（Virtual Machine Layer）"):
            evm = Server("EVM 虚拟机")
            wasm_vm = Server("WASM 虚拟机")
            move_vm = Server("Move 虚拟机")
            interpreter = Server("解释器")
            gas_meter = Server("Gas 计量器")
            execution_engine = Server("执行引擎")
            evm >> interpreter
            wasm_vm >> interpreter
            move_vm >> interpreter
            interpreter >> gas_meter
            gas_meter >> execution_engine

        with Cluster("共识层（Consensus Layer）"):
            proof_of_work = Server("工作量证明 (PoW)")
            proof_of_stake = Server("权益证明 (PoS)")
            delegated_pos = Server("委托权益证明 (DPoS)")
            proof_of_authority = Server("权威证明 (PoA)")
            byzantine_fault = Server("拜占庭容错 (BFT)")
            consensus_engine = Server("共识引擎")
            proof_of_work >> consensus_engine
            proof_of_stake >> consensus_engine
            delegated_pos >> consensus_engine
            proof_of_authority >> consensus_engine
            byzantine_fault >> consensus_engine

        with Cluster("网络层（Network Layer）"):
            peer_discovery = Server("节点发现")
            gossip_protocol = Server("Gossip 协议")
            message_routing = Server("消息路由")
            network_transport = Server("网络传输")
            p2p_protocol = Server("P2P 协议")
            sync_mechanism = Server("同步机制")
            peer_discovery >> gossip_protocol
            gossip_protocol >> message_routing
            message_routing >> network_transport
            network_transport >> p2p_protocol
            p2p_protocol >> sync_mechanism

        with Cluster("数据层（Data Layer）"):
            merkle_tree = Server("Merkle 树")
            block_storage = Server("区块存储")
            state_trie = Server("状态树")
            transaction_pool = Server("交易池")
            utxo_set = Server("UTXO 集合")
            account_model = Server("账户模型")
            merkle_tree >> block_storage
            block_storage >> state_trie
            state_trie >> transaction_pool
            transaction_pool >> utxo_set
            utxo_set >> account_model

        with Cluster("加密层（Cryptography Layer）"):
            hash_functions = Server("哈希函数")
            digital_signatures = Server("数字签名")
            public_key_crypto = Server("公钥密码学")
            zero_knowledge = Server("零知识证明")
            multi_sig = Server("多重签名")
            threshold_crypto = Server("门限密码学")
            hash_functions >> digital_signatures
            digital_signatures >> public_key_crypto
            public_key_crypto >> zero_knowledge
            zero_knowledge >> multi_sig
            multi_sig >> threshold_crypto

        with Cluster("存储层（Storage Layer）"):
            ipfs_storage = Server("IPFS 存储")
            distributed_storage = Server("分布式存储")
            local_storage = Server("本地存储")
            cold_storage = Server("冷存储")
            hot_storage = Server("热存储")
            backup_storage = Server("备份存储")
            ipfs_storage >> distributed_storage
            distributed_storage >> local_storage
            local_storage >> cold_storage
            cold_storage >> hot_storage
            hot_storage >> backup_storage

        with Cluster("跨链层（Cross-Chain Layer）"):
            bridge_protocol = Server("跨链桥协议")
            atomic_swaps = Server("原子交换")
            sidechains = Server("侧链")
            parachains = Server("平行链")
            relay_chain = Server("中继链")
            interop_protocol = Server("互操作协议")
            bridge_protocol >> atomic_swaps
            atomic_swaps >> sidechains
            sidechains >> parachains
            parachains >> relay_chain
            relay_chain >> interop_protocol

        with Cluster("治理层（Governance Layer）"):
            dao_governance = Server("DAO 治理")
            token_voting = Server("代币投票")
            proposal_system = Server("提案系统")
            treasury_management = Server("资金管理")
            upgrade_mechanism = Server("升级机制")
            parameter_adjustment = Server("参数调整")
            dao_governance >> token_voting
            token_voting >> proposal_system
            proposal_system >> treasury_management
            treasury_management >> upgrade_mechanism
            upgrade_mechanism >> parameter_adjustment

        with Cluster("DeFi 层（DeFi Layer）"):
            dex_protocols = Server("去中心化交易所")
            lending_protocols = Server("借贷协议")
            yield_farming = Server("流动性挖矿")
            synthetic_assets = Server("合成资产")
            insurance_protocols = Server("保险协议")
            derivatives = Server("衍生品")
            dex_protocols >> lending_protocols
            lending_protocols >> yield_farming
            yield_farming >> synthetic_assets
            synthetic_assets >> insurance_protocols
            insurance_protocols >> derivatives

        with Cluster("NFT 层（NFT Layer）"):
            nft_marketplace = Server("NFT 市场")
            nft_standards = Server("NFT 标准")
            metadata_storage = Server("元数据存储")
            royalty_system = Server("版税系统")
            nft_gaming = Server("NFT 游戏")
            digital_collectibles = Server("数字收藏品")
            nft_marketplace >> nft_standards
            nft_standards >> metadata_storage
            metadata_storage >> royalty_system
            royalty_system >> nft_gaming
            nft_gaming >> digital_collectibles

        with Cluster("基础设施层（Infrastructure Layer）"):
            node_software = Server("节点软件")
            mining_software = Server("挖矿软件")
            validator_software = Server("验证器软件")
            rpc_services = Server("RPC 服务")
            indexer_services = Server("索引服务")
            monitoring_tools = Server("监控工具")
            node_software >> mining_software
            mining_software >> validator_software
            validator_software >> rpc_services
            rpc_services >> indexer_services
            indexer_services >> monitoring_tools

        with Cluster("安全层（Security Layer）"):
            formal_verification = Server("形式化验证")
            security_auditing = Server("安全审计")
            bug_bounty = Server("漏洞赏金")
            multi_sig_wallets = Server("多重签名钱包")
            hardware_security = Server("硬件安全模块")
            key_management = Server("密钥管理")
            formal_verification >> security_auditing
            security_auditing >> bug_bounty
            bug_bounty >> multi_sig_wallets
            multi_sig_wallets >> hardware_security
            hardware_security >> key_management

        # 关键数据流连接
        api_client >> Edge(label="交易请求") >> solidity_contracts
        solidity_contracts >> Edge(label="合约执行") >> evm
        evm >> Edge(label="执行结果") >> consensus_engine
        consensus_engine >> Edge(label="共识达成") >> block_storage
        block_storage >> Edge(label="区块数据") >> merkle_tree

        # 应用层到智能合约层
        dapp_frontend >> Edge(label="DApp 调用") >> solidity_contracts
        mobile_wallet >> Edge(label="钱包交易") >> rust_contracts
        web_wallet >> Edge(label="Web 交易") >> go_contracts
        desktop_wallet >> Edge(label="桌面交易") >> wasm_contracts

        # 智能合约到虚拟机
        solidity_contracts >> Edge(label="编译后字节码") >> evm
        rust_contracts >> Edge(label="编译后字节码") >> wasm_vm
        go_contracts >> Edge(label="编译后字节码") >> move_vm
        wasm_contracts >> Edge(label="WASM 字节码") >> wasm_vm

        # 虚拟机到共识
        execution_engine >> Edge(label="执行结果") >> proof_of_stake
        gas_meter >> Edge(label="Gas 消耗") >> consensus_engine
        interpreter >> Edge(label="执行状态") >> byzantine_fault

        # 共识到网络
        consensus_engine >> Edge(label="共识消息") >> gossip_protocol
        proof_of_work >> Edge(label="挖矿结果") >> peer_discovery
        delegated_pos >> Edge(label="验证结果") >> message_routing

        # 网络到数据
        sync_mechanism >> Edge(label="同步数据") >> block_storage
        p2p_protocol >> Edge(label="P2P 数据") >> transaction_pool
        network_transport >> Edge(label="网络数据") >> state_trie

        # 数据到加密
        merkle_tree >> Edge(label="哈希验证") >> hash_functions
        digital_signatures >> Edge(label="签名验证") >> public_key_crypto
        zero_knowledge >> Edge(label="隐私保护") >> multi_sig

        # 存储链路
        block_storage >> Edge(label="区块数据") >> ipfs_storage
        state_trie >> Edge(label="状态数据") >> distributed_storage
        transaction_pool >> Edge(label="交易数据") >> local_storage

        # 跨链链路
        bridge_protocol >> Edge(label="跨链交易") >> atomic_swaps
        sidechains >> Edge(label="侧链数据") >> parachains
        relay_chain >> Edge(label="中继数据") >> interop_protocol

        # 治理链路
        dao_governance >> Edge(label="治理决策") >> token_voting
        proposal_system >> Edge(label="提案执行") >> upgrade_mechanism
        treasury_management >> Edge(label="资金分配") >> parameter_adjustment

        # DeFi 链路
        dex_protocols >> Edge(label="交易执行") >> lending_protocols
        yield_farming >> Edge(label="收益分配") >> synthetic_assets
        insurance_protocols >> Edge(label="风险对冲") >> derivatives

        # NFT 链路
        nft_marketplace >> Edge(label="NFT 交易") >> nft_standards
        metadata_storage >> Edge(label="元数据管理") >> royalty_system
        nft_gaming >> Edge(label="游戏资产") >> digital_collectibles

        # 基础设施链路
        node_software >> Edge(label="节点运行") >> mining_software
        validator_software >> Edge(label="验证服务") >> rpc_services
        indexer_services >> Edge(label="索引数据") >> monitoring_tools

        # 安全链路
        formal_verification >> Edge(label="验证结果") >> security_auditing
        bug_bounty >> Edge(label="安全修复") >> multi_sig_wallets
        hardware_security >> Edge(label="硬件保护") >> key_management

        # 反馈控制链路
        monitoring_tools >> Edge(label="监控数据") >> dao_governance
        security_auditing >> Edge(label="安全报告") >> dao_governance
        key_management >> Edge(label="密钥更新") >> mobile_wallet


if __name__ == "__main__":
    create_blockchain_system_diagram(filename="blockchain_system_design", outformat="png")
    create_blockchain_system_diagram(filename="blockchain_system_design", outformat="pdf")
