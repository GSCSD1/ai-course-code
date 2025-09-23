"""
    split(obj,n=-1)  从左到右以obj字符串进行分割n次  列表形式进行返回
    split(obj="\n“) = splitlines  以"\n进行分割"

    partition(obj)  从左到右以obj字符串进行分割，分割成三个部分  前部分 obj字符串  后部分
    rpartition(obj)  从右到左以obj字符串进行分割，分割成三个部分  前部分 obj字符串  后部分
"""

s1="15:38:56"
res = s1.split(":",1)
print(res)
# print(f"hour:{res[0]} min:{res[1]} sec:{res[2]}")

# s1 = "张三,王五，李四,王五,赵六,麻子"
# print(s1.partition("王五"))

# print(s1.rpartition("王五"))