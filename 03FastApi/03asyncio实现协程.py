
"""第一版      装饰器实现协程   """
import asyncio
import time
from threading import current_thread

# python3.4 开始  3.8能继续使用  3.11弃用
# @asyncio.coroutine  # 协程函数装饰器
# def f1():
#     print("f1 start",current_thread())
#     yield  from asyncio.sleep(1)   # 采用异步提交方式  阻塞1s  将线程切换给其他任务
#     print("f1 end", current_thread())
#
# @asyncio.coroutine  # 协程函数装饰器
# def f2():
#     print("f2 start",current_thread())
#     yield  from asyncio.sleep(1)
#     print("f2 end", current_thread())
#
# # 产生一个事件循环
# loop =  asyncio.get_event_loop()
# # loop.run_until_complete(f1())  # 协程函数名+ () 为协程对象
# # loop.run_until_complete(f2())  # 这种方式会变成同步调用
#
# tasks = [f1(),f2()]  # 将协程对象放入列表
# loop.run_until_complete(asyncio.wait(tasks))  # 通过asyncio.wait将列表转为future对象

"""------------------------第二版      async+await 实现协程----------------------"""
# python3.5之后 高版本3.11已经无法运行
# 协程函数 ： async + 函数名

# 不再需要yield  await + 可能产生阻塞的语句(IO任务) 执行异步任务，并将线程切换给其他任务 可以接收函数的返回值

# async def f1():
#     print("f1 start",current_thread())
#     await asyncio.sleep(1)   # 采用异步提交方式  阻塞1s  将线程切换给其他任务
#     print("f1 end", current_thread())
#
# async def f2():
#     print("f2 start",current_thread())
#     await asyncio.sleep(1)
#     print("f2 end", current_thread())
#
# tasks = [f1(),f2()]  # 将协程对象放入列表
# loop =  asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))  # 通过asyncio.wait将列表转为future对象


"""------------------------第三版      async+await 实现协程----------------------"""
# python3.7之后 高版本3.11已经无法运行
# 优化了事件循环和添加任务的代码
# loop =  asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))  两句等价于 asyncio.run(asyncio.wait(tasks))

"""
    await 必须在协程函数中 后面只能跟一种对象  可等待对象（协程对象 task对象 future对象 ）
    
    阻塞操作必须替换成相应的异步库提供的函数
    time.sleep -> asyncio.sleep
    socket::accpet -> loop.sock_accept
    conn.recv -> loop.sock_recv
    
    
    自定义函数中有可能发生阻塞 ，我需要通过await切换任务 但没有异步函数 ，应该怎么做 ？
    后面再说
"""


async def f1():
    print("f1 start",current_thread())
    await asyncio.sleep(1)   # 采用异步提交方式  阻塞1s  将线程切换给其他任务
    print("f1 end", current_thread())

async def f2():
    print("f2 start",current_thread())
    await asyncio.sleep(1)
    print("f2 end", current_thread())

tasks = [f1(),f2()]  # 将协程对象放入列表
asyncio.run(asyncio.wait(tasks))


