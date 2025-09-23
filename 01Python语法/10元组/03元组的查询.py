"""
    count  查询列表中某个元素数量
    成员运算符 in  not in   元素是否在指定容器中
    index()  值来查索引，未查到则报错
"""

ls1 = (1,2,3,2,3,4)
# count 查询 2 有多少个
print(ls1.count(2))
print(len(ls1))
# 判断2是否在列表中
print(2 in ls1)
print(5 not in ls1)

print(ls1.index(3))
