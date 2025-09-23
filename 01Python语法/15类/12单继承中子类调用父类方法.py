
"""
    子类如何调用父类中的方法：  类名.方法名()
    对象如何调用父类方法 ： 子类不要重写（覆盖）父类方法
"""

# 定义一个类A实现两位数的加法
class  A:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2


# 实现三个数的加法
class B(A):
    def __init__(self,num1,num2,num3):
        # 调用A的构造函数
        A.__init__(self,num1,num2)
        # self.num1 = num1
        # self.num2 = num2
        self.num3 = num3

    def add(self):
        return A.add(self)+self.num3

# a = A(10,220)
# print(a.add())
b = B(10,20,12)
print(b.add())