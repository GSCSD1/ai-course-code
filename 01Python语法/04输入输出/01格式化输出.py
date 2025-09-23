"""
    格式化输出：
                上古时代    % 格式化
                近代       format输出
                现代       f-string输出
"""
# 直接输出
print("hello")
print(12)
name = "老王"
print("隔壁",name,"来敲门了")
#版本一 上古时代    % 格式化  能凑合用  缺点：需要记住大量的符号 %s(string) %d(decimalism)
name = "阳哥"
age = 18
print("大家好,我叫 %s,今年 %d 岁"%(name,age))
#版本二  近代       format输出
print("大家好,我叫 {},今年 {} 岁".format(name,age))
#版本三 现代       f-string输出
print(f"大家好,我叫 {name},今年 {age} 岁")

# 对齐与填充
"""
    *******购物管理系统********
    ******01用户登录**********
    ******02用户注册**********
    *****03商品列表页面********
"""
print("*******购物管理系统********")
print("******01用户登录**********")
print("******02用户注册**********")
print("******03商品列表*********")

print(f'{"left":<10}')  # 宽度为10 左对齐
print(f'{"right":>10}')  # 宽度为10 右对齐
print(f"{'center':^10}") # 宽度为10 居中对齐
print(f'{"fill":@^10}') # 用@

print(f'{"购物管理系统":*^20}')
print(f'{"01用户登录":^20}')
print(f'{"02用户注册":^20}')
print(f'{"03商品列表页面":^20}')
print(f'{"底部":*^20}')

# 格式化数字
pi = 3.141592653589793
print(f"π 约等于 {pi:.2f}")  # 保留小数位数

money = 100_000_000
print(f"{money:,}")   # 千位分隔符

percet = 0.75#  print(f'{percet*100}%')
print(f"{percet:.0%}")

"""
    print(*args, sep=' ', end='\n', file=None, flush=False)
     sep : 在值与值之间插入字符串 默认是空格
     end : 在值最后后插入字符串，默认为换行
     
"""


# help(print)
name = "老王"
# print("隔壁",name,"来敲门了",sep="*")

print(1)
print(2,end='')


#  print 最终调用是sys.stdout.write() 函数

import sys
sys.stdout.write("hello")
sys.stdout.write("hello")