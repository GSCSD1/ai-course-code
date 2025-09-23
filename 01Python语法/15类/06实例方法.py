"""
    实例方法：  第一个参数传入self参数，那么该函数就是实例方法
    实例方法调用 ： 对象.方法
"""

class Person:
    # 类属性
    def __init__(self, name, age,gender):
        # 实例属性  self.实例属性名 修改值
        self.name = name
        self.age = age
        self.gender = gender

    def changeName(self, name):
        self.name = name

    def changeAge(self, age):
        self.age = age

person1 = Person("zhangsan",22,"男")

person1.changeName("lisi")

person1.changeAge(20)
print(person1.name)
print(person1.age)
