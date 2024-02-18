import socket
if __name__ == '__main__':

    #创建socket客户端对象
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #设置端口复用                     socket设置选项      端口复用选项            打开
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #设置ip地址和端口
    tcp_server_socket.bind(("192.168.0.114",8080))
    #打开监听
    tcp_server_socket.listen(100)
    while True:
        #等待接受客户端的接受请求
        print('正在等待连接...')
        tcp_connect,ip_port=tcp_server_socket.accept()
        print('连接成功！')
        print(f'当前用户为：{ip_port}')
        #发送数据
        tcp_send=input('发送:')
        tcp_connect.send(tcp_send.encode())
        #接收数据
        tcp_data=tcp_connect.recv(1024)
        print(f'接收到的数据为：{tcp_data.decode()}')
        #关闭服务端
        tcp_connect.close()
    tcp_server_socket.close()