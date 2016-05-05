# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)


while True:
    user_input = input("cmd>>:").strip()
    if not user_input:
        continue
    if user_input == 'q':
        break
    sk.send(bytes(user_input,'utf8'))
    while True:  # 收大文件

        server_reply = sk.recv(500)   # 不能实现,因为最后会停住
        if not server_reply:
            print('----recv done----')
            break

        print(str(server_reply,'utf8'))
sk.close()

