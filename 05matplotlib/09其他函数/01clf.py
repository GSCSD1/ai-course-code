
"""
    用于清除内容
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
plt.clf()
plt.show()



