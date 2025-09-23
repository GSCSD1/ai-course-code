"""
    创建进程 ：
                os.fork   linux 环境
                multiprocessing  主要模块
                subprocess 运维要用  功能不多
    Process() 参数
        target： 执行目标任务名，这里指函数名
        name ： 进程名  一般不用设置
        group： 进程组 ，目前只能使用None
        args : 以元组的方式给执行任务传参
        kwargs： 以字典的方式给执行任务传参
"""
from multiprocessing  import Process  # 马尔踢普罗塞斯星
import time
# def coding():
#    for i in range(3):
#        print("coding....")
#        time.sleep(0.2)
#
# def music():
#    for i in range(3):
#        print("music....")
#        time.sleep(0.2)
# # 单任务
# # coding()
# # music()
#
# # 进程下执行多任务
# # 启动进程
# if __name__ == '__main__':
#     # 通过进程类创建进程对象
#     coding_process = Process(target=coding)
#     music_process = Process(target=music)
#     coding_process.start()
#     music_process.start()

"""-----------------------创建多进程执行带有参数的任务------------------------------------------------"""
# 注意：  创建多进程是在内存申请一块内存空间，然后把需要运行的代码放进去，多个进程的内存空间，彼此是隔离的，进程与进程之间的数据，
# 他们没办法直接交互，如果需要交互，需要借助第三方模块

# a = 0
# def coding(num,name):
#    for i in range(num):
#        global a
#        print("coding....")
#        print(name)
#        a = a +1
#        print('cod',a)
#        time.sleep(0.2)
#
# def music(count):
#    for i in range(count):
#        print("music....")
#        print('music', a)
#        time.sleep(0.2)
#
#
# # 启动进程
# if __name__ == '__main__':
#     # 通过进程类创建进程对象
#     coding_process = Process(target=coding,kwargs={"num":3,"name":"华清"})
#     music_process = Process(target=music,args=(3,))
#     coding_process.start()
#     music_process.start()



"""-----------------------自定义类的方式创建进程   能看懂程序即可------------------------------------------------"""


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.task_name = name

    def run(self):
        print(f"{self.task_name}任务开始")
        time.sleep(2)
        print(f"{self.task_name}任务结束")


if __name__ == '__main__':
    p = MyProcess("测试")
    p.start()
    print("主进程")