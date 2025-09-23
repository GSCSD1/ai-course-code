"""
    创建目录 ：
                 os.mkdir(path)  创建单个目录 存在则报错
                 os.makedirs(path)  创建多级目录  存在则报错
"""
import os
# os.mkdir('./test1')  # 创建单个目录
# os.makedirs('./dataset/train/images')  #创建多级目录

"""
    获取当前目录 ： os.getcwd()
    改变当前目录 ： os.chdir(path)
"""
# print(os.getcwd())
# # os.chdir('../')
# os.chdir(r'C:\Users\33122\Desktop\01Python语法')
# print(os.getcwd())

"""
    列出目录中的内容： os.listdir()   获取到的内容会以列表形式返回，元素类型为字符串类型
"""
# print(os.listdir('./'))

"""
    重命名目录: os.rename(src, dst)  src：原路径   dst ： 重命名之后的路径
"""
# os.rename("./dataset/train", "./dataset/test")

"""
    检查路径是否为文件   os.path.isfile()  
    检查路径是否为目录   os.path.isdir()  
"""
print(os.path.isdir('./test1'))
print(os.path.isfile('./test.txt'))


"""
    路径拼接：  拼接路径  
    os.path.join
    根据操作系统的文件系统约定来正确处理路径分割符
"""
# 将 C:\Users\33122\Desktop\01Python语法\21文件和目录操作\  和    test1 拼接
path1 = "C:\\Users\\33122\\Desktop\\01Python语法"
path2 = "21文件和目录操作"
# print(path1 + path2)
print(os.path.join(path1,path2))


"""
    路径拆分 ：  将路径分割成两部分  路径和文件名
    os.path.split()
"""
print(os.path.split(r"C:\Users\33122\Desktop\01Python语法\21文件和目录操作\1.png"))


"""
    获取文件的绝对路径  os.path.abspath()
    检查路径是否存在   os.path.exists()
"""
print(os.path.abspath('./test.txt'))

print(os.path.exists('./test2'))