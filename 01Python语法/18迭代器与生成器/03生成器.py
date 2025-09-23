# 需要一个迭代器，能产生三个值
import random

I = [1,2,3]
I = I.__iter__()
# 需要一个迭代器，能产生1亿个值
I = range(100_000_000)
I = I.__iter__()
# 需要一个迭代器，能产生1亿个0-1的随机浮点数
I = [] # 比较浪费内存
# for i in range(100_000_000):
#     I.append(random.random())

"""
    生成器：不依赖于range和其他数据类型就可以直接
    定义出来的迭代器方法。
    作用：避免一次性生成所有值从而占用大量内存。
    生成器使用yield语句来产生值。
"""
# 每次调用只能返回一个值
def func():
    print("第一次执行")
    yield 1
    print("第二次执行")
    yield 2
    print("第三次执行")
    yield 3
    print("第四次执行")
    yield 4
    print("第五次执行")
func()
func()
# 返回的是生成器对象
res = func()
print(func)
# 调用生成对象中的next方法才能使程序往下执行
# 调用next时如果后面没有yield关键字会抛出StopIteration异常
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

# for i in res:
#     print(i)

# 需要一个迭代器，能产生1亿个0-1的随机浮点数
def generate_random_floats():
    count = 3
    while count > 0:
        count = count - 1
        yield random.random()

res = generate_random_floats()

for i in res:
    print(i)