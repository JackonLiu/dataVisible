# MatplotlibProject
python-数据可视化

使用Anaconda的jepyter Notebook工具即可可视化图像


Python的主要作图库是Matplotlib，而pandas基于Matplotlib并对某些命令进行了简化，
因此作图通常是Matplotlib和pandas相互结合使用。在作图之前通常都要加载以下代码：

    import matplotlib.pyplot as plt                #导入作图库
    plt.rcParams['font.sans-serif'] = ['SimHei']   #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False     #用来正常显示负号
    plt.figure(figsize = (7, 5))                   #创建图像区域，指定比例

做完图后，一般通过plt.show()来显示作图结果。

在Jupyter Notebook中，最好能够把作图代码完整输入，否则可能会出现意想不到的问题。
如果使用Matplotlib绘图，有时是弹不出图像框的，此时别忘了在开头加入“%matplotlib inline”。
