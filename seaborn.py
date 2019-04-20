##具体详细内容可以参阅知乎上“Seaborn（sns）官方文档学习笔记”（https://zhuanlan.zhihu.com/p/27435863）
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
import seaborn as sns
sns.set(color_codes = True)
# 数据分布可视化，直方图和密度函数
## distplot()函数默认绘出数据的直方图和核密度估计
sns.distplot(df["petal length (cm)"], bins = 15)
plt.show()
print("直方图与核密度估计图")

# 使用seaborn的jointplot()函数同时绘制散点图和直方图
sns.jointplot(x = "sepal length (cm)", y = "sepal width (cm)", data = df, size = 8)
plt.show()
print("散点图与直方图")

## 分组散点图
# 用seaborn's FaceGrid 标记不同的种类
sns.FacetGrid(df, hue = 'target', size = 8).map(plt.scatter,
                "sepal length (cm)", "sepal width (cm)").add_legend()
plt.show()
print("分组散点图")

## 六边形
sns.axes_style("white")
sns.jointplot(x = "sepal length (cm)", y = "petal length (cm)",
             data = df, kind = "hex", color = "k")
plt.show()
print("六边形图")

## 二维核密度估计图
g = sns.jointplot(x = "sepal length (cm)", y = "petal length (cm)",
                data = df, kind = "kde", color = "m")
## 添加散点图
g.plot_joint(plt.scatter, c = "w", s = 30, linewidth = 1, marker = "+")
g.ax_joint.collections[0].set_alpha(0)
plt.show()
print("二维核密度估计图")

## 矩阵散点图
g = sns.PairGrid(df)
g.map(plt.scatter)
plt.show()
print("矩阵散点图")

##在对角线上绘制不同的函数，以显示每列中变量的单变量分布。
g = sns.PairGrid(df)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.show()
print("矩阵散点图")

##通过单独的分类变量来绘制观察值。（矩阵散点图——分类变量绘制）
g = sns.PairGrid(df, hue = "target")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()
plt.show()
print("矩阵散点图——分类变量绘制")

##默认情况下，会使用数据集中的每个数字列，但如果需要，可以专注于特定的关系。（矩阵散点图——特定关系绘制）
g = sns.PairGrid(df, vars = ["sepal length (cm)", "sepal width (cm)"], hue = "target")
g.map(plt.scatter)
plt.show()
print("矩阵散点图——特定关系绘制")

##使用上下三角形中使用不同的功能来强调关系的不同方面(矩阵散点图——多功能绘制)
g = sns.PairGrid(df)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot, cmap = "Blues_d")
g.map_diag(sns.kdeplot, lw = 3, legend = False)
plt.show()
print("矩阵散点图——多功能绘制")

##PairGrid是灵活的，但是要快速查看一个数据集，使用pairplot()会更容易。
##默认情况下，该功能使用散点图和直方图。但是还可以添加其他几种（如绘制对角线上的KEDs的回归图）
##矩阵散点图——对角线直方图
sns.pairplot(df, hue = "target", size = 2.5)
plt.show()
print("矩阵散点图——对角线直方图")

##使用关键字参数控制显示细节，并返回PairGrid实例进行进一步的调整。
g = sns.pairplot(df, hue = "target", palette = "Set2", diag_kind = "kde", size = 2.5)
plt.show()
print("矩阵散点图——关键字控制")


##线性相关图
sns.lmplot(x = "sepal length (cm)", y = "petal length (cm)", data = df, hue = "target")
plt.show()
print("线性相关图")


##分类数据可视化
#小提琴图（盒型图的变化）
#小提琴图是“箱线图”于“核密度图”的结合，箱线图展示了分位数的位置，
#小提琴图则展示了任意位置的密度，通过小提琴图可以知道哪些位置的密度较高。
sns.violinplot(x = "target", y = "sepal length (cm)", data = df, inner = None)
#散点图
sns.swarmplot(x = "target", y = "sepal length (cm)", data = df, color = "w", alpha = 0.5)
plt.show()
print("小提琴图")


##盒型图
plt.figure(figsize = (8, 6))
sns.boxplot(x = "target", y = "sepal width (cm)", data = df)
plt.title("Boxplot")
plt.show()
print("盒型图")


##热力图
#相关系数大小的可视化
import numpy as np
newdata = df
datacor = np.corrcoef(newdata, rowvar = 0)
datacor = pd.DataFrame(data = datacor, columns = newdata.columns, index = newdata.columns)
#形式1
mask = np.zeros_like(datacor)
mask[np.triu_indices_from(mask)] = True
plt.figure(figsize = (8, 8))
with sns.axes_style("white"):
    ax = sns.heatmap(datacor, mask = mask, square = True, annot = True)
ax.set_title("Iris data Variables Relation")
plt.show()
##形式2
plt.figure(figsize = (8, 8))
with sns.axes_style("white"):
    ax = sns.heatmap(datacor, square = True, annot = True, fmt = "f")
ax.set_title("Iris data Variables Relation")
plt.show()
print("热力图")
