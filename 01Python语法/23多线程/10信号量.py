"""
    信号量：  锁    可以用来控制同时访问特定资源的线程数量

    互斥锁 ： 同一时间内只允许有一个任务
    信号量： 同一时间任务可以有多个
"""
from threading import Thread,Semaphore
import time
import random
# 限制同时访问只有5个任务
sp = Semaphore(5)
def task(name):
    sp.acquire()
    print(name,'抢到车位')
    time.sleep(random.randint(3,5))
    sp.release()

if __name__ == '__main__':
    for i in range(25):
        t = Thread(target=task, args=(f"宝马{i}",))
        t.start()