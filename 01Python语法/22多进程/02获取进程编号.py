"""
    获取进程编号 ： 当程序中的进程数量越来越多，就无法区分主进程和对个子进程。为了方便管理，
    每个进程都有自己的编号，通过获取自己编号可以快速区分不同的进程
"""
import os
from multiprocessing import Process
import time
def coding():
   # 获取进程号
   print(f"coding>>>",os.getpid())  # process ID
   print(f"coding父进程>>>",os.getppid())
   for i in range(3):
       print("coding....")
       time.sleep(0.2)

def music():
   # 获取进程号
   print(f"music>>>", os.getpid())
   print(f"music父进程>>>", os.getppid())
   for i in range(3):
       print("music....")
       time.sleep(0.2)

if __name__ == '__main__':
    print(f"主进程>>>", os.getpid())
    cod_process =  Process(target=coding)
    music_process = Process(target=music)
    cod_process.start()
    music_process.start()