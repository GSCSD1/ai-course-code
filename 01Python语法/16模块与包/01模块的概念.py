"""
    模块：  以.py为后缀的文件
    模块可以被其他python程序导入和使用，也可以自己
    独立执行

    模块的导入： random.py  {randint(1,10)}
                import 模块名           import random      random.randint(1,10)
                import 模块名 as 别名   import random  as rd  rd.randint(1,10)
                from 模块 import 子模块  from import import randint   randint(1,10)
                from 模块 import *    导入模块中所有内容 from import import *  randint(1,10)

    模块的作用： 不需要从零开始，不用重复"造轮子"
               避免同一模块命名重复的问题
               方便代码维护和管理 ，提高代码的可读性

    模块内置变量：  dir()  查看模块的内置变量

            __name__ : 用于确定模块是否被直接运行还是被导入到其他模块，当一个模块被直接运行，值为 __main__,否则我模块名称
            __doc__ : 查看模块说明文档
            __file__ : 查看模块的文件路径
            __all__ : 定义一个模块中哪些变量、函数、或  类可以通过导入
            __package__ : 包含模块所在的包路径
            __dict__:  包含模块的全局命名空间，可以用来查看模块的结构

    模块的类型 ：
                内置模块 : python解释器自带的标准库模块
                第三方模块：  pip 去安装   安装pyq5 pip install pyqt5  安装指定版本  pip install 模块名==版本号
                自定义模块： 根据需求去编写py文件
"""

# print(__name__)
# print(__file__)
print(__package__)
# print(__doc__)
import random
print(random.__dict__)

# import MouleA  # 调用:模块名.子模块
# print(MouleA.add(1, 2))

# import MouleA as MA # 调用:别名.子模块
# print(MA.add(1, 2))
#
# from MouleA import add,div  # 调用:子模块()
# print(add(1, 2))
# print(div(1, 2))

from MouleA import *  # 调用:子模块()
print(add(1, 2))
# print(div(1, 2))

# import random
# print(random.randint(1,10))


# print(dir(random))
# print(random.__doc__ )