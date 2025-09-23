"""
两个进程里面的两个线程    主进程和子进程结束顺序： 默认情况下，主进程会等待所有子进程结束完之后才会结束
1个进程里面的两个线程     主线程和子线程结束顺序：默认情况下，主线程会等待所有子线程结束完之后才会结束
"""
# 注意 ： 默认情况下主进程会等待所有子进程结束后再结束
from threading import Thread
import time

def work():
    for i in range(10):
        print("工作1...")
        time.sleep(0.2)

if __name__ == '__main__':
    work_thread = Thread(target=work)
    # 设置守护线程，主线程退出后子线程直接销毁，不再执行子线程中代码
    work_thread.daemon = True  # 设置守护线程

    # 启动进程
    work_thread.start()
    time.sleep(1)

    print("主进程执行完毕")
