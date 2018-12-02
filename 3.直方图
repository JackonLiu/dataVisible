##直方图
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# example data
mu = 100            #分布的均值
sigma = 15          #分布的标准差
x = mu + sigma * np.random.randn(10000)

##直方图的条数
num_bins = 50
# 绘制直方图
n, bins, patches = plt.hist(x, num_bins, normed = 1, facecolor = 'green', alpha = 0.5)
# 添加一个最佳拟合和曲线
y = mlab.normpdf(bins, mu, sigma)  ##返回关于数据的pdf数值（概率密度函数）

plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')

##在图中添加公式需要使用latex的语法（$ $）
plt.title('Histogram of IQ: $\mu = 100$, $\sigma = 15$')
# 调整图像的间距，防止y轴数值与label重合
plt.subplots_adjust(left = 0.15)
plt.show()
print("bind:\n", bins)
