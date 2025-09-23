"""
    列表增加 ：
                append()  向列表尾部追加一个元素
                extend()  向列表尾部追加多个个元素
                insert(index,object)         向列表位置插入元素

"""

#  append()
# def fun1():
#     print("hello word")
# ls1= [1,2,3]
# ls1.append(4)
# ls1.append([1,2,3])
# ls1.append(3.523)
# ls1.append(fun1)
# print(ls1)

#  extend()
# ls1= [1,2,3]
# ls1.extend([4, 5, 6])
# print(ls1)

# insert()
ls1= [1,2,3]
# 往头部追加一个"hello"
ls1.insert(0, "hello")
print(ls1)
