from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server


def create_im_sdk_rtc(filename: str, outformat: str) -> None:
    with Diagram("IM 实时音视频（RTC）", filename=filename, show=False, outformat=outformat, direction="LR"):
        with Cluster("应用与 SDK"):
            app_ui = Server("Call UI")
            sdk_api = Server("RTC API")
            event_bus = Server("RTC Events")
            app_ui >> Edge(label="拨打/接听") >> sdk_api >> Edge(label="事件") >> event_bus

        with Cluster("信令与会控"):
            signaling = Server("信令/会控")
            sdp = Server("SDP 协商")
            ice = Server("ICE/候选")
            signaling >> sdp >> ice

        with Cluster("媒体引擎"):
            capture = Server("采集（音频/视频）")
            codecs = Server("编解码（Opus/H.264/H.265/AV1）")
            agc_aec_ans = Server("AGC/AEC/ANS")
            jitter = Server("抖动缓冲")
            fec_nack = Server("FEC/NACK")
            bandwidth = Server("带宽估计/自适应码率")
            capture >> codecs
            codecs >> agc_aec_ans
            agc_aec_ans >> jitter
            jitter >> fec_nack
            fec_nack >> bandwidth

        with Cluster("NAT 穿透"):
            stun = Server("STUN")
            turn = Server("TURN")
            ice >> stun
            ice >> turn

        with Cluster("传输与加密"):
            srtp = Server("SRTP/SRTCP")
            dtls = Server("DTLS")
            rtp = Server("RTP/RTCP")
            dtls >> srtp >> rtp

        with Cluster("服务端（抽象）"):
            sig_srv = Server("信令服务")
            media_srv = Server("媒体中继（SFU/MCU）")
            rec_srv = Server("录制/旁路直播")
            qos_srv = Server("QoS/监控")

        # flows
        sdk_api >> Edge(label="注册/加入会话") >> signaling
        signaling >> Edge(label="下发策略") >> sig_srv
        sdp >> Edge(label="Offer/Answer") >> sig_srv
        ice >> Edge(label="候选收集/打洞") >> sig_srv

        dtls >> Edge(label="握手/密钥") >> srtp
        rtp >> Edge(label="媒体流") >> media_srv
        stun >> Edge(label="探测") >> media_srv
        turn >> Edge(label="中继") >> media_srv

        bandwidth >> Edge(label="码率调节") >> codecs
        fec_nack >> Edge(label="重传/纠错") >> rtp
        jitter >> Edge(label="时序平滑") >> rtp

        media_srv >> Edge(label="统计/监控") >> qos_srv
        qos_srv >> Edge(label="回传指标") >> event_bus
        media_srv >> Edge(label="录制/转推") >> rec_srv


if __name__ == "__main__":
    create_im_sdk_rtc(filename="im_sdk_rtc", outformat="png")
    create_im_sdk_rtc(filename="im_sdk_rtc", outformat="pdf")
