"""
    位置不定长参数： 函数在定义时可以接收任意数量的位置参数
    在定义时，一般用*args来表示 。调用时传入的位置参数会被打包成一个元组
"""

def myfunc1(*args):
    for i in args:
        print(i)
    print(args)
    print(type(args))
# myfunc1(1,2,3,"abc")
# myfunc1(1,2,3,[12,42],(2,43,5))

# 传入任意参数，类型为int ，求出最大值
def max_args(*args):
    # 方法一
    # max = args[0]
    # for i in args[1:]:
    #     if i>max:
    #         max = i
    # print(max)
    # 方法二
    nmax = max(args)
    print(nmax)

# max_args(12,54,102,77,88)
max_args(1,64,756,7456,8657,643,767)


# 注意：如果位置不定长参数右边还有其他参数，必须使用关键字传参

def fun1(*args,x,y):
    print("args:",args)
    print("x:", x)
    print("y:", y)

fun1(1,2,3,x=4,y=5)

def fun1(x,y,*args):
    print("args:",args)
    print("x:", x)
    print("y:", y)

fun1(1,2,3,4,5,6,7)

def fun1(x,*args,y):
    print("args:",args)
    print("x:", x)
    print("y:", y)
fun1(1,2,3,4,5,6,y=7)
"""
    函数：
            打包 : 将多个值打包为一个元组
            解包：将一个元组的元素拆分并分别赋值给对应的变量
"""
a = 1,2,3,4
print(a)

def test():
    return 1,2,3,4

print(test())


def fun1(x,y,m,n):
    print(x,y,m,n)
args = (1,2,3,4)
fun1(*args)   # 位置参数解包