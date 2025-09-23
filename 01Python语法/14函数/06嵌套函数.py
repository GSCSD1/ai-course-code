"""
    嵌套函数 ： 函数体里面创建函数
            1、如果一个函数内部定义了另一个函数，这个函数就叫嵌套函数，
            外部函数叫外函数，内部就叫内函数
            2、内部函数只能在外部函数中调用

"""
# 定义外函数
def outer_func():
    # 定义内函数
    def inner_func():
        print("这是一个内部函数")
    # 调用内函数
    inner_func()
    print("这是一个外部函数")

# outer_func()

"""
    闭包函数：如果内部函数使用外函数的局部变量，并且外函数把内部函数返回处理的过程叫做闭包，里面的函数叫闭包函数
"""
""" 
    嵌套函数的特性：内函数访问外函数某个变量时操作变量不会随外函数调用完毕而销毁，而是被内函数所保留
"""
def multiplier(factor):
    # 将形传给了局部变量y
    y =  factor
    x = 4
    # 定义了内函数
    def multiply_by(x):
        return x*y
    print("x:",x)
    # 返回的是一个函数
    return multiply_by

# 创建一个乘5的函数  times_2 = multiply_by
times_2 =  multiplier(5)
print(type(times_2))
print(times_2(3)) # multiply_by(3)

def outer_func(x):
    def middle_func(y):
        def inner_func(z):
            return x+y+z
        return inner_func
    return middle_func
"""
    执行流程：
            1、outer_func(x=10)  return  middle_func
            2、 middle_func(20)(y=20)  return  inner_func
            3、inner_func(z=30)  return x+y+z  return 10+20+30
"""

result = outer_func(10)(20)(30)
print(result)
"""
    nonlocal:   可以通过内函数修改外函数的局部变量
    global : 局部变量修改全局变量  
    注意： nonlocal和global不能同时修饰一个变量  会报错
"""
x = 3
def outer_func():
    global x
    x = 1
    def inner_func():  # nonlocal 内函数如何修改外函数的局部变量
        # nonlocal x     # 注意： nonlocal和global不能同时修饰一个变量  会报错
        x = 2
        y = 2
        print(x,y)   #2,2
        return x

    x = inner_func()
    print(x)   # 2

outer_func()
print(x)  # 2