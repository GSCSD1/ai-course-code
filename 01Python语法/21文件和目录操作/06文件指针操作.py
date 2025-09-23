"""
操作文件指针：
    seek(offset,whence)
         offset:偏移量 可正可负，单位为字节  中文为3个字节

    whence：
            0 表示从文件开头
            1 当前文件指针位置
            2 表示从文件末尾
            文本模式下只能使用 0  很重要
读取文件指针：
    tell（）  返回当前文件指针位置，单位为字节

"""


with open('./test2.txt','rb+') as fd:
    # # 移动指针到好后面
    # fd.seek(6,0)  # 光标以起始位置为起点移动6个字节
    # fd.write('world'.encode('utf-8'))
    # print(res)
    fd.seek(2,0) # 移到j后面
    fd.seek(8,1)  # 移到o后面
    print(fd.tell()) # 10
    fd.seek(0, 2) # 移到d后面
    print(fd.tell())   # 13


""" 
    实现文件拷贝功能    
    实现账号密码持久化存储
"""