import threading
import traceback
from interface import socket_interface
from multiprocessing import Process

def home():
    print("登录管理界面".center(30,'*'))
    print("01 注册".center(30 ))
    print("02 登录".center(30))


def login(client):
    username = input("请输入你的账号>>")
    password = input("请输入你的密码>>")
    # 将原始内容转换成字典
    data_dic = socket_interface.RequsetData2dic('login', username=username, pwd=password)
    # print(data_dic)
    # 发送数据
    socket_interface.send(client, data_dic)
    data_dic = socket_interface.recv(client)
    data_dic.get('code')
    # print(data_dic)
    return True if data_dic.get('code') == 200 else False,username


def chat_msgRecv(client,user):
    while True:
        data_dic = socket_interface.recv(client)
        print(data_dic.get('time'))
        print(f"{data_dic.get('user')}:{data_dic.get('msg')}")
        print(f"{user}>>>",end="")

def chat(client,user):
    global chat_msgRecv_thread_daemon
    chat_msgRecv_thread_daemon = False
    print("欢迎来到聊天室".center(30,'*'))
    chat_msgRecv_thread = Process(target=chat_msgRecv,args=(client,user))
    chat_msgRecv_thread.start()
    while True:
        msg =  input(f"{user}>>>")
        data_dic = socket_interface.RequsetData2dic('chat', username=user, msg=msg)
        socket_interface.send(client, data_dic)
        if msg == "exit":
            chat_msgRecv_thread.terminate()
            break


if __name__ == '__main__':
    client = socket_interface.client_create('127.0.0.1', 2346)

    while True:
        try:
            # 功能选择页面
            home()
            choice = input("请选择你的功能:")
            if choice=="2":
                ret,user = login(client)  #登录功能
                if ret :
                    chat(client,user)  # 聊天页面

        except ConnectionRefusedError:
            print("服务器未启动")
        except Exception as e:
            print(e)
            # traceback.print_exc()