"""
    add_axes: 往任意位置添加子图
    matplotlib.figure.Figure.add_axes(rect, **kwargs)
    rect ： [左边界，底边界，宽度，高度]
"""
import matplotlib.pyplot as plt
fig = plt.figure()

# 图像的位置为左边界10%，底边界10%，宽度50%，高度50%
ax =  fig.add_axes([0.1,0.1,0.5,0.5])
ax.plot([1,2,3],[4,5,6])

plt.show()