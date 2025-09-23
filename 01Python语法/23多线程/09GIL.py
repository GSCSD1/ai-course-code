"""
GIL 全局解释锁：在cpython中，GIL是一把互斥锁，用来阻止用一个线程下的
    多个线程同时执行，也就是说在同一个进程下的多个线程，多个cpu不能并行，一次
    只有cpu来执行
    核心原理：在解释器里面加互斥锁

    加锁原因：如果多个运行，导致python内存管理不是线程安全的
    总结： 1、GIL不是python的特点，而是CPYTHON解释器独有的
          2、GIL会导致同一个进程下的多个线程不能同时执行，无法利用多核能力
          3、GIL的目的是为了保证解释器级别的数据安全
          4、写代码的时候，该怎么写就怎么写，不需要考虑GIL(冷门)

    问题： python多线程无法利用多核优势，即使有多个核，一次也只能用一个,执行效率和进程比是不是很低

    分情况：
            计算密集型场景(进程执行效率高)     IO密集型场景(线程执行效率高)
"""

import time
from multiprocessing import Process
from threading import  Thread

"""计算密集型场景"""
# def task():
#     res = 0
#     for i in range(100000000):
#         res += i
#
# if __name__ == '__main__':
#     start = time.time()
#     task_handle = []
#     for i in range(8):
#         # p = Process(target=task)  # 进程花费时间： 3.1862778663635254
#         p = Thread(target=task)     # 线程花费时间：22.450464725494385
#         p.start()
#         task_handle.append( p)
#     # 等待所有任务执行完毕
#     for i in task_handle:
#         i.join()
#     end = time.time()
#     print("总耗时：",end-start)

"""IO密集型场景"""

def in_task():
    with open("test.txt",'w') as f:
        for _ in range(100000):
            f.write("hello world\n")

    with open("test.txt", 'r') as f:
        for _ in range(100000):
            lines = f.readlines()

if __name__ == '__main__':
    start = time.time()
    task_handle = []
    for i in range(8):
        # p = Process(target=in_task)  # 进程花费时间： 5.161083459854126
        p = Thread(target=in_task)     # 线程花费时间：3.5235466957092285
        p.start()
        task_handle.append( p)
    # 等待所有任务执行完毕
    for i in task_handle:
        i.join()
    end = time.time()
    print("总耗时：",end-start)