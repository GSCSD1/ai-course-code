"""
    账号的注册 和 登录
    注册 ： 将账号和密码存入到  user.txt
    登录：  从user.txt匹配账号和密码
"""
print(f"{'登录管理界面':*^20}")
print(f"{'01 注册':^20}")
print(f"{'02 登录':^20}")
choice =  input("请选择你的功能:")
import json
import re
if choice == "1":  # 注册功能
    username =  input("请输入你要注册的账号>>")
    password =  input("请输入你要注册的密码>>")
    user_dict = f"{username}:{password}\n"
    with open("user.txt","a",encoding="utf-8") as f:
        f.write(user_dict)
elif choice == "2": # 登录功能
    username = input("请输入你的账号")
    password = input("请输入你的密码")
    with open("user.txt","r",encoding="utf-8") as f:
        for line in f:
            print(line)
            print(line.split(":")[0].strip('\n'))  #  去除行首和行尾的字符串
            print(line.split(":")[1].strip('\n'))
            if line.split(":")[0].strip('\n') ==username and line.split(":")[1].strip('\n') ==password :
                    print("登录成功")
        # res = f.read()
        # res_list = re.findall(r"['\d]+:[ '\d]+",res)
        # print(res)
        # for res in res_list:
        #     # print(res)
        #     print(res.split(": ")[0])
        #     print(res.split(": ")[1])
