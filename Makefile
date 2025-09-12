PY=python3

.PHONY: all data os k8s clean

all: data os k8s

# 生成数据密集型系统图（PNG/PDF）
data:
	$(PY) diagram.py

# 生成操作系统设计图（PNG/PDF）
os:
	$(PY) os_diagram.py

# 生成 Kubernetes 子系统图（PNG/PDF）
k8s:
	$(PY) k8s_diagram.py

# 清理输出文件
clean:
	rm -f data_intensive_system.png data_intensive_system.pdf \
	      os_design.png os_design.pdf \
	      k8s_design.png k8s_design.pdf
