import matplotlib.pyplot as plt
import numpy as np
# 创建一个图形和一个子图
fig, ax = plt.subplots()
# 生成一些数据
t = np.arange(0, 10, 0.01)
s = np.sin(t)
# 绘制第一条线
ax.plot(t, s)
# 显示图形
# plt.show(block=False)  # 图形不阻塞
# 更新线的数据并暂停
for phase in np.arange(0, 3 * np.pi, 0.05):
 ax.plot(t + phase, np.sin(t + phase))
 plt.pause(0.1)  # 延时0.1s

plt.show()