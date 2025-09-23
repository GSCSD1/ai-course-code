"""
    面向对象编程： 将数据和方法封装到一起来帮我们去解决实际问题
    在项目复杂的时候帮我们更好的管理程序

    面向对象编程 三大特性 ： 封装  继承  多态

    类的封装 ： 将数据和方法封装到一个类中，并且通过设置访问权限
    将类属性和方法隐藏在类的内部，可以防止类属性和方法被外部直接访问或者修改。
    提高代码的安全性和可维护性，
            __(双下划线)  设置私有权限   外部无法访问
            _(单下划线)   人为规定该属性或方法内部使用，事实上外部可以访问
            __ __(双下划线前后缀)  __init__  __dict__
                    表示python中特殊的属性和方法，有特殊的意义和用途，不推荐自己定义
"""

# 造npc
class Person:
    def __init__(self,name,password):
        self.name = name
        self.__password = password  # 设置私有权限  隐藏属性


    def say1(self):
        print("我的密码是：",self.__password)

    # 设置私有方法
    def __say2(self):
        print("我的密码是：",self.__password)

npc1 = Person("zhangsan","123456")
# # print(npc1.name)
# # print(npc1.__password)
# npc1.say2()

print(Person.__dict__)
print(npc1.__dict__)
print("调用私有方法:")
npc1._Person__say2()   # 强行访问私有属性
print("访问私有属性:",npc1._Person__password)  # 强行访问私有属性