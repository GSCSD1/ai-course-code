"""---------------------进程间的执行顺序 无序----------------"""
import time
from multiprocessing import Process
import os

def get_info(a):
    print("get_nfo", a)
    time.sleep(2)

    # 获取pid
    # print("get_info",os.getpid())


if __name__ == '__main__':
    # 创建10个子进程
    for i in range(10):
        sub_process =  Process(target=get_info,args=(i,))
        sub_process.start()

"""---------------------线程间的执行顺序 无序----------------"""
#
# import time
# from threading import Thread,current_thread
# import os
#
# def get_info(a):
#
#     time.sleep(0.5)
#     print(a)
#     # 获取pid
#     # print("get_info",a)
#     # print("get_info",current_thread())
#
# if __name__ == '__main__':
#     # 创建10个子进程
#     for i in range(10):
#         sub_process =  Thread(target=get_info,args=(i,))
#         sub_process.start()