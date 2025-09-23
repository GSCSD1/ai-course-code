
# 自定义异常
class Myexception(Exception):
    def __init__(self,message,error_code=None):
        super().__init__(message)  # 初始化父类中的参数
        self.error_code = error_code

try:
    raise Myexception("自己定义的异常",101)
except Myexception as e:
    print(e) # 输出提示信息
    print(e.error_code)

