"""
    read(size=-1)
        在文本模式下： 一次最多读取文件指针后面size大小的字符

        在二进制模式下： 一次最多读取文件指针后面size大小的字节
    注意 ： 文本有非ASCII字符 考虑使用utf-8编码
            二进制模式下没有编码概念
    readline() 从文件中读取单行数据 返回的是字符串类型
    readlines()  从文件中读取所有行  将每一行的数据存到列表中
"""
f =  open('./test.txt','rt',encoding='utf-8')
# print(f.read(2)) # 读取两个字符
# print(f.read()) # 读取所有字符
# print(f.readline()) # 从文件中读取单行数据 返回的是字符串类型
"""分块读出所有数据  （解决大文件读取问题）"""
f =  open('./test.txt','rt',encoding='utf-8')
print(f.readlines())
# 从文件中读取所有行  将每一行的数据存到列表中
# 方法一 只针对文本文件
# while True:
#     res =  f.readline()
#     if res == '':
#         break
#     print(bytes(res,'utf-8'))
#
# print(":",f.readline())
# print(":",f.readline())

# 方法二  只针对文本文件
for line in f:
    print(line)

# 方法三： 通用
while True:
    res =  f.read(1024)
    if res == '':
        break
    print(res)
