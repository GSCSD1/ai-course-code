
"""
  一般情况以kwargs作为关键字不定长参数的标志   将关键字不定长转为字典类型
    这个参数将输入的关键字当做键值对的键，将关键字的实参当做
    键值对的值
"""

# kw  keyword
def fun1(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

fun1(name="zhangsan",age=10,weight=70,height = 170)

#对传入的参数的值进行相乘
def mul(**kwargs):
    res=1
    for i in kwargs.values():
        res=res*i
    print(res)

mul(a=1,b=2,c=3)
mul(a=1,b=2,c=3,d=12,e =0 )

"""
    注意：kwargs永远放在最后
"""
def test(x,y,z,*args,**kwargs):
    print(x, y, z)
    print(args)
    print(kwargs)

test(1,2,3,4,5,6,a=2,b=3,c=5)


# 关键字参数解包

def test(x,y,z,n):
    print(x, y, z,n)

# a = (1,2,3,4)
a = {"z":3,'x':1,'y':2,'n':4}
# test(*a)
test(**a)