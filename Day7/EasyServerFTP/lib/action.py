# -*- coding:utf-8 -*-

import subprocess, socket, os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config.settings import BUFFER_SIZE
class Action(object):

    def __init__(self, conn):
        self.conn = conn

    def send_handle(self, result_bytes):
        """
        无论发送什么字节,都先发送长度,再接收(防止粘包),再发送具体内容的方式实现,这样无论什么东西都是用大文件的方式发送.
        :param result_bytes:
        :return:
        """
        if not result_bytes:
            result_bytes = b'cmd exec has no return output'
        ack_msg = bytes('CMD_RESULT_SIZE|%s' % len(result_bytes), 'utf8')
        self.conn.send(ack_msg)
        self.conn.recv(BUFFER_SIZE)  # 请求客户端确认
        self.conn.sendall(result_bytes)

    def cmd(self, cmd):
        if cmd.split()[0] == 'cd':
            try:
                os.chdir(cmd.split()[1])
                path_bytes = bytes(os.path.abspath('.'), 'utf8')
            except:
                path_bytes = b'cmd error'
            self.send_handle(path_bytes)
        else:
            try:
                result_bytes = subprocess.check_output(cmd, shell=True)
            except:
                result_bytes = b'cmd error'
            self.send_handle(result_bytes)

    def put(self, filename):
        pass

    def get(self, filename):
        pass


