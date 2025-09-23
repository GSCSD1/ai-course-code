"""
    try:
        # 有可能发生异常的代码
    except Exception as e:
        # 异常发生后要执行代码
    else :
        # 如果没有异常发生，在try执行完毕会执行这里的代码
    finally:
        # 不管有没有捕获到异常，最后都执行这里的代码
    Exception 通用的异常类  用于表示所有异常
"""

try:
     # 1/0  # division by zero
     # a - 1  # name 'a' is not defined
    my_list = [1,2,3]
    print(my_list[5]) # list index out of range
    #  import time
    #  for i in range(10):
    #      print(i)
    #      time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
except Exception as e:
    print(e)
else :
    print("没有捕获到异常")
finally:
    print("不管有没有异常，都会执行")   # 1 3 5


"""
    异常传递性： 当一个函数或方法抛出一个异常时，这个异常会被传递到调用方那里，如果调用者没有捕获到异常的话，
    那么程序会终止
"""
def method1():
    print('in method1')
    method2()
    print('out method1')

def method2():
    print('in method2')
    print(1/0)
    print('out method2')

try:
    method1()  #   in method1  in method2  division by zero
except Exception as e:
    print(e)