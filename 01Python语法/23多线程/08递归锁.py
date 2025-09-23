"""
    递归锁： 相当于计数器  每acquire一次 计数器就会加1  ，每release一次计数器就会减一

    只有计数器为0，才能抢到这把锁

"""

import time
from threading import Thread,RLock,current_thread


mutex1 = RLock()
mutex2 = mutex1
#  递归锁  不要求掌握     了解递归锁的创建和工作原理
def task():
    mutex1.acquire()  # 锁=1
    print(f'{current_thread().name}抢到锁1')
    mutex2.acquire()  # 锁=2
    print(f'{current_thread().name}抢到锁2')
    mutex2.release()  # 锁=1
    mutex1.release()  # 锁=0

    mutex2.acquire()  # 锁=1
    print(f'{current_thread().name}抢到锁2')
    time.sleep(1)
    mutex1.acquire()   # 锁=2
    print(f'{current_thread().name}抢到锁1')
    mutex2.release()  # 锁=1
    mutex1.release() # 锁=0

if __name__ == '__main__':
    for i in range(8):
        t = Thread(target=task)
        t.start()