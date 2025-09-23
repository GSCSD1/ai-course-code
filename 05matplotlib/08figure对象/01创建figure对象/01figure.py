"""
    1 inch = 2.54cm

    打印：
    如果你打算打印图形，通常使用较高的 dpi 值，通常 300 dpi 是打印图像的标准分辨率。这对于打印图形时保证清晰度非常重要。
    对于非常高质量的打印（例如专业出版），可能会使用 600 dpi 或更高。
保存图像（屏幕或打印）：
    100 dpi：适用于屏幕显示，文件大小较小，适用于快速预览或网页使用。
    200-300 dpi：适用于高质量输出，如打印和出版。
    300 dpi 以上：适用于需要非常高质量的打印或出版物，图形会更精细，但文件大小也会更大。

    figure:用于创建一个新的图形窗口，或者获取当前活跃的图形窗口
    每个图形窗口可以包含一个或者多个坐标轴（axes）,可以在其上绘制数据

    plt.figure(num=None, figsize=None, dpi=None, facecolor=None,
    edgecolor=None, frameon=True, clear=False, **kwargs)

    num(可选参数)：指定图形窗口的编号或名称。
    figsize(可选参数)：图形窗口的大小，以英寸为单位  主要控制图形的物理尺寸
    dpi:图形的分辨率，以点每英寸为单位 dpi越高，图像越清晰
    facecolor: 背景颜色
    edgecolor: 边缘颜色
    frameon ； 布尔值  指定是否绘制边框
    clear   ： 指定是否清除图形窗口内容
"""
from matplotlib import pyplot as  plt
# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号


# 指定窗口大小
plt.figure(num=1,figsize=(2,2))
plt.title("第一个窗口")
plt.plot([1,2,3],[4,5,6])
plt.figure(num=2,figsize=(2,2),facecolor='r')
plt.title("第二个窗口")
plt.plot([1,2,3],[4,5,6])
# 切换到第一个窗口进行绘制
plt.figure(num=1)
plt.plot([10,20,30],[54,87,87])

plt.show()
