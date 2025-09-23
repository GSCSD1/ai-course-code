"""
    update(iterable)  传入可迭代对象  实现增加多个元素

    add      实现增加1个元素
"""
# 单个元素添加
my_set = {4,2,3,4,5}
# my_set.add("hello")
# my_set.add(123)


# 多个元素添加
# ls1 =  ["123",(333,444),True]  # True等价于1
# for  i  in  ls1:
#     my_set.add(i)
# my_set.update(["123",(333,444),True])
# my_set.update(("123",(333,444),True))
my_set.update({"123",(333,444),True})
print(my_set)