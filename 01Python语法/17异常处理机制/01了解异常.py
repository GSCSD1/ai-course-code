"""
    异常： 是一个事件，会在程序执行过程中产生，影响程序的正常执行

    一般情况下，python遇见错误的代码或者无法正常处理的程序就会产生一个
    异常并抛出。异常抛出后，可以捕获，捕获后的程序会按照某种机制继续执行，
    如果对抛出的异常不做任何处理，那么程序程序会终止运行

        KeyboardInterrupt : 用户主动结束程序时触发
        AttributeError : 尝试访问对象没有的属性时 触发
        TypeError   : 操作非法类型数据时触发
        indexError : 访问不存在的索引时触发
        KeyError :   映射中没有键时触发
"""
import  time
# 用户主动结束程序时触发
# for i in range(10):
#     print(i)
#     time.sleep(1)
# 尝试访问对象没有的属性时
# my_string = "abdefg"
# print(my_string.hdf)

# 操作非法类型数据时触发
# a = "hello"
# b = 5
# print(a+b)

# 访问不存在的索引时触发
# my_list = [1,2,3]
# print(my_list[5]) # indexError

# KeyError
my_dict = {"name":"Alice",'age':10}
my_dict['address'] = "changsha"  # 元素增加
print(my_dict['address'])
