"""
        字典的访问 ；
                    1，通过键来访问  键不存在会报错
                    2、get（key,default）  键不存在不会报错 会返回default中的值   setdefault

"""

boy ={"name":"bob","height":173, "weight":100}
"""通过键来访问"""
# 查询身高
# print(boy['height'])
# print(boy['name'])
# # 键不存则会报错
# print(boy['age'])
"""get来访问  查询是否有age这个键"""
res  = boy.get('age',"空")
if res == "空":
    # 字典的增加
    boy.setdefault('age',18)
print(boy)
# print(boy.get('age',"空"))

