##饼图
import matplotlib.pyplot as plt

## 切片将按顺时针方向排列并绘制
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'   ##标注
sizes = [15, 30, 45, 10]                   ##大小
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
                                           ##颜色
##0.1代表第二个块从圆中分离出来
explode = (0, 0.1, 0, 0)     #only "explode" the 2nd slice (i.e. 'Hogs')
##绘制饼图
plt.pie(sizes, explode = explode, labels = labels, colors = colors,
       autopct = '%1.1f%%', shadow = True, startangle = 90)

plt.axis('equal')
plt.show()
