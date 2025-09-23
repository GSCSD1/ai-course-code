"""
    类属性： 在类定义时所定义的属性，用来说明类本身
    类属性的访问：类.类属性名  对象.类属性名
    类属性的修改：类.类属性名
"""
class Circle:
    pi = 3.14
    radius = 1.24
    def area(self):
        print(f"{Circle.pi*Circle.radius**2}")

c1 = Circle()
# 类.类属性名
# Circle.radius = 2.48
print(Circle.radius)
# 对象.类属性名
c1.radius = 2.48  # self.redius = 2.48   实例属性

# print(c1.radius)
print(Circle.radius)
