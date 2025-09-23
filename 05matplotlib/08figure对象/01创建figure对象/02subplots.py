'''
    subplots： 用来创建多个子图
    fig, axs = matplotlib.pyplot.subplots(nrows=1, ncols=1,sharex=False, sharey=False,
    squeeze=True, width_ratios=None,height_ratios=None, subplot_kw=None, gridspec_wk=None,**fig_kw)

    nrows: 子图行数
    ncols：子图的列数
    sharex：布尔值 是否共享x坐标
    sharey：布尔值 是否共享y坐标
    squeeze:布尔值 如果为True 如果只创建一个子图，返回一个子图对象而不是一个只包含一个子图对象的数组
    width_ratios：列宽比例的序列
    height_ratios： 行高比例序列
    subplot_kw：字典值 表示额外的关键字传递给add_subplot调用，可以用来设置子图属性

    gridspec_kw：字典值  以用来设置子图布局
    fig_kw:字典值 以用来设置图形窗口属性

    返回值：
        fig：图形窗口对象
        axs：子图对象（Axes） 数组类型

'''
from matplotlib import pyplot as  plt
import numpy as np

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

xs = np.linspace(0,10,100)
# 生成四个图像的数据
ys1 = np.sin(xs)
ys2 = np.cos(xs)
ys3 = np.tan(xs)
ys4 = 1/(1+np.exp(-xs))

# 创建2行2列的子图 返回图形窗口对象和子图对象数组
fig,axs =  plt.subplots(2,2)

# 第一个子图显示正弦图
axs[0][0].plot(xs,ys1)
axs[0][0].set_title("正弦曲线")
axs[0][0].set_xlabel("时间轴： t/s")


# 第2个子图显示余弦图
axs[0][1].plot(xs,ys2)
axs[0][1].set_title("余弦曲线")
axs[0][1].set_xlabel("时间轴： t/s")


fig.tight_layout()
plt.show()