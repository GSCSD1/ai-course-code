"""
    join方法 ： 在进程可以阻塞主进程的执行，直接等待子进程全部完成之后才继续运行主进程后面的代码

"""

# 注意 ： 默认情况下主进程会等待所有子进程结束后再结束
from multiprocessing import Process
import time

def work():
    for i in range(10):
        print("工作1...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = Process(target=work)
    # 方法一：
    # 设置守护进程，主进程退出后子进程直接销毁，不再执行子进程中代码
    work_process.daemon = True  # 设置守护进程
    # 启动进程
    work_process.start()

    time.sleep(1)
    work_process.join()  # 阻塞主进程，等待子进程执行完毕之后才往下执行
    print("主进程执行完毕")
