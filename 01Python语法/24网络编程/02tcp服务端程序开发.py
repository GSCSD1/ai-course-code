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
import socket
import threading

#
# if __name__ == '__main__':
#     # 1、创建客户端套接字对象
#     # AF_INET IPV4 SOCK_STREAM为TCP通讯方式
#     tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 2、绑定ip地址和端口号
#     tcp_server_socket.bind(('127.0.0.1',2345))
#     # 3、设置监听  等待排队的最大数量
#     tcp_server_socket.listen(5)
#     # 4、等待接受客户端的连接请求  阻塞等待
#     # 返回一个用以和客户端通信socket对象  客户端的ip地址和端口
#     conn_socket,ip_port = tcp_server_socket.accept()
#     print(ip_port)
#     # 5、接收数据
#     recv_data =  conn_socket.recv(1024)
#     print("服务端接收到数据:",recv_data.decode("utf-8"))
#     # 6、发送数据
#     conn_socket.send("服务端数据已发送".encode("utf-8"))
#     # 7、关闭连接
#     conn_socket.close()


"""---------------------------服务端如何循环接收多个客户端数据------------------------"""

def handle_client(client_socket,ip_port):
    while True:
        client_socket.send('a'.encode())
        # 5、接收数据
        recv_data = client_socket.recv(1024)
        print(f"服务端接收到{ip_port}数据:", recv_data)
        if not recv_data:
            # 关闭客户端
            client_socket.close()
            print(f"{ip_port}已经下线")
            break


if __name__ == '__main__':
    # 1、创建客户端套接字对象
    # AF_INET IPV4 SOCK_STREAM为TCP通讯方式
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2、绑定ip地址和端口号
    tcp_server_socket.bind(('127.0.0.1',2345))
    # 3、设置监听  等待排队的最大数量
    tcp_server_socket.listen(5)
    # 4、等待接受客户端的连接请求  阻塞等待
    while True:
    # 返回一个用以和客户端通信socket对象  客户端的ip地址和端口
        conn_socket,ip_port = tcp_server_socket.accept()
        threading.Thread(target=handle_client,args=(conn_socket,ip_port)).start()
        # print(ip_port)

    # 7、关闭连接
    conn_socket.close()