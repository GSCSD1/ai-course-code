"""
    len   获取序列长度
    max   获取序列最大值
    min   获取序列最小值
    sum   获取序列总和
    sorted  对序列进行排序
    reversed  对序列元素进行反转 返回的是迭代器
    all     当序列里的所有元素都为真（或者序列为空）时，返回 True，否则返回 False。
    any    只要序列中有一个元素为真，就返回 True；只有当序列中的所有元素都为假或者序列为空时，才返回 False。
    enumerate   返回的是一个枚举对象  这个的每个元素是由索引和对应元素组成的元组
    zip      拉链  将多个序列中对应元素进行组合，放到一个元组里面
    map    对可迭代对象中每个元素应用一个指定的函数，返回的是一个迭代器

    filter  根据提供的函数对迭代对象每个元素进行运算，并将运算结果为真的与真的元素以迭代器的方式进行返回
"""

ls1 = [64, 23, 88, 24, 75]
s = "hello"
print(len(s))
print(max(s))
print(min(s))
print(sum(ls1))

print(sorted(ls1))
print(list(reversed(ls1)))
s1  = [1,2,3,0,7]
print(all(s1)) # False
print(any(s1)) # True


s1 = ['a','b','c','d']
s2 = enumerate(s1)  #  0 1 2 3

print("s2:",list(s2))

l1 = [1,2,3,4]
l2 = [4,5,6]
l3 = [7,8,9]
print(list(zip(l1,l2,l3)))  
# 
"""
        语文  数   英
 小明    76   80    90 
 小红    80   30    30 
 小花    90   50    80 
 
 输出 ：
        0 : (76 ,80,90)
        1 : (80 ,30,50)
        2 : (90 ,30,80)
"""
# zip+enumerate  将每一门科目的分数全部输出出来
stu1 = [76,80,90]
stu2 = [80,30,30]
stu3 = [90,50,80]
for  index,nums  in enumerate(zip(stu1,stu2,stu3)):
    print(f'{index}:{nums}')

l1 = ["apple","banana","name"]

print(list(map(sorted, l1)))

l2 = ["apple","banana123","12345"]

print(list(filter(str.isdigit,l2)))
