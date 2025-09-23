
# 迭代器 ： 重复取值/遍历数据 工具

# 如果并没有提供迭代器功能
I_1 = ['A','B','C','D','E']
I_2 = ('A','B','C','D','E')
str1 = "hello world"
set1 = {30,80,700,1000,1200}
# dict1 = {"name":'job',"age":10}
# index = 0
# dict1_tmp = list(dict1.items())
# print(dict1_tmp)
# while index<len(dict1):
#     # tmp = set1.pop()
#     print(dict1_tmp[index])
#     # set1.add(tmp)
#     # print(set1[index])
#     index+=1

#  碰到没有索引的数据类型会导致遍历数据方法不统一


dict1 = {"name":'job',"age":10}

# 将字典转换为迭代器对象
dic_iter = dict1.__iter__() # 如果数据类型里面有__iter__方法被称为可迭代对象
print(dic_iter==dic_iter.__iter__())
# print(dic_iter)
# print(dic_iter.__next__())
# print(dic_iter.__next__())
# print(dic_iter.__next__())

"""
    迭代器对象的特点： 
               迭代器： 1、内置__iter__()方法，内置__next__()
                       2、迭代器可以调用__iter__方法,得到的还是迭代器。
                迭代器调用next方法，会迭代下一个值
    可迭代对象不一定就是迭代器   。例子 ： 列表是典型的可迭代对象，但不是迭代器对象 
"""
# 通过迭代器实现遍历数据

def iterFun(obj):
    """方法一"""
    # 将容器转为迭代器
    # my_iter = obj.__iter__()
    # count = 0
    # while count<len(obj):
    #     # 迭代值
    #     print(my_iter.__next__())
    #     count = count + 1
    """方法2   for循环底层原理"""
    # 将容器转为迭代器
    my_iter = obj.__iter__()
    while True:
        try:
            # 迭代值
            print(my_iter.__next__())
        except StopIteration:
            break

iterFun(I_1.__iter__().__iter__().__iter__())


"""
    for i in [1,2,3]:
        print(i)
    
    先将可遍历对象转为迭代器，循环调用迭代器next()函数，每次获取一个元素并赋值给临时变量i，当迭代器中没有
    更多元素时，next会抛出StopIteration异常，for循环捕获异常后自动终止
"""

