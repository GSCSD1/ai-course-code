import os
import time

# 获取文件大小  os.path.getsize
nsize =  os.path.getsize('./user.txt')
print(nsize)

# 获取文件最后修改时间 os.path.getmtime
lastmTime_sec =  os.path.getmtime('./user.txt')  # 获取自1970年1月1日以来经过的秒数
lotime =  time.localtime(lastmTime_sec)  #转换为时间结构体
# 转换为字符串
res=  time.strftime("%Y-%m-%d %H:%M:%S", lotime)
print(res)


# 获取文件创建时间    os.path.getctime
createTime_sec =  os.path.getctime('./user.txt')  # 获取自1970年1月1日以来经过的秒数
lotime =  time.localtime(createTime_sec)  #转换为时间结构体
# 转换为字符串
res=  time.strftime("%Y-%m-%d %H:%M:%S", lotime)
print(res)

# 获取文件最后访问时间  os.path.getatime   # access
accTime_sec =  os.path.getatime('./user.txt')  # 获取自1970年1月1日以来经过的秒数
lotime =  time.localtime(accTime_sec)  #转换为时间结构体
# 转换为字符串
res=  time.strftime("%Y-%m-%d %H:%M:%S", lotime)
print(res)