"""
    count 统计字符串出现的次数
    join  将序列中的元素连接成一个新的字符串
    replace  替换指定的字符串  并且可以指定替换次数
    len() 返回字符串长度
"""

s1 = 4j



s1 = "hello world hello"
# 统计ll字符串个数
print(s1.count("ll"))
#  将_2_字符串和ls1中的字符串进行连接
s1 = "_2_"
ls1 = ["hello","world","hello world"]
print(s1.join(ls1))  # 
s1 = "hello world hello"
print(s1.replace("hello", "Hello",1))
print(len(s1))
