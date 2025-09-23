
"""
构造函数和析构函数能手动调用

    构造函数 ：  __init__  在创建对象时自动调用，目的就是为了初始化属性，
    可以在需要的时候定义，通过__init__()来创建构造函数

    析构函数：__del__  在对象引用计数清零时自动调用，目的就是为了释放资源
                            不推荐使用，python有自己的垃圾回收机制
"""
class nTime:
    Hour = 0
    Minute = 0
    Second = 0
    ntime_s = [[12,3,523,5234]]
    def __init__(self,Hour,Minute,Second):
        nTime.Hour = Hour
        nTime.Minute = Minute
        nTime.Second = Second

    def setTime(self,Hour,Minute,Second):
        nTime.Hour = Hour
        nTime.Minute = Minute
        nTime.Second = Second
    def GetTime(self):
        print(nTime.Hour,nTime.Minute,nTime.Second)

    def __del__(self):
        del nTime.Hour

# 通过构造函数初始化属性
myTime = nTime(16,6,32)
myTime.__init__(20,20,20)
myTime.__del__()
# myTime.setTime(16,6,32)
myTime.GetTime()
# 销毁对象
del myTime

while  True:
    pass