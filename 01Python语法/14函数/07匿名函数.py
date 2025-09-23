"""
    匿名函数： 用于在该函数体只有一句且返回值只有一个时候才使用
    格式： lambda 参数列表:表达式

    lambda 自带return
    lambda 参数列表的规则与函数参数规则完全相同，表达式只能包含一个
    lambda 只返回一个值，值为表达式的结果
    lambda 函数生命周期很短，调用后立即回收
"""
# 标准定义方式
def add(x,y):
    return x+y

print(add(1,2))
add = lambda x,y:x+y
# print((lambda x,y:x+y)(1,2))
print(add(1,2))

# 判断一个数是不是偶数  匿名函数写
func  =   lambda x:x%2==0
print(func(10))

# 无参数
func  =   lambda :print("hello world")
func()

# 默认参数
add = lambda x,y=12:x+y
print(add(10))

# 位置不定长参数
func1 = lambda *args:args
print(func1(10,123,5,324,32))