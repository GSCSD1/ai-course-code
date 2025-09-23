"""
     面向过程编程（opp）Oriented Procedure  Programming

     自己做菜
     买菜  洗菜  切菜 开火 倒油  炒菜  加盐  出锅

     面向过程以“过程/函数”为中心编程思想。强调通过一系列顺序来完成任务
     数据和操作时分离的

     面向对象编程(oop) Oriented  Object  Programming
     餐厅点菜
     服务员  厨师    用户
     面向对象是以对象为中心的编程思想。
     对象是由数据和操作方法组成
      程序被视为一组互相交互的对象，这些对象通过方法来操作内部的数据，从而实现功能
"""
#  编程 ：面向数据和功能
# 面向过程：一切流程化  执行细节
# 面向对象： 一切框架化   顶层设计   高级容器：数据类型 方法以及方法定义


# 为什么需要对象， 水果店管理系统
#
# shopping_name = "葡萄"
# shopping_jingjia = 3
# shopping_price = 5
# shopping_zhekou = 0.8
#
# # 输出商品信息
# print(f"{shopping_name}:{shopping_jingjia}:{shopping_price}:{shopping_zhekou}")
# shopping_price = 8
#
# # 用户会员卡
# user_name ="lisi"
# user_money = 100
# user_level = 3
#
#
# print(f"{user_name}:{user_money}:{user_level =}")
#
# user_name ="zhangsan"
# print(f"{user_name}:{user_money}:{user_level =}")

"""
    功能和功能之间没有明显的区分 不好管理，代码维护成本巨大
"""
#
# shopping_name = "葡萄"
# shopping_jingjia = 3
# shopping_price = 5
# shopping_zhekou = 0.8

# shopping_name = "橘子"
# shopping_jingjia = 2
# shopping_price = 3
# shopping_zhekou = 0.8
#
# # 展示商品信息
# def show_shopping_info():
#     print(f"{shopping_name}:{shopping_jingjia}:{shopping_price}:{shopping_zhekou}")
#
# # 设置水果价格
# def set_shopping_price(price):
#     global shopping_price
#     shopping_price = price
#
# set_shopping_price(10)
# show_shopping_info()
#
#
# # 用户会员卡
# user_name ="lisi"
# user_money = 100
# user_level = 3
#
# # 输出用户信息
# def show_user_info():
#     print(f"{user_name}:{user_money}:{user_level}")
#
# # 设置会员名
# def set_user_name(name):
#     global user_name
#     user_name = name
#
# set_user_name("zhangsan")
# show_user_info()

"""各个模块在一起还是比较乱   分类   """
# 管理商品的模块  怎么做到分类
"""类的定义  高级容器   类：存放的同类共有的数据和功能"""
class Fruit:
    # 类属性  ： 负责存放对象里面共有的属性
    shopping_name = "葡萄"
    shopping_jingjia = 3
    shopping_price = 5
    shopping_zhekou = 0.8
    # 方法 : 责存放对象里面共有的方法
    # 展示商品信息
    def show_shopping_info(self):
        print(f"{Fruit.shopping_name}:{Fruit.shopping_jingjia}:{Fruit.shopping_price}:{Fruit.shopping_zhekou}")

    # 设置水果价格
    def set_shopping_price(self,price):
        Fruit.shopping_price = price

# print(Fruit.__dict__)
#
# #查看shopping_name
# print(Fruit.__dict__['shopping_name'])
# #查看shopping_name
# print(Fruit.__dict__['shopping_jingjia'])
# # 调用show_shopping_info()
# Fruit.__dict__['show_shopping_info'](None)
# Fruit.__dict__['set_shopping_price'](None,30)  #   = Fruit.set_shopping_price(None,30)
# Fruit.set_shopping_price(None,10)
# # Fruit.__dict__['show_shopping_info'](None)
# Fruit.show_shopping_info(None)
#
# """类的使用 """
# apple =  Fruit()
# apple.shopping_name = "苹果"
# apple.shopping_jingjia = 4
# apple.shopping_price = 6
# apple.shopping_price = 0.7
# print(apple.shopping_name)
# print(apple.shopping_jingjia)
# print(apple.shopping_price)
# print(apple.shopping_zhekou)
#
# orange =  Fruit()
# orange.shopping_name = "橘子"
# orange.shopping_jingjia = 2
# orange.shopping_price = 5
# orange.shopping_price = 0.7
# print(orange.shopping_name)
# print(orange.shopping_jingjia)
# print(orange.shopping_price)
# print(orange.shopping_zhekou)





# 创建类
"""
    创建类：
        class 类名：
                类属性 : 存放对象里面共有的属性
                类方法 ： 存放对象里面共有的方法
"""

"""
    对象与类之间的关系：
            1、对象拥有类全部的属性和方法
            2、对象的属性和行为可以单独进行增加、删除、修改
            3、对象不能单独创建，必须依托于类的实例化，一个类可以实例化多个对象
            4、对象之间的类属性共享，方法不共享
"""
class car:
    # 类属性
    ncolor = None
    nspeed = None

    # 类中的方法
    def setSpeed(self):
       pass

    def setColor(self):
        pass

""" 通过类创建对象 类名() 类的实例化   car1就是对象  lbjl-兰博基尼 """
lbjl = car()
# 对象属性独立
lbjl.ncolor = "red"
# 类属性  类.属性名
car.ncolor = "red"
bm = car()
bm.ncolor = "blue"
car.ncolor = "blue"
car3 = car()
car3.ncolor = "green"
car.ncolor = "green"


# 类属性
print("car.ncolor",car.ncolor)


# 访问对象中的属性
print("lbjl.ncolor",lbjl.ncolor)
print(lbjl.nspeed)
# 访问对象中的方法
lbjl.setSpeed()
lbjl.setColor()

""" 增加对象的属性   """
lbjl.price = 1_000_000
print("lbjl价格：",lbjl.price)
# print(car.price)  错误访问方式

""" 删除对象的属性   """
# del lbjl.price
# print("lbjl价格：",lbjl.price)

""" 修改对象的属性   """
lbjl.price = 5_000_000
print("lbjl价格：",lbjl.price)

"""  增加对象的函数   """
def mysetPrice(self,price):
    print("price为:",price)

from types import MethodType
# 第一个参数为要加入的函数，第二个参数为要操作的对象
lbjl.mysetPrice =MethodType(mysetPrice,lbjl)
lbjl.mysetPrice(100)

# 对象之间方法不共享
car3.mysetPrice(100)
# car2 = car()
# car3 = car()
