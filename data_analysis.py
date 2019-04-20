import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_data = pd.read_csv('5_chengji.csv')  # 读取训练数据
print(csv_data.shape)  # (189, 9)
N = 50
csv_batch_data = csv_data.tail(N)  # 取后5条数据
print(csv_batch_data.shape)  # (5, 9)
# train_batch_data = csv_batch_data[list(range(3, 6))]  # 取这20条数据的3到5列值(索引从0开始)
# print(train_batch_data)
## 条形图
## 平均分和标准差
means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4 ,1, 2)

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)
##条形图
fig, ax = plt.subplots()
##生成0, 1, 2, 3, ...
# index = np.arange(csv_batch_data)
bar_width = 0.35 ## 条的宽度
csv_batch_data[csv_batch_data["mes_sub_name"] =='育才中学'].head()
opacity = 0.4

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
# plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
plt.legend()    # 显示标注
## 自动调整subplot的参数给指定的填充区
plt.tight_layout()
plt.show()
