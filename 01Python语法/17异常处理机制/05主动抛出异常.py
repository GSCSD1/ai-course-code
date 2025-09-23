"""
    raise  异常名（错误信息）
"""

import time

# for  i in range(10):
#     print(i)
#     time.sleep(1)
#     raise NameError("手动抛出异常")

def check_age(age):
    if age <0:
        raise Exception("年龄不能为负数")
    elif age <18:
        raise Exception("年龄小于18岁")
    else:
        print("已成年")

try:
    age = 12
    check_age(age)
except Exception as e:
    print(e)
