"""
    super函数 ： 严格根据对象所在的类里面的mro继承顺序去搜索父类指定的函数，并且直接绑定好self参数

"""
# 执行顺序
class A:
    def __init__(self):
        print('A')

class B1(A):
    def __init__(self):
        # super().__init__()  # 初始化父类参数
        print('B1')

class B2(A):
    def __init__(self):
        # super().__init__()  # 初始化父类参数
        print('B2')

class C(B1,B2):
    def __init__(self):
        super().__init__()  # 初始化父类参数
        print('C')

print(C.mro())
c = C()  # B2 B1  C

