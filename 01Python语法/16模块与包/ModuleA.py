
__a = 1  # 单下划线 和双下划线   设置私有属性  只对 from ModuleA import * 有效
b = 2

def add(x,y): # 设置私有方法
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    if y == 0:
        return None
    return x/y


if __name__ == '__main__':
    # 当本模块被导入时不执行下面程序
    print(add(1, 3))
    print(sub(1, 3))
    print(div(1, 2))

# 定义一个模块中哪些变量、函数、类可以导入
# __all__ = ['add']