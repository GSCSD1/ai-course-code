"""
  任意位置添加文本
      matplotlib.axes.Axes.text(x, y, s, **kwargs)
      x, y：文本位置坐标
      **kwargs ： fontsize color horizontalalignment（水平对齐方式，如 ‘left’,
‘center’, ‘right’）、 verticalalignment（垂直对齐方式，如 ‘top’, ‘center’, ‘bottom’
"""
import matplotlib.pyplot as plt
fig = plt.figure()

fig.text(0.5,0.5,"fig Test",fontsize=20,color='red')

ax1 =  fig.add_subplot(121)
ax1.text(0.2,0.2,"axes Test")

plt.show()