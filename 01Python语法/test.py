import socket
import threading
def fun1(client_socket):
    while True:
        a = input("user:")
        client_socket.send(a.encode('utf-8'))
        # if a.encode('utf-8') == b"exit":
        #     break

if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1',2480))
    tcp_thread = threading.Thread(target=fun1,args=(tcp_client_socket,))
    tcp_thread.start()
    while True:
        re_data = tcp_client_socket.recv(1024)
        print("客户端收集到的数据为：", re_data.decode('utf-8'))
        print('user>>>')
        if re_data == "exit":
            break
tcp_client_socket.close()