"""
    创建线程 ：
                threading
    Thread() 参数
        target： 执行目标任务名，这里指函数名
        name ： 进程名  一般不用设置
        group： 进程组 ，目前只能使用None
        args : 以元组的方式给执行任务传参
        kwargs： 以字典的方式给执行任务传参
"""
from threading import Thread
import time
def coding():
   for i in range(3):
       print("coding....")
       time.sleep(0.2)

def music():
   for i in range(3):
       print("music....")
       time.sleep(0.2)
# 单任务
# coding()
# music()

# 线程下执行多任务
# 启动线程
if __name__ == '__main__':
    # 通过线程类创建进程对象
    coding_thread = Thread(target=coding)
    music_thread = Thread(target=music)
    coding_thread.start()
    music_thread.start()
#


"""-----------------------创建多线程执行带有参数的任务------------------------------------------------"""
# 注意： 由于多个线程都是在一个进程中，多个进程使用的资源都是同一个进程中的资源,因此多线程之间共享全局变量
# 他们没办法直接交互，如果需要交互，需要借助第三方模块
#
# a = 0
# def coding(num,name):
#    for i in range(num):
#        global a # 声明为全局变量
#        print("coding....")
#        print(name)
#        a += 1
#        print("coding:",a)
#        time.sleep(0.2)
#
# def music(count):
#    for i in range(count):
#        print("music....")
#        print("music:", a)
#        time.sleep(0.2)
#
#
# # 启动进程
# if __name__ == '__main__':
#     # 通过进程类创建进程对象
#     coding_thread = Thread(target=coding,kwargs={"num":3,"name":"华清"})
#     music_thread = Thread(target=music,args=(3,))
#     coding_thread.start()
#     music_thread.start()
#

"""-------------------------------------通过自定义类的方式创建多线程------------------------------------"""

class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.task_name = name

    def run(self):
        print(f"{self.task_name}任务开始")
        time.sleep(2)
        print(f"{self.task_name}任务结束")


if __name__ == '__main__':
    p = MyThread("测试")
    p.start()
    print("主进程")