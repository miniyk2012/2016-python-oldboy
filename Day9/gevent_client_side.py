# -*- coding:utf-8 -*-


import socket, threading

HOST = 'localhost'    # The remote host
PORT = 8001           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
def run(n):
    while True:
        msg = bytes("Hello", encoding="utf8")
        s.sendall(msg)
        data = s.recv(1024)
        print('Thread [%s]:[%s]\n' % (n, data))

        # print('Received', repr(data))
    s.close()

res_list = []
for i in range(100):
    t = threading.Thread(target=run, args=[i, ])
    t.start()
    res_list.append(t)

for r in res_list:
    r.join()