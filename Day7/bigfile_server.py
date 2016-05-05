#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import subprocess
import time
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
            cmd_result = subprocess.check_output(cmd, shell=True)  # 返回的是bytes哟
        except:
            cmd_result = b'cmd error'
        # cmd_call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        if not cmd_result:
            cmd_result = b'cmd exec has no return output'
        ack_msg = bytes('CMD_RESULT_SIZE|%s' % len(cmd_result), 'utf8')
        # 以下两条命令有可能粘包,就是放到缓冲里后一起发出去
        conn.send(ack_msg)
        time.sleep(1)
        conn.send(cmd_result)
    conn.close()
