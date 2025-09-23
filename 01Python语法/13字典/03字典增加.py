"""
        setdefault  增加一个键值对/元素  键存在函数无效
        通过键来增加元素  键不存在则添加成功 键存在会修改键对应的值

        update  合并两个字典，重复的键会覆盖
"""
boy ={"name":"bob","height":173, "weight":100}
#1、  setdefault增加 键值对
# boy.setdefault("age",18)
#2、  通过键来增加元素  键不存在则添加成功 键存在会修改键对应的值
# boy["age"] = 18
boy["height"] = 18

# 3、
dict1  = {"phone":"133xxxxx","address":"Changsha1","name":"TOM"}
boy.update(dict1)
print(boy)