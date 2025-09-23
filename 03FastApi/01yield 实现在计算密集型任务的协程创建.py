import time
""" 同步执行多个任务 """
def f1():
    n = 0
    for i in range(50000000):
        n += i

def f2():
    n = 0
    for i in range(50000000):
        n += i

start = time.time()
f1()
f2()
end = time.time()
print("总耗时：",end-start)  #   2.327294111251831

""" 协程执行多个任务   在单线程下实现并发    核心：单线程下实现多任务的切换   不推荐这么做"""

def f1():
    n = 0
    for i in range(50000000):
        n += i
        yield


g  = f1()  # g是生成器对象   f1 不会执行
def f2():
    n = 0
    for i in range(50000000):
        n += i
        next(g)  # g.__next__()


start = time.time()
f2()
end = time.time()
print("总耗时：",end-start)   # 3.9372928142547607


