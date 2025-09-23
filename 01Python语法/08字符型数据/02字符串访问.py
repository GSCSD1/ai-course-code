"""
    1、下标访问(访问单个元素)  索引值>0 从左到右访问 索引值<0 从右到左访问
    2、切片 (访问多个元素)
    [start:stop:step=1]  [start,stop)
    3、字符串不可变  不能增删改
"""

# s1 = "hello world" # 'hello world'
# # 取出第二个元素
# print(s1[1])
# # 取出倒数第二个元素
# print(s1[-2])
# # 访问前5个元素
# print(s1[0:5])
# print(s1)
# # 逆序取出元素
# print(s1[-1::-1])
# print(s1[::-1])
# #  取出 lrow
# print(s1[-2:-6:-1])
s1 = "hello world" # 'hello world'
#ell  el
print(s1[1:3])
#wor  wo
print(s1[-5:-3])
#“”
print(s1[-7:-3:-2]) # start = ’o'  stop =  'r'
# hello
print(s1[:5])
# “”
print(s1[2:5:-1]) # start = ’l'  stop =  ' '
# llo worl
print(s1[2:10:1])
# "hello world"
print(s1[:100:]) # start = ’h'  stop =  “”


s1 = "hello world"
# hello world
print(s1[::]) # start = 0  ,stop = 11, step =1
# eoo
print(s1[1:9:3])
#row ol
print(s1[8:2:-1])
#""
print(s1[2:8:-1])