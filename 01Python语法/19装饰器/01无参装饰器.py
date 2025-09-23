
"""
    给函数添加功能 ： 最好遵循开放封闭原则
    开放： 对扩展功能开发
    封闭： 对修改源代码封闭

    装饰器 ： 本质上是一种嵌套函数，它接受一个函数作为参数（该函数就是被装饰的函数），返回一个新的
    函数(装饰之后的函数)。
    作用： 可以让我们在不改变被装饰函数的代码和函数名字和调用方式的情况下增加功能
    应用：
                性能检测 检测程序运行时间
                记录日志
                权限验证
"""


"""给函数添加  计算函数花费时间的功能"""

# 方法一： 通过增加调用方式前后的代码可以增加该功能 但是如果多处都调用了inside函数   会导致大量的重复代码
import time
# def inside(group,s):
#     print("欢迎来到王者荣耀")
#     print(f"你出生在{group}阵营")
#     print(f"敌军还有{s}到达战场")
#     time.sleep(s)
#     print("全军出击")

def inside(group,s,z):
    print("欢迎来到王者荣耀")
    print(f"你出生在{group}阵营")
    print(f"敌军还有{s}到达战场")
    time.sleep(s)
    print(f"{z}出击")
# # 获取时间
# ntime = time.time()
# inside("红方",5)
# last =  time.time()
# print("程序花费时间：",last-ntime)
#
# ntime = time.time()
# inside("红方",5)
# last =  time.time()
# print("程序花费时间：",last-ntime)
#
# ntime = time.time()
# inside("红方",5)
# last =  time.time()
# print("程序花费时间：",last-ntime)

# 方法二：解决了程序冗余 但源代码参数一旦增加或者修改  会导致自己封装的函数出问题
# def warapper():
#     ntime = time.time()
#     inside("红方",5)
#     last =  time.time()
#     print("程序花费时间：",last-ntime)
#
# warapper()

# 方案三：无论怎么传参，我的封装函数依然能把参数传递过去。无法解决一个装饰函数去装饰多个功能，因为内部函数已经定死了
# def warapper(*args,**kwargs):
#     ntime = time.time()
#     inside(*args,**kwargs)
#     last =  time.time()
#     print("程序花费时间：",last-ntime)
#
#
# warapper("红方",s=5,z="全军")

# 方案四：解决了装饰函数去装饰多个功能，装饰之后无法取得返回值
def recharge(num):
    print("开始充电")
    time.sleep(num)
    print("充电完成")
    return num

# func = inside
# def warapper(*args,**kwargs):
#     ntime = time.time()
#     func(*args,**kwargs)
#     last =  time.time()
#     print("程序花费时间：",last-ntime)
#
# warapper("红方",s=5,z="全军")
# func = recharge
# warapper(3)

# 方案五：解决返回值问题。如何再不修改函数的情况下增加功能
func = inside
def warapper(*args,**kwargs):
    ntime = time.time()
    res = func(*args,**kwargs)
    last =  time.time()
    print("程序花费时间：",last-ntime)
    return res
#
# print(warapper(3))


# 方案六  不修改函数的情况下增加功能
# inside = warapper
# inside("红方",s=5,z="全军")

# 方案7  整合上面的方案  重点理解

# def outer(func):  #  闭包   装饰器函数
#     def warapper(*args,**kwargs):
#         ntime = time.time()
#         res = func(*args,**kwargs)
#         last =  time.time()
#         print("程序花费时间：",last-ntime)
#         return res
#     return warapper
#
#
# inside = outer(inside)
# recharge = outer(recharge)
# inside("红方",s=5,z="全军")
# recharge(2)


# 方案8 自带语法糖实现
"""
    语法糖： 可以让代码更简洁，易于理解，但这些特性不会带来新的功能，也就是说使用
    或者不使用，最终程序行为是相同的，但是语法糖可以是代码更易于阅读和维护
"""
def outer(func):  #  闭包   装饰器函数
    def warapper(*args,**kwargs):
        ntime = time.time()
        res = func(*args,**kwargs)
        last =  time.time()
        print("程序花费时间：",last-ntime)
        return res
    return warapper

@outer # inside = outer(inside)
def inside(group,s,z):
    print("欢迎来到王者荣耀")
    print(f"你出生在{group}阵营")
    print(f"敌军还有{s}到达战场")
    time.sleep(s)
    print(f"{z}出击")


# inside("红方",s=5,z="全军")

# 给home函数加入权限验证 功能,保证不修改函数名，内容，和调用方式  ，必须输入正确的账号z12345和密码321321才能进入到该函数，否则提示密码错误
def outer(func):  #  闭包   装饰器函数
    def warapper(*args,**kwargs):
        if input("user>>")=="z12345" and input("password>>")=="321321":
            res = func(*args,**kwargs)
        else:
            print("密码错误")
            res = None
        return res
    return warapper

@outer # home = outer(home)
def home():
    time.sleep(2)
    print("welcome to home！")

print(home)

# home()


# 无参装饰器模板  装饰器模板需要自己能够熟练敲出来
def outer(func):
    def wrapper(*args,**kwargs):
        # userCode .....
        res = func(*args,**kwargs)
        # userCode .....
        return res
    return wrapper