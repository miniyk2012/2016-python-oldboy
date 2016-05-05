# -*- coding:utf-8 -*-  

import socket, os, sys, logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config.settings import BIND_HOST, BIND_PORT, BUFFER_SIZE
from lib.action import Action


class Client(object):

    def __init__(self, ip, port):
        self.sk = socket.socket()
        self.ip = ip
        self.port = port

    def connect(self):
        self.sk.connect((self.ip, self.port))
        self.login()

    def login(self):
        username = input('enter your username>>')
        password = input('enter your password>>')
        self.sk.sendall(bytes('%s|%s' %(username, password), 'utf8'))
        confirm_msg = str(self.sk.recv(BUFFER_SIZE), 'utf8')
        while True:
            if confirm_msg == 'PASS':
                print('welcome %s' % username)
                break
            else:
                print(confirm_msg)
                username = input('enter your username>>')
                password = input('enter your password>>')
                if not username and not password:
                    continue
                self.sk.sendall(bytes('%s|%s' %(username, password), 'utf8'))
                confirm_msg = str(self.sk.recv(BUFFER_SIZE), 'utf8')


    def communicate(self):
        while True:
            user_input = input("cmd>>").strip()
            if not user_input:
                continue
            if user_input == 'q':
                break
            self.sk.send(bytes(user_input, 'utf8'))
            server_ack_msg = self.sk.recv(BUFFER_SIZE)
            self.sk.send(b'ok')
            cmd_res_msg = str(server_ack_msg, 'utf8').split('|')
            if cmd_res_msg[0] == 'CMD_RESULT_SIZE':
                cmd_res_size = int(cmd_res_msg[1])
                res = ''
            received_size = 0
            while received_size < cmd_res_size:  # 收大文件

                server_reply = self.sk.recv(BUFFER_SIZE)
                received_size += len(server_reply)
                res += str(server_reply, 'utf8')
            else:
                if res == 'cmd exec has no return output':
                    print()
                else:
                    print(res)





client = Client(BIND_HOST, BIND_PORT)
client.connect()
client.communicate()
