import os
from threading import Thread,current_thread
import time
def coding():
   # 获取进程号
   print(f"coding>>>",os.getpid())  # process ID
   # 获取线程信息
   print("coding>>>",current_thread())
   for i in range(3):
       print("coding....")
       time.sleep(0.2)

def music():
   # 获取进程号
   print(f"music>>>", os.getpid())
   # 获取线程信息
   print("music>>>", current_thread())
   for i in range(3):
       print("music....")
       time.sleep(0.2)

if __name__ == '__main__':
    print(f"主进程>>>", os.getpid())
    cod_thread =  Thread(target=coding)
    music_thread = Thread(target=music)
    cod_thread.start()
    music_thread.start()