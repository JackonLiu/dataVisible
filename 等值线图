#marplotlib 绘制三维图像
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##生成数据
delta = 0.2
x = np.arange(-3, 3, delta)
y = np.arange(-3, 3, delta)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2
x = X.flatten()    # 返回一维的数组，但是该函数只能适用于numpy对象（array或者mat）
y = Y.flatten()
z = Z.flatten()

fig = plt.figure(figsize = (12, 6))
ax1 = fig.add_subplot(121, projection = '3d')
ax1.plot_trisurf(x, y, z, cmap = cm.jet, linewidth = 0.01)  #cmap指颜色，默认绘制为RGB（A）颜色空间， jet表示“蓝-青-黄-红”颜色
plt.title("3D")

ax2 = fig.add_subplot(122)
cs = ax2.contour(X, Y, Z, 15, cmap = 'jet', )    #注意这里是大写X,Y,Z。 15代表的是显示等高线的密集程度，数值越大，面的等高线数就越多
ax2.clabel(cs, inline = True, fontsize = 10, fmt = '%1.1f')
plt.show()
