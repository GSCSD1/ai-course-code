"""
    try:
        # 有可能发生异常的代码
    except (异常名1,异常名2,....):
        # 异常发生后要执行代码
    else :
        # 如果没有异常发生，在try执行完毕会执行这里的代码
    finally:
        # 不管有没有捕获到异常，最后都执行这里的代码
"""

try:
    print("1")
    1/0  # NameError
    print("2")
except (NameError,ZeroDivisionError):
    print("捕获到了异常")
else :
    print("没有捕获到异常")
finally:
    print("不管有没有异常，都会执行")   # 1 3 5