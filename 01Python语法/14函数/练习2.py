
#  实际处理形参的时候，为了防止破坏原有数据，建议提前先拷贝
def my_fun(b):
    b = b.copy()
    b.pop()  # 删除集合在内存中第一个元素
    # print(id(b))    #
    print(b)

a = {54, 64, 123, 5}
help(a.pop)
# my_fun(a)
print(a) # a?
a.pop()
print(a)


# a = 10
a = [10]
b = 20
# c = [a]   # c= [10]  # 存储a的值
c = [a]  # 存储a的引用
a[0] = 100    # a= 15

print(c)