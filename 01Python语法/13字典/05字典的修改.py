"""
        通过键来改一个元素

        update  通过键来改多个个元素
"""
boy ={"name":"bob","height":173, "weight":100}
boy["height"] = 18
print(boy)


dict1  = {"weight":50,"name":"TOM"}
boy.update(dict1)
print(boy)