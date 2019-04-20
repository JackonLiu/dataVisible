import matplotlib.pyplot as plt
import numpy as np

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
plt.xlabel("正弦")
plt.ylabel("余弦")
plt.title("一个圆形")

##显示图像
plt.show()
