import socket
import pickle

"""绝对路径"""
import sys
sys.path.append("..")
from interface import commom

server_count = 0

def getClientNum():
    return server_count

def in_server():
    global server_count
    server_count += 1
    return server_count

def out_server():
    global server_count
    if server_count <= 0:
        server_count = 0
    else:
        server_count -= 1
    return server_count

def client_create(ip,port):
    """
    :param ip:  ip地址
    :param port:  端口
    :return: 客户端socket对象
    """
    # 创建socket对象 使用IPV4 TCP协议
    socket_client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务端
    socket_client.connect((ip,port))
    return socket_client

def server_create(ip,port,clientNum=5):
    # 创建socket对象 使用IPV4 TCP协议
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip地址和端口
    socket_client.bind((ip,port))
    # 设置监听  等待排队的最大数量
    socket_client.listen(clientNum)
    return socket_client

def send(n_socket,data_dic:dict):
    """
    :param n_socket:  要操作的socket对象
    :param data_dic:  发送的数据内容  字典类型
    :return:
    """
    dic_bytes = pickle.dumps(data_dic)
    dic_len = len(dic_bytes).to_bytes(8, byteorder='big')
    n_socket.send(dic_len)
    n_socket.send(dic_bytes)

def recv(n_socket):
    # 接收长度
    byte_len = n_socket.recv(8)
    if not byte_len:
        raise Exception("客户端已断开")
    # 将字节码转为int类型
    stream_len = int.from_bytes(byte_len, byteorder="big")
    """开始接收数据"""
    dic_bytes = bytes()
    while stream_len > 0:
        # 数据大小小于4096 直接接完所有数据
        if stream_len < 4096:
            temp = n_socket.recv(stream_len)
        # 数据大于4096分块接收
        else:
            temp = n_socket.recv(4096)
        if not temp:
            raise Exception("客户端已断开")
        dic_bytes += temp
        stream_len -= len(temp)
    """字节转字典"""
    # requests_dic = json.loads(dic_bytes.decode("utf8"))
    requests_dic = pickle.loads(dic_bytes)  # 将字节对象反序列化为字典对象
    # print(requests_dic, type(requests_dic))
    return requests_dic

def  RequsetData2dic(mode,**kwargs):
    """
        :param mode:  请求包模式
        :param kwargs:
                        username ： 账号
                        pwd     :密码
                        msg     : 发送的内容

        :return:
    """
    if mode == 'login' or mode == 'register':
        data = {
            'mode': mode,
            'user': kwargs.get('username'),
            'pwd': kwargs.get('pwd')
        }
        return data
    elif mode =='chat':
        data = {
            'mode': mode,
            'user': kwargs.get('username'),
            'msg' : kwargs.get('msg'),
            'time': commom.getTime()
        }
        return data
    return None

def  ResponseData2dic(mode,**kwargs):
    """
        :param mode:  请求包模式
        :param kwargs:
                        code  ： 状态码
                        msg  :状态码的描述信息
        :return:
    """
    if mode == 'login' or mode == 'register':
        data = {
            'code': kwargs.get('code'),
            'mode': mode,
            'msg': kwargs.get('msg')
        }
        return data
    if mode == 'chat':
        data = {
            'mode': mode,
            'code': kwargs.get('code'),
            'user': kwargs.get('username'),
            'msg': kwargs.get('msg'),
            'time': commom.getTime()
        }
        return data
    return None