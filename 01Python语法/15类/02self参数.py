"""
    self：表示对象自身，里面存放着对象的地址。
    如果希望类中的方法可以被对象调用，那么第一个参数必须是self，
    作用就是将对象与类方法进行绑定，这样每个对象都能调用属于自己的方法（实例方法）。
"""
class Dog:
    def Speak(self):
        pass
        # print(f"{self}在说话")
        # self.Speak()
# 实例化对象 self = 自己
dog1 = Dog()
# 实例方法
dog1.Speak()