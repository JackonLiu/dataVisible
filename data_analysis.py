import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_data = pd.read_csv('chengji.csv')  # 读取训练数据
print(csv_data.shape)  # (189, 9)
N = 50
csv_batch_data = csv_data.tail(N)  # 取后5条数据
print(csv_batch_data)  # (5, 9)
## 条形图
## 平均分和标准差
means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4 ,1, 2)

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)
##条形图
fig, ax = plt.subplots()
##生成0, 1, 2, 3, ...
index = np.arange(5)
bar_width = 0.35 ## 条的宽度
className = csv_batch_data['mes_sub_name']
print(className)
mes_StudentID = csv_batch_data['mes_StudentID']
opacity = 0.4
error_config = {'ecolor': '0.3'}
mes_T_Score = csv_batch_data['mes_T_Score']
print(mes_T_Score)
school=csv_batch_data['育才中学' == csv_batch_data['mes_sub_name']].head()
print(school)
## 条形图的第一类条
rects1 = plt.bar(index, mes_T_Score, bar_width,
                alpha = opacity,
                color = 'b',
                yerr = std_men,
                error_kw = error_config,
                label = 'score')
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))

plt.legend()    # 显示标注
## 自动调整subplot的参数给指定的填充区
plt.tight_layout()
plt.show()
