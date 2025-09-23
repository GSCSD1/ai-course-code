"""
带参装饰器模板：
    def g_outer(x):
        def outer(func):
            def wrapper(*args, **kwargs):
                res = func(*args, **kwargs)
                return res
            return wrapper
        return outer
带参装饰器模板：@装饰器函数名(参数)
"""
import time
# 根据不同登录方式来决定是否进去
# source = "access"
def auth(source):
    def outer(func):  #  闭包   装饰器函数
        def warapper(*args,**kwargs):
            if source == 'file':
                user = input("user>>")
                passwd = input("password>>")
                if user=="z12345" and passwd=="321321":
                    res = func(*args,**kwargs)
                else:
                    print("密码错误")
                    res = None
            elif source == 'mysql':
                res = None
                print("基于mysql的登录验证")
            elif source == 'access':
                res = None
                print("基于access的登录验证")
            return res
        return warapper
    return outer

#
@auth("file")
def home():
    time.sleep(2)
    print("welcome to home！")

# outer = auth("mysql")
# home =  outer(home)
home()