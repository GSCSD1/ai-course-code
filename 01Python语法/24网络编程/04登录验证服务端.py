"""
    socket 类
        AddressFamily: IP地址类型  IPV4  IPV6
        Type ： 传输协议

    客户端使用到的函数
    bind      绑定ip地址和端口号
    listen    监听端口
    accept    等待接受客户端的连接请求
    send     发送数据
    recv     接收数据
    close    关闭连接

    # 1、创建服务端套接字
    # 2、绑定ip地址和端口号
    # 3、设置监听
    # 4、等待接受客户端的连接请求
    # 5、接收数据
    # 5、发送数据
    # 7、关闭套接字
"""
import json
import pickle
import socket
import threading

# 查询用户名是否在文件库中，返回查询到的用户名和密码
def select_user(user):
    db_User= None
    db_Passwd = None
    with open('./db/user.txt', 'r') as f:
        for line in f: # 读取每行文件中的账号和密码
            if user == line.split(':')[0]: # 判断账号
                db_User = user
                db_Passwd = line.split(':')[1].strip('\n')
                break
    return db_User, db_Passwd


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

"""---------------------------服务端如何循环接收多个客户端数据------------------------"""
def handle_client(client_socket,ip_port):
    try:
        while True:
            # 阻塞接收数据
            requests_dic = recv(client_socket)
            if requests_dic.get('mode')=='register':  #  注册功能
                dbUser,dbPwd =  select_user(requests_dic.get('user'))
                user_passdat = f"{requests_dic.get('user')}:{requests_dic.get('pwd')}\n"
                if dbUser is None: # 如果账号不存在
                    with open('./db/user.txt','at') as f:
                        f.write(user_passdat)
                    print(f"{user_passdat}注册成功")
                    statusCode = 200
                    msg = "注册成功"
                else:
                    print(f"{user_passdat}账号已经存在")
                    statusCode = 400
                    msg = "账号已经存在"

                response_dic = {
                    "code" : statusCode,
                    "mode" : "register",
                    "msg"  : msg
                }
                send(client_socket,response_dic)
            elif requests_dic.get('mode')=='login':
                user = requests_dic.get('user')
                passwd = requests_dic.get('pwd')
                dbUser, dbPwd = select_user(user)
                # print(requests_dic)
                # print(dbUser,dbPwd.encode("utf-8"))
                if dbUser and passwd ==  dbPwd: # 账号存在且密码匹配成功
                           statusCode = 200
                           msg = "账号密码匹配成功"
                           # print("账号密码匹配成功")
                else:
                    statusCode = 400
                    msg = "账号和密码输入错误"
                    # print("账号和密码输入错误")

                response_dic = {
                    "code": statusCode,
                    "mode": "login",
                    "msg": msg
                }
                send(client_socket, response_dic)
    except Exception as e:
        print(e)
        client_socket.close()
"""
    实现多人聊天室功能：
        1、服务端能记录在线人数
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
if __name__ == '__main__':
    # 1、创建客户端套接字对象
    # AF_INET IPV4 SOCK_STREAM为TCP通讯方式
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定ip地址和端口号
    tcp_server_socket.bind(('127.0.0.1',2345))
    # 3、设置监听  等待排队的最大数量
    tcp_server_socket.listen(5)
    print("服务端已经启动!")
    # 4、等待接受客户端的连接请求  阻塞等待
    while True:
    # 返回一个用以和客户端通信socket对象  客户端的ip地址和端口
        conn_socket,ip_port = tcp_server_socket.accept()
        threading.Thread(target=handle_client,args=(conn_socket,ip_port)).start()
        print(ip_port)


    # 7、关闭连接
    conn_socket.close()