
# 多继承中子类如何初始化各个父类   弄清楚调用顺序
class A:
    def __init__(self):
        print('A')

class B1(A):
    def __init__(self):
        A.__init__(self)  # 初始化父类参数
        print('B1')

class B2(A):
    def __init__(self):
        A.__init__(self)  # 初始化父类参数
        print('B2')

class C(B1,B2):
    def __init__(self):
        B1.__init__(self)  # 初始化父类参数
        B2.__init__(self)  # 初始化父类参数
        print('C')

c = C()  # B1 B2 C