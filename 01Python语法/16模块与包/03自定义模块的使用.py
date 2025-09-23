
"""
    注意： 导入模块时会先执行模块文件里面的内容
"""
# 导入ModuleA模块
# from ModuleA import *  # 受all参数影响
from ModuleA import add,div,__a  # 不受all参数影响
# import ModuleA  # 不受all参数影响
# print(add(1, 2))
# print(div(1, 2))

print(__a)


