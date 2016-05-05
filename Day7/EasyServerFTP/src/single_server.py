#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, subprocess, os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config.settings import BIND_HOST, BIND_PORT, BUFFER_SIZE, USER_ACCOUNT
from lib.action import Action

class SingleClientServer(object):

    request_queue_size = 5

    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server_bind(ip, port)
        except(Exception, ValueError) as e:
            print(e)
            self.server_close()

    def server_bind(self, ip, port):
        self.socket.bind((ip, port,))

    def server_activate(self):
        self.socket.listen(SingleClientServer.request_queue_size)
        while True:
            print('server is waiting...')
            self.conn, address = self.socket.accept()
            self.run()
            self.conn.close()

    def server_close(self):
        self.socket.close()

    def auth(func):
        def inner(self):
            while True:
                auth_msg = str(self.conn.recv(BUFFER_SIZE), 'utf8')
                if not auth_msg:
                    break
                auth_list = auth_msg.split('|')
                try:
                    user_name = auth_list[0]
                    password = auth_list[1]
                except:
                    self.conn.sendall(bytes('登录格式错误', 'utf8'))
                    continue
                if user_name in USER_ACCOUNT and USER_ACCOUNT[user_name]['password'] == password:
                    self.conn.sendall(b'PASS')
                    break
                else:
                    self.conn.sendall(b'auth not passed!')
            return func(self)
        return inner

    @auth
    def run(self):
        """
        和某一台客户端通信
        :return:
        """
        while True:
            client_bytes = self.conn.recv(BUFFER_SIZE)
            if not client_bytes:  # 如果客户端断开,则跳出
                break
            client_str = str(client_bytes, 'utf8').strip()
            obj = Action(self.conn)
            cmd = client_str.split('|')
            if len(cmd) == 1:   # 为普通命令
                if client_str == 'exit':
                    break
                obj.cmd(client_str)
            elif len(cmd) > 1:    # 为传输文件的命令, 和客户端规定好,put|file;get|file
                action = cmd[1]
                file = cmd[2]
                is_exist = hasattr(obj, action)
                if is_exist:
                    func = getattr(obj, action)
                    func(file)
        # get request
        # while True:
        #
        #     while True:
        #         client_bytes = conn.recv(1024)
        #         if not client_bytes:  # 如果客户端断开
        #             break
        #         # client_data是字节类型
        #         # 将字节变成字符串
        #         client_str = str(client_bytes, 'utf-8')
        #         o = client_str.split('|')
        #         if len(o) > 0:
        #             obj = Action(conn)
        #             func = getattr(obj, o[0])
        #             func(o)
        #         else:
        #             conn.sendall(bytes('输入格式错误', 'utf-8'))
        #     conn.close()

server = SingleClientServer(BIND_HOST, BIND_PORT)
server.server_activate()









