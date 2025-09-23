"""
    实例属性 ： 属于对象本身的属性，存在于__init__函数中，在对象创建时会赋值给该对象

    # 对象能访问类属性和实例属性  但是无法修改类属性

    实例属性的访问  ： self.实例属性名   对象.示例属性名
    实例属性的修改  ： self.实例属性名   对象.示例属性名
"""

class Person:
    # 类属性
    a = 1
    def __init__(self, name, age,gender):
        # 实例属性  self.实例属性名 修改值
        self.name = name
        self.age = age
        self.gender = gender

    def changeName(self, name):
        self.name = name


person1 = Person("zhangsan",1,'男')
print(person1.name)
print(person1.age)

#对象.示例属性名修改值
person1.name = "lisi"
print(person1.name)

"""

                        实例属性                                           类属性
定义方式               self.实例属性名                                     类中定义变量
存储位置         存在每个对象的内存中，每个对象的实例属性是独立的              存在的是共享内存区域
访问方式                  对象                                                类，对象
作用范围           每个对象独立，修改仅影响该对象                      对所有对象共享，修改影响所有对象
生命周期           随着对象的生命周期存在                                   随类的生命周期存在
修改权限                  对象                                                类
使用场景             每个实例独有的属性                                对于所有实例（对象）共有属性或者常量
"""

