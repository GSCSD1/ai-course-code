"""
    for 临时变量 in 可遍历对象:
        代码块

    1、迭代器，遍历可迭代数据  列表 字符串 元祖  集合
    2、有循环周期的场景 常与range配合
"""
# 1、迭代器，遍历可迭代数据
str1 = "1234567abcdef"
for s in str1:
    print(s)
ls1  = [12,43,"name",123]
for s in ls1:
    print(s)

# 2、 有循环周期的场景
# 输出1-100
# python3 空间上做了优化 range(start , stop step=1) 返回的一个迭代器 给了一只能下100个蛋的鸡    start:起始值 stop：结束值 step:步长 [start,end)
# python2 range(start , stop step=1)  返回的是一个列表  匡里面装了100个鸡蛋
print(list(range(1,101,1)))
for i  in  range(1,101):
    if i %2 == 0:
        print(i)

# for +  range
"""
    输出1-1000内所有水仙花数
    水仙花：每个位的三次方之和为数据本身
"""
for i in range(1,1001):  # 1234
    g =  i%10//1  # i//1%10
    s =  i%100//10  # i//10%10
    b =  i%1000//100 #  i//100%10
    q =  i%10000//1000 #  i//1000%10
    if i == g**3 + s**3 + b**3 + q**3:
        print(i)