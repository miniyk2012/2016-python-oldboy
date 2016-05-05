#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)


while True:
    user_input = input(">>:").strip()
    if not user_input:  # 很重要哟,如果发出去为空,服务器端就会一直等,不发信息过来,那客户端这边也一直等,那就僵死了,所以必须发出去有字节哟.
        continue
    if user_input == 'q':
        break
    sk.send(bytes(user_input,'utf8'))
    server_reply = sk.recv(1024)
    print(str(server_reply,'utf8'))
sk.close()
