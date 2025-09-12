from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_er_diagram(filename: str, outformat: str) -> None:
    with Diagram("IM 系统 ER 图（含分库分表/索引/审计）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("用户与设备"):
            user = Server("User{id PK, uid SK, phone UQ, email UQ, profile, created_at, updated_at, deleted_at?}")
            device = Server("Device{id PK, user_id FK, type, token UQ, created_at, updated_at, deleted_at?}")
            session = Server("Session{id PK, user_id FK, device_id FK, status, last_seen_idx, created_at, updated_at, deleted_at?}")
            user >> Edge(label="1..n") >> device
            user >> Edge(label="1..n") >> session

        with Cluster("联系人与关系"):
            contact = Server("Contact{id PK, owner_id FK, peer_id FK, alias, created_at, updated_at, deleted_at?} UQ(owner_id,peer_id)")
            block = Server("Blocklist{id PK, owner_id FK, peer_id FK, created_at, deleted_at?} UQ(owner_id,peer_id)")
            user >> Edge(label="1..n owns") >> contact
            user >> Edge(label="1..n blocks") >> block

        with Cluster("会话/群组"):
            conv = Server("Conversation{id PK, type, title, shard_key, created_at, updated_at, deleted_at?}")
            member = Server("ConversationMember{conv_id FK, user_id FK, role, joined_at, deleted_at?} PK(conv_id,user_id)")
            group = Server("Group{id PK, owner_id FK, name, created_at, updated_at, deleted_at?}")
            group_attr = Server("GroupAttr{group_id FK, k, v, updated_at} PK(group_id,k)")
            conv >> Edge(label="1..n") >> member
            group >> Edge(label="1..n attrs") >> group_attr
            conv >> Edge(label="optional link") >> group

        with Cluster("消息与回执"):
            message = Server("Message{id PK, conv_id FK, sender_id FK, seq, ts, shard_key, created_at, deleted_at?} UQ(conv_id,seq)")
            message_body = Server("MessageBody{msg_id PK/FK, mime, content} 1:1 Message")
            receipt = Server("Receipt{msg_id FK, user_id FK, status, ts} PK(msg_id,user_id)")
            unread = Server("Unread{conv_id FK, user_id FK, count, updated_at} PK(conv_id,user_id)")
            message >> Edge(label="1..1") >> message_body
            message >> Edge(label="1..n read/recv") >> receipt
            conv >> Edge(label="1..n has") >> message
            conv >> Edge(label="n..n track") >> unread

        with Cluster("媒体与存储"):
            media = Server("Media{id PK, owner_id FK, url, hash UQ, size, created_at, deleted_at?}")
            message >> Edge(label="0..1 attach") >> media
            user >> Edge(label="1..n owns") >> media

        with Cluster("权限与组织（可选）"):
            role = Server("Role{id PK, name UQ}")
            user_role = Server("UserRole{user_id FK, role_id FK, assigned_at} PK(user_id,role_id)")
            org = Server("Org{id PK, name UQ}")
            org_user = Server("OrgUser{org_id FK, user_id FK, joined_at} PK(org_id,user_id)")
            role >> Edge(label="n..n") >> user_role
            user >> Edge(label="n..n") >> user_role
            org >> Edge(label="n..n") >> org_user
            user >> Edge(label="n..n") >> org_user

        with Cluster("索引与分片建议"):
            idx_conv = Server("IDX: Message(conv_id,seq) UNIQUE")
            idx_time = Server("IDX: Message(conv_id,ts DESC)")
            idx_unread = Server("IDX: Unread(user_id,updated_at)")
            shard = Server("Shard: by conv_id hash / sender_id range")
            idx_conv >> message
            idx_time >> message
            idx_unread >> unread
            shard >> message
            shard >> conv

        # Cross-entity links
        member >> Edge(label="n..1 user") >> user
        member >> Edge(label="n..1 conv") >> conv
        receipt >> Edge(label="n..1 user") >> user
        unread >> Edge(label="n..1 user") >> user


if __name__ == "__main__":
    create_im_er_diagram(filename="im_er_design", outformat="png")
    create_im_er_diagram(filename="im_er_design", outformat="pdf")
