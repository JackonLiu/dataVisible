##OpenCV是一个C++库，用于实时处理计算机视觉问题，即实时处理计算机视觉的C++库。
##首先要安装OpenCV，打开Anaconda目录下的Anaconda Prompt，并输出conda install opencv

import cv2
##读取图像,注意路径上不能有中文
im = cv2.imread(r"F:\PythonTest\BigData\zhouzhou.jpg")
print(im.shape)
##保存图像,注意路径上不能有中文
cv2.imwrite(r"F:\PythonTest\BigData\zhouzhou1.png", im)


##颜色空间
##在OpenCV中，图像不是按传统的RGB颜色通道，而是按BGR顺序（即RGB的倒序）存储的。
##创建灰度图像
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(gray)
print(gray.shape)



##图像实现
##可是使用matpltlib来显示OpenCV中的图像
import matplotlib.pyplot as plt
import cv2
##读取图像
im = cv2.imread(r"F:\PythonTest\BigData\zhouzhou.jpg")
##创建灰度图像
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
##计算图像的积分
intim = cv2.integral(gray)
##归一化并保存
intim = (255 * intim) / intim.max()
plt.figure(figsize = (12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray)
plt.title("YTZ picture")
plt.subplot(1, 2, 2)
plt.imshow(intim)
plt.title("YTZ integral")
plt.show()
