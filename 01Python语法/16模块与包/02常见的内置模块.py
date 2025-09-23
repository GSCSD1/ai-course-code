"""
    os模块  主要处理文件相关的
"""
# import os
# if os.path.exists("test") ==False:
#     os.mkdir("test")
"""
    sys模块
"""
import sys
# hds124
print(sys.version) # 输出python版本号
# sys.exit(0)  # 结束程序 返回错误代码  0 正常退出  非0 异常

"""
    math模块
"""
import math
print(math.pi)
print(math.sin(math.pi))
print(math.cos(math.pi))

"""
    time 模块
"""
# import time
# for i in range(100):
#     ntime = time.time()
#     time.sleep(0.5) # 延时0.5s
#     Diff_time = time.time() - ntime  # 记录花费时间
#     print(Diff_time)
#     print(i)
# cur_time = time.time() # 自1970年1月1日以来经过的秒数
# print(cur_time)

"""
    random
"""
import random
print(random.random())   # 输出0-1的小数
print(random.randint(1, 10))  #输出1-10的随机整数
# 打乱容器中的数据
list1 = [1,2,3,4,5,6]
# 将数据随机打乱
random.shuffle(list1)
print(list1)