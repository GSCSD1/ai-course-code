"""
    多态：  运行不同对象对一个方法做出不同响应
    简单理解： 一个函数能根据不同状态做相应的处理实现相同功能
"""
print(len("1234"))
print(len([1,2,3,4]))

# 鸭子模型 ： 有个东西走路像鸭子，叫声也像鸭子，行为也像鸭子，那么就认为这个东西是鸭子

class disk:
    def read(self):
        print("disk read")
    def write(self):
        print("disk write")

class Memory:
    def read(self):
        print("memory read")
    def write(self):
        print("Memory read")

class File:
    def read(self):
        print("file read")
    def write(self):
        print("file write")

disk = disk()
mem = Memory()
file = File()

def read(x):
    x.read()

def write(x):
    x.write()

read(disk)
read(mem)
read(file)