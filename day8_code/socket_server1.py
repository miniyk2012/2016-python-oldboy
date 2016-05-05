#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print("Building secure connection chanel...")
    def handle(self):
        print("New Conn:",self.client_address)
        while True:

            data = self.request.recv(1024)
            if not data:break  # 客户端断了
            print("Client Says:",data.decode())
            self.request.send(data)
    def finish(self):
        print("client conn is done...")
if __name__ == '__main__':
    HOST, PORT = "localhost", 50007
    # 把刚才写的类当作一个参数传给ThreadingTCPServer这个类，下面的代码就创建了一个多线程socket server
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # 启动这个server,这个server会一直运行，除非按ctrl-C停止
    server.serve_forever()