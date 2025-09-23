"""
    in 和 not in  用来判断键是否在字典中
"""
boy ={"name":"bob","height":173, "weight":100}

if "hfd" in boy:
    boy["name"] = "TOM"

else:
    print("键不在字典中")

print( boy)