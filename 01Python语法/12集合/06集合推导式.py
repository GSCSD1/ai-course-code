
"""
    列表推导式 ： 通过简化for循环对已有列表的所有元素进行循环处理得到新的集合
               集合变量名 = {表达式 for 临时变量 in 可迭代对象  if 条件表达式}

"""
ls1 = [1,2,3,4,5]
# 创建一个新列表，对所有元素求平方
# ls2 = []
# for i in ls1:
#     i = i**2
#     ls2.append(i)
# print(ls2)

ls2 = {i**2 for i in ls1 if i**2>9 }
print(ls2)

