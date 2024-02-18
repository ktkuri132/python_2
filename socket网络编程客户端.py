import socket

if __name__=='__main__':
    #创建网络连接工具                       ipv4类型      tcp连接
    tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #和服务端建立连接
    tcp_client_socket.connect(('192.168.0.105',8080))
    #发送数据
    tcp_client_socket.send('nihao'.encode(encoding='utf-8'))
    #接收数据
    tcp_data=tcp_client_socket.recv(1024)
    #关闭连接
    tcp_client_socket.close()

    print(tcp_data.decode())

#



