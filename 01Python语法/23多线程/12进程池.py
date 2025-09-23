"""
    池： 确保资源（cpu、GPU、内存、磁盘等）在被多个任务被用户共享时，能够
    安全、可靠的执行，在此基础上最大限度利用计算机资源。

    水池 ：  在有水的情况下合理分配水

    降低程序执行效率（限制了程序进程/线程数量），但能数据安全。
"""
import time
from concurrent.futures  import ProcessPoolExecutor


pool =  ProcessPoolExecutor(10)  # 不传参，默认开设的进程数量为CPU核数

# def task(name):
#     print(name)
#     time.sleep(3)

# if __name__ == '__main__':
#     for i in range(50):
#         pool.submit(task, i)  # 往进程程中添加任务，异步提交
#         # 如果进程超过线程池的数量需要排队，等待其他任务执行完毕

"""---------------------进程池如何获取返回结果--------------------------------------"""
def task(name):
    print(name)
    time.sleep(3)
    return name+10

def call_back(future):
    print("函数返回结果:",future.result())

if __name__ == '__main__':

    for i in range(50):
        future =  pool.submit(task, i)  # 往线程中添加任务，异步提交
        future.add_done_callback(call_back)   # 添加回调函数  推荐这种方式获取返回值
