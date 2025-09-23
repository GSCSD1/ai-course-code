"""
    remove() 删除指定的元素  不存在会报错
    pop()    删除集合对象中第一个元素
    discard() 删除指定的元素  不存在不会报错

    del  删除对象 无法指定下标中的元素
    clear

"""

set1 = {1,2,4,5,6}
"""删除单个元素"""
# remove 删除流程
# for i in  ls1:
#     if i==4:
#          # 找到4对应的内存地址
#          # 释放内存
#         del ls1[i]

# ls1.remove(50)
set1.discard(50)
print(set1)

"""删除所有元素"""
set1 = {1,2,4,5,6}
# del ls1
set1.clear()
print(set1)
