import matplotlib.pyplot as plt
# 创建一个图形和坐标轴
fig = plt.figure()
ax1 =  fig.add_subplot(1,2,1)
ax2 =  fig.add_subplot(1,2,2)
# 获取当前活动的子图的属性。
ax = plt.gca()
# 使用坐标轴对象进行自定义
ax.set_title('Sample Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
# 显示图形
plt.show()