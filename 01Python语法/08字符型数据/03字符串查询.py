"""
        find : 从左往右找指定的字符串 ，找到则返回第一个结果对应的索引，否则返回-1
        index: 从左往右找指定的字符串 ，找到则返回第一个结果对应的索引，否则报错
        rfind ： 从右往左找指定的字符串 ，找到则返回第一个结果对应的索引，否则返回-1
        rindex 从右往左找指定的字符串 ，找到则返回第一个结果对应的索引，否则报错
"""
s1 = "西瓜-杨梅-榴莲"
# 检测输入
userFruit =  input("请输入你想要的水果:")
# res =  s1.find(userFruit)
res =  s1.index(userFruit)
if res != -1:
    print(f"找到了{userFruit}位置:{res}")
else:
    print("没有找到")