"""
    python文件  - > 字节码
    字节码 -> cpython解释器 （c语言实现）
    c -> 汇编 -> 机器码    字节码  ： python版本号+时间戳+操作码(字节码)
"""
import dis

def hello():
    print("hello world")

# hello()
# 查看函数编译后的指令内容
dis.dis(hello)