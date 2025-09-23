"""
    静态方法：第一个参数直接是函数的参数列表
    静态方法修饰符： staticmethod
"""

class email:
    a = 1
    def __init__(self,username):
        self.username = username
    @staticmethod
    def is_valid_email(nemail): # 12421412@qq.com
        print("类属性:",email.a)
        if '@' in nemail and '.com' in nemail:
            return True
        else:
            return False
email1 = email("gsdf")
print(email1.is_valid_email("1321321qq.com"))

"""
               类方法           静态方法                 实例方法
    绑定对象     cls               无                    self
    访问属性     cls            可以访问类属性         可以访问类属性和实例属性
    使用场景    操作类属性       工具方法，不操作属性        操作实例属性 
"""
