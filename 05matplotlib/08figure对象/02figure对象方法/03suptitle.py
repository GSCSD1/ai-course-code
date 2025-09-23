"""
    往figure添加标题 （居中对齐）

    matplotlib.figure.Figure.suptitle(t, **kwargs)

    t：标题名字
    **kwargs： 用于控制标题样式  fontsize  color
"""

import matplotlib.pyplot as plt
fig = plt.figure()

# 设置窗口标题
fig.suptitle('figure title')

# 创建四个子图
fig.add_subplot(2,2,1)
fig.add_subplot(2,2,2)
fig.add_subplot(2,2,3)
fig.add_subplot(2,2,4)

plt.show()