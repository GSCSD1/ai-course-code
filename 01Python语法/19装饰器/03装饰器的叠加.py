"""
    装饰器叠加(嵌套)
                装饰顺序： 先里后外 先下后上

"""
# 无参装饰器
def outer3(func):
    def wrapper(*args,**kwargs):
        print('开始执行outer3.wrapper')
        func(*args,**kwargs)
        print('outer3.wrapper执行完毕')
    return wrapper
# 带参装饰器
def gouter2(x):
    def outer2(func):
        def wrapper(*args,**kwargs):
            print('开始执行outer2.wrapper')
            func(*args,**kwargs)
            print('outer2.wrapper执行完毕')

        return wrapper
    return outer2
# 无参装饰器
def outer1(func):
    def wrapper(*args,**kwargs):
        print('开始执行outer1.wrapper')
        res = func(*args,**kwargs)
        print('outer1.wrapper执行完毕')
        return res
    return wrapper

# @outer1
# def home(z):
#     print('执行home功能',z)
# home(1)  # 开始执行outer1.wrapper  执行home功能 1  outer1.wrapper执行完毕
#
# @outer3
# def home(z):
#     print('执行home功能',z)
# home(2)   # 开始执行outer3.wrapper 执行home功能 2   outer3.wrapper执行完毕
#
# @gouter2(10) # outer2 = gouter2(10) home=outer2(home)
# def home(z):
#     print('执行home功能',z)
# home(3)   # 开始执行outer2.wrapper 执行home功能 3 outer2.wrapper执行完毕



# 加载顺序 ： 先outer1->gouter2->outer3
@outer3
@gouter2(10)
@outer1
def home(z):
    print('执行home功能',z)
"""
        print('开始执行outer3.wrapper')   ->outer3(10)装饰效果
        
        print('开始执行outer2.wrapper')   ->gouter2(10)装饰效果
     
        print('开始执行outer1.wrapper')    ->outer1装饰效果
        res = home(2)
        print('outer1.wrapper执行完毕')
        
        print('outer2.wrapper执行完毕')
        
        print('outer3.wrapper执行完毕')
"""


home(2)



