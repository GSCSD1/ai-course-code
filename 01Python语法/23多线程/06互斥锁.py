import time

# 导入互斥锁
from threading import Thread,Lock
"""----------------------------------------------不加互斥锁-------------------------------"""
# 100个线程去抢100张票
#
# ticket_num = 100  # 定义100张票
# def task():
#     global ticket_num
#     temp = ticket_num
#     time.sleep(0.05)
#     ticket_num = temp-1
#
#
# if __name__ == '__main__':
#     tasklist = []
#     for i in range(100):
#         sub_thread = Thread(target=task)  # 创建线程
#         sub_thread.start()
#         tasklist.append(sub_thread)  # 将线程对象加入到列表
#
#     # 等待所有任务执行完毕
#     for task in tasklist:
#         task.join()
#
#     print("主线程：",ticket_num)
"""----------------------------------------------加互斥锁-------------------------------"""

ticket_num = 100  # 定义100张票
def task(mutex):
    # 请求锁
    mutex.acquire()  # 一直请求锁，直到拿到锁程序才会往下执行
    global ticket_num
    temp = ticket_num
    time.sleep(0.05)
    ticket_num = temp-1
    mutex.release()  # 释放锁


if __name__ == '__main__':
    tasklist = []
    # 创建互斥锁对象
    mutex = Lock()
    for i in range(100):
        sub_thread = Thread(target=task,args=(mutex,))  # 创建线程
        sub_thread.start()
        tasklist.append(sub_thread)  # 将线程对象加入到列表

    # 等待所有任务执行完毕
    for task in tasklist:
        task.join()

    print("主线程：",ticket_num)