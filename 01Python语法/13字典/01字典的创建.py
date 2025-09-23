"""
    字典变量名 = {key1:value1,key2:value2,...}
    key:value 称为键值对   key键 value为值
    键 必须不可变   只能为数字、字符串、元组....
    值  任何类型

    无序
"""
"""字典的创建   直接创建"""
# 户口管理系统  姓名 地址  身高 体重 年龄
s1 = ["bob","Changsha",173,100,90]
s2 = ["goudan","Changsha",150,80,89]

# json  = 字典->字符串
person1 ={"name":"bob","address":"Changsha","height":173,
        "weight":100,"age":90}
person2 ={"name":"goudan","address":"Changsha","height":150,
        "weight":80,"age":89}

"""字典的创建   fromkeys  一次性创建创建多个键值对，所有的键都使用指定的值 ，值默认是None"""
# 不指定值的情况
people1 =  dict.fromkeys(["name","address","height","weight","age"])
print(people1)
# 指定默认值的情况
people1 =  dict.fromkeys(["name","address","height","weight","age"],"空")
print(people1)
