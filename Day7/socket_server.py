# -*- coding: utf-8 -*-

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting...')
    conn,addr = sk.accept()  # 等待链接，针对等到的链接生成一个专门的实例conn，这个实例只为该客户端服务，addr保存客户端的地址
    print('addr:', addr)
    client_data = conn.recv(1024)  # 从客户端接收数据1024bit是字节,如果没有接收到就一直等待,但是如果客户端断开的话,那么recv就不阻塞了.
    print(str(client_data, 'utf8'))
    conn.sendall(bytes('hello', 'utf8'))  # 貌似sendall也有个阻塞的过程,自己调试看看

    conn.close()

