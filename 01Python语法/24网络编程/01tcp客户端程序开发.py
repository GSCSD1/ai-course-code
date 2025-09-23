"""
    socket 类
        AddressFamily: IP地址类型  IPV4  IPV6
        Type ： 传输协议

    客户端使用到的函数
    connect  和服务端套接字建立连接
    send     发送数据
    recv     接收数据
    close    关闭连接

    # 1、创建客户端套接字对象
    # 2、和服务端建立连接 参数为元组类型
    # 3、发送数据
    # 4、接收数据 阻塞等待
    # 5、关闭客户端连接
"""
import socket

if __name__ == '__main__':
    # 1、创建客户端套接字对象
    # AF_INET IPV4 SOCK_STREAM为TCP通讯方式
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、和服务端建立连接 参数为元组类型
    tcp_client_socket.connect(('127.0.0.1', 2345))
    # 3、发送数据
    # tcp_client_socket.send("你好吗?".encode("utf-8"))
    while True:
        # 4、接收数据 阻塞等待
        recv_data =  tcp_client_socket.recv(1024)
        if not recv_data:
            print("服务端下线")
            tcp_client_socket.close()
            break
        print("客户端接收到的数据",recv_data.decode("utf-8"))
    # 5、关闭客户端连接
    tcp_client_socket.close()
