"""
    进程间通信(IPC) : 管道 共享内存 信号   队列(常用)
"""
from multiprocessing import Process,Queue
import time
# 厨师进程
def task1(q):
    for i in ["宫保鸡丁","北京烤鸭"]:
        time.sleep(2)
        q.put(i)
        print(f"TASK1:{i}已经做好")

# 顾客进程
def task2(q):
    while  True:
        print("TASK2:",q.get())
        time.sleep(2)

if __name__ == '__main__':
    # 实例化先进先出队列
    q = Queue()
    task1_process = Process(target=task1,args=(q,))
    task2_process = Process(target=task2,args=(q,))

    # 启动进程
    task1_process.start()
    task2_process.start()


