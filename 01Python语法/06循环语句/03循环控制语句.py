"""
    break  立即结束本层循环
    continue   终止本次循环，继续下一轮循环
    pass  为空语句   为代码使用进行占位，防止语法报错
    while 循环条件：
        代码块
    else:
        循环结束时执行(没有被break打断)
"""

# breaak

# i = 1
# while i<=10:
#     if i == 5:  # 1 2 3 4
#         i+=1
#         break  # 立即结束本层循环
#     print(i)
#     i+=1
# else:
#     print("循环结束")
#
#
# i = 1
# while i<=10:
#     if i == 5:  # 1  2  3  4  6  7 8 9 10  循环结束
#         i+=1
#         continue  # 终止本次循环，继续下一轮循环
#     print(i)
#     i+=1
# else:
#     print("循环结束")


# i = 1
# while i<=10:
#     if i == 5:  #1 2 3 4 7 8 9 10循环结束
#         i+=2
#         continue  # 终止本次循环，继续下一轮循环
#     print(i)
#     i+=1
# else:
#     print("循环结束")


# i = 1  # 1 2 3 4
# while i<=10:
#     if i == 5:
#         i+=2
#         continue  # 终止本次循环，继续下一轮循环
#     if i == 7:
#         break
#     print(i)
#     i+=1
# else:
#     print("循环结束")

i = 1  # 1 2 3 4  5 6
while i<=10:
    if i == 7:
        break
    print(i)
    i+=1
else:
    print("循环结束")

while True:
    pass