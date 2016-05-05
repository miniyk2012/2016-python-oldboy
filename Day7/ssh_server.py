#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import subprocess

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)


while True:
    print('server waiting...')
    conn,addr = sk.accept()
    while True:
        client_data = conn.recv(1024)
        if not client_data.decode():break  # 如果客户端断开,则会接收到一个空字符串,并往下跑.
        cmd = str(client_data, 'utf8').strip()
        print('recv: %s', cmd)
        try:
            cmd_result = subprocess.check_output(cmd, shell=True)
        except:
            cmd_result = b'cmd error'
        # cmd_call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        if not cmd_result:
            cmd_result = b'cmd exec has no return output'
        conn.send(cmd_result)
    conn.close()
