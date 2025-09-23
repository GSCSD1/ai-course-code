"""
    pop   通过键能删除对应的元素  返回要删除键对应的值
    popitem 随机弹出一个键值对 在python3.7之后 弹出最后一个
    del   既能删除整个字典 也能通过键能删除对应的元素
    clear  清空字典
"""
boy ={"name":"bob","height":173, "weight":100}

# del boy["name"]
# print(boy.pop("name"))
# print(boy.popitem())
boy.clear()
print(boy)

ls=[1,2,3,45,4]
# print(ls.pop())
help(ls.pop())