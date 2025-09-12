from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_er_diagram(filename: str, outformat: str) -> None:
    with Diagram("IM 系统 ER 图", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("用户与设备"):
            user = Server("User{id, phone, email, profile}")
            device = Server("Device{id, user_id, type, token}")
            session = Server("Session{id, user_id, device_id, status}")
            user >> Edge(label="1..n") >> device
            user >> Edge(label="1..n") >> session

        with Cluster("联系人与关系"):
            contact = Server("Contact{id, owner_id, peer_id, alias}")
            block = Server("Blocklist{id, owner_id, peer_id}")
            user >> Edge(label="1..n owns") >> contact
            user >> Edge(label="1..n blocks") >> block

        with Cluster("会话/群组"):
            conv = Server("Conversation{id, type, title}")
            member = Server("ConversationMember{conv_id, user_id, role}")
            group = Server("Group{id, owner_id, name}")
            group_attr = Server("GroupAttr{group_id, k, v}")
            conv >> Edge(label="1..n") >> member
            group >> Edge(label="1..n attrs") >> group_attr
            conv >> Edge(label="optional link") >> group

        with Cluster("消息与回执"):
            message = Server("Message{id, conv_id, sender_id, seq, ts}")
            message_body = Server("MessageBody{msg_id, mime, content}")
            receipt = Server("Receipt{msg_id, user_id, status, ts}")
            unread = Server("Unread{conv_id, user_id, count}")
            message >> Edge(label="1..1") >> message_body
            message >> Edge(label="1..n read/recv") >> receipt
            conv >> Edge(label="1..n has") >> message
            conv >> Edge(label="n..n track") >> unread

        with Cluster("媒体与存储"):
            media = Server("Media{id, owner_id, url, hash, size}")
            message >> Edge(label="0..1 attach") >> media
            user >> Edge(label="1..n owns") >> media

        with Cluster("权限与组织（可选）"):
            role = Server("Role{id, name}")
            user_role = Server("UserRole{user_id, role_id}")
            org = Server("Org{id, name}")
            org_user = Server("OrgUser{org_id, user_id}")
            role >> Edge(label="n..n") >> user_role
            user >> Edge(label="n..n") >> user_role
            org >> Edge(label="n..n") >> org_user
            user >> Edge(label="n..n") >> org_user

        # Cross-entity links
        member >> Edge(label="n..1 user") >> user
        member >> Edge(label="n..1 conv") >> conv
        receipt >> Edge(label="n..1 user") >> user
        unread >> Edge(label="n..1 user") >> user


if __name__ == "__main__":
    create_im_er_diagram(filename="im_er_design", outformat="png")
    create_im_er_diagram(filename="im_er_design", outformat="pdf")
