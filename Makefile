.PHONY: all system-designs company-tech-stacks commercial-algorithms financial-quantitative-algorithms clean clean-system-designs clean-company-tech-stacks clean-commercial-algorithms clean-financial-quantitative-algorithms

# 生成所有图表
all: system-designs company-tech-stacks commercial-algorithms financial-quantitative-algorithms

# 生成系统架构设计图表
system-designs:
	cd system-designs && $(MAKE) all

# 生成知名公司技术栈图表
company-tech-stacks:
	cd company-tech-stacks && $(MAKE) all

# 生成商业算法图表
commercial-algorithms:
	cd commercial-algorithms && $(MAKE) all

# 生成金融量化算法图表
financial-quantitative-algorithms:
	cd financial-quantitative-algorithms && $(MAKE) all

# 清理所有输出文件
clean: clean-system-designs clean-company-tech-stacks clean-commercial-algorithms clean-financial-quantitative-algorithms

# 清理系统架构设计输出文件
clean-system-designs:
	cd system-designs && $(MAKE) clean

# 清理公司技术栈输出文件
clean-company-tech-stacks:
	cd company-tech-stacks && $(MAKE) clean

# 清理商业算法输出文件
clean-commercial-algorithms:
	cd commercial-algorithms && $(MAKE) clean

# 清理金融量化算法输出文件
clean-financial-quantitative-algorithms:
	cd financial-quantitative-algorithms && $(MAKE) clean