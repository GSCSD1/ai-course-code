"""
    用于将当前图形保存到文件png中
    matplotlib.pyplot.savefig(fname, dpi='figure', format=None,
    metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto',
    edgecolor='auto', backend=None, **kwargs)

    fname：文件名
    dpi ： 分辨率   figure：使用图形窗口分辨率
    format： 文件格式   None：使用的是文件名后缀的文件格式
    metadata： 元数据
    bbox_inches：tight：则matplotlib会尝试裁剪图形周围的空白
    pad_inches： 填充空白
    facecolor：背景颜色
    edgecolor：边缘颜色
    backend  ： 用于保存图像的特定后端    通常不需要设置
    kwargs：其他关键字函数
"""
from matplotlib import pyplot as plt

import numpy as np
xs = np.array(["语文", "数学", "英语", "物理", "化学", "生物"])
ys = np.array([85, 92, 73, 65, 87, 93])
print(xs)
# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 绘制柱形图
plt.bar(xs,ys,width=0.3,
        align='center',
        facecolor='y',
        edgecolor='r',
        hatch = 'x',
        log = True,
        label='各科的平均成绩',
        linewidth=3)


plt.legend()
# plt.show()

plt.savefig("savefig.png")



