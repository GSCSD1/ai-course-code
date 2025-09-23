"""
    类的多继承 ： 一个类里面多个父类
    多继承格式：
                class 类名(父类1，父类2，....)

                继承优先级  ： 子类和多个父类有相同属性或方法时，遵循以下优先级
                 子类 > 从左到右第一个父类 > 第二个父类  > 第三个> .....

                 对于复杂继承关系  ，使用mro方法来获取继承顺序
"""

class A:
    a =  100
    def run(self):
        print("我会跑步")

    def say(self):
        print('1')

class B:
    a =  200
    def swim(self):
        print("我会游泳")
    def say(self):
        print('2')

class C(A,B):
    pass

c = C()
c.run()
c.swim()
c.say() #  1
print(c.a)
print("继承顺序：",C.mro())