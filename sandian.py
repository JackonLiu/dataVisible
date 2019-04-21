##起泡图（散点图）
import matplotlib.pyplot as plt
import pandas as pd

##导入数据
df_data = pd.read_csv('https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv')
df_data.head()

##作图
fig, ax = plt.subplots()
# 设置气泡图颜色
colors = ["#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021",
          '#FFF16E', '#0D8ECF', '#FA4D3D', '#D2D2D2', '#FFDE45', '#9b59b6']

# 创建气泡图SepalLength为x, SepaWidth为y, 同时设置PetalLength为气泡大小，并设置颜色透明度等
ax.scatter(df_data['SepalLength'], df_data['SepalWidth'],
           s=df_data['PetalLength'], alpha=0.6)
# 第三个变量声明根据[PeralLength] * 100数据显示气泡大小

ax.set_xlabel('SepalLength(cm)')
ax.set_ylabel('SepalWidth(cm)')
ax.set_title('PetalLength(cm) * 100')

# 显示网格
ax.grid(True)
fig.tight_layout()
plt.show()
