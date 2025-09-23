

# 导入python编译器模块
import py_compile
# 导入操作系统模块
import os

# 指定要编译的python文件
source_file = "01python程序转字节码.py"

# 指定要存放字节码文件的路径
target_dir = './pyc_files'

# 将python文件转成字节码文件
py_compile.compile(source_file,cfile=os.path.join(target_dir,'main.pyc'))

