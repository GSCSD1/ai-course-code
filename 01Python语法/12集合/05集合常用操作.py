"""
     交  并    补
     & intersection  求交集      求公共部分
     | union         求并集      两个集合所有元素
     - difference    求补集      值在全集中属于A之外的元素组成的集合

     issubset        两个集合是不是子集关系
     issuperset      两个集合是不是父集关系
"""
my_set1 = {1,2,3}
my_set2 = {1,2,3,4}
print(my_set1 &  my_set2)
print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))
print(my_set2.difference(my_set1))
print(my_set1.issubset(my_set2))
print(my_set2.issuperset(my_set1))

my_set2 = {1,2,3,4}
# 集合没有+ *运算符操作
# {1,2,3}+{1,5} = {1,2,3,5}
# print({1,2,3}+{1,5})
# {1,2,3}*2 = {1,2,3}
# print({1,2,3}*2)

# 集合不能被嵌套&
print({1,2,4}) # 不可哈希       不可变元素才能被哈希  哈希值是唯一 不可逆