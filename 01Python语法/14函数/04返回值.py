"""
    return 结束函数  同时返回值给调用方
    不带表达式的return 相当于返回None
"""

# 减法 无return情况会返回None
def sub(x,y):
    print(x-y)

res = sub(3,4)
print(res)

# 返回一个值
def div(x,y):
    if y==0:
        print("除数不能为0")
    else:
        return x/y

res = div(3,2)
print(res)

# 返回多个结果
def calculate(x,y):
    return x+y,x-y,x*y,x/y

res = calculate(3,2)
print(res)
z1,z2,z3,z4 = res
print("calculate",z1,z2,z3,z4)

# 实现计算列表长度的功能
def listLen(mylist):
    ncount = 0
    for i in mylist:
        ncount = ncount+1
    return ncount

print(listLen([1, 2, 45]))
print(listLen([1, 2, 23,64,435,634,545]))

