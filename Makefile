PY=python3

.PHONY: all data os clean

all: data os

# 生成数据密集型系统图（PNG/PDF）
data:
	$(PY) diagram.py

# 生成操作系统设计图（PNG/PDF）
os:
	$(PY) os_diagram.py

# 清理输出文件
clean:
	rm -f data_intensive_system.png data_intensive_system.pdf \
	      os_design.png os_design.pdf
