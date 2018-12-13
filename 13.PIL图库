##PIL库在Python3中可以使用pillow库来替代。


##读取图片
from PIL import Image
##读取图片文件
pil_im = Image.open(r"F:\Python练习\BigData\zhouzhou.jpg")
##读取图片并将它转化为灰度图
pil_im = Image.open(r"F:\Python练习\BigData\zhouzhou.jpg").convert("L")
pil_im


##创建缩略图
# 创建最长边为128像素的缩略图
pil_im.thumbnail((128, 128))
pil_im


##复制和粘贴图像区域
# 使用crop()方法可以从一副图像中裁剪指定的区域
from PIL import Image
pil_im = Image.open(r"F:\Python练习\BigData\zhouzhou.jpg")
box = (150, 350, 400, 600)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_90)
pil_im.paste(region, box)
pil_im.show()


##调整尺寸和旋转
# 要调整一副图像的大小，可以调用resize()方法，该方法的参数为一个元组，用来指定新图像的大小。
# 使用rotate()方法旋转图像，该方法的数值参数表示逆时针旋转角度。
##读取图片文件
pil_im = Image.open(r"F:\Python练习\BigData\zhouzhou.jpg")
# 调整大小
out = pil_im.resize((128, 128))
out
# 旋转图像
out = out.rotate(45)
out


##图像轮廓和直方图
import numpy as np
import matplotlib.pyplot as plt
im = np.array(Image.open(r"F:\Python练习\BigData\zhouzhou.jpg").convert("L"))
print("图片大小", im.shape)
##图像轮廓
plt.figure()
##不使用颜色信息
plt.gray()
##在原点的左上角显示图像轮廓
plt.contour(im, origin = "image")
plt.axis("equal")               # 设置坐标轴位正方形
                                # plt.axis("off")
plt.show()
##直方图
plt.hist(im.flatten(), 128)
plt.show()
