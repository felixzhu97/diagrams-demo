PY=python3

.PHONY: all data os k8s imsdk imsdk-mobile imsdk-desktop imsdk-web imsdk-rtc bigdata datamining clean

all: data os k8s imsdk imsdk-mobile imsdk-desktop imsdk-web imsdk-rtc bigdata datamining

# 生成数据密集型系统图（PNG/PDF）
data:
	$(PY) diagram.py

# 生成操作系统设计图（PNG/PDF）
os:
	$(PY) os_diagram.py

# 生成 Kubernetes 子系统图（PNG/PDF）
k8s:
	$(PY) k8s_diagram.py

# 生成 IM SDK 设计图（PNG/PDF）
imsdk:
	$(PY) im_sdk_diagram.py

# 生成 IM SDK（移动端）
imsdk-mobile:
	$(PY) im_sdk_mobile_diagram.py

# 生成 IM SDK（桌面端）
imsdk-desktop:
	$(PY) im_sdk_desktop_diagram.py

# 生成 IM SDK（Web）
imsdk-web:
	$(PY) im_sdk_web_diagram.py

# 生成 IM 实时音视频（RTC）
imsdk-rtc:
	$(PY) im_sdk_rtc_diagram.py

# 生成 大数据系统图
bigdata:
	$(PY) big_data_diagram.py

# 生成 数据挖掘系统图
datamining:
	$(PY) data_mining_diagram.py

# 清理输出文件
clean:
	rm -f data_intensive_system.png data_intensive_system.pdf \
	      os_design.png os_design.pdf \
	      k8s_design.png k8s_design.pdf \
	      im_sdk_design.png im_sdk_design.pdf \
	      im_sdk_mobile.png im_sdk_mobile.pdf \
	      im_sdk_desktop.png im_sdk_desktop.pdf \
	      im_sdk_web.png im_sdk_web.pdf \
	      im_sdk_rtc.png im_sdk_rtc.pdf \
	      big_data_design.png big_data_design.pdf \
	      data_mining_design.png data_mining_design.pdf
