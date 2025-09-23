"""
    write(text) : 将text内容覆盖到当前文件指针位置的后面，并将文件指针移动到新写入的
    位置，返回写入的字符数量。
    注意：写入其他类型的对象时，要先将他们转换为字符串或字节对象
    writelines： 参数为列表，元素为指针后面要写入的内容
    注意 ： 有中文情况下 读写模式下都需要 指定utf-8编码
"""
# a模式下打开文件
# f =  open('./test.txt','a',encoding='utf-8')
# res =  f.write("hello 你好")
# f.writelines(["123","456"])
# help(f.writelines)



# 二进制模式下读写
""" 字节对象与字符串互相转换"""
# f =  open('./test.txt','rb')
# # 字节对象转换为字符串
# print(f.read().decode('utf-8'))
# # 字符串转换为字节对象
# print("hello world".encode('utf-8'))

f =  open('./test.txt','ab')
res =  f.write("hello 你好".encode('utf-8'))