# -*- coding:utf-8 -*-

import sys
import socket
import time
import gevent

from gevent import socket, monkey
monkey.patch_all()  # 自动把各种阻塞的东东变成非阻塞的东东

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)  # 最多监听500个链接
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)  # 启动协程,cli是socket对象
def handle_request(s):
    try:
        while True:
            data = s.recv(1024)
            print("recv:", data)
            s.send(data)
            if not data:
                s.shutdown(socket.SHUT_WR)

    except Exception as ex:
        print(ex)
    finally:

        s.close()
if __name__ == '__main__':
    server(8001)