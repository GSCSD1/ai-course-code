"""
    实现多人聊天室功能：
        1、服务端能记录在线人数  在线(登录到服务器)
        2、用户聊天之前需要先登录
        3、登录成功的用户可以发送消息到聊天室，所有在线用户都能接收到消息，消息需包含发送者用户名和发送时间。
        4、退出机制：用户输入 exit 退出聊天室，关闭客户端与服务端的连接。
        消息格式：消息以字典形式传输，包含 mode（操作类型，如注册、登录、聊天）、user（用户名）、msg（消息内容）、time（发送时间）等字段。
    示例输入输出：
        ********登录管理界面********
               01 注册
               02 登录
        请选择你的功能: 1
        请输入你要注册的用户名>>Alice
        请输入你要注册的密码>>123456
        注册成功！
        ********登录管理界面********
               01 注册
               02 登录
        请选择你的功能: 2
        请输入你的账号>>Alice
        请输入你的密码>>123456
        登录成功！
        ********欢迎来到聊天室********
        Alice>>>Hello, everyone!
        2025-7-22-1-26-30
        Alice:Hello, everyone!
        2025-7-22-1-26-32
        Bob:Hi, Alice!
        Alice>>>
"""
import time
import traceback

from interface import socket_interface
from interface import user_interface
from threading import Thread
from interface import commom

# 存储所有的客户端sock对象
sockets_list = []

def login_request(conn_socket,data_dict):
    is_valid = user_interface.login(data_dict.get("user"), data_dict.get("pwd"))
    # print(is_valid)
    if is_valid:
        socket_interface.in_server()  # 记录在线人数
        for socket in sockets_list:
            if socket.get("socket_handle") == conn_socket:
                socket["status"] = True    # 记录登录状态

    status_code = 200 if is_valid else 400
    msg = "登录成功！" if is_valid else "登录失败！"
    data_dic = socket_interface.ResponseData2dic('login', code=status_code, msg=msg)
    socket_interface.send(conn_socket, data_dic)
    # 获取年月日时分秒
    ntime = time.time()
    lotime = time.localtime(ntime)  # 转换为时间结构体
    # 转换为字符串
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", lotime)
    print(f"{ip_port} - - {data_dict} - - {str_time} 'login' {data_dic} 在线人数:{socket_interface.getClientNum()}")

def chat_request(conn_socket,data_dict):

    username = data_dict.get("user")
    msg = data_dict.get("msg")
    if msg == 'exit':
        socket_interface.out_server()  # 在线人数减1
        for socket in sockets_list:
            if socket.get("socket_handle") == conn_socket:
                 socket["status"] = False # 记录登录状态

        print(f"{ip_port} - - {data_dict} - - {commom.getTime()}  在线人数:{socket_interface.getClientNum()}")
    else:
        response_dict = socket_interface.ResponseData2dic('chat', code=200, username=username, msg=msg)
        # 遍历所有客户端
        for socket in sockets_list:
            socket_interface.send(socket,response_dict)

        print(f"{ip_port} - - {data_dict} - - {commom.getTime()} 'chat' {response_dict} 在线人数:{socket_interface.getClientNum()}")

def client_handle(conn_socket,ip_port):
    try:
        while True:
            data_dict = socket_interface.recv(conn_socket)
            # print(f"服务端接收到{ip_port}数据:",data_dict)
            if data_dict.get("mode")=='login':
                login_request(conn_socket,data_dict)
            elif data_dict.get("mode")=='chat':
                chat_request(conn_socket,data_dict)
    except Exception as e:
        print(e)
        traceback.print_exc()
        conn_socket.close()
        # 客户端连接断开 且 客户端是已经登录的状态
        for socket in sockets_list:
            if socket.get("socket_handle") == conn_socket:
                if socket.get("status") == True:
                    socket_interface.out_server()
            sockets_list.remove(socket)

        print(f"{ip_port} 已经断开连接 ----  在线人数:{socket_interface.getClientNum()}")



if __name__ == '__main__':
    server =  socket_interface.server_create('0.0.0.0',2346)
    print("服务器已运行:：2346")
    while True:
        # 阻塞等待客户端接入
        conn_socket,ip_port = server.accept()
        print(f"{ip_port}已连接....")
        sockets_list.append({"socket_handle":conn_socket,"ip_port":ip_port,"status":False})
        Thread(target=client_handle,args=(conn_socket,ip_port)).start()


