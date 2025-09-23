"""
    类方法：  第一个参数传入cls参数，
    类方法修饰符：@classmethod
    应用场景：方便修改类属性
"""
class Person:
    # 类属性
    name = "zhangsan"
    # 创建类方法
    @classmethod   # 类方法装饰器
    def changeName(cls,name):
        cls.name = name

print(Person.name)
# 调用类方法
Person.changeName("lisi")
print(Person.name)