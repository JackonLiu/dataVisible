##subplot()绘制多个子图
import numpy as np
import matplotlib.pyplot as plt

##生成X
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

##生成Y
y1 = np.cos(2 * np.pi * x1) * np.exp(x1)
y2 = np.cos(2 * np.pi * x2)

##绘制第一个子图
plt.subplot(4, 1, 1)
plt.plot(x1, y1, 'r.-')
plt.title('A table of 2 subplots')
plt.ylabel('Damped oscillation')

##绘制第二个子图
plt.subplot(4, 2, 4)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()
