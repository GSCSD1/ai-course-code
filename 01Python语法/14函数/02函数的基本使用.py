"""
    易读  简洁
    def 函数名(形参):
        函数体内容
        return 参数值
    return 结束函数 选择性返回一个值给调用方
    没写return 默认返回None  形参，return按实际需求写，可写可不写

    函数的作用 ：为了代码的重复使用

    函数的基本组成：
                    名称
                    功能
                    参数
                    返回值
"""

#1、 创建函数/函数定义
# 连续输出5次hello world
# 函数不会执行
def my_func():
    for i in range(3):
        print("hello world")

# 2、函数的调用  函数名字()
my_func()
print("8"*100)
my_func()

#pass : 在函数开始定义且没有功能时，作为一个占位符，防止编译器报错
def login():
    pass

def register():
    pass
