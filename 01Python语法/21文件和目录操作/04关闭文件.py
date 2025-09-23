"""
    close : 释放文件资源
    操作系统每隔一段时间会扫描文件系统，如果发现有没使用的文件会自动帮我们关闭
"""

res =  open(r"./test.txt",'a')
print(res)
res.close()