"""
    除了可以自定义一个新的闭包函数用作装饰器之外，也可以将类作为装饰器。
    为被装饰函数添加新功能。
    类装饰器通过实现类中__call__方法，使得实例可以被当做函数来调用从而实现
    对其他函数的装饰
"""
class MyDecorator:
    def __init__(self, func):
        self.func = func  # 存储被装饰的函数
    def __call__(self,*args,**kwargs):
        print("开始执行")
        ret = self.func(*args,**kwargs)
        print("结束执行")
        return ret

@MyDecorator
def say_hello(name):
    print(f'hello,{name}')


say_hello("lisi")