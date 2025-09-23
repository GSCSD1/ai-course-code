"""
    pop  通过下标来删除单个元素，返回删除的结果
    remove 通过值来删除单个元素  如果需要删除的元素不存在则报错
    clear  清空
    del  删除对象
"""
ls1 = [10,7,55,33,3]
del ls1[1]
print(ls1)
print(ls1.pop(3))
ls1 = [10,7,55,7,3]
ls1.remove(7)
ls1.remove(7)
print(ls1)
ls1.clear()
print(ls1)


l1 = [3,4,5,6]
l1[:3] = [1,1,1]
print(l1)