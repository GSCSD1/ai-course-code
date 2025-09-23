"""
    显示像素点数据  （图片数据）
    matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None,
interpolation=None, alpha=None, vmin=None, vmax=None, origin=None,
**kwargs)
    X：图像数据
    cmap：颜色映射  通常是virdis
    norm：用于归一化方法
    aspect：控制图像纵横比
    interpolation:控制图像缩放时的插值方法
    origin：图像原点
"""
import numpy as np
from matplotlib import pyplot as plt
# 1、显示灰度图

# 100x100 整数范围（0-255）随机数  创建100x100灰度图像
image_data = np.random.randint(0,256,(100,100))

# 显示灰度图
plt.imshow(image_data,cmap='gray')
# plt.show()

# 2、显示彩色图
image_data = np.random.randint(0,256,(100,100,3))
plt.imshow(image_data)
plt.show()

# 显示插值图像 billnear

image_data = np.random.randint(0,256,(10,10))

plt.imshow(image_data,interpolation='bilinear')
plt.colorbar()
plt.show()

# 显示热图
image_data = np.random.randint(0,256,(100,100))


plt.imshow(image_data,cmap='hot')
plt.colorbar()
plt.show()