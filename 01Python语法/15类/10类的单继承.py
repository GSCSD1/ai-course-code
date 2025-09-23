"""
    继承： 创建新类的方法，通过继承创建的类称为子类，
    被继承的类称为父类

    子类会继承父类所有的属性和方法，并且一个子类可以有多个

    继承语法：
            class  类名(要继承的类):
                pass
    在python3中，所有类都有一个共同的父类，叫做object类，即使自定义类时，会默认继承object，子类会拥有
    object类中所有的属性和方法：

    在python2中 ：
            新式类： 继承了object子类
            经典类:  没有继承object子类

    object类：
                __dict__:  显示存放的属性和方法
                __bases__ :  查看基类
                __init__() : 构造函数
                __eq__()   : 定义比较操作符   类1 == 类2
                __iter__  ： 使对象支持迭代    for循环能够遍历
                __next__ :  迭代下一个值
                __class__ :  对象所属的类
                __doc__ :  对象的文档
                __name__ :  类的名字
                __new__ ：  创建对象自动调用的函数  如果当前函数没有返回对象，则不会进入构造函数
"""

class Zhangsan(object):
    def __init__(self):
        self.height = 100
        self.weight = 80
        self.age = 18
        print("构造方法")
    def say(self):
        print("你好")



class Lisi(Zhangsan):
    """
        继承Zhangsan类
        可以调用Zhangsan相应方法

    """
    pass
print(Zhangsan==Lisi)
#创建lisi对象
lisi1 = Lisi()
# 调用say方法
lisi1.say()
# 访问weight属性
print(lisi1.weight)

print("lisi1所属的类:",lisi1.__class__)
print("Lisi帮助信息:",lisi1.__doc__)
# 查看lisi的父类
print("Lisi父类：",Lisi.__bases__)
print("Zhangsan父类：",Zhangsan.__bases__)