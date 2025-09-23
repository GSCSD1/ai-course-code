"""
    手动调节子图布局
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
    left： 子图与图形窗口左边缘之间的距离     范围是从0-1      相对于窗口大小
    bottom： 子图与图形窗口下边缘之间的距离     范围是从0-1
    right： 子图与图形窗口右边缘之间的距离     范围是从0-1
    top： 子图与图形窗口上边缘之间的距离     范围是从0-1

    wspace：子图之间的水平间距  相对于坐标轴大小
    hspace：子图之间的垂直间距
"""

import matplotlib.pyplot as plt
# 创建一个图形和坐标轴
fig = plt.subplots(2,2)

plt.subplots_adjust(left=0.2,bottom=0.3,wspace=0.5,hspace=0.4)
plt.show()



