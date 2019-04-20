import matplotlib.pyplot as plt
import numpy as np

# 设置字体
from matplotlib.font_manager import FontProperties
font = FontProperties(fname = "C:/Windows/Fonts/simsun.ttc", size = 14)


# 绘制一个圆形散点图的示例
t = np.arange(1, 10, 0.05)
x = np.sin(t)
y = np.cos(t)
##定义一个图像窗口
plt.figure(figsize = (8, 5))
##绘制一条线
plt.plot(x, y, "r-*")
##使坐标轴相等
plt.axis("equal")
plt.xlabel("正弦", fontproperties = font)
plt.ylabel("余弦", fontproperties = font)
plt.title("一个圆形", fontproperties = font)

##显示图像
plt.show()
