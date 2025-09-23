"""
    如果作用于axes  清除子图内容

    如果作用于图形窗口 清除图形窗口内所有内容
"""


import matplotlib.pyplot as plt
import numpy as np

# 创建一个图形和坐标轴
fig = plt.figure()
ax1 =  fig.add_subplot(1,2,1)
ax1.scatter(np.linspace(0,10,100),np.random.randn(100))
ax2 =  fig.add_subplot(1,2,2)
ax2.scatter(np.linspace(0,10,100),np.random.rand(100))

# fig.clear()  # 清除图形窗口内所有内容

ax1.clear()  # 清楚第一个子图内容
plt.show()