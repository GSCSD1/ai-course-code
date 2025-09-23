"""
    pow(x,y)   返回的是x的y次方   =  a**b
    abs(x)   返回的是绝对值
    round(a,b)   a为要操作的对象  b为保留小数位数
       保留小数点后面的位数
    help()  查看函数说明文档
"""
# 根据函数名字查看文档
# help(pow)
ls = [1,2,3]
help(ls.sort)
# 通过交互界面查询文档
# help()

a = 3
b = 2
print(pow(a, b)) # 9
print(abs(-3))
print(abs(-3.14159))
print(round(3.14159, 2))
