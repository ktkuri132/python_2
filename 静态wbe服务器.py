import socket
if __name__ == '__main__':
    #创建一个tcp套接字服务端框架
    #创建socket服务端对象
    http_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #允许端口复用
    http_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #设置IP地址端口号
    http_server_socket.bind(('192.168.0.114',80))
    #打开监听
    http_server_socket.listen(10)
    #等待客户端接受请求
    client_connect,ip_port=http_server_socket.accept()
    #接受HTTP请求数据
    http_requests_data=client_connect.recv(2048)
    #筛选出请求数据
    requests_data=http_requests_data.decode().split(' ')
    print(requests_data)
    print(http_requests_data.decode())
    #读取固定页面数据,把页面数据组装成HTTP响应报文数据发送给浏览器
    requests_key_word=requests_data[1]
    #应答行
    response_line="HTTP/1.1 200 OK\r\n"
    #应答头
    response_hand="server:fuck you\r\n"
    #应答体
    with open(f".{requests_key_word}",'rb') as f:
        html_file=f.read()
    response_body=html_file
    #整体应答数据
    response_data=(response_line+response_hand+"\r\n").encode()+response_body
    #发送HTTP响应数据
    client_connect.send(response_data)
    #关闭客户端连接
    client_connect.close()
    #数据发送完成后关闭客户端套接字连接
    http_server_socket.close()