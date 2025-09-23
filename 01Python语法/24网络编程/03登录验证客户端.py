
"""
    账号的注册 和 登录
    注册 ： 将账号和密码存入到  user.txt
    登录：  从user.txt匹配账号和密码
"""

import json
import pickle
import re
import socket



def send(conn_client_socket,data_dic):
    dic_bytes = pickle.dumps(data_dic)
    dic_len = len(dic_bytes).to_bytes(8, byteorder='big')
    conn_client_socket.send(dic_len)
    conn_client_socket.send(dic_bytes)

def recv(conn_client_socket):
    # 接收长度
    byte_len = conn_client_socket.recv(8)
    if not byte_len:
        pass
    # 将字节码转为int类型
    stream_len = int.from_bytes(byte_len, byteorder="big")
    """开始接收数据"""
    dic_bytes = bytes()
    while stream_len > 0:
        # 数据大小小于4096 直接接完所有数据
        if stream_len < 4096:
            temp = conn_client_socket.recv(stream_len)
        # 数据大于4096分块接收
        else:
            temp = conn_client_socket.recv(4096)
        if not temp:
            break
        dic_bytes += temp
        stream_len -= len(temp)
    """字节转字典"""
    # requests_dic = json.loads(dic_bytes.decode("utf8"))
    requests_dic = pickle.loads(dic_bytes)  # 将字节对象反序列化为字典对象
    # print(requests_dic, type(requests_dic))
    return requests_dic

if __name__ == '__main__':
    print(f"{'登录管理界面':*^20}")
    print(f"{'01 注册':^20}")
    print(f"{'02 登录':^20}")
    # 1、创建客户端套接字对象
    # AF_INET IPV4 SOCK_STREAM为TCP通讯方式
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、和服务端建立连接 参数为元组类型
    tcp_client_socket.connect(('127.0.0.1', 2345))
    choice = input("请选择你的功能:")
    if choice == "1":  # 注册功能
        username =  input("请输入你要注册的账号>>")
        password =  input("请输入你要注册的密码>>")
        user_dict = f"{username}:{password}\n"
        data = {
            'mode':'register',
            'user':username,
            'pwd':password
        }
        """json"""
        send(tcp_client_socket,data)

        recv_dict = recv(tcp_client_socket)
        if recv_dict.get('mode') == "register":
            print(recv_dict.get('msg'))

    elif choice == "2": # 登录功能
        username = input("请输入你的账号>>")
        password = input("请输入你的密码>>")
        user_dict = f"{username}:{password}\n"
        data = {
            'mode': 'login',
            'user': username,
            'pwd': password
        }
        send(tcp_client_socket,data)
        recv_dict = recv(tcp_client_socket)
        print(recv_dict)
        if recv_dict.get('mode') == "login":
            print(recv_dict.get('msg'))

