"""
        实现登录和注册  注册的账号和密码保存在字典中
"""
#  用户数据存储 - 使用字典来保存用户名和密码
users = {}
import sys
while True:
    print(f"{'用户管理系统':*^20}")
    print(f"{'01注册':^20}")
    print(f"{'02登录':^20}")
    print(f"{'03退出':^20}")
    choice = int(input("请选择操作 (1-3):"))

    if choice == 1:
        print(f"{'注册功能':*^20}")
        username = input("请输入用户名:").strip() # 去掉字符串首尾的空格
        password = input("请输入密码:").strip() # 去掉字符串首尾的空格

        users[username] =  password
        print(f"注册成功，欢迎{username}")
        print(users)
    elif choice == 2:
        print(f"{'登录功能':*^20}")
        username = input("请输入用户名:").strip()  # 去掉字符串首尾的空格
        password = input("请输入密码:").strip()  # 去掉字符串首尾的空格
        res = users.get(username,-1)
        if res==password:
            print(f"登录成功，欢迎回来 {username}")
        else:
            print("用户名或密码错误")
    elif choice == 3:
        sys.exit(0)

