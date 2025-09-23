"""
    axes : 获取窗口里面所有子图对象

"""

import matplotlib.pyplot as plt
fig = plt.figure()

fig.add_subplot(1,2,1)
fig.add_subplot(1,2,2)

# 获取所有的子图的操作句柄
axes = fig.axes
print(axes)
for ax in axes:
    ax.plot([1,2,3],[4,5,6])
    print(ax)  # ax 存储子图的位置和大小

plt.show()
