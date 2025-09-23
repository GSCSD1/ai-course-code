"""
    with语句 ： 上下文管理器 用于简化资源打开和关闭的过程 ，确保资源不需要时得到适当释放
"""

# with open(r"./test.txt",'r',encoding='utf-8') as f:
#     print(f.read())


# 同时操作多个文件
with open(r"./test.txt",'r',encoding='utf-8') as f1,\
     open(r"./test2.txt", 'r', encoding='utf-8') as f2:
     print(f1.read())
     print(f2.read())