"""
    sort  对元素进行排序
    reverse  反转列表中的元素
"""
ls1 = [12421,32,236,23,6235,6,325,123]
# sort  默认是升序
ls1.sort(reverse=True)
print(ls1)


# reverse   反转列表中的元素
ls1 = [12421,32,236,23,6235,6,325,123]
ls1.reverse()
print(ls1)


# 深拷贝
import copy
ls1 = [[12,32],5,6,87,23]
ls2 = copy.deepcopy(ls1)
# ls2 = ls1.copy()

ls1[0][0] = 100
print(ls1)
print(ls2)


