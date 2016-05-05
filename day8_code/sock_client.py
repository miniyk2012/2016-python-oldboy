#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',50007)

sk = socket.socket()
sk.connect(ip_port)
while True:
    msg = input(">>:").strip()
    sk.sendall(bytes(msg,'utf8'))
    server_reply = sk.recv(1024)
    print("Server Reply:",str(server_reply,'utf8'))
sk.close()
