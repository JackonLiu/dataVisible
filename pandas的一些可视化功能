# 获取鸢尾花数据，后面在运行代码时，都要先运行这段代码，以获取数据df
from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()    # 载入数据
iris.data             # 查看数据
iris                  # 查看数据的详细记录信息
# 把数据转化为Data Frame
from pandas import DataFrame
df = DataFrame(iris.data, columns = iris.feature_names)
df['target'] = iris.target      # 把分类也加上
#print(df)

# 数据可视化
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
## 在Jupyter中显示图像
%matplotlib inline
## 在视网膜屏幕上显示高清图片
%config InlineBackend.figure_format = "retina"
import seaborn as sns
sns.set(color_codes = True)

## 用pandas绘制，箱线图
df.boxplot(by = "target", figsize = (12, 6))
plt.show()
print("箱线图")

##时间序列图也叫折线图，是以时间轴为横轴，变量为纵轴的一种图。
# pandas绘制折线图
ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
ts = ts.cumsum()
ts.plot()
plt.show()
##多条折线图
df0 = pd.DataFrame(np.random.randn(1000, 4), index = ts.index, columns = list('ABCD'))
df0 = df0.cumsum()
print("数据的前几行：\n", df0.head())
plt.figure()
df0.plot()
plt.show()
print("折线图")


##在数据可视化中，安德鲁曲线是一种可视化高维数据结构的方法，可以看作平滑版本的平行坐标图。
##平行坐标图是一种常用的可视化方法，一般用于对高维几何和多元数据的平行可视化。
from pandas.tools.plotting import andrews_curves
from pandas.tools.plotting import parallel_coordinates

# andrews curves(安德鲁曲线)
plt.figure(figsize = (6, 4))
andrews_curves(df, "target")
plt.title("andrews curves")
plt.show()
print("安德鲁曲线")

# parallel coordinates(平行坐标图)
plt.figure(figsize = (6, 4))
parallel_coordinates(df, "target")
plt.title("parallel coordinates")
plt.show()
print("平行坐标图")


##弹簧张力高维数据图是基于一个简单的弹簧张力最小化算法。
# 弹簧张力高维数据图
from pandas.tools.plotting import radviz
plt.figure(figsize = (8, 6))
radviz(df, "target")
plt.show()
print("弹簧张力高维数据图")
