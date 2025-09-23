"""
    自定义迭代器：
        1、生成自定义的数据
        2、按需生成数据
        3、分页查找  一页一页迭代

"""

# 自定义range迭代器  MyRange(5)  ->[0,1,2,3,4]

class MyRange:
    def __init__(self,end):
        # 存储结束参数
        self.end = end
        self.num=-1
    def __iter__(self):   # 返回本身
        return self

    def __next__(self):   # 迭代下一个值
        self.num +=1
        if self.num<self.end:
            return self.num
        else:
            raise StopIteration

# 创建一个迭代器对象
# range_iter =  MyRange(15)
# for i in range_iter:
#     print(i)

"""
    斐波那契数列 定义如下：
    1. 数列的前两个数是0和1。
    2. 从第三个数开始，每个数都是前两个数的和。比如0，1，1，2，3，5，8，...
    使用迭代器去生成指定个数的斐波那契数列
"""
# 创建一个斐波拉契数列迭代器
class FibonacciIterator:
    def __init__(self,count):
        self.count = count
        self.cnt = 0
        # 记录前两个数
        self.num1 = 0
        self.num2 = 0
    def __iter__(self):  # 返回本身
        return self
    def __next__(self):
        self.cnt +=1

        if self.cnt <= self.count:
            if self.cnt == 1:
                self.num1 = 0
                return 0
            elif self.cnt == 2:
                self.num2 = 1
                return 1
            else: # 个数大于2情况
                 # 返回前两个数的和
                 sum = self.num1 + self.num2
                 self.num1 = self.num2
                 self.num2 = sum
                 return sum
        else:
            raise StopIteration

fib_iterator =  FibonacciIterator(7)

for i in fib_iterator:
    print(i)